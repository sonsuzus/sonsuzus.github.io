---
layout: post
title: "C ile Kendi Mini Yorumlayıcını Yazmak: Sözdiziminden Bytecode’a"
math: true
categories: 
  - Proje
tags: 
  - C
  - yorumlayıcı
  - derleyici
  - parser
  - bytecode
---

Derleyiciler bazen kara kutu gibi görünür: kodu yazarsın, bir şeyler olur ve işlemci “tamamdır” der. Oysa içeride oldukça sistemli bir mutfak çalışır. Bu yazıda C ile minicik bir dil motoru tasarlayarak `SET x 5`, `ADD x 3`, `PRINT x` gibi komutları okuyacak, sözdizimini analiz edecek ve bunları basit bir “makine dili” yani bytecode’a çevireceğiz.
``
Bir yorumlayıcının temel fikri şudur: metin hâlindeki program önce anlamlı parçalara ayrılır, sonra kurallara göre dizilir, en sonunda da çalıştırılabilir talimatlara dönüştürülür. Gerçek derleyicilerde bu süreç daha karmaşıktır; optimizasyon, tip denetimi ve hedef mimari gibi konular devreye girer. Bizim oyuncak dilimizde ise değişkenler, sayılar ve birkaç komut yeterli olacak.

Teorik olarak kaynak koddan çalışmaya giden yol şöyle modellenebilir:

$$Kaynak\ Kod \rightarrow Tokenlar \rightarrow AST/Komutlar \rightarrow Bytecode \rightarrow VM$$

Burada “VM”, sanal makine demektir. Gerçek CPU yerine kendi küçük işlemcimizi C içinde simüle ederiz. Mesela `ADD x 3` komutu, bellekteki `x` değerini alıp üzerine 3 ekleyen bir bytecode talimatına dönüşür.

| Aşama | Görevi | Örnek |
|---|---|---|
| Lexer | Metni parçalara ayırır | `ADD`, `x`, `3` |
| Parser | Sıralamanın doğru olup olmadığını kontrol eder | `ADD IDENT NUMBER` |
| Codegen | Komutu bytecode’a çevirir | `OP_ADD, var_id, 3` |
| VM | Bytecode’u çalıştırır | `x = x + 3` |

Önce komut kümemizi tanımlayalım. Bu dilde üç işlem olsun: değişkene değer atama, toplama ve ekrana yazdırma. Matematiksel olarak belleği bir fonksiyon gibi düşünebiliriz: $M(v)$, `v` değişkeninin değeridir. `ADD x 3` çalışınca yeni durum $M'(x)=M(x)+3$ olur.

```c
typedef enum {
    OP_SET,
    OP_ADD,
    OP_PRINT,
    OP_HALT
} OpCode;

typedef struct {
    OpCode op;
    int var;
    int value;
} Instruction;
```

Bu yapı bizim mini makine dilimizdir. `op` hangi işlemin yapılacağını söyler, `var` değişkenin kimliğini, `value` ise sayısal argümanı taşır. Gerçek makinelerde bunlar baytlara sıkıştırılır; biz okunabilir kalsın diye `struct` kullandık.

Şimdi basit bir değişken tablosu yazalım. Oyuncak örnekte değişkenleri tek harf kabul etmek işi çok kolaylaştırır: `a`, `b`, `x` gibi. Böylece `x - 'a'` bize 0-25 arası bir indeks verir.

```c
int var_id(const char *name) {
    if (name[0] >= 'a' && name[0] <= 'z' && name[1] == '\0')
        return name[0] - 'a';
    return -1;
}
```

Parser tarafında satırı okuyup ilk kelimeye göre karar verebiliriz. Bu, tam teşekküllü bir parser değildir ama sözdizimi analizinin özünü gösterir: beklenen kalıba uyuyor mu?

```c
int compile_line(char *line, Instruction *out) {
    char cmd[16], name[16];
    int value;

    if (sscanf(line, "SET %15s %d", name, &value) == 2) {
        out->op = OP_SET;
        out->var = var_id(name);
        out->value = value;
        return out->var >= 0;
    }

    if (sscanf(line, "ADD %15s %d", name, &value) == 2) {
        out->op = OP_ADD;
        out->var = var_id(name);
        out->value = value;
        return out->var >= 0;
    }

    if (sscanf(line, "PRINT %15s", name) == 1) {
        out->op = OP_PRINT;
        out->var = var_id(name);
        out->value = 0;
        return out->var >= 0;
    }

    return 0;
}
```

Bu kodun eğlenceli yanı, `sscanf` ile minik bir dilbilgisi kontrolü yapmasıdır. Daha ciddi bir projede token üretir, ardından recursive descent parser yazardık. Örneğin `expr -> term ((+|-) term)*` gibi kurallarla matematiksel ifadeleri ayrıştırmak mümkün olurdu.

Son adımda bytecode’u çalıştıran sanal makineyi yazıyoruz:

```c
void run(Instruction *code, int count) {
    int memory[26] = {0};

    for (int ip = 0; ip < count; ip++) {
        Instruction in = code[ip];

        switch (in.op) {
            case OP_SET:
                memory[in.var] = in.value;
                break;
            case OP_ADD:
                memory[in.var] += in.value;
                break;
            case OP_PRINT:
                printf("%d\n", memory[in.var]);
                break;
            case OP_HALT:
                return;
        }
    }
}
```

Buradaki `ip`, instruction pointer’dır; yani sıradaki talimatın adresini gösterir. CPU’larda da benzer bir mantık vardır. Program sayacı ilerler, talimat çözülür, işlem yapılır. Bizim VM bunu C döngüsüyle taklit eder.

Örnek program şöyle olabilir:

```text
SET x 10
ADD x 7
PRINT x
```

Derleme sonucunda yaklaşık olarak şu bytecode dizisi oluşur:

| Kaynak Satır | Bytecode |
|---|---|
| `SET x 10` | `OP_SET, 23, 10` |
| `ADD x 7` | `OP_ADD, 23, 7` |
| `PRINT x` | `OP_PRINT, 23, 0` |

Çıktı doğal olarak `17` olur. Küçük ama güçlü bir fikir yakaladık: sözdizimi sadece metin kontrolü değildir; anlamlı eylemlere açılan kapıdır. Buradan sonra ifadeler, koşullar, döngüler ve hata mesajları ekleyerek mini dilinizi büyütebilirsiniz. Bir noktadan sonra fark edeceksiniz: derleyiciler büyü yapmıyor, sadece çok disiplinli bir çeviri işi gerçekleştiriyor.
