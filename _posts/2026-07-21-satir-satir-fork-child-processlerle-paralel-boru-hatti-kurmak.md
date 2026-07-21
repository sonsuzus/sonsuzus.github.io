---
layout: post
title: "Satır Satır Fork: Child Process’lerle Paralel Boru Hattı Kurmak"
math: true
categories: 
  - Program
tags: 
  - linux
  - c
  - process
  - pipe
  - fork
---

Bir metin dosyasındaki her satırı ayrı bir iş birimi gibi düşünelim: Her satır küçük bir paket, her child process de bu paketi işleyen minik bir işçi. Sistem çağrısı seviyesinde paralel boru hattı kurmanın amacı, bu işçileri `fork()`, `pipe()`, `dup2()`, `exec()` ve `wait()` gibi yapı taşlarıyla yönetip çıktıları tek bir satırda birleştirmektir. Bu yaklaşım, shell komutlarını taklit etmekten öte, işletim sisteminin süreç ve dosya tanımlayıcı mantığını gerçekten kavratır.
``

## Temel fikir: satır = görev, process = işçi

Klasik bir program dosyayı satır satır okur ve her satırı sırayla işler. Paralel modelde ise $n$ satır için en fazla $n$ child process üretilebilir. Her child kendi satırını işler, sonucunu pipe üzerinden parent process’e yollar. Parent da sonuçları okuyup tek satır hâline getirir.

Teorik olarak toplam süre şöyle düşünülebilir:

$T_{seri} = \sum_{i=1}^{n} t_i$

Paralel modelde ideal durumda:

$T_{paralel} \approx \max(t_i) + T_{fork} + T_{pipe} + T_{wait}$

Yani her şey bedava değildir. Process oluşturmanın, pipe açmanın ve context switch’in maliyeti vardır. Bu yüzden bu yöntem özellikle satır başına yapılan işlem yeterince “ağırsa” mantıklıdır.

| Yaklaşım | Avantaj | Dezavantaj |
|---|---|---|
| Seri okuma | Basit, az kaynak tüketir | Yavaş olabilir |
| Thread tabanlı | Daha hafif paralellik | Paylaşımlı bellek dikkat ister |
| Process tabanlı | İzolasyon güçlüdür | `fork()` ve IPC maliyetlidir |
| Shell pipeline | Hızlı prototip | Kontrol daha sınırlıdır |

## Kullanacağımız sistem çağrıları

| Çağrı | Görevi | Akılda kalıcı benzetme |
|---|---|---|
| `fork()` | Child process üretir | İşçiyi klonlamak |
| `pipe()` | İki uçlu veri kanalı açar | Konuşma borusu |
| `dup2()` | Dosya tanımlayıcı yönlendirir | Mikrofonu başka kabloya takmak |
| `exec()` | Process’in programını değiştirir | İşçiye yeni meslek vermek |
| `waitpid()` | Child bitişini bekler | Mesai kontrolü |

Aşağıdaki örnekte her satırı ayrı child process’e veriyoruz. Child, satırı küçük bir işlemden geçiriyor: boşlukları `_` karakterine çeviriyor ve sonucu pipe ile parent’a gönderiyor. Gerçek hayatta bu bölüm `exec()` ile harici bir programa da devredilebilir.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#define MAX_LINE 256
#define MAX_CHILD 128

void transform(char *s) {
    for (int i = 0; s[i]; i++) {
        if (s[i] == ' ' || s[i] == '\n') s[i] = '_';
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Kullanim: %s dosya.txt\n", argv[0]);
        return 1;
    }

    FILE *fp = fopen(argv[1], "r");
    if (!fp) { perror("fopen"); return 1; }

    int pipes[MAX_CHILD][2];
    pid_t pids[MAX_CHILD];
    int count = 0;
    char line[MAX_LINE];

    while (fgets(line, sizeof(line), fp) && count < MAX_CHILD) {
        if (pipe(pipes[count]) == -1) { perror("pipe"); exit(1); }

        pid_t pid = fork();
        if (pid == -1) { perror("fork"); exit(1); }

        if (pid == 0) {
            close(pipes[count][0]);
            transform(line);
            dprintf(pipes[count][1], "%s", line);
            close(pipes[count][1]);
            _exit(0);
        }

        close(pipes[count][1]);
        pids[count] = pid;
        count++;
    }
    fclose(fp);

    printf("Sonuc: ");
    for (int i = 0; i < count; i++) {
        char buffer[MAX_LINE];
        ssize_t n = read(pipes[i][0], buffer, sizeof(buffer) - 1);
        if (n > 0) {
            buffer[n] = '\0';
            printf("%s ", buffer);
        }
        close(pipes[i][0]);
        waitpid(pids[i], NULL, 0);
    }
    printf("\n");

    return 0;
}
```

Kodun önemli noktası şudur: Child sadece yazma ucunu, parent ise sadece okuma ucunu kullanır. Kullanılmayan pipe uçlarını kapatmazsak EOF davranışı bozulabilir ve program “neden bitmiyor?” diye bizi gece 03:00’te kahveye mahkûm edebilir.

## `exec()` eklemek istersek

Child içinde kendi fonksiyonumuzu çalıştırmak yerine harici bir komuta veri göndermek mümkündür. Bunun için genellikle iki pipe gerekir: biri child’ın stdin’ine, diğeri stdout’una bağlanır. Mantık şu şekildedir:

```c
// child tarafında kavramsal akış
// dup2(inputPipe[0], STDIN_FILENO);
// dup2(outputPipe[1], STDOUT_FILENO);
// execlp("tr", "tr", "a-z", "A-Z", NULL);
```

Burada `tr` komutu stdin’den aldığı metni dönüştürür, stdout’a yazar. Parent da stdout pipe’ından sonucu toplar. Böylece her satır ayrı bir Unix filtresinden geçmiş olur.

## Sıralama ve güvenlik notları

Parent sonuçları `pids` dizisindeki sıraya göre okuduğu için çıktı dosyadaki satır sırasını korur. Ancak çok büyük dosyalarda her satıra process açmak tehlikelidir. Daha sağlıklı model, aynı anda en fazla $k$ child çalıştırmaktır. Bu durumda yaklaşık kaynak sınırı:

$aktif\_process \leq k$

Sonuç olarak bu paralel boru hattı, process izolasyonunu, pipe tabanlı iletişimi ve Unix’in “her şey dosya tanımlayıcıdır” felsefesini aynı sahnede buluşturur. Küçük dosyalarda eğlenceli, ağır satır işlemlerinde güçlü, sınırsız process açıldığında ise tam bir kaynak canavarına dönüşebilir.
