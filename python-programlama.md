# Python Programlama

Bu bölümde python programlama ile ilgili dersler ve ipuçları olacaktır.

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
