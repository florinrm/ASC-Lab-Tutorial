# Laboratorul 2 - Python - multithreading - partea 1
## Clase în Python
- în Python putem defini clase în felul următor:
```python
class Song:
    # self este echivalentul lui this din Java
    # __init__ este constructorul unei clase din Python
    def __init__(self, artist, title, year):
        self.artist = artist
        self.title = title
        self.year = year

    # echivalentul toString() din Java
    # cand vrem sa folosim membri ai clasei, trebuie sa ii folosim cu self.
    # altfel va aparea eroare (nu merge ca in Java, unde puteai sa folosesti un membru al clasei fara this)
    def __str__(self):
        return self.title + " by " + self.artist


    def play(self):
        print('Now playing %s by %s, released in %d' %(self.title, self.artist, self.year))

    # cu adnotarea @staticmethod definim o metoda statica a clasei
    @staticmethod
    def class_method():
        print('static method')
```
- de reținut în Python este faptul că **nu** se folosește `new` la instanțierea unei clase:
```python
song = Song('Eminem', 'Killshot', 2018) # instantierea unei clase
print(song) # este apelata metoda __str__
# calling a method
song.play()
Song.class_method() # metoda statica
```

### Moștenirea claselor in Python
- moștenirea claselor în Python are următorul template:
```python
class SubClass(SuperClass1, SuperClass2):
    def __init__(self):
        SuperClass1.__init__(self) # se apeleaza constructorul din clasa parinte
        SuperClass2.__init__(self) # este echivalentul lui super din Java
```
- este de observat că, în Python, o clasă poate moșteni mai multe clase în același timp (ca în exemplul de mai sus)
Exemplu:
```python
# clasa RapSong mosteneste clasa Song
class RapSong(Song):
    def __init__(self):
        RapSong.__init__(self)
        # putem folosi ca alternativa urmatoarea varianta
        # super().init() # nu este nevoie sa folosim self
```

### Clase abstracte
- pentru a folosi clase abstracte ]n Python, trebuie importat modulul abc, de unde luăm clasa ABC (care reprezintă clasa abstractă sau mai pe românește keyword-ul `abstract` din Java) și adnotarea `abstractmethod`.
- Exemplu:
```python
from abc import ABC, abstractmethod

class A(ABC):
    # metoda abstracta
    @abstractmethod
    def some_method():
        pass

class B(A):
    def some_method():
        print('works')
```

## Folosirea de thread-uri in Python
### Clasa Thread

### Lock