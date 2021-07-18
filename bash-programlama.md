# Bash programlama

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

{% include footer.html %}

{% include analytics.html %}
