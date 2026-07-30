---
layout: post
title: "Python Kurulumu ve VS Code ile Geliştirme Ortamı Hazırlama"
math: true
categories: 
  - Bilgi
tags: 
  - Python
  - VS Code
  - Geliştirme Ortamı
---

Python öğrenmeye başlarken ilk programdan önce küçük ama önemli bir görevimiz var: bilgisayara Python dilini çalıştıracak yorumlayıcıyı tanıtmak ve kod yazacağımız ortamı hazırlamak. Bu süreç, bir mutfakta yemek yapmadan önce ocağı bağlamaya ve araçları tezgâha dizmeye benzer. Doğru kurulan bir ortam sayesinde ileride “Kodum mu bozuk, bilgisayar mı naz yapıyor?” ikilemiyle daha az karşılaşırız.
``
## Python yorumlayıcısı ne yapar?

Python, yüksek seviyeli ve yorumlanan bir programlama dilidir. Yazdığımız kaynak kod doğrudan işlemcinin anlayacağı makine dili değildir. Python yorumlayıcısı kodu okur, bytecode adı verilen ara gösterime dönüştürür ve Python Sanal Makinesi üzerinde çalıştırır.

Bu ilişkiyi basitleştirirsek:

$$\text{Kaynak Kod} \rightarrow \text{Bytecode} \rightarrow \text{Python VM} \rightarrow \text{Çıktı}$$

Bir programın toplam çalışma süresini kavramsal olarak şöyle düşünebiliriz:

$$T_{toplam} = T_{çeviri} + T_{çalıştırma}$$

Bu yaklaşım Python’a taşınabilirlik kazandırır. Aynı `.py` dosyası, uygun yorumlayıcı bulunduğu sürece Windows, macOS ve Linux üzerinde çalışabilir.

| Kavram | Görevi | Örnek |
|---|---|---|
| Yorumlayıcı | Python kodunu çalıştırır | `python`, `python3` |
| Editör | Kod yazmayı kolaylaştırır | VS Code |
| Terminal | Komutları işletim sistemine iletir | PowerShell, Bash |
| PATH | Çalıştırılabilir dosyaların konumunu bildirir | Python klasörü |
| Sanal ortam | Proje bağımlılıklarını izole eder | `venv` |

## Python kurulumu

Python, resmi olarak [python.org](https://www.python.org/downloads/) adresinden indirilebilir. Windows kurulumunda **Add Python to PATH** kutusunu işaretlemek kritik önemdedir. PATH, işletim sisteminin `python` komutunu yazdığımızda yorumlayıcıyı nerede bulacağını belirleyen dizinler listesidir.

macOS kullanıcıları Homebrew, Linux kullanıcıları ise dağıtımlarının paket yöneticisini tercih edebilir:

```bash
# macOS
brew install python

# Ubuntu veya Debian
sudo apt update
sudo apt install python3 python3-venv
```

Kurulumun başarılı olduğunu terminalde doğrulayalım:

```bash
python --version
# Bazı sistemlerde:
python3 --version
```

Ekranda `Python 3.x.x` benzeri bir sonuç görülüyorsa yorumlayıcı göreve hazırdır. Komut bulunamıyorsa terminali yeniden başlatmak ve PATH ayarını kontrol etmek gerekir.

## VS Code ortamını hazırlama

VS Code kurulduktan sonra sol menüdeki Extensions bölümünü açıp Microsoft tarafından yayımlanan **Python** eklentisini yükleyin. Bu eklenti sözdizimi renklendirme, otomatik tamamlama, hata analizi ve hata ayıklama gibi özellikler sağlar.

Ardından bir proje klasörü oluşturup VS Code ile açın. Terminali `Ctrl + Ö` veya menüdeki **Terminal > New Terminal** seçeneğiyle çalıştırabilirsiniz. Projeye özel sanal ortam oluşturalım:

```bash
python -m venv .venv
```

Sanal ortamı etkinleştirme komutu işletim sistemine göre değişir:

| Sistem | Komut |
|---|---|
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows CMD | `.venv\Scripts\activate.bat` |
| macOS / Linux | `source .venv/bin/activate` |

Sanal ortam, bir projede kurulan paketlerin diğer projeleri etkilemesini önler. Örneğin bir proje `Paket 1.0`, diğeri `Paket 2.0` kullanabilir; böylece bağımlılık kavgası çıkmaz.

VS Code’da `Ctrl + Shift + P` tuşlarına basıp **Python: Select Interpreter** komutunu seçin ve `.venv` içindeki yorumlayıcıyı işaretleyin.

## İlk programı çalıştırma

`main.py` adlı bir dosya oluşturup aşağıdaki kodu yazalım:

```python
name = input("Adın nedir? ")
message = f"Merhaba {name}, Python ortamın çalışıyor!"
print(message)
```

Bu program `input()` ile kullanıcıdan veri alır, f-string ile metin oluşturur ve `print()` ile sonucu terminale gönderir. Çalıştırmak için şu komutu kullanın:

```bash
python main.py
```

Artık yorumlayıcı, editör, terminal ve sanal ortam aynı ekipte çalışıyor. Kısacası sahne hazır; bundan sonra hatalar bile öğrenme macerasının eğlenceli karakterleri olacak!
