# Bash programlama

## Kabuk Programlamaya Giriş 

Her kabuğun kendine özgü programlama dili yapısı vardır. Bash kabuğu ise güçlü programlama özellikleriyle karmaşık programların rahatça yazılmasına izin verir. Mantıksal operatörler, döngüler , değişkenler ve modern programlama dillerinde bulunan pek çok özellik bash kabuğunda da vardır ve işleyiş tarzları da hemen hemen aynıdır. 

Genellikle, bir programı oluşturacak olan komutlar bir dosyaya yazılırlar ve ardından bu dosya çalıştırılır. Herhangi bir editör yardımıyla yazılan program, daha sonra kabuk altında çalıştırılır. Bir kabuk programı diğerlerini çalıştırabilir. Bu düzende kabuk programlarını daha karmaşık komutların biraraya gelmiş ve yapısallaşmış haline benzetebiliriz. 

Bash'in en büyük dezavantajı, derlenerek çalıştırılan dillere göre (C, C++ gibi) daha yavaş olması, sistem kaynaklarını biraz daha fazla tüketmesidir. 

### Kabuk Programları 

Kabuk programları, bir veya birden fazla Linux komutunu tutan dosyalardır. Bu dosya yaratıldıktan sonra doğrudan dosyanın ismi girilerek veya dosya isminden önce '.' karakteri getirerek çalıştırılabilir. Bir kabuk programı, çalıştırma bitini 1 yapmak suretiyle "çalıştırılabilir" hale getirilir. chmod komutu yardımıyla bir programı çalıştırılabilir yapmak için , 

```
$ chmod +x komut-ismi
```



yazılabilir. Bundan sonra programın ismi yazılıp enter tuşuna basıldığı zaman bir program Linux komutuymuş gibi çalışacaktır. 
```
$ cat calistir
echo -n "Tarih : "
date
$ chmod +x calistir
$ calistir
Tarih : Sun Dec  8 07:11:51 EET 1996
```
Yukarıdaki örnekte "calistir" isimli iki satırlık bir kabuk programının önce içeriği ekrana yazıldı, ardından çalıştırılacak duruma getirildi ve çalıştırıldı. 
Kabuk programları yazarken dosyanın işlevini ve her satırdaki komutun veya komut kümesinin ne amaçla kullanıldığını gösteren açıklama satırları kullanmak işe yarar. Bir açıklama eklemek için satır başına (veya boş satıra) # işareti eklenir ve ardından istenilen cümle girilir. # işaretinden sonraki tüm satır kabuk tarafından gözardı edilir. Aşağıdaki programda komut öncesinde yeralan açıklama satırı, komut hakkında bilgi veriyor. 
```
# gunzip komutu dosya acmak icin kullanilir.
gunzip sistem.gz
```
Yorum satırı, komutun sonuna da eklenebilir. 
```
ps -aux         # sistem surecleri hakkinda ayrintili bilgi..
```
Bir kabuk altında çalışırken başka bir kabuk için yazılmış bir programı çalıştırmak mümkündür. Örneğin tcsh altındasınız ve daha evvel bash kullanarak yazdığınız bir programı çalıştırmak istiyorsunuz. Önce bash yazarak kabuk değiştirmeli, ardından programı çalıştırmalı, ve tekrar tcsh'a dönmelisiniz. Tüm bunları otomatik olarak yaptırabilirsiniz. Programın en başına #! karakterini, ardından programın çalışacağı kabuğun patikasını yazın. Örneğin #!/bin/bash komutunu programın en üstüne eklerseniz bu program bash kabuğu altında çalışacaktır. 

## Değişkenlerin Kullanımı 
Bir değişkene değer atandığı anda sistem tarafından tanınır. Değişkenler alfabetik veya nümerik karakterlerden oluşabilirler fakat bir değişken sayısal bir değer ile başlayamaz. Bir değişkene değer ataması "=" işareti yardımıyla yapılır. 
```
$ mesaj="aksama yemege geliyorum"
```
İçeriği olan bir değişkene başına "$" işareti konularak ulaşılır. Aşağıda, echo komutu yardımıyla bir değişkenin içeriği ekrana basılıyor. 
```
$ echo $mesaj
aksama yemege geliyorum
$ echo yarin $mesaj
yarin aksama yemege geliyorum
```
Aynı mesajı değişken kullanmadan da görüntüleyebiliriz. 
```
$ echo "Aksama yemege geliyorum"
Aksama yemege geliyorum
```

Linux kabuğundaki küçük ama işe yarar kod parçalarını bu bölümde bulabilirsiniz.

Çok sayıda dosyayı kopyalamak için
```
for i in file_dir/*; do cp "$i" target_dir/; done
```

Yine biriken tmp dosyaları inode sınırını geçince sitelerde sıkıntı oluyor. Kontrol etmek için
```
df -i
# temizlemek içinse
rm -rfv /tmp/lshttpd/swap/*
```

Çok sayıda dosyayı silmek için
```
find . -type f -delete
```

Biriken log dosyalarını silmek için
```
rm -rf /usr/local/lsws/logs/*
```

{% include footer.html %}

{% include analytics.html %}
