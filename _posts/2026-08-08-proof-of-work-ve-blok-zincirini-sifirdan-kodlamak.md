---
layout: post
title: "Proof of Work ve Blok Zincirini Sıfırdan Kodlamak"
math: true
categories: 
  - Proje
tags: 
  - blockchain
  - proof-of-work
  - python
---

Blok zinciri çoğu zaman kripto paralarla özdeşleştirilse de temelinde oldukça anlaşılır bir fikir vardır: Kayıtları bloklar hâlinde birbirine bağlamak ve geçmişi değiştirmeyi hesaplama açısından pahalılaştırmak. Bu projede hazır blockchain kütüphanelerine dokunmadan Python ile blok, zincir ve Proof of Work mekanizması oluşturacağız.

``

## Zincir neden güvenilir kabul edilir?

Her blok; zaman damgası, işlemler, önceki bloğun özeti ve `nonce` adı verilen bir sayaç taşır. Bu veriler bir hash fonksiyonundan geçirilir. SHA-256 için sonucu kabaca şöyle gösterebiliriz:

$$H = SHA256(index + timestamp + transactions + previousHash + nonce)$$

Hash fonksiyonunun önemli özelliği tek yönlü olmasıdır. Girdideki küçücük bir değişiklik tamamen farklı bir çıktı üretir. Bir saldırgan eski bir işlemi değiştirirse o bloğun hash değeri değişir; sonraki blokta saklanan `previousHash` artık eşleşmez ve zincir kırılır.

Proof of Work, geçerli hash üretimine ek bir şart koyar. Örneğin hash değerinin dört sıfırla başlaması istenebilir. Madenci uygun sonucu doğrudan hesaplayamaz; `nonce` değerini tekrar tekrar değiştirerek deneme yapar.

| Kavram | Görevi | Değişiklik sonucu |
|---|---|---|
| Hash | Bloğun dijital parmak izini üretir | Blok kimliği değişir |
| Previous hash | Blokları birbirine bağlar | Zincir bağlantısı kopar |
| Nonce | Yeni hash denemeleri sağlar | İş kanıtı aranır |
| Zorluk | Gerekli sıfır sayısını belirler | Madencilik maliyeti artar |

Bir hash’in istenen $d$ adet sıfırla başlama olasılığı, onaltılık gösterimde yaklaşık $1/16^d$ olur. Beklenen deneme sayısı ise:

$$E = 16^d$$

Yani zorluğu yalnızca bir artırmak işi yaklaşık 16 kat pahalılaştırır. Küçük bilgisayarımız şimdiden terlemeye başladı!

## Ham blok modelini oluşturalım

Aşağıdaki sınıf blok verisini deterministik biçimde JSON’a dönüştürür. `sort_keys=True` önemlidir; alan sırası değişirse aynı veri farklı metne, dolayısıyla farklı hash’e dönüşebilir.

```python
import hashlib
import json
import time
from dataclasses import dataclass, field

@dataclass
class Block:
    index: int
    transactions: list
    previous_hash: str
    timestamp: float = field(default_factory=time.time)
    nonce: int = 0
    hash: str = ''

    def calculate_hash(self):
        payload = {
            'index': self.index,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'nonce': self.nonce
        }
        raw = json.dumps(payload, sort_keys=True).encode()
        return hashlib.sha256(raw).hexdigest()

    def mine(self, difficulty):
        target = '0' * difficulty
        while True:
            candidate = self.calculate_hash()
            if candidate.startswith(target):
                self.hash = candidate
                return
            self.nonce += 1
```

`mine` metodu doğru cevabı matematiksel bir kestirmeyle bulmaz. Nonce’u artırır, hash’i yeniden hesaplar ve hedef sağlanana kadar devam eder. Gerçek ağlarda bu işlem özel donanımlarla saniyede trilyonlarca kez yapılabilir.

## Zinciri kurmak ve doğrulamak

Şimdi genesis adı verilen ilk bloğu üretip yeni blokları son bloğa bağlayalım. Doğrulama sırasında hem kayıtlı hash’i yeniden hesaplıyor hem de bağlantıları ve iş kanıtını kontrol ediyoruz.

```python
class Blockchain:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty
        self.chain = []
        self.add_block(['Genesis'])

    def add_block(self, transactions):
        previous = self.chain[-1].hash if self.chain else '0' * 64
        block = Block(len(self.chain), transactions, previous)
        block.mine(self.difficulty)
        self.chain.append(block)
        print(f'Blok üretildi: {block.hash}')

    def is_valid(self):
        target = '0' * self.difficulty
        for i, block in enumerate(self.chain):
            if block.hash != block.calculate_hash():
                return False
            if not block.hash.startswith(target):
                return False
            if i > 0 and block.previous_hash != self.chain[i - 1].hash:
                return False
        return True

chain = Blockchain(difficulty=4)
chain.add_block(['Ayşe -> Can: 5 coin'])
chain.add_block(['Can -> Ece: 2 coin'])
print('Zincir geçerli mi?', chain.is_valid())
```

Bir işlemi sonradan değiştirip `is_valid()` çağırırsanız sonuç `False` olacaktır. Saldırgan yalnızca ilgili bloğu değil, ondan sonra gelen bütün blokları yeniden kazmalıdır. Dürüst ağ bu sırada yeni bloklar üretmeye devam ettiği için saldırganın yetişmesi giderek zorlaşır.

Bu örnek eğitim amaçlıdır; eşler arası iletişim, dijital imzalar, ödüller, çatallanma seçimi ve dinamik zorluk ayarı içermez. Yine de blok zincirinin sihir değil; hash bağlantıları, olasılık ve hesaplama maliyetinin zekice birleşimi olduğunu açıkça gösterir.
