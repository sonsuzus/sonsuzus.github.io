---
layout: post
title: "Python ile Satranç Motoru Geliştirmek: Minimax ile Zeki Hamleler"
math: true
categories: 
  - Proje
tags: 
  - Python
  - Satranç Motoru
  - Minimax
  - Algoritmalar
---

Satranç motoru yazmak, kulağa “büyük ustaların laboratuvarı” gibi gelse de aslında algoritmik düşünceyi öğrenmek için harika bir oyun alanıdır. Python ile basit bir bot geliştirerek taşların değerini hesaplayabilir, olası hamleleri ağaç gibi düşünebilir ve minimax algoritmasıyla “ben oynarsam ne olur, rakip cevap verirse ne olur?” sorusunu kodla cevaplayabilirsiniz.
``
Satrançta her hamle yeni bir oyun durumu üretir. Bu durumları düğüm, hamleleri de kenar kabul edersek elimizde kocaman bir **karar ağacı** oluşur. Motorun amacı bu ağacı tamamen gezmek değildir; çünkü satrançta olası oyun sayısı astronomiktir. Bunun yerine belirli bir derinliğe kadar bakar, konumu puanlar ve en mantıklı yolu seçer.

Minimax algoritmasının temel fikri şudur: Biz skoru maksimize etmeye çalışırız, rakip ise bizim skorumuza göre en kötü sonucu seçer. Yani bot kendi açısından en iyi hamleyi ararken, rakibin de en iyi savunmayı yapacağını varsayar. Matematiksel olarak:

$$
V(s) = \max_{a \in A(s)} V(result(s,a))
$$

rakibin sırası geldiğinde ise:

$$
V(s) = \min_{a \in A(s)} V(result(s,a))
$$

Burada $s$ konumu, $a$ hamleyi, $A(s)$ mevcut hamleleri ve $V(s)$ konumun değerini temsil eder.

| Kavram | Satrançtaki Karşılığı | Kod Tarafındaki Rolü |
|---|---|---|
| Düğüm | Tahtanın anlık hali | Board nesnesi |
| Kenar | Yapılan hamle | Move nesnesi |
| Derinlik | Kaç hamle sonrasına bakıldığı | Recursive limit |
| Değerlendirme | Konumun iyi/kötü olması | Skor fonksiyonu |

Python’da satranç kurallarını sıfırdan yazmak yerine `python-chess` kütüphanesini kullanabiliriz. Böylece rok, şah, mat, geçerken alma gibi detaylarla boğuşmadan algoritmaya odaklanırız.

```python
import chess

piece_values = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 0
}

def evaluate(board):
    if board.is_checkmate():
        return -99999 if board.turn else 99999
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    score = 0
    for square, piece in board.piece_map().items():
        value = piece_values[piece.piece_type]
        score += value if piece.color == chess.WHITE else -value
    return score
```

Bu fonksiyon oldukça basit çalışır: Tahtadaki taşları dolaşır, beyaz taşları artı, siyah taşları eksi puan olarak yazar. Eğer botumuz beyaz oynuyorsa pozitif skor iyi, siyah oynuyorsa negatif skor iyidir. Elbette gerçek motorlar yalnızca taş saymaz; merkez kontrolü, şah güvenliği, piyon yapısı gibi konuları da değerlendirir.

Şimdi minimax fonksiyonunu yazalım:

```python
def minimax(board, depth, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    if maximizing:
        best_score = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, False)
            board.pop()
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, True)
            board.pop()
            best_score = min(best_score, score)
        return best_score
```

Burada `push` hamleyi tahtaya uygular, `pop` ise geri alır. Bu ikili, karar ağacında ileri gidip geri dönmemizi sağlar. Yani bot küçük bir zaman yolculuğu yapar: “Bu hamleyi oynarsam, sonra şu olur, rakip bunu yapar...” diye düşünür.

En iyi hamleyi seçmek için tüm yasal hamleleri deneriz:

```python
def find_best_move(board, depth):
    best_move = None
    best_score = -float('inf') if board.turn == chess.WHITE else float('inf')

    for move in board.legal_moves:
        board.push(move)
        score = minimax(board, depth - 1, board.turn == chess.WHITE)
        board.pop()

        if board.turn == chess.WHITE and score > best_score:
            best_score = score
            best_move = move
        elif board.turn == chess.BLACK and score < best_score:
            best_score = score
            best_move = move

    return best_move
```

| Derinlik | Botun Bakışı | Performans |
|---|---|---|
| 1 | Sadece anlık kazanç | Çok hızlı, safça |
| 2 | Rakibin cevabını görür | Hâlâ hızlı |
| 3 | Mini taktikleri yakalar | Orta seviye |
| 4+ | Daha ciddi hesap yapar | Yavaşlayabilir |

Minimax’ın en büyük sorunu dallanma faktörüdür. Ortalama her konumda yaklaşık 30 yasal hamle varsa, derinlik $d$ için karmaşıklık yaklaşık $O(30^d)$ olur. Bu nedenle gerçek motorlarda **alpha-beta budama** kullanılır. Alpha-beta, sonucu değiştirmeyecek dalları keserek aynı kararı daha hızlı verir.

Sonuç olarak bu proje, sadece satranç botu yazmak değildir; aynı zamanda özyineleme, karar ağaçları, sezgisel değerlendirme ve oyun teorisini pratikte öğrenmektir. İlk motorunuz dünya şampiyonunu yenemeyebilir ama bir taşı bedavaya bırakmadığında duyacağınız mutluluk paha biçilemez. Sonraki adım olarak alpha-beta budama, açılış kitabı ve taş-kare tabloları ekleyerek botunuzu küçük bir dijital büyükustaya dönüştürebilirsiniz.
