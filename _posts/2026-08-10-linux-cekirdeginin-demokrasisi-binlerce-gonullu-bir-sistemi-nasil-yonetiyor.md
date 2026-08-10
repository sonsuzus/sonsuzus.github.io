---
layout: post
title: "Linux Çekirdeğinin Demokrasisi: Binlerce Gönüllü Bir Sistemi Nasıl Yönetiyor?"
math: true
categories: 
  - Bilgi
tags: 
  - Linux
  - Açık Kaynak
  - Yönetişim
  - Demokrasi
  - Git
---

Linux çekirdeği, tek bir merkezî otoritenin yazdığı dev bir program değildir; şirket çalışanları, bağımsız geliştiriciler, akademisyenler ve donanım üreticilerinden oluşan küresel bir ağın ortak ürünüdür. Bu ağın başarısı, “herkes eşit oy kullanır” türünden saf bir demokrasiye değil; teknik uzmanlık, itibar, şeffaf müzakere ve yetki devrine dayanan karma bir yönetişim modeline dayanır. Dolayısıyla Linux’u anlamak, yalnızca C kodu okumak değil, dijital çağda katılımın nasıl örgütlenebileceğini incelemektir.
``

Siyasi katılım kuramları vatandaşların karar alma süreçlerine hangi araçlarla katıldığını sorgular. Linux dünyasında vatandaşın karşılığı katkıcıdır; dilekçe yerine **patch** gönderir, meclis tartışması yerine e-posta listelerinde teknik gerekçe sunar. Katılımın temel birimi oy değil, denetlenebilir emektir. Bir değişiklik önerisinin değeri, öneriyi yapan kişinin ününden çok kodun kalitesi, test sonuçları ve mevcut mimariyle uyumuyla ölçülür.

Bu süreçte Git, yalnızca sürüm kontrol sistemi değil, aynı zamanda bir tür anayasal kayıt defteridir. Her commit; kim tarafından, ne zaman ve hangi açıklamayla önerildiğini saklar. İnceleme zincirindeki `Reviewed-by`, `Acked-by` ve `Signed-off-by` satırları da kararın sosyal tarihçesini görünür kılar. Böylece tartışmalı bir karar geriye dönük olarak incelenebilir; bu, demokratik kurumların hesap verebilirlik ilkesine benzer.

| Siyasi katılım kavramı | Linux çekirdeğindeki karşılığı | Gücü | Riski |
|---|---|---|---|
| Temsili demokrasi | Alt sistem bakımcıları | Hızlı uzmanlaşmış kararlar | Bakımcı darboğazı |
| Müzakereci demokrasi | E-posta listesi tartışmaları | Gerekçeler açıktır | Yeni katılımcı için yüksek eşik |
| Meritokrasi | Sürekli, kaliteli katkı | Teknik güven üretir | Görünmez emek dışarıda kalabilir |
| Federalizm | Alt sistemlerin özerkliği | Karmaşıklık bölünür | Politikalar tutarsızlaşabilir |

Linux’un hiyerarşisi bu nedenle paradoksal biçimde hem merkezî hem dağıtıktır. Bir sürücü alt sisteminin bakımcısı kendi alanında yüksek özerkliğe sahiptir; ancak değişiklikler sonunda üst düzey bakımcıların ve çekirdek sürüm yöneticisinin ağacına akar. Bu yapı, federal devletlerdeki yerel yönetim–merkez ilişkisini andırır. Yetki, coğrafyaya göre değil, teknik sınıra göre dağıtılır.

Karar kalitesini basitleştirilmiş bir modelle şöyle düşünebiliriz:

$$K = U \times I \times S$$

Burada $K$ karar kalitesi, $U$ uzmanlık, $I$ inceleme yoğunluğu ve $S$ süreç şeffaflığıdır. Bir değişiklik çok parlak olsa bile yeterince incelenmezse ($I$ düşükse) çekirdeğe girmesi zorlaşır. Bu yaklaşım, çoğunluğun anlık tercihinden ziyade hataya dayanıklı karar üretmeyi hedefler.

Örneğin orta düzeyde bir katkı akışı şöyledir:

```bash
# Çalışma dalında değişikliği kaydet
git add drivers/foo.c
git commit -s -m "foo: correct timeout handling"

# Patch serisini bakımcıya gönder
git format-patch -1 --cover-letter
git send-email 0000-cover-letter.patch 0001-foo-correct-timeout-handling.patch
```

`-s` seçeneği, geliştiricinin katkı sertifikasını ekler; `format-patch` ise değişikliği e-posta ile tartışılabilir bir belgeye dönüştürür. Ardından inceleme yorumları gelir, geliştirici yeni sürüm gönderir ve bakımcı uygun bulursa değişikliği kendi dalına alır. Bu döngü, kanun tasarısının komisyonlarda olgunlaşmasına benzer; fakat burada nihai test çoğu zaman çalışan koddur.

Yine de Linux kusursuz bir dijital cumhuriyet değildir. Teknik dil, zaman maliyeti, sert inceleme kültürü ve kurumsal sponsorların ağırlığı katılımı eşitsizleştirebilir. “Kim konuşabilir?” sorusu kadar “kimin kod yazmaya zamanı var?” sorusu da politiktir. Açık kaynak yönetişiminin büyük dersi şudur: Açıklık, yalnızca deponun herkese açık olması değildir; itirazın duyulabildiği, kararın gerekçelendirildiği ve katkının iz bırakabildiği süreçler kurmaktır.
