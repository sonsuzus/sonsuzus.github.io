---
layout: post
title: "Sıfırdan Turing Tam Bir Programlama Dili Tasarlamak"
math: true
categories: 
  - Proje
tags: 
  - programlama dili
  - lexer-parser
  - yorumlayıcı
---

Bir programlama dili yapmak, bilgisayara yeni kelimeler öğretmekten çok daha fazlasıdır: Önce metni parçalara ayırır, sonra bu parçaların dilbilgisine uyup uymadığını denetler ve en sonunda anlamlarını çalıştırırsınız. Bu projede değişkenleri, aritmetik işlemleri, koşulları ve döngüleri destekleyen MiniLang adında küçük ama teorik olarak Turing tam bir dil tasarlayacağız.
``

## Turing tamlık ne anlama gelir?

Bir dil, yeterli zaman ve bellek verildiğinde herhangi bir hesaplanabilir algoritmayı ifade edebiliyorsa Turing tam kabul edilir. Pratik bir dil için temel gereksinimler şunlardır:

| Özellik | MiniLang karşılığı | Neden gerekli? |
|---|---|---|
| Bellek | Değişkenler | Ara sonuçları saklamak |
| Hesaplama | `+`, `-`, `*`, `/` | Veriyi dönüştürmek |
| Karar | `if` | Farklı yürütme yolları oluşturmak |
| Tekrar | `while` | Sınırsız adım gerçekleştirmek |

Özellikle `while` döngüsü ve teorik olarak sınırsız büyüyebilen sayılar sayesinde dilimiz, bir sayaç makinesini simüle edebilir. Örneğin bir sayıyı tekrar tekrar azaltmak şu geçişi oluşturur:

$$x_{n+1}=x_n-1$$

Koşullu sıçramalarla birleşen bu işlem, genel hesaplama modellerini ifade etmek için yeterlidir. Gerçek bilgisayarların belleği elbette sonludur; Turing tamlık idealize edilmiş sınırsız kaynak varsayımına dayanır.

## Dilin söz dizimi

MiniLang ile faktöriyel hesabı şöyle görünebilir:

```text
let n = 5;
let result = 1;
while (n > 1) {
    result = result * n;
    n = n - 1;
}
print result;
```

Burada amaçlanan sonuç $5! = 5\times4\times3\times2\times1 = 120$ değeridir. Şimdi kaynak kodun yorumlayıcıdan geçerken uğradığı üç durağa bakalım.

## 1. Lexer: Metni jetonlara ayırmak

Lexer, karakterleri `NUMBER`, `IDENT`, `PLUS` gibi tokenlara dönüştürür. Böylece parser tek tek karakterlerle boğuşmaz.

```python
import re

TOKEN_RE = re.compile(
    r'(?P<NUMBER>\d+)|(?P<IDENT>[A-Za-z_]\w*)|'
    r'(?P<OP>==|>|[+\-*/=;(){}])|(?P<SPACE>\s+)'
)

def lex(source):
    tokens = []
    for match in TOKEN_RE.finditer(source):
        kind, value = match.lastgroup, match.group()
        if kind != 'SPACE':
            tokens.append((kind, value))
    return tokens
```

Bu fonksiyon boşlukları atlar, sayıları ve isimleri tanır. Sağlam bir sürüm ayrıca eşleşmeyen karakterlerin konumunu bildirerek anlaşılır hata mesajları üretmelidir.

## 2. Parser: Tokenlardan anlamlı bir ağaç kurmak

Parser, token dizisini soyut sözdizimi ağacına, yani AST'ye çevirir. Basit gramerimizin özeti şöyledir:

```text
statement  -> 'let' IDENT '=' expression ';'
            | IDENT '=' expression ';'
            | 'while' '(' expression ')' block
            | 'print' expression ';'
expression -> comparison
comparison -> term ('>' term)*
term       -> factor (('+' | '-') factor)*
factor     -> primary (('*' | '/') primary)*
```

Öncelik katmanları önemlidir: `2 + 3 * 4`, $(2+3)\times4$ değil, $2+(3\times4)=14$ biçiminde ayrıştırılmalıdır. Recursive descent yaklaşımında her gramer kuralı bir Python fonksiyonuna dönüştürülür. Örneğin toplama katmanı:

```python
def parse_term(self):
    node = self.parse_factor()
    while self.peek_value() in ('+', '-'):
        operator = self.advance()[1]
        right = self.parse_factor()
        node = ('binary', operator, node, right)
    return node
```

Üretilen tuple, operatörü ve iki alt ifadeyi taşıyan küçük bir AST düğümüdür.

## 3. Yorumlayıcı: Ağacı çalıştırmak

Yorumlayıcı değişkenleri bir sözlükte tutar ve AST düğümlerini değerlendirir:

```python
def evaluate(node, env):
    kind = node[0]
    if kind == 'number':
        return int(node[1])
    if kind == 'variable':
        return env[node[1]]
    if kind == 'binary':
        _, op, left, right = node
        a, b = evaluate(left, env), evaluate(right, env)
        operations = {
            '+': lambda: a + b, '-': lambda: a - b,
            '*': lambda: a * b, '/': lambda: a // b,
            '>': lambda: int(a > b)
        }
        return operations[op]()
```

`while` düğümü için koşul sıfır olmadığı sürece gövde tekrar yorumlanır. Atama düğümü de `env[name] = evaluate(expression, env)` işlemini yapar. Böylece lexer harfleri tokenlara, parser tokenları ağaca, yorumlayıcı ise ağacı davranışa dönüştürür. Birkaç hata mesajı, fonksiyon desteği ve REPL eklediğinizde MiniLang artık oyuncak görünümündeki ciddi bir hesaplama laboratuvarıdır.
