---
layout: post
title: "Python ile Otomatik Değerlendirme Sistemleri: Güvenli Kod Çalıştırma ve Notlandırma"
math: true
categories: 
  - Proje
tags: 
  - python
  - auto-grader
  - eğitim teknolojileri
  - test otomasyonu
---

Bir öğrencinin yazdığı kodu saniyeler içinde çalıştırıp çıktısını kontrol eden, puanını hesaplayan ve geri bildirim veren sistemler kulağa küçük bir sihirbazlık gibi gelir. Aslında bu sihrin adı auto-grader: test senaryoları, izole çalışma ortamı ve adil puanlama mantığının birleşimi. Python ile böyle bir sistem geliştirmek hem eğitim platformları hem de kodlama yarışmaları için çok güçlü bir projedir.
``
Auto-grader sisteminin temel problemi şudur: Kullanıcının gönderdiği kodu çalıştırmak istiyoruz, ama bu kod güvenilmez olabilir. Sonsuz döngüye girebilir, dosya sistemini kurcalayabilir, çok fazla bellek tüketebilir veya gizli testleri okumaya çalışabilir. Bu yüzden auto-grader yalnızca `subprocess.run()` çağırıp sonucu okumaktan ibaret değildir; güvenlik, zaman sınırı, kaynak sınırı ve test tasarımı birlikte düşünülmelidir.

Teorik olarak her soru için bir değerlendirme fonksiyonu vardır. Öğrencinin cevabını $S$, beklenen çıktıyı $E$, üretilen çıktıyı $O$ kabul edelim. Basit bir çıktı karşılaştırmasında puan fonksiyonu şöyle yazılabilir: $score(S)=100$ eğer $O=E$, aksi halde $0$. Daha gelişmiş sistemlerde çoklu test kullanılır: $$score=\frac{passed\_tests}{total\_tests}\times100$$ Böylece öğrencinin çözümü bazı durumları doğru ele alıyorsa kısmi puan alabilir.

| Yaklaşım | Avantaj | Risk | Kullanım Yeri |
|---|---|---|---|
| Çıktı karşılaştırma | Basit ve hızlı | Format hatalarına hassas | Başlangıç ödevleri |
| Birim test | Fonksiyon davranışını ölçer | Kod yapısı beklentisi vardır | Algoritma soruları |
| Gizli testler | Ezber çözümü engeller | Test kalitesi kritik | Yarışmalar |
| Sandbox | Güvenliği artırır | Kurulum maliyetli | Gerçek platformlar |

En küçük auto-grader çekirdeği, öğrencinin kodunu geçici bir dosyaya yazıp belirli girdilerle çalıştırabilir. Aşağıdaki örnek, zaman aşımı olan basit bir değerlendirme yapar. Bu sürüm öğretici amaçlıdır; üretimde Docker, kullanıcı yetkisi düşürme ve dosya sistemi izolasyonu eklenmelidir.

```python
import subprocess
import tempfile
from pathlib import Path

TESTS = [
    {'input': '2 3\n', 'expected': '5'},
    {'input': '10 -4\n', 'expected': '6'},
]

def grade_python_code(source_code, timeout=2):
    results = []
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / 'solution.py'
        path.write_text(source_code, encoding='utf-8')

        for test in TESTS:
            try:
                run = subprocess.run(
                    ['python', str(path)],
                    input=test['input'],
                    text=True,
                    capture_output=True,
                    timeout=timeout
                )
                output = run.stdout.strip()
                passed = output == test['expected']
                results.append({
                    'passed': passed,
                    'output': output,
                    'expected': test['expected'],
                    'error': run.stderr.strip()
                })
            except subprocess.TimeoutExpired:
                results.append({
                    'passed': False,
                    'output': '',
                    'expected': test['expected'],
                    'error': 'Zaman aşımı'
                })

    score = sum(r['passed'] for r in results) / len(results) * 100
    return score, results
```

Bu kodun yaptığı iş şudur: gönderilen Python kodu geçici klasöre kaydedilir, her test girdisi programa verilir, standart çıktı yakalanır ve beklenen sonuçla karşılaştırılır. `timeout` parametresi sonsuz döngüleri durdurmak için ilk savunma hattıdır. Fakat tek başına yeterli değildir; öğrenci kodu `open()` ile dosya okuyabilir veya çok bellek harcayabilir.

Daha güvenli mimaride her çözüm ayrı bir konteyner içinde çalışır. Docker tabanlı yaklaşımda işlemci, bellek ve dosya sistemi sınırlandırılır. Mantık kabaca şöyledir:

```python
import subprocess

def run_in_docker(file_path):
    return subprocess.run(
        [
            'docker', 'run', '--rm',
            '--network', 'none',
            '--memory', '128m',
            '--cpus', '0.5',
            '-v', f'{file_path}:/app/solution.py:ro',
            'python:3.12-slim',
            'python', '/app/solution.py'
        ],
        text=True,
        capture_output=True,
        timeout=3
    )
```

Burada `--network none` ağ erişimini kapatır, `--memory` bellek sınırı koyar, `--cpus` işlemci kullanımını kısıtlar. Dosya `:ro` ile salt okunur bağlanır. Yani öğrenci kodu küçük bir akvaryumda yüzer; okyanusa açılamaz.

Test tasarımı da en az güvenlik kadar önemlidir. Sadece örnek testlerle notlandırma yapmak, öğrencileri çıktı ezberlemeye iter. İyi bir sistemde görünür testler öğrenmeyi destekler, gizli testler ise genelleme yeteneğini ölçer. Ayrıca geri bildirim metinleri pedagojik olmalıdır: yalnızca yanlış demek yerine, hangi durumda hata oluştuğunu söylemek öğrencinin öğrenmesini hızlandırır.

Sonuç olarak Python ile auto-grader geliştirmek; `subprocess`, test mühendisliği, güvenlik ve eğitim psikolojisini bir araya getiren harika bir projedir. Küçük başlayın: birkaç test, zaman sınırı ve JSON sonuçları üretin. Sonra Docker sandbox, gizli test havuzu, kısmi puanlama ve web arayüzü ekleyin. Bir süre sonra fark edeceksiniz: artık sadece kod çalıştıran bir araç değil, öğrenciye anında geri bildirim veren mini bir öğretmen inşa ettiniz.
