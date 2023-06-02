# Python Programlama

Bu bölümde python programlama ile ilgili dersler ve ipuçları olacaktır. Aşama aşama konular ve açıklamları ayrıca önemli ipuçlarının bulunacağı bu bölümle ilgili sorularınızı yorum bölümünden sorabilirsiniz.

Öncelikle python hakkında genel bilgilendirme yapalım.

## Python Nedir?

Tahmin edebileceğiniz gibi Python (C, C++, Perl, Ruby ve benzerleri gibi) bir programlama dilidir ve tıpkı öteki programlama dilleri gibi, önünüzde duran kara kutuya, yani bilgisayara hükmetmenizi sağlar.

Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python olmasına aldanarak, bu programlama dilinin, adını piton yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır.

Dediğimiz gibi, Python bir programlama dilidir. Üstelik pek çok dile kıyasla öğrenmesi kolay bir programlama dilidir. Bu yüzden, eğer daha önce hiç programlama deneyiminiz olmamışsa, programlama maceranıza Python’la başlamayı tercih edebilirsiniz.

### Neden Python?
Python programlarının en büyük özelliklerinden birisi, C ve C++ gibi dillerin aksine, derlenmeye gerek olmadan çalıştırılabilmeleridir. Python’da derleme işlemi ortadan kaldırıldığı için, bu dille oldukça hızlı bir şekilde program geliştirilebilir.

Ayrıca Python programlama dilinin basit ve temiz söz dizimi, onu pek çok programcı tarafından tercih edilen bir dil haline getirmiştir. Python’ın söz diziminin temiz ve basit olması sayesinde hem program yazmak, hem de başkası tarafından yazılmış bir programı okumak, başka dillere kıyasla çok kolaydır.

Python’ın yukarıda sayılan özellikleri sayesinde dünya çapında ün sahibi büyük kuruluşlar (Google, YouTube ve Yahoo! gibi) bünyelerinde her zaman Python programcılarına ihtiyaç duyuyor. Mesela pek çok büyük şirketin Python bilen programcılara iş imkanı sağladığını, Python’ın baş geliştiricisi Guido Van Rossum’un 2005 ile 2012 yılları arasında Google’da çalıştığını, 2012 yılının sonlarına doğru ise Dropbox şirketine geçtiğini söylersek, bu programlama dilinin önemi ve geçerliliği herhalde daha belirgin bir şekilde ortaya çıkacaktır.

Python programlama dili ve bu dili hakkıyla bilenler sadece uluslararası şirketlerin ilgisini çekmekle kalmıyor. Python son zamanlarda Türkiye’deki kurum ve kuruluşların da dikkatini çekmeye başladı. Bu dil artık yavaş yavaş Türkiye’deki üniversitelerin müfredatında da kendine yer buluyor.

Sözün özü, pek çok farklı sebepten, başka bir programlama dilini değil de, Python programlama dilini öğrenmek istiyor olabilirsiniz.

[print() fonksiyonu için tıklayınız.](https://sonsuzus.github.io/python-print)

[input() fonksiyonu için tıklayınız.](https://sonsuzus.github.io/python-input)

## Örnek Python soruları ve cevapları

Bu bölüm [Algoritma](https://sonsuzus.github.io/algoritma-programlama) sayfasındaki soruların çözümlerini içermektedir.

Dolap düdük ve kapaklar sorusu için python kodu aşağıdadır.

```python
dolap = [-1 for i in range(101)]
for duduk in range(1,101):
    for i in range(1,101):
        if i%duduk==0:
            dolap[i]=-dolap[i]
for i in range(101):
    if dolap[i]==1:
        print(i," nolu dolap açıktır")
```

[Python programlama post metodu kullanımı](https://sonsuzus.github.io/python-programlama-post-metodu-kullanimi) için tıklayabilirsiniz.


{% include footer.html %}

{% include analytics.html %}
