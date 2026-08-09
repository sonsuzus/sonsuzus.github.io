---
layout: post
title: "Düşman Yapay Zekâsı: Sonlu Durum Makinesi mi, Davranış Ağacı mı?"
math: true
categories: 
  - Program
tags: 
  - oyun yapay zekâsı
  - sonlu durum makinesi
  - davranış ağacı
---

Bir düşmanın oyuncuyu görünce kovalamaya başlaması, canı azalınca kaçması ve hedefini kaybedince devriye rotasına dönmesi basit görünür. Ancak bu kararlar doğrudan kodun içine serpiştirildiğinde kısa sürede yönetilemeyen bir koşul çorbası oluşur. Sonlu Durum Makinesi ve Davranış Ağacı, aynı düşman davranışını daha düzenli, test edilebilir ve genişletilebilir biçimde modelleyen iki klasik oyun yapay zekâsı tekniğidir.
``
## Önce problemi modelleyelim

Örnek düşmanımız dört temel eylem gerçekleştirsin: devriye gezme, oyuncuyu kovalama, saldırma ve kaçma. Karar verirken oyuncuya olan $d$ mesafesini, düşmanın $h$ sağlık oranını ve oyuncunun görülüp görülmediğini kullanalım.

Saldırı koşulu basitçe şöyle ifade edilebilir:

$$Attack = visible \land d \leq d_{attack}$$

Kaçma kararı ise $h < 0.2$ olduğunda etkinleşsin. Buradaki önemli ayrım şudur: Sonlu Durum Makinesi, karakterin **hangi durumda bulunduğuna**; Davranış Ağacı ise hedefe ulaşmak için **hangi kararların hangi sırayla sınanacağına** odaklanır.

## Sonlu Durum Makinesi

Sonlu Durum Makinesi veya FSM, durumlar ve bu durumlar arasındaki geçişlerden oluşur. Düşman aynı anda yalnızca bir etkin durumda bulunur. Matematiksel olarak FSM, $M=(S,\Sigma,\delta,s_0)$ biçiminde gösterilebilir. Burada $S$ durum kümesi, $\Sigma$ girdiler, $\delta$ geçiş fonksiyonu ve $s_0$ başlangıç durumudur.

Aşağıdaki C# örneği temel karar döngüsünü uygular:

```csharp
enum EnemyState { Patrol, Chase, Attack, Flee }

EnemyState state = EnemyState.Patrol;

void UpdateAI(bool visible, float distance, float health)
{
    if (health < 0.2f)
        state = EnemyState.Flee;
    else if (!visible)
        state = EnemyState.Patrol;
    else if (distance <= attackRange)
        state = EnemyState.Attack;
    else
        state = EnemyState.Chase;

    ExecuteState();
}

void ExecuteState()
{
    switch (state)
    {
        case EnemyState.Patrol: FollowPatrolRoute(); break;
        case EnemyState.Chase: MoveToPlayer(); break;
        case EnemyState.Attack: UseWeapon(); break;
        case EnemyState.Flee: MoveAwayFromPlayer(); break;
    }
}
```

Bu kod, sensör verilerini tek bir duruma dönüştürür ve ilgili eylemi çalıştırır. Küçük düşmanlar için okunaklıdır; fakat onlarca durum eklendiğinde her durumdan diğerlerine geçiş ihtimali doğar. En kötü durumda geçiş sayısı yaklaşık $|S|(|S|-1)$ olur. İşte spagetti canavarı burada doğar!

## Davranış Ağacı

Davranış Ağacı, kökten yapraklara doğru değerlendirilen hiyerarşik düğümler kullanır. Her düğüm `Success`, `Failure` veya `Running` sonucu döndürür. `Selector`, başarılı olan ilk çocuğu seçerken `Sequence`, bütün çocukların sırayla başarılı olmasını bekler.

```text
Selector
├── Sequence: Kaç
│   ├── Sağlık %20 altında mı?
│   └── Oyuncudan uzaklaş
├── Sequence: Saldır
│   ├── Oyuncu görünür mü?
│   ├── Menzilde mi?
│   └── Silah kullan
├── Sequence: Kovala
│   ├── Oyuncu görünür mü?
│   └── Oyuncuya ilerle
└── Devriye gez
```

Basitleştirilmiş düğüm mantığı şöyledir:

```csharp
Node root = new Selector(
    new Sequence(IsLowHealth, FleeFromPlayer),
    new Sequence(CanSeePlayer, IsInRange, AttackPlayer),
    new Sequence(CanSeePlayer, ChasePlayer),
    Patrol
);

void UpdateAI() => root.Tick();
```

Ağaç her güncellemede öncelikli davranışları yukarıdan aşağı sınar. Böylece kaçma davranışı saldırıdan önce değerlendirilir. Yeni bir “yardım çağır” dalı eklemek, çoğu zaman mevcut düğümlerin içini değiştirmeden mümkündür.

## Karşılaştırma

| Ölçüt | FSM | Davranış Ağacı |
|---|---|---|
| Temel yapı | Durum ve geçiş | Hiyerarşik düğüm |
| Öğrenme eğrisi | Düşük | Orta |
| Küçük yapay zekâ | Çok uygun | Gereğinden kapsamlı olabilir |
| Büyük davranış seti | Geçişler karmaşıklaşır | Modüler biçimde büyür |
| Hata ayıklama | Etkin durum izlenir | Çalışan dal izlenir |
| Yeniden kullanım | Sınırlı | Alt ağaçlar paylaşılabilir |

## Hangisini seçmeli?

Kapı, tuzak veya üç-dört davranışlı sıradan düşmanlar için FSM yalın ve hızlıdır. Boss karakterleri, takım koordinasyonu ya da önceliği sık değişen kararlar için Davranış Ağacı daha sürdürülebilirdir. İki yaklaşım rakip olmak zorunda da değildir: Üst seviyede FSM ile “Savaş” ve “Keşif” kipleri yönetilirken, her kipin ayrıntıları bir Davranış Ağacıyla çalıştırılabilir. En iyi oyun yapay zekâsı, en karmaşık sistem değil; tasarım ekibinin davranışı rahatça anlayıp değiştirebildiği sistemdir.
