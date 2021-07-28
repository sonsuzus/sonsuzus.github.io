# SQL programlama

İşe yarar sql kodları ile başlayalım. Veritabanında bul değiştir fonksiyonu replace

```
UPDATE dbo.xxx
SET Value = REPLACE(Value, '123', '')
WHERE ID <=4
```

Düşünceleri yoruma çevirmek için
```
UPDATE qa_posts c INNER JOIN qa_posts p ON c.parentid = p.postid 
SET c.type = 'A', c.parentid = p.parentid 
WHERE c.type = 'C' AND p.type = 'A' AND length(c.content)>100;
```
Biriken eventlogları silme
```
DELETE FROM `qa_eventlog` WHERE `datetime` < CURDATE() - INTERVAL 60 DAY
```

{% include footer.html %}

{% include analytics.html %}
