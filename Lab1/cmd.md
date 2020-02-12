Deschideți terminalul de Python și scrieți următoarele comenzi:
```bash
>>> a = 2
>>> a
2
>>> a = '2'
>>> a
'2'
>>> a = 'some string'
>>> a
'some string'
>>> b = 10
>>> a = 2
>>> a, b = b, a
>>> b
2
>>> a
10
>>> s = 'ana are mere'
>>> s[0]
'a'
>>> s[4]
'a'
>>> s[1:5]
'na a'
>>> s = "ana are mere"
>>> s[0]
'a'
>>> s[1:5]
'na a'
>>> l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l[0]
1
>>> l[1:]
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l[-1]
10
>>> l[:-1]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l[2:4]
[3, 4]
>>> list(filter(lambda x: x > 4, l))
[5, 6, 7, 8, 9, 10]
>>> list(map(lambda x: x * 2, l))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> [x for x in l]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> [x for x in l if x > 3]
[4, 5, 6, 7, 8, 9, 10]
>>> d = dict()
>>> d1 = {}
>>> d
{}
>>> d1
{}
>>> d[4] = 42
>>> d['pika'] = 41
>>> d
{4: 42, 'pika': 41}
>>> d[4] = 69
>>> d
{4: 69, 'pika': 41}
>>> tup = (1, 2, 3, 4, 5)
>>> tup[0]
1
>>> tup[0] = 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> 'ana are ' + ' mere'
'ana are  mere'
>>> 'ana are ' + 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
>>> 'ana are ' + str(42)
'ana are 42'
```