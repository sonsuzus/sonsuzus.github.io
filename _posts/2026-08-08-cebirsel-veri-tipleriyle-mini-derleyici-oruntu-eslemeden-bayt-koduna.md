---
layout: post
title: "Cebirsel Veri Tipleriyle Mini Derleyici: Örüntü Eşlemeden Bayt Koduna"
math: true
categories: 
  - Proje
tags: 
  - fonksiyonel-programlama
  - derleyici
  - örüntü-eşleme
---

Bir programlama dilinin nasıl çalıştığını anlamanın en eğlenceli yollarından biri, küçük ama gerçek bir derleyici yazmaktır. Bu projede Haskell benzeri, cebirsel veri tiplerini ve örüntü eşlemeyi destekleyen bir dili yığın tabanlı sanal makine komutlarına çevireceğiz. Hedefimiz yeni bir Haskell üretmek değil; sözdizimi ağacı, tipler, örüntüler ve kod üretimi arasındaki ilişkiyi elle tutulur hâle getirmek.
``

## Dilimizin temel modeli

Cebirsel veri tipi, mevcut tipleri **toplam** ve **çarpım** işlemleriyle birleştirir. Örneğin `Bool`, iki olası değerden oluştuğu için toplam tipidir:

$$Bool = True + False$$

`Pair Int Bool` ise iki değeri birlikte taşıdığı için çarpım tipidir:

$$|Pair\ Int\ Bool| = |Int| \times |Bool|$$

Bu bakış açısı yalnızca matematiksel süs değildir. Derleyici, bir `case` ifadesinin tüm olasılıkları kapsayıp kapsamadığını bu yapı üzerinden inceleyebilir.

| Kavram | Anlamı | Dilimizdeki örnek |
|---|---|---|
| Toplam tipi | Alternatiflerden biri seçilir | `Maybe a = None | Some a` |
| Çarpım tipi | Değerler birlikte taşınır | `Point = Point Int Int` |
| Örüntü | Değeri parçalayarak sınar | `Some x -> x` |
| Kaplayıcılık | Tüm kurucuların ele alınması | `None` ve `Some` dalları |

## Soyut sözdizimi ağacı

Kaynak kodu doğrudan makine komutlarına çevirmek yerine önce bir AST oluştururuz. AST, boşluk ve parantez gibi ayrıntıları atarak programın anlamını saklar.

```haskell
data Expr
  = LitInt Int
  | Var Name
  | Add Expr Expr
  | Con Name [Expr]
  | Case Expr [Branch]

data Pattern
  = PWildcard
  | PVar Name
  | PCon Name [Pattern]

data Branch = Branch Pattern Expr
```

`Con` veri kurucusu oluşturur; `PCon` ise aynı kurucuyu örüntü içinde arar. Örneğin `Some 42`, `Con Some [LitInt 42]` biçiminde temsil edilir. Bu ayrım önemlidir: ifade bir değer **üretirken**, örüntü mevcut değeri **sorgular**.

## Örüntüleri derlemek

Sanal makinemizin yığın kullandığını varsayalım. Her cebirsel değer, kurucu etiketi ve alanlarından oluşsun. `Some 7` kabaca `(Some, [7])` şeklinde düşünülebilir.

```haskell
data Instr
  = PushInt Int
  | Load Name
  | Build Name Int
  | TestTag Name Label
  | Unpack Int
  | Jump Label
  | Mark Label
  | FailMatch
```

Bir örüntüyü derleyen fonksiyon, başarısızlık durumunda gidilecek etiketi alır:

```haskell
compilePattern :: Pattern -> Label -> [Instr]
compilePattern PWildcard _ = []
compilePattern (PVar name) _ = [Bind name]
compilePattern (PCon tag fields) fail =
  [TestTag tag fail, Unpack (length fields)]
  ++ concatMap (`compilePattern` fail) fields
```

Buradaki fikir kısa ama güçlüdür: `TestTag`, değerin kurucusunu kontrol eder; uyuşmazsa sonraki dala sıçrar. `Unpack`, kurucunun alanlarını yığına açar. Alt örüntüler daha sonra aynı yöntemle özyinelemeli olarak işlenir.

## `case` ifadesinin kod üretimi

Her dal için bir sonraki dal etiketi ve ortak bir bitiş etiketi üretiriz:

```haskell
compileCase scrutinee branches =
  compileExpr scrutinee ++ go branches
  where
    go [] = [FailMatch]
    go (Branch pat body : rest) =
      let next = freshLabel()
          done = caseEndLabel
      in  [Dup]
       ++ compilePattern pat next
       ++ [Pop]
       ++ compileExpr body
       ++ [Jump done, Mark next]
       ++ go rest
```

`Dup`, aynı değerin sonraki dalda tekrar denenebilmesini sağlar. Başarılı dal gövdesini çalıştırıp sona atlar; hiçbir dal eşleşmezse `FailMatch` devreye girer. Gerçek bir derleyicide etiket üretimi saf bir `State` monadıyla yönetilebilir.

## Kaplayıcılık ve son dokunuşlar

Çalışma zamanındaki `FailMatch` yararlıdır, fakat hatayı derleme aşamasında bulmak daha iyidir. `Maybe a` üzerinde yalnızca `Some x` dalı varsa eksik kurucu kümesi şöyledir:

$$Eksik = \{None, Some\} - \{Some\} = \{None\}$$

İlk sürümde yalnızca üst seviye kurucuları karşılaştırabilir, joker örüntüsü görüldüğünde kümeyi tamamen kapsanmış sayabiliriz. Sonraki adımlarda iç içe örüntüler, tip çıkarımı, gereksiz dal uyarıları ve kuyruk çağrısı optimizasyonu eklenebilir. Böylece küçük derleyicimiz, birkaç veri tanımından başlayıp fonksiyonel dillerin kalbindeki önemli fikirlere uzanan sevimli bir laboratuvara dönüşür.
