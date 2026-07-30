---
layout: post
title: "Blockchain'in Sosyolojik Vaadi: Güvenmeden Güvenmek Mümkün mü?"
math: true
categories: 
  - Bilgi
tags: 
  - blockchain
  - merkeziyetsizlik
  - toplumsal güven
---

Blockchain çoğu zaman “güveni ortadan kaldıran teknoloji” diye tanıtılır. Bu ifade etkileyicidir; fakat sosyolojik açıdan biraz fazla iddialıdır. İnsanlar Bitcoin gönderirken bankaya güvenmek zorunda olmayabilir, ancak yazılıma, kriptografiye, ağ katılımcılarına ve protokolün değişmeyeceğine ilişkin beklentilere hâlâ sahiptir. Dolayısıyla asıl soru, güvenin yok olup olmadığı değil, **kimden neye aktarıldığıdır**.

``

## Toplumsal güven ne işe yarar?

Güven, geleceğin belirsizliğini yönetmemizi sağlar. Her alışverişte satıcının geçmişini araştırmak, her sözleşmede karşı tarafı gözetlemek veya her sabah kullandığımız köprünün mühendislik hesaplarını doğrulamak zorunda kalsaydık toplumsal hayat kilitlenirdi.

Sosyolog Niklas Luhmann'a göre güven, toplumsal karmaşıklığı azaltan bir mekanizmadır. Anthony Giddens ise modern toplumlarda bireylerin yüzünü hiç görmedikleri uzmanlara ve kurumlara dayanan **soyut sistemlerden** söz eder. Banka hesabımızdaki sayı da aslında bu kurumsal güvenin dijital ifadesidir.

Basit bir modelle, bir işlemin beklenen faydasını şöyle gösterebiliriz:

$$E(U) = p \cdot K - (1-p) \cdot Z - D$$

Burada $p$ işlemin dürüst biçimde sonuçlanma olasılığı, $K$ beklenen kazanç, $Z$ olası zarar ve $D$ doğrulama maliyetidir. Geleneksel kurumlar $p$ değerini hukuk ve itibarla yükseltirken blockchain, kriptografik kanıtlarla $D$ ve manipülasyon ihtimalini azaltmaya çalışır.

## Kurumsal güven ve blockchain güveni

| Boyut | Merkezi kurum | Blockchain ağı |
|---|---|---|
| Doğrulama | Yetkili kuruluş yapar | Düğümler ve protokol yapar |
| Kayıt kontrolü | Tek veya sınırlı otorite | Dağıtık katılımcılar |
| Hata çözümü | Mahkeme, banka, yönetici | Kod, yönetişim, topluluk |
| Güven kaynağı | Hukuk ve kurumsal itibar | Kriptografi ve ekonomik teşvik |
| Temel risk | Yetkinin kötüye kullanılması | Kod hatası, çoğunluk veya yönetişim krizi |

Blockchain'in toplumsal güven kuramlarıyla örtüştüğü nokta, davranışları öngörülebilir hâle getirmesidir. Akıllı sözleşme belirli koşullarda aynı sonucu üretir; dağıtık kayıt ise geçmişin tek taraflı değiştirilmesini zorlaştırır. Böylece tanımadığımız kişilerle iş birliği yapabiliriz.

Çelişki ise “güvensiz sistem” söyleminde ortaya çıkar. Toplum yalnızca doğru kayıt üretmekten ibaret değildir. Adalet, niyet, merhamet ve istisna gibi kavramlar algoritmik kesinliğe kolayca sığmaz. Kod, “ödeme gecikti” durumunu görebilir; fakat gecikmenin deprem nedeniyle yaşandığını kendiliğinden anlayamaz.

## Kod gerçekten hakem olabilir mi?

Aşağıdaki basitleştirilmiş Solidity sözleşmesi, tarafların ödeme sırasında birbirine değil kurala güvenmesini sağlar:

```solidity
contract Escrow {
    address public buyer;
    address payable public seller;

    constructor(address payable _seller) {
        buyer = msg.sender;
        seller = _seller;
    }

    function approveDelivery() external {
        require(msg.sender == buyer, "Yalnizca alici onaylayabilir");
        seller.transfer(address(this).balance);
    }

    receive() external payable {}
}
```

Bu kod parayı emanette tutar ve alıcı teslimatı onayladığında satıcıya aktarır. Aracı banka ortadan kalkmıştır; fakat güven kaybolmamıştır. Kullanıcılar derleyiciye, blokzincir ağına, sözleşmenin hatasız olduğuna ve alıcının dürüst onay vereceğine güvenir. Fiziksel teslimat bilgisini zincire taşıyan bir oracle kullanılırsa bu kez oracle yeni güven merkezi olur.

## Merkeziyetsizlik iktidarı yok eder mi?

Merkeziyetsizlik, iktidarı otomatik olarak dağıtmaz. Büyük madencilik havuzları, doğrulayıcılar, token sahipleri ve geliştiriciler karar süreçlerinde diğer kullanıcılardan daha etkili olabilir. “Bir kişi, bir oy” yerine “bir token, bir oy” kullanıldığında ekonomik eşitsizlik doğrudan siyasal güce dönüşebilir.

Bu nedenle blockchain'in gerçek vaadi **güvenmeden güvenmek** değil, güven ilişkilerini görünür, denetlenebilir ve alternatifli hâle getirmektir. Teknoloji belirli aracılara bağımlılığı azaltabilir; ancak ortak normların, hukukun ve topluluk uzlaşmasının yerini tamamen alamaz. Kısacası blockchain güveni silmez: onu kurumdan protokole, yöneticiden topluluğa ve kapalı defterden incelenebilir koda taşır.
