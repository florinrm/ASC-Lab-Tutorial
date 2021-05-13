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

## main

## String-uri

## Structuri condiționale și repetitive
### if
Exemple (C vs Python):
- C
```c
if (a > 4) {
	printf("Greater than 4\n");
} else if (a < 4) {
	printf("Lesser than 4\n");
} else {
	printf("Equal to 4\n");
}
```
- Python
```python
if a > 4:
	print('Greater than 4')
elif a < 4:
	print('Lesser than 4')
else:
	print('Equal to 4')
```
- este de notat că în Python nu există switch-case
### for
Exemple (C vs Python):
- C
```c
for (int i = 0; i < 10; i++) {
	printf("%d\n", i);
}
```
- Python
```python
# daca scriem asa, este default de la 0 la 10, cu pasul 1 in for
# range genereaza o lista [1, 2, ..., 10]
for i in range(10):
	print(i)

# xrange nu genereaza o lista, ci un numar intr-o iteratie
for i in xrange(10):
	print(i)

# putem parcurge o lista in Python in 2 moduri
# prima modalitate - folosind lungimea listei
for i in range(len(l)):
	print(l[i])

# a doua modalitate - folosind un for de tip foreach
for element in l:
	print(element)
```
### while
Exemple (C vs Python):
- C
```c
while (a < 10) {
	printf("%d\n", a);
	a++;
}
```
- Python
```python
while a < 10:
	print(a)
	a = a + 1 # de notat ca in Python nu putem face a++ / ++a
	# a += 1 # este permisa in Python
```

## Structuri de date
### Liste
```python
l1 = [] # lista goala
l2 = [1, 2, 3, 4, 5, 6] # lista populata
l2[0] # primul element
l2[1:4] # sublista cu elementele care se afla intre pozitiile 1 si 4
l2[-1] # ultimul element din lista
l2.append(7) # adaugarea unui element la sfarsitul unei liste
```
### Tupluri
```python
```
### Dicționare
```python
d = dict() # dictionar gol
d1 = {} # dictionar gol
d2 = {4: 7, 'pikachu': 'raichu'} # dictionar initializat cu valori de tip cheie-valoare
```

### Cheatsheets
https://www.pythoncheatsheet.org/

Aveți cheatsheets în plus în folder-ul Cheatsheets.
