---
layout: post
title: "C++ ile Kriptografik Şifreleme: Matematiği Kodla Kilide Çevirmek"
math: true
categories: 
  - Program
tags: 
  - C++
  - Kriptografi
  - RSA
  - Veri Güvenliği
---

Kriptografi, bilgisayar biliminin en havalı sihirbazlık numaralarından biridir: okunabilir bir mesajı, matematiksel işlemlerle anlamsız görünen bir yığına dönüştürür; sonra doğru anahtarla tekrar eski haline getirir. C++ ise belleğe yakın çalışması, hızlı aritmetik işlemleri ve sistem seviyesinde kontrol sunması sayesinde bu algoritmaları anlamak için harika bir laboratuvardır.
``
## Şifreleme fikri: kilit, anahtar ve dönüşüm

Bir şifreleme algoritmasını kabaca şu fonksiyon gibi düşünebiliriz: $C = E(M, K)$. Burada $M$ açık mesaj, $K$ anahtar, $E$ şifreleme fonksiyonu ve $C$ şifreli metindir. Çözme tarafında ise $M = D(C, K)$ ya da asimetrik sistemlerde farklı bir anahtar kullanılarak $M = D(C, K_{private})$ elde edilir.

Temel ayrım şudur:

| Yaklaşım | Kullanılan anahtar | Hız | Tipik kullanım |
|---|---:|---:|---|
| Simetrik şifreleme | Aynı gizli anahtar | Çok hızlı | Dosya, disk, veri akışı |
| Asimetrik şifreleme | Açık + özel anahtar | Daha yavaş | Anahtar değişimi, imza |
| Hash | Anahtar yok / opsiyonel | Hızlı | Bütünlük kontrolü, parola özeti |

Bu yazıda eğitim amacıyla küçük bir RSA benzeri yapı kuracağız. Gerçek dünyada kendi kriptonuzu üretip canlı sistemde kullanmak genellikle kötü fikirdir; AES, ChaCha20, RSA-OAEP gibi incelenmiş standartlar ve OpenSSL/libsodium gibi kütüphaneler tercih edilmelidir. Ama mantığı kodlamak öğrenmenin en iyi yollarından biridir.

## RSA’nın matematiksel kalbi

RSA, büyük asal sayıların çarpanlara ayrılmasının zorluğuna dayanır. İki asal seçeriz: $p$ ve $q$. Sonra $n = p \times q$ hesaplanır. Bu $n$, hem açık hem özel anahtar tarafında kullanılır.

Euler phi değeri: $\varphi(n) = (p-1)(q-1)$.

Açık üs $e$, $\varphi(n)$ ile aralarında asal seçilir. Özel üs $d$ ise şu koşulu sağlar: $d \times e \equiv 1 \pmod{\varphi(n)}$.

Şifreleme: $C = M^e \mod n$  
Çözme: $M = C^d \mod n$

Buradaki sihir, modüler aritmetiktedir. Sayılar devasa büyümeden üs alma yapmak için “hızlı üs alma” tekniği kullanılır.

## C++ ile mini RSA deneyi

Aşağıdaki kod güvenli değildir; çünkü çok küçük asal sayılar kullanır. Amacı, RSA mantığını elle tutulur hale getirmektir.

```cpp
#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;

uint64_t modPow(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }
    return result;
}

int64_t egcd(int64_t a, int64_t b, int64_t &x, int64_t &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    int64_t x1, y1;
    int64_t g = egcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

uint64_t modInverse(uint64_t e, uint64_t phi) {
    int64_t x, y;
    egcd(e, phi, x, y);
    return (x % (int64_t)phi + phi) % phi;
}

int main() {
    uint64_t p = 61, q = 53;
    uint64_t n = p * q;
    uint64_t phi = (p - 1) * (q - 1);
    uint64_t e = 17;
    uint64_t d = modInverse(e, phi);

    uint64_t message = 42;
    uint64_t encrypted = modPow(message, e, n);
    uint64_t decrypted = modPow(encrypted, d, n);

    cout << "Acik anahtar (e,n): (" << e << "," << n << ")\n";
    cout << "Ozel anahtar d: " << d << "\n";
    cout << "Mesaj: " << message << "\n";
    cout << "Sifreli: " << encrypted << "\n";
    cout << "Cozulen: " << decrypted << "\n";
}
```

`modPow` fonksiyonu, $M^e$ gibi astronomik büyüyebilecek ifadeleri güvenli şekilde mod içinde tutar. `egcd` yani genişletilmiş Öklid algoritması ise modüler ters bulur; RSA’daki özel anahtarın matematiksel üretim noktası burasıdır.

## Neden gerçek sistemlerde daha fazlası gerekir?

Oyuncak RSA sadece iskeleti gösterir. Gerçek kriptografide asal üretimi, rastgelelik, dolgu şemaları ve yan kanal saldırılarına dayanıklılık kritik önemdedir.

| Konu | Oyuncak örnek | Gerçek dünya beklentisi |
|---|---|---|
| Asal sayılar | 61 ve 53 | 2048+ bit güvenli asal |
| Rastgelelik | Sabit değerler | Kriptografik RNG |
| Dolgu | Yok | OAEP, PSS gibi standartlar |
| Veri boyutu | Küçük sayı | Bloklama / hibrit şifreleme |

Pratikte RSA genellikle tüm dosyayı şifrelemek için değil, AES anahtarını güvenli taşımak için kullanılır. Buna hibrit şifreleme denir: hızlı simetrik algoritma veriyi şifreler, asimetrik algoritma ise anahtarı korur.

Sonuç olarak C++ ile kriptografi yazmak, matematik ve sistem programlamayı aynı masaya oturtur. Kendi mini aracınızı geliştirmek size $\mod$, asal sayılar ve anahtar mantığını öğretir; ancak üretimde güvenlik için test edilmiş kütüphanelere güvenmek en akıllıca hamledir.
