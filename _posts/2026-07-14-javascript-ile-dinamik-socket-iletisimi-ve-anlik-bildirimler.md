---
layout: post
title: "JavaScript ile Dinamik Socket İletişimi ve Anlık Bildirimler"
math: true
categories: 
  - Program
tags: 
  - javascript
  - socket.io
  - websocket
  - anlık-bildirim
---

Bir forumda yeni cevap geldiğinde sayfayı yenilemeden bildirim almak ya da mesajlaşma uygulamasında karşı tarafın yazdığını anında görmek artık lüks değil, kullanıcı beklentisi. JavaScript ile dinamik socket iletişimi kurarak istemci ve sunucu arasında sürekli açık kalan, düşük gecikmeli bir kanal oluşturabiliriz. Amaç basit: kullanıcı beklemeden, sistem bağırmadan, veri doğru zamanda doğru kişiye ulaşsın.
``

## Socket Mantığı: HTTP’den Farkı Ne?

Klasik HTTP modelinde tarayıcı sunucuya istek atar, sunucu cevap verir ve bağlantı kapanır. Bu model forum sayfası yüklemek için harikadır; fakat “yeni mesaj var mı?” sorusunu her 2 saniyede bir sormak verimsizdir. Socket yaklaşımında ise bağlantı açık kalır. Sunucu, olay oluştuğunda istemciye kendisi veri gönderir.

Basit gecikme fikrini şöyle düşünebiliriz: $latency = t_{receive} - t_{send}$. Canlı bildirimlerde hedef bu değeri olabildiğince küçük tutmaktır. Polling’de bu süre istek aralığına bağlıyken, WebSocket’te olay gerçekleştiği anda veri kanala yazılır.

| Yöntem | Çalışma Şekli | Avantaj | Dezavantaj |
|---|---|---|---|
| Polling | İstemci belirli aralıklarla sorar | Kurulumu kolay | Gereksiz trafik üretir |
| Long Polling | Sunucu cevap için bekler | Daha az istek | Bağlantı yönetimi karmaşıklaşır |
| WebSocket | İki yönlü açık kanal | Gerçek zamanlı ve verimli | Durum yönetimi gerekir |
| Server-Sent Events | Sunucudan istemciye tek yönlü akış | Bildirim için pratik | İstemciden sunucuya kanal yok |

## Temel Mimari

Canlı bildirim sisteminde genellikle üç ana parça vardır: istemci, socket sunucusu ve veri kaynağı. Kullanıcı yeni mesaj gönderdiğinde önce API veya socket sunucusu bu olayı alır. Ardından ilgili odaya, kullanıcıya veya gruba bildirim yayılır. Buradaki kritik kavram “room” yani odadır. Örneğin forumdaki her konu bir oda olabilir.

$$aktifBildirimler = kullaniciSayisi * ortalamaOlayFrekansi$$

Bu ifade bize ölçekleme baskısını hatırlatır. 10 kullanıcıda çalışan sistem, 10.000 kullanıcıda bağlantı, bellek ve yayın stratejisi ister.

## Sunucu Tarafı: Socket.IO ile Başlangıç

Aşağıdaki örnekte Node.js ve Socket.IO kullanıyoruz. Kodun görevi, kullanıcıyı ilgili forum konusunun odasına almak ve yeni cevap geldiğinde sadece o odaya bildirim göndermek.

```js
import { Server } from 'socket.io';
import http from 'http';

const server = http.createServer();
const io = new Server(server, {
  cors: {
    origin: 'http://localhost:3000'
  }
});

io.on('connection', (socket) => {
  console.log('Bağlandı:', socket.id);

  socket.on('forum:join', ({ topicId, userId }) => {
    socket.join(`topic:${topicId}`);
    socket.data.userId = userId;
  });

  socket.on('forum:new-reply', ({ topicId, message, author }) => {
    io.to(`topic:${topicId}`).emit('notification:new', {
      type: 'reply',
      topicId,
      message,
      author,
      sentAt: Date.now()
    });
  });

  socket.on('disconnect', () => {
    console.log('Ayrıldı:', socket.id);
  });
});

server.listen(4000);
```

Burada `forum:join` istemcinin hangi konuyu dinleyeceğini belirler. `forum:new-reply` ise yeni cevap olayını alır ve sadece `topic:123` gibi ilgili odaya yayın yapar. Böylece herkes her bildirimi almaz; sistem daha temiz ve ekonomik çalışır.

## İstemci Tarafı: Dinleme ve Yeniden Bağlanma

Tarayıcı tarafında bağlantı kurar, odaya katılır ve bildirim olaylarını dinleriz. Bağlantı koparsa Socket.IO otomatik yeniden bağlanmayı destekler; yine de kullanıcı deneyimi için durum bilgisini göstermek akıllıcadır.

```js
import { io } from 'socket.io-client';

const socket = io('http://localhost:4000', {
  transports: ['websocket'],
  reconnectionAttempts: 5,
  reconnectionDelay: 1000
});

socket.on('connect', () => {
  console.log('Canlı kanal açık');
  socket.emit('forum:join', { topicId: 42, userId: 7 });
});

socket.on('notification:new', (payload) => {
  console.log('Yeni bildirim:', payload.message);
  showToast(`${payload.author}: ${payload.message}`);
});

socket.on('disconnect', () => {
  console.log('Bağlantı koptu, tekrar deneniyor...');
});

function showToast(text) {
  const div = document.createElement('div');
  div.textContent = text;
  div.className = 'toast';
  document.body.appendChild(div);
  setTimeout(() => div.remove(), 4000);
}
```

Bu yapı sayesinde kullanıcı forum konusunu açık tutarken yeni cevapları anında görür. Mesajlaşma platformunda da aynı mantık `room:${conversationId}` ile uygulanabilir.

## Güvenlik ve Performans İpuçları

Socket bağlantısı açık diye her olaya güvenmemeliyiz. Kullanıcının gerçekten ilgili odaya erişim yetkisi var mı, sunucuda kontrol edilmelidir. Ayrıca olay adlarını standartlaştırmak, payload boyutunu küçük tutmak ve gereksiz yayınlardan kaçınmak gerekir.

| Problem | Çözüm |
|---|---|
| Herkese gereksiz bildirim gitmesi | Room bazlı yayın kullan |
| Bağlantı kopmaları | Yeniden bağlanma stratejisi ekle |
| Yetkisiz dinleme | Token doğrulama yap |
| Yüksek trafik | Payload sadeleştir, Redis adapter kullan |

Özetle dinamik socket iletişimi, modern web uygulamalarının nabzıdır. Doğru oda modeli, güvenli kimlik doğrulama ve kontrollü yayın stratejisiyle forumlar, sohbetler ve bildirim panelleri gerçekten canlı hissettirilir.
