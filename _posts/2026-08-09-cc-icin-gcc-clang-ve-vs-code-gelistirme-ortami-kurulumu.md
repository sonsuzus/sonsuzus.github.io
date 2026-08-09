---
layout: post
title: "C/C++ İçin GCC, Clang ve VS Code Geliştirme Ortamı Kurulumu"
math: true
categories: 
  - Bilgi
tags: 
  - C/C++
  - VS Code
  - GCC ve Clang
---

C ve C++, işlemciye ve belleğe yakın çalışabilmeleri sayesinde işletim sistemlerinden oyun motorlarına kadar pek çok alanda karşımıza çıkar. Ancak ilk programı yazmadan önce derleyici, hata ayıklayıcı ve editör üçlüsünü doğru biçimde hazırlamak gerekir. Bu rehberde GCC/Clang altyapısını kuracak, VS Code'u yapılandıracak ve kaynak kodun çalıştırılabilir programa nasıl dönüştüğünü öğreneceğiz.

``

## Derleme süreci nasıl çalışır?

C/C++ kaynak kodu doğrudan işlemci tarafından anlaşılmaz. Yazdığımız `.c` veya `.cpp` dosyaları birkaç aşamadan geçer:

1. **Ön işleme:** `#include` ve `#define` ifadeleri işlenir.
2. **Derleme:** Kod, assembly diline dönüştürülür.
3. **Assembly:** Makine kodunu içeren nesne dosyası üretilir.
4. **Bağlama:** Nesne dosyaları ve kütüphaneler tek programda birleştirilir.

Basitleştirilmiş dönüşüm şöyledir:

$$KaynakKod \rightarrow NesneDosyasi \rightarrow CalistirilabilirProgram$$

Donanıma yakınlık özellikle veri boyutlarında hissedilir. Örneğin $N$ bitlik işaretsiz bir tamsayı, $0$ ile $2^N-1$ arasındaki değerleri temsil edebilir. Belleğin sınırlı olduğu gömülü sistemlerde seçilen veri türü bu nedenle önemlidir.

| Araç | GCC | Clang |
|---|---|---|
| C derleyicisi | `gcc` | `clang` |
| C++ derleyicisi | `g++` | `clang++` |
| Güçlü tarafı | Yaygın platform desteği | Açıklayıcı hata mesajları |
| Hata ayıklayıcı | GDB | LLDB |
| Lisans ailesi | GNU GPL | Apache 2.0 |

## Derleyici kurulumu

Ubuntu ve Debian tabanlı sistemlerde GCC araç zinciri şu komutla kurulabilir:

```bash
sudo apt update
sudo apt install build-essential gdb
```

Clang kullanmak isteyenler ayrıca şunu çalıştırabilir:

```bash
sudo apt install clang lldb
```

macOS üzerinde Terminal'den `xcode-select --install` komutu Apple Clang araçlarını kurar. Windows'ta ise **MSYS2** kurulup UCRT64 terminalinde aşağıdaki komut kullanılabilir:

```bash
pacman -S mingw-w64-ucrt-x86_64-gcc mingw-w64-ucrt-x86_64-gdb
```

Ardından MSYS2'nin `ucrt64/bin` klasörü `PATH` değişkenine eklenmelidir. Kurulumu doğrulamak için `gcc --version`, `g++ --version` veya `clang --version` çalıştırılır.

## İlk program ve manuel derleme

`main.cpp` adında bir dosya oluşturalım:

```cpp
#include <iostream>

int main() {
    int sayi = 42;
    std::cout << "Bellekteki değer: " << sayi << '\n';
    return 0;
}
```

Programı GCC ile derlemek için şu komut yeterlidir:

```bash
g++ -std=c++20 -Wall -Wextra -g main.cpp -o uygulama
```

Burada `-std=c++20` dil standardını seçer, `-Wall -Wextra` olası hatalar için uyarıları açar, `-g` ise hata ayıklama bilgisi ekler. Linux/macOS üzerinde program `./uygulama`, Windows'ta `uygulama.exe` komutuyla çalıştırılır.

## VS Code yapılandırması

VS Code'a **C/C++** uzantısını kurduktan sonra proje klasöründe `.vscode/tasks.json` dosyası oluşturulur:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "C++ Derle",
      "type": "shell",
      "command": "g++",
      "args": [
        "-std=c++20",
        "-Wall",
        "-Wextra",
        "-g",
        "${file}",
        "-o",
        "${fileDirname}/${fileBasenameNoExtension}"
      ],
      "group": { "kind": "build", "isDefault": true },
      "problemMatcher": ["$gcc"]
    }
  ]
}
```

Bu görev, açık olan dosyayı **Ctrl+Shift+B** ile derler. Clang tercih ediliyorsa `command` alanı `clang++` yapılabilir.

Hata ayıklama sırasında breakpoint kullanmak, değişkenlerin bellekteki değişimini adım adım izlemeyi sağlar. VS Code'un **Run and Debug** bölümünden C++ yapılandırması seçildiğinde GDB veya LLDB çalıştırılır. Böylece yalnızca programın sonucunu değil; çağrı yığınını, işaretçileri ve bellek adreslerini de inceleyebilirsiniz.

Son olarak derleyici uyarılarını düşman değil, ücretsiz kod inceleme ekibi olarak görün. C/C++ öğrenirken `-Wall -Wextra` kullanmak ve küçük programları hata ayıklayıcıyla yürütmek, bellek yönetimi ile donanım arasındaki ilişkiyi çok daha görünür hâle getirir.
