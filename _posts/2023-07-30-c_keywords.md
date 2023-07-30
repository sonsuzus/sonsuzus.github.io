---
title:  C Anahtar kelimeler
author: sonsuz
date: 2023-07-30 22:05:51 +0300
categories: [Program,C]
tags: [c,programlama,anahtar kelimeler]
---



C dilinde farklı amaçlarla kullanılmak üzere tahsis edilmiş olan kelimelere anahtar kelimeler denir. Bu kelimeleri değişken, veri ve döngü tanımlamaları ve benzeri işlemlerde kullanabilirsiniz. ANSI standartlarına göre C'de kullanılmakta olan toplam 32 adet anahtar kelime vardır. Bu kelimeler değişken ve fonksiyon adı olarak kullanılamaz.

## C anahtar kelimeleri

| auto | break | case | char | const | continue | default |
| do | double | else | enum | extern | float | for |
| goto | if | int | long | register | return | short |
| signed | sizeof | static | struct | switch | type | void |
| volatile | while | union | unsigned |  |  |  |

C derleyicilerinden bazıları yukarıdaki tabloya ek olarak bazı anahtar kelimeler daha kullanmaktadırlar. Bu kelimelerden en çok kullanılanlar aşağıda gösterilmektedir:

```c
  asm          _cs          _ds          _es
  _ss          cdecl        far          huge
  interrupt    near         pascal

```

Ayrıca, C99 standartları ile birlikte aşağıdaki anahtar kelimeler de eklenmiştir.

```c
  _Bool        _Complex     _Imaginary
  inline       restrict

```

C'de bütün anahtar kelimeler küçük harfle yazılmalıdır. Aksi takdirde derleyiciler tarafından tanınmazlar.
