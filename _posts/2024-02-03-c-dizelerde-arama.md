---
title:  C Programlama Dizelerde Karakter Arama fonksiyonu
author: sonsuz
date: 2024-02-03 14:26:15 +0300
categories: [Program,C]
tags: [c,programlama,alıştırma,algoritma,örnek,karakter,dize,arama]
---

C programlama için oldukça kullanışlı basit bir fonksiyon. c karakteri \*s dizisinde olup olmadığını kontrol eden basit ama kullanışlı fonksiyon python `if c in s:` yöntemine benziyor.

```c
int isin(char *s,char c)
{
    while(*s)
    {
        if(*s==c) return 1;
        else s++;
    }
    return 0;
}
```

Eğer c s dizesi içinde bir karakterle eşleşirse geriye 1 döndürüyor. Eğer hiç eşleşme olmadan while döngüsü son bulursa geriye 0 döndürüyor.
