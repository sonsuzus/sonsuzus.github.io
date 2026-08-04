---
layout: post
title: "Sınıflar ve Erişim Belirleyicilerle Güvenli Kapsülleme"
math: true
categories: 
  - Bilgi
tags: 
  - nesne yönelimli programlama
  - sınıflar
  - kapsülleme
---

Bir sınıfı yalnızca değişkenleri ve metotları bir araya getiren bir kutu olarak düşünmek eksik kalır. İyi tasarlanmış bir sınıf, kendi verisini koruyan ve dış dünyaya kontrollü bir kullanım alanı sunan küçük bir kale gibidir. `public`, `private` ve `protected` erişim belirleyicileri ise bu kalenin hangi kapılarının herkese, hangilerinin yalnızca içeridekilere açılacağını belirler.
``

## Kapsülleme neden gereklidir?

Nesne yönelimli programlamanın temel ilkelerinden biri olan **kapsülleme**, bir nesnenin durumunu temsil eden veriler ile bu verileri yöneten davranışların aynı sınıfta toplanmasıdır. Ancak asıl amaç, alanları sınıfın içine taşımaktan daha fazlasıdır: Verinin geçersiz veya tehlikeli biçimde değiştirilmesini önlemek.

Bir sınıfın durumunu $S$, izin verilen geçerli durumlar kümesini ise $V$ ile gösterelim. İyi bir sınıfın hedefi şudur:

$$S \in V$$

Dışarıdaki kod alanları doğrudan değiştirebiliyorsa bu koşul kolayca bozulabilir. Örneğin bir banka hesabının bakiyesi, kontrol yapılmadan negatif bir değere dönüştürülebilir. Kapsülleme sayesinde değişiklikler metotlar üzerinden geçirilir ve sınıf kendi kurallarını korur.

## Erişim belirleyiciler ne söyler?

Java, C# ve C++ gibi dillerde ayrıntılar değişebilse de temel yaklaşım benzerdir:

| Belirleyici | Aynı sınıf | Alt sınıf | Dış kod | Yaygın kullanım |
|---|---:|---:|---:|---|
| `public` | Evet | Evet | Evet | Kullanıcıya sunulan metotlar |
| `private` | Evet | Hayır | Hayır | Alanlar ve iç yardımcı metotlar |
| `protected` | Evet | Evet | Genellikle hayır | Kalıtıma özel genişletme noktaları |

`public`, sınıfın dış dünyaya verdiği sözleşmedir. Bu nedenle her alanı veya metodu düşünmeden `public` yapmak, evin bütün kapılarını açık bırakmaya benzer. `private`, bir üyenin yalnızca tanımlandığı sınıf tarafından kullanılmasını sağlar. `protected` ise özellikle kalıtım sırasında alt sınıflara kontrollü erişim vermek için kullanılır.

## Java ile kapsüllenmiş hesap örneği

Aşağıdaki sınıf, bakiyeyi dışarıdan doğrudan değiştirmeye izin vermez:

```java
public class BankAccount {
    private String owner;
    private double balance;

    public BankAccount(String owner, double initialBalance) {
        if (initialBalance < 0) {
            throw new IllegalArgumentException("Başlangıç bakiyesi negatif olamaz.");
        }
        this.owner = owner;
        this.balance = initialBalance;
    }

    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Tutar pozitif olmalıdır.");
        }
        balance += amount;
    }

    public boolean withdraw(double amount) {
        if (amount <= 0 || amount > balance) {
            return false;
        }
        balance -= amount;
        return true;
    }

    public double getBalance() {
        return balance;
    }
}
```

Burada `balance` alanı `private` olduğu için aşağıdaki müdahale derleme hatası üretir:

```java
BankAccount account = new BankAccount("Ada", 1000);
// account.balance = -5000; // Erişim yasak!
account.deposit(250);
account.withdraw(100);
```

`deposit` ve `withdraw` metotları birer kontrol noktasıdır. Para yatırıldıktan sonra yeni bakiye matematiksel olarak

$$B_{yeni} = B_{eski} + T, \quad T > 0$$

şeklinde hesaplanır. Böylece nesnenin iş kuralları tek yerde uygulanır.

## Protected kullanırken dikkat

Bir alt sınıfın bazı davranışları özelleştirmesi gerekiyorsa `protected` yararlı olabilir:

```java
public class RewardAccount extends BankAccount {
    protected double calculateBonus(double amount) {
        return amount * 0.02;
    }
}
```

Ancak alanları doğrudan `protected` yapmak, alt sınıfların geçersiz değerler atamasına yol açabilir. Bu yüzden alanları yine `private` tutup, gerektiğinde `protected` metotlar sağlamak daha güvenlidir. Kalıtım var diye kasanın anahtarını teslim etmek gerekmez!

## Getter ve setter her zaman çözüm mü?

Her `private` alan için otomatik olarak getter ve setter üretmek gerçek kapsülleme değildir. Kontrolsüz bir `setBalance()` metodu, alanı `public` yapmakla neredeyse aynı riski taşır. Sınıfın teknik yapısını değil, anlamlı davranışlarını dışarı açmak gerekir. `setBalance(500)` yerine `deposit(500)` denmesi, işlemin niyetini ve kurallarını açıkça ifade eder.

Özetle alanlarda varsayılan tercihiniz `private`, dışarıya sunulan güvenli davranışlarda `public`, alt sınıfların kontrollü biçimde kullanacağı genişletme noktalarında ise `protected` olmalıdır. Böylece sınıflar yalnızca veri taşımaz; kendi tutarlılığını koruyan güvenilir yazılım bileşenlerine dönüşür.
