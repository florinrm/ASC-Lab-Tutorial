# Laboratorul 3 - Python - multithreading - partea 2
## Event
Un event reprezinta un element de sincronizare, care functioneaza in felul urmator:
- thread-urile se blocheaza voluntar (sunt in starea waiting) pana cand un alt thread semnaleaza aparitia unui eveniment - o conditie sa aiba valoarea true (comportament similar cu bariera) - pe scurt, un event functioneaza ca un wake-up al thread-urilor din starea waiting
- un event poate inlocui un semafor (mai multe thread-uri pot fi blocate si deblocate in acelasi timp)
## Condition
- un condition functioneaza similar cu un event, adica thread-urile sunt blocate in mod voluntar (se afla in waiting) pana cand se semnaleaza aparitia unei conditii de catre un thread.

- diferenta fata de un event este ca aici se foloseste un Lock (sau RLock). La constructor se poate da ca parametru un Lock sau un RLock (mai ales daca se creeaza mai multe obiecte Condition, cu un lock partajat). Daca la constructor nu se paseaza un Lock / RLock, este creat automat un RLock.

Exemplu de folosire:
```python
cv = Condition()
# cv = Condition(Lock())

# Consume one item

cv.acquire()
while not an_item_is_available():
    cv.wait()
get_an_available_item()
cv.release()

# Produce one item
cv.acquire()
make_an_item_available()
cv.notify()
cv.release()
```

- cand se folosesc `wait()`, `notify()` si `notifyAll()`, lock-ul din Condition ramane blocat, pana cand se apeleaza `release()`.
- cand se apeleaza `notify()` si / sau `notifyAll()`, thread-urile nu ajung imediat in starea running, ele asteapta sa lock-ul sa fie released cu `release()`.