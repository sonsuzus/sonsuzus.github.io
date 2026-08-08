---
layout: post
title: "Pekiştirmeli Öğrenme: Ödüllerle Strateji Öğrenen Ajanlar"
math: true
categories: 
  - Bilgi
tags: 
  - pekiştirmeli öğrenme
  - yapay zeka
  - makine öğrenmesi
---

Bir labirentte olduğunuzu düşünün: Haritanız yok, bazı yollar çıkmaza ulaşıyor ve doğru kapıyı bulduğunuzda puan kazanıyorsunuz. Pekiştirmeli öğrenme, bir yapay zekâ ajanının benzer biçimde çevresiyle etkileşime girerek hangi kararların uzun vadede daha iyi sonuç verdiğini öğrenmesini sağlar. Ajana her adımı ezberletmek yerine ona hedefi, olası eylemleri ve geri bildirim mekanizmasını veririz; gerisini deneme, yanılma ve biraz da matematik halleder.

``

## Temel fikir: Ajan, ortam ve ödül

Pekiştirmeli öğrenmede **ajan**, belirli bir **durumda** eylem seçer. **Ortam** bu eyleme karşılık yeni bir durum ve sayısal bir ödül üretir. Bu döngü, ajan başarılı bir strateji geliştirene kadar sürer.

| Kavram | Anlamı | Oyun örneği |
|---|---|---|
| Ajan | Karar veren sistem | Oyuncu karakteri |
| Durum ($s$) | Ortamın mevcut görünümü | Karakterin konumu |
| Eylem ($a$) | Ajanın seçebileceği hamle | Sağa veya sola gitmek |
| Ödül ($r$) | Hamlenin sayısal geri bildirimi | Hazine için $+10$ |
| Policy ($\pi$) | Duruma göre eylem seçme stratejisi | Tehlikede geri çekilmek |

Amaç, yalnızca anlık ödülü değil, gelecekte elde edilecek toplam ödülü büyütmektir. İndirgenmiş toplam getiri şu şekilde gösterilir:

$$G_t = r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + \cdots$$

Buradaki $\gamma$, $0 \leq \gamma < 1$ aralığındaki **iskonto katsayısıdır**. Küçük bir $\gamma$, ajanı kısa vadeli kazançlara yöneltir. Büyük bir değer ise gelecekteki ödülleri önemseyen, daha sabırlı bir ajan oluşturur.

## Markov karar süreci

Birçok pekiştirmeli öğrenme problemi, Markov Karar Süreci ile modellenir ve $(S, A, P, R, \gamma)$ bileşenleriyle ifade edilir. $S$ durumları, $A$ eylemleri, $P$ geçiş olasılıklarını, $R$ ödülleri temsil eder. Markov varsayımına göre geleceği tahmin etmek için mevcut durum yeterlidir; ajanın bütün geçmişi yanında taşıması gerekmez.

Bir durumun değerini hesaplayan Bellman eşitliği, bugünkü ödülle gelecekteki olası değeri birleştirir:

$$V^{\pi}(s)=\sum_a \pi(a|s)\sum_{s'}P(s'|s,a)\left[R(s,a,s')+\gamma V^{\pi}(s')\right]$$

Bu ifade ilk bakışta matematik canavarı gibi görünse de mesajı basittir: “Bir durumun değeri, şimdi kazanacağım ödül ile sonra ulaşacağım durumların değeridir.”

## Keşif mi, sömürü mü?

Ajan sürekli bildiği en iyi eylemi seçerse daha iyi seçenekleri keşfedemeyebilir. Sürekli rastgele davranırsa da öğrendiklerinden yararlanamaz. Bu ikileme **exploration-exploitation** dengesi denir.

| Yaklaşım | Avantaj | Risk |
|---|---|---|
| Keşif | Yeni ve daha iyi yollar bulabilir | Kötü eylemler seçebilir |
| Sömürü | Bilinen ödülü verimli toplar | Yerel optimumda kalabilir |
| $\epsilon$-greedy | İkisini basitçe dengeler | $\epsilon$ ayarı gerektirir |

$\epsilon$-greedy yaklaşımında ajan, $\epsilon$ olasılıkla rastgele; diğer durumlarda en yüksek değere sahip eylemi seçer.

## Q-Learning ile küçük bir uygulama

Q-Learning, ortam modelini önceden bilmeden durum-eylem değerlerini öğrenir. Güncelleme kuralı şöyledir:

$$Q(s,a) \leftarrow Q(s,a)+\alpha\left[r+\gamma\max_{a'}Q(s',a')-Q(s,a)\right]$$

Aşağıdaki Python kodu bu güncellemenin özünü gösterir:

```python
import random

Q = {}
alpha, gamma, epsilon = 0.1, 0.95, 0.1

def value(state, action):
    return Q.get((state, action), 0.0)

def choose_action(state, actions):
    if random.random() < epsilon:
        return random.choice(actions)  # Keşif
    return max(actions, key=lambda a: value(state, a))  # Sömürü

def update(state, action, reward, next_state, next_actions):
    old_q = value(state, action)
    best_next = max(value(next_state, a) for a in next_actions)
    target = reward + gamma * best_next
    Q[(state, action)] = old_q + alpha * (target - old_q)
```

`choose_action` keşif-sömürü dengesini kurarken `update`, alınan ödülü ve gelecekteki en iyi tahmini kullanarak Q tablosunu düzeltir. Eğitim ilerledikçe yüksek Q değerlerine sahip eylemler ajanın policy’sini oluşturur.

Pekiştirmeli öğrenme robotik, oyun, trafik kontrolü ve kaynak yönetimi gibi alanlarda güçlüdür. Ancak ödül yanlış tasarlanırsa ajan hedefin ruhunu değil, puan kazanmanın açığını öğrenebilir. Kısacası iyi bir ajan yetiştirmek için yalnızca algoritma değil, doğru ödül tasarımı da gerekir; yoksa robotunuz odayı temizlemek yerine kiri halının altına süpürebilir!
