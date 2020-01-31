# Laboratorul 1 - introducere în Python
## I/O
In Python, putem citi de la consolă folosind funcția input(), care returnează un string.

Exemplu:
```python
line = input()
nr = int(input()) # nr este un numar
```

Pentru afișare la consolă, folosim funcția print().

Exemplu:
```python
# in Python 3
print(nr)
print("Numarul este " + str(nr))
'''
ca sa concatenam un numar la un string,
trebuie sa convertim acel numar la string folosind functia str(),
care este echivalentul lui toString() din Java
'''

# in Python 2 - deprecated
print nr
```
## Funcții
În Python, nu se specifică tipul de retur al funcțiilor și nici tipul parametrilor de intrare. Pentru a defini o funcție, se folosește keyword-ul `def`.

Exemplu:
```python
def add(x, y, z):
  return x + y + z
```

Exemplu:
## `pass`
Keyword-ul `pass` descrie un bloc gol în Python (echivalentul lui {} din C / Java).

Exemple (C vs Python):
- C
```c
for (int i = 0; i < 10; i++) {

}
```
- Python
```python
for i in range(10):
  pass
```
