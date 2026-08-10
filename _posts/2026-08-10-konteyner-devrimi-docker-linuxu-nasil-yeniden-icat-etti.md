---
layout: post
title: "Konteyner Devrimi: Docker Linux'u Nasıl Yeniden İcat Etti?"
math: true
categories: 
  - Bilgi
tags: 
  - Docker
  - Linux
  - Konteyner
  - Sanallaştırma
  - DevOps
---

Docker, Linux'a yeni bir çekirdek eklemedi; daha ilginç bir şey yaptı: Çekirdeğin yıllardır sunduğu izolasyon mekanizmalarını geliştiricinin günlük iş akışına taşıdı. Böylece “benim makinemde çalışıyor” cümlesi, yazılım dünyasının en meşhur mazeretlerinden biri olmaktan çıkmaya başladı. Konteynerler, uygulamayı kodu, bağımlılıkları, çalışma zamanı ve yapılandırmasıyla birlikte paketleyerek işletim sistemi tasarımına daha modüler bir bakış getirdi.
``

## Sanal makine mi, konteyner mi?

Klasik sanallaştırmada bir hipervizör üzerinde birden fazla sanal makine (VM) çalışır. Her VM, kendi misafir işletim sistemi çekirdeğine, sürücülerine ve kullanıcı alanına sahiptir. Bu yaklaşım güçlü bir izolasyon sağlar; ancak her makinenin ayrı bir işletim sistemi yüklemesi maliyetlidir.

Docker konteynerleri ise ana makinenin Linux çekirdeğini paylaşır. Her konteyner, kullanıcı alanında bağımsız bir Linux sistemi gibi görünür; fakat gerçek anlamda ayrı bir çekirdek çalıştırmaz. Bu nedenle açılış süreleri saniyelerden milisaniyelere iner ve aynı donanım üzerinde çok daha fazla iş yükü barındırılabilir.

| Özellik | Sanal Makine | Docker Konteyneri |
|---|---|---|
| Çekirdek | Her VM için ayrı | Ana makineyle ortak |
| Başlatma süresi | Saniyeler veya dakikalar | Milisaniyeler veya saniyeler |
| Kaynak maliyeti | Daha yüksek | Daha düşük |
| İzolasyon seviyesi | Çok güçlü | Çekirdek paylaşımı nedeniyle göreli |
| Taşınabilirlik | Disk imajı odaklı | İmaj katmanları odaklı |

Bu farkı kabaca şöyle düşünebiliriz: Bir sunucunun kullanılabilir kaynağı $R$ ve tek bir iş yükünün ihtiyacı $r$ olsun. Sanal makinede işletim sistemi ek yükü $o_{vm}$ iken konteynerde bu maliyet $o_c$ olur. Yaklaşık kapasite:

$$N_{vm} = \left\lfloor \frac{R}{r + o_{vm}} \right\rfloor, \qquad N_c = \left\lfloor \frac{R}{r + o_c} \right\rfloor$$

Genellikle $o_c \ll o_{vm}$ olduğundan, konteyner yoğunluğu daha yüksektir.

## Docker'ın Linux sihri: namespace ve cgroup

Docker'ın “her uygulama kendi makinesindeymiş gibi” davranmasını sağlayan iki temel Linux özelliği vardır. **Namespace**'ler süreçlerin gördüğü dünyayı ayırır: işlem kimlikleri (PID), ağ arabirimleri, kullanıcılar, dosya sistemi bağlama noktaları ve IPC kaynakları ayrı görünür. Bir konteynerdeki süreç, dışarıdaki yüzlerce süreci göremez.

**Control group** ya da cgroup'lar ise kaynak tüketimini düzenler. Bir uygulamaya kaç CPU döngüsü, ne kadar bellek veya ne kadar disk I/O verileceğini belirleyebilirsiniz. Örneğin bir servis tüm belleği tüketip komşu servisleri deviremesin diye limit koymak mümkündür.

```bash
# Nginx'i arka planda çalıştırır ve belleği 256 MB ile sınırlar
docker run -d \
  --name web-gateway \
  --memory=256m \
  -p 8080:80 \
  nginx:alpine
```

Bu komutta Docker, imajı katmanlardan oluşturur, yeni namespace'ler üretir ve cgroup üzerinden bellek sınırını uygular. `-p 8080:80` ise ana makinenin 8080 numaralı portunu konteyner içindeki 80 numaralı porta bağlar.

## İmaj katmanları: tekrarın önündeki akıllı engel

Docker imajları tek parça dev diskler değildir; katmanlı dosya sistemi kullanırlar. Bir `FROM python:3.12-slim` satırı, daha önce indirilmiş katmanlardan yararlanabilir. Aynı tabanı kullanan on farklı uygulama, taban katmanını on kez saklamak zorunda kalmaz.

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

Bu Dockerfile'ın önemli noktası sıralamasıdır: Bağımlılık listesi önce kopyalanır. Uygulama kodu değişse bile `requirements.txt` değişmediyse Docker bağımlılık katmanını önbellekten kullanabilir. Bu, derleme sürelerini ciddi biçimde azaltır.

## İşletim sistemi tasarımına etkisi

Docker, Linux'u tek bir büyük sunucu olarak değil, paylaşılabilir bir uygulama çalıştırma platformu olarak düşünmemizi sağladı. Süreç izolasyonu, kaynak kotaları ve deklaratif imajlar; mikroservisler, CI/CD hatları ve Kubernetes gibi orkestrasyon araçlarının temelini oluşturdu. Yine de konteyner bir güvenlik duvarı değildir: çekirdek ortak olduğu için güncel imajlar, en az yetki ilkesi ve güvenlik profilleri kritik önem taşır. Konteyner devriminin asıl başarısı, Linux'un eski ama güçlü yapıtaşlarını modern yazılım üretiminin ortak diline çevirmesidir.
