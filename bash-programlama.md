# Bash programlama

## Kabuk Programlamaya Giriş 

Her kabuğun kendine özgü programlama dili yapısı vardır. Bash kabuğu ise güçlü programlama özellikleriyle karmaşık programların rahatça yazılmasına izin verir. Mantıksal operatörler, döngüler , değişkenler ve modern programlama dillerinde bulunan pek çok özellik bash kabuğunda da vardır ve işleyiş tarzları da hemen hemen aynıdır. 

Genellikle, bir programı oluşturacak olan komutlar bir dosyaya yazılırlar ve ardından bu dosya çalıştırılır. Herhangi bir editör yardımıyla yazılan program, daha sonra kabuk altında çalıştırılır. Bir kabuk programı diğerlerini çalıştırabilir. Bu düzende kabuk programlarını daha karmaşık komutların biraraya gelmiş ve yapısallaşmış haline benzetebiliriz. 

Bash'in en büyük dezavantajı, derlenerek çalıştırılan dillere göre (C, C++ gibi) daha yavaş olması, sistem kaynaklarını biraz daha fazla tüketmesidir. 

### Kabuk Programları 

Kabuk programları, bir veya birden fazla Linux komutunu tutan dosyalardır. Bu dosya yaratıldıktan sonra doğrudan dosyanın ismi girilerek veya dosya isminden önce '.' karakteri getirerek çalıştırılabilir. Bir kabuk programı, çalıştırma bitini 1 yapmak suretiyle "çalıştırılabilir" hale getirilir. chmod komutu yardımıyla bir programı çalıştırılabilir yapmak için , 

>$ chmod +x komut-ismi

yazılabilir. Bundan sonra programın ismi yazılıp enter tuşuna basıldığı zaman bir program Linux komutuymuş gibi çalışacaktır. 

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
