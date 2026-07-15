---
layout: post
title: "JavaScript ile Mantık Bulmacaları Çözücüleri: Tarayıcıda Adım Adım Algoritma Şovu"
math: true
categories: 
  - Proje
tags: 
  - javascript
  - algoritma
  - bulmaca
  - backtracking
  - web
---

Bir Sudoku karesine bakıp beyninizin fanlarının hızlandığını hissettiyseniz, yalnız değilsiniz. Güzel haber şu: JavaScript ile tarayıcı üzerinde çalışan, hem bulmacayı çözen hem de çözüm adımlarını görselleştiren etkileşimli çözücüler yazabiliriz. Bu yazıda mantık bulmacalarını sadece kodla çözmeyi değil, algoritmanın nasıl düşündüğünü kullanıcıya sahne sahne göstermeyi konuşacağız.
``

## Bulmaca çözmek aslında arama problemidir

Birçok mantık bulmacası, bilgisayar bilimi açısından bir **durum uzayı araması** problemidir. Elimizde başlangıç durumu, geçerli hamle kuralları ve hedef durum vardır. Örneğin Sudoku için hedef, her satırda, sütunda ve 3x3 kutuda 1’den 9’a kadar sayıların çakışmadan yerleşmesidir.

Teorik olarak her boş hücre için olasılıkları deneriz. Eğer $b$ her adımda ortalama seçenek sayısı, $d$ ise boş hücre sayısıysa kaba karmaşıklık $O(b^d)$ olur. Kulağa korkutucu geliyor; çünkü gerçekten de öyle. Ama kısıtlar ve akıllı seçim stratejileriyle arama ağacını ciddi biçimde budayabiliriz.

| Yaklaşım | Mantık | Avantaj | Dezavantaj |
|---|---|---|---|
| Brute force | Tüm olasılıkları dener | Basit uygulanır | Çok yavaş olabilir |
| Backtracking | Hatalı yolda geri döner | Pratik ve anlaşılır | Kötü seçimlerde dallanır |
| Constraint propagation | İmkansız seçenekleri erken eler | Çok hızlandırır | Kuralları modellemek gerekir |
| Heuristic seçim | En az seçenekli hücreyi seçer | Aramayı küçültür | Ek hesaplama ister |

## Tarayıcı neden harika bir oyun alanı?

Tarayıcı bize üç güzel şey verir: DOM ile görsel arayüz, Canvas/SVG ile çizim ve `async/await` ile adım adım animasyon. Böylece algoritma sadece sonucu basmaz; hangi hücreyi denediğini, nerede çuvalladığını ve neden geri döndüğünü de gösterir. Kullanıcı için bu, kara kutu yerine cam kutu deneyimidir.

Aşağıdaki örnek, basitleştirilmiş bir Sudoku çözücünün kalbini gösterir. Amaç, boş hücre bulmak, geçerli sayıları denemek ve çıkmaz sokakta geri almaktır.

```js
function findEmpty(board) {
  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      if (board[r][c] === 0) return { r, c };
    }
  }
  return null;
}

function isValid(board, r, c, n) {
  for (let i = 0; i < 9; i++) {
    if (board[r][i] === n || board[i][c] === n) return false;
  }

  const sr = Math.floor(r / 3) * 3;
  const sc = Math.floor(c / 3) * 3;

  for (let i = sr; i < sr + 3; i++) {
    for (let j = sc; j < sc + 3; j++) {
      if (board[i][j] === n) return false;
    }
  }
  return true;
}
```

Bu iki fonksiyon hakem gibi çalışır. `findEmpty`, sıradaki problemi bulur; `isValid` ise önerilen hamlenin kurallara uygun olup olmadığını söyler. Şimdi buna görsellik ekleyelim.

```js
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

async function solve(board, render) {
  const cell = findEmpty(board);
  if (!cell) return true;

  for (let n = 1; n <= 9; n++) {
    if (isValid(board, cell.r, cell.c, n)) {
      board[cell.r][cell.c] = n;
      render(board, cell, 'try');
      await sleep(80);

      if (await solve(board, render)) return true;

      board[cell.r][cell.c] = 0;
      render(board, cell, 'backtrack');
      await sleep(80);
    }
  }
  return false;
}
```

Burada `render` fonksiyonu arayüzü günceller. `try` durumunda hücre yeşil, `backtrack` durumunda kırmızı gösterilebilir. Böylece kullanıcı algoritmanın düşündüğü yolları izler.

## Daha zeki çözücü: en az adaylı hücre

Sıradaki boş hücreyi soldan sağa seçmek kolaydır ama her zaman akıllıca değildir. Daha iyi strateji, aday sayısı en az olan hücreyi seçmektir. Buna genellikle **MRV**, yani minimum remaining values denir. Eğer bir hücrede sadece 2 ihtimal, diğerinde 7 ihtimal varsa önce 2 ihtimalli hücreye bakmak mantıklıdır.

Bu yaklaşım arama ağacını küçültür. Örneğin teorik olarak $5^{40}$ gibi devasa bir deneme alanı, iyi kısıtlarla çok daha yönetilebilir hale gelir. Elbette garanti sihir değildir; fakat gerçek bulmacalarda fark şaşırtıcıdır.

## Görsel bulmacalara genişletmek

Aynı model Sudoku dışında Nonogram, KenKen, labirent, taş kaydırma oyunları ve hatta satranç problemleri için kullanılabilir. Değişen şey `isValid` fonksiyonunun kurallarıdır. Nonogram’da satır ipuçlarını, labirentte duvarları, satrançta taş hareketlerini kontrol edersiniz. Genel iskelet aynı kalır: durum üret, geçerliliği kontrol et, uygunsa ilerle, değilse geri dön.

## Son dokunuşlar

Kullanıcıya hız kontrolü, adım sayacı, duraklat-devam et düğmesi ve çözüm geçmişi eklerseniz proje bir algoritma demosundan mini eğitim aracına dönüşür. Hatta her hamleyi bir listeye yazıp neden seçildiğini açıklayabilirsiniz. İşin eğlenceli tarafı şu: JavaScript burada yalnızca çözüm üreten bir araç değil, algoritmanın zihnini görünür kılan bir sahne yönetmenidir.
