---
layout: post
title: "GDB Python ile Yığındaki Stringleri Avlayan Renkli Komut Yazmak"
math: true
categories: 
  - Program
tags: 
  - gdb
  - python
  - debugging
  - stack
  - reverse-engineering
---

Debug oturumunda bazen en değerli ipucu, register’larda değil yığının arasında saklanan minicik bir stringdir: bir token, hata mesajı, dosya yolu ya da “buradayım!” diye bağıran bir parola. GNU Debugger, Python API’si sayesinde yalnızca komut çalıştırdığımız bir araç olmaktan çıkar; kendi mini dedektif komutlarımızı yazabileceğimiz genişletilebilir bir platforma dönüşür.
``
Bu yazıda GDB’ye özel bir komut ekleyerek çalışan programın **stack/yığın** bellek bölgesini tarayacak, yazdırılabilir karakterlerden oluşan stringleri bulacak ve terminalde renklendirerek göstereceğiz. Ama önce sahneyi kuralım: yığın, fonksiyon çağrıları sırasında yerel değişkenlerin, dönüş adreslerinin ve geçici verilerin tutulduğu bellek alanıdır. Çoğu mimaride yığın aşağı doğru büyür; yani yeni veri eklendikçe adresler küçülür. Basitçe düşünürsek bir tarama aralığı için $$N = end - start$$ bayt okuruz ve ardışık yazdırılabilir karakterleri string adayı kabul ederiz.

| Bölge | Tipik İçerik | Debug İçin Değeri |
|---|---|---|
| Stack | Yerel değişkenler, geçici buffer’lar | Anlık durum ve sızıntı ipuçları |
| Heap | Dinamik ayrılan nesneler | Uzun yaşayan veri yapıları |
| .rodata | Sabit stringler | Programın gömülü mesajları |

GDB’nin Python tarafında en sevdiğimiz oyuncular `gdb.Command`, `gdb.selected_inferior()` ve `read_memory()` fonksiyonlarıdır. `gdb.Command` ile yeni komut tanımlarız, inferior dediğimiz şey debug edilen süreçtir, `read_memory()` ise belirli adres aralığındaki ham baytları okumamızı sağlar. Linux üzerinde `/proc/<pid>/maps` dosyasından `[stack]` satırını okuyarak gerçek yığın sınırlarını yakalayabiliriz.

Aşağıdaki betik `stackstrings` adlı yeni bir GDB komutu ekler. Minimum uzunluğu parametre olarak verebilir, aksi halde 4 karakterden uzun stringleri listeler. Çıktıda adresler mavi, stringler yeşil renktedir; çünkü debug yaparken biraz neon ışık herkesin hakkı!

```python
# stackstrings.py
import gdb
import string

GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'

PRINTABLE = set(bytes(string.printable, 'ascii')) - {0x0b, 0x0c}

class StackStrings(gdb.Command):
    '''Yığın bölgesindeki yazdırılabilir stringleri bulur: stackstrings [min_len]'''

    def __init__(self):
        super(StackStrings, self).__init__('stackstrings', gdb.COMMAND_DATA)

    def get_stack_range(self):
        inferior = gdb.selected_inferior()
        pid = inferior.pid
        if pid == 0:
            raise gdb.GdbError('Çalışan bir süreç yok. Önce run veya attach kullan.')

        with open(f'/proc/{pid}/maps', 'r') as maps:
            for line in maps:
                if '[stack]' in line:
                    region = line.split()[0]
                    start_s, end_s = region.split('-')
                    return int(start_s, 16), int(end_s, 16)
        raise gdb.GdbError('Stack bölgesi bulunamadı.')

    def invoke(self, arg, from_tty):
        min_len = int(arg) if arg.strip() else 4
        start, end = self.get_stack_range()
        inferior = gdb.selected_inferior()
        mem = inferior.read_memory(start, end - start).tobytes()

        found = 0
        i = 0
        while i < len(mem):
            if mem[i] in PRINTABLE:
                j = i
                while j < len(mem) and mem[j] in PRINTABLE:
                    j += 1
                if j - i >= min_len:
                    raw = mem[i:j]
                    text = raw.decode('ascii', errors='replace')
                    addr = start + i
                    print(f'{BLUE}0x{addr:x}{RESET}: {GREEN}{text}{RESET}')
                    found += 1
                i = j
            else:
                i += 1

        print(f'{YELLOW}Toplam {found} string bulundu. Aralık: 0x{start:x}-0x{end:x}{RESET}')

StackStrings()
```

Kullanmak için betiği kaydedip GDB içinde yüklemek yeterli:

```bash
gdb ./program
(gdb) run
(gdb) source stackstrings.py
(gdb) stackstrings 6
```

Buradaki algoritma oldukça basittir: belleği soldan sağa tarar, karakter `PRINTABLE` kümesindeyse bir koşu başlatır, koşu uzunluğu minimum değeri geçerse sonuç üretir. Zaman karmaşıklığı $$O(N)$$, bellek maliyeti ise okunan yığın kadar yani $$O(N)$$ kabul edilir. Büyük yığınlarda parça parça okuma yapılabilir; fakat öğretici olması için tek parça okuma daha anlaşılırdır.

| Yaklaşım | Avantaj | Dezavantaj |
|---|---|---|
| `/proc/pid/maps` ile sınır bulma | Gerçek stack aralığını tarar | Linux odaklıdır |
| `$sp` çevresini tarama | Taşınabilir fikre daha yakındır | Tüm yığını kaçırabilir |
| Sabit adres aralığı | Hızlı test edilir | ASLR nedeniyle kırılgandır |

Bu komut özellikle CTF, tersine mühendislik, exploit geliştirme ve “ben bu değişkene ne zaman ne yazdım?” soruşturmasında işe yarar. Yine de dikkat: Stack içinde gördüğünüz her karakter dizisi anlamlı string değildir. Rastgele baytlar bazen tesadüfen okunabilir karakterlere dönüşebilir. Bu yüzden bulunan sonuçları bağlamla, register’larla ve backtrace ile birlikte değerlendirmek gerekir.

Sonuç olarak GDB’nin Python API’si, debugger’ı kişisel bir analiz laboratuvarına çevirir. Bugün stack stringlerini renklendirdik; yarın heap tarayıcı, otomatik breakpoint raporlayıcı ya da şüpheli pointer avcısı yazabilirsiniz. Debug dünyasında büyüteç sizde, Python ise büyütecin LED ışığıdır.
