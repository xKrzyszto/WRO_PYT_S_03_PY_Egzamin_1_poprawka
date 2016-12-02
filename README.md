<img alt="Logo" src="http://coderslab.pl/wp-content/themes/coderslab/svg/logo-coderslab.svg" width="400">

# Podstawy programowania w Pythonie &ndash; egzamin.

Przed przystąpieniem do rozwiązywania zadań przeczytaj poniższe wskazówki

## Jak zacząć?

1. Stwórz [*fork*][forking] repozytorium z zadaniami.
2. [*Sklonuj*][ref-clone] repozytorium na swój komputer.
3. Rozwiąż zadania i [*skomituj*][ref-commit] zmiany do swojego repozytorium.
4. [*Wypchnij*][ref-push] zmiany do swojego repozytorium na GitHubie.
5. Stwórz [*pull request*][pull-request] do oryginalnego repozytorium, gdy skończysz wszystkie zadania.

#### Pamiętaj, że pull request musi być stworzony, aby wykładowca dostał Twoje odpowiedzi.

* podczas egzaminu **możesz** korzystać z notatek, kodu napisanego wcześniej, internetu i prezentacji,
* zabroniona jest jakakolwiek komunikacja z innymi kursantami oraz osobami na zewnątrz.

##### Odpowiedzi na pytania opisowe umieszczaj w pliku *answers.txt*.
##### Odpowiedzi na pytania programistyczne umieszczaj w module *answers.py*.

**Powodzenia!**

----------------------------------------------------------------------------------------

#### Zadanie 1. (3 pkt)

1. Jakiego narzędzia użyjesz do zaimportowania zewnętrznych bibliotek do Pythona?
2. Co zrobisz, jeśli w projekcie A używasz biblioteki libA, a w projekcie B &ndash; libB, które wzajemnie się wykluczają?
3. Jak aktywujesz środowisko wirtualne, a jak je deaktywujesz?



#### Zadanie 2. (4pkt)

Napisz funkcję `name_sorter`, która przyjmie jako parametr listę imion męskich i żeńskich. 

Funkcja ma zwrócić słownik:
* klucz o nazwie `male` ma mieć jako wartość imiona męskie z listy wejściowej,
* klucz o nazwie `female` ma mieć jako wartość imiona żeńskie z listy wejściowej.

Dodatkowo, posortuj imiona w ramach swoich list.

**Hint:** Możesz przyjąć, że imiona żeńskie, to te, które kończą się literą "a". Barnabę możemy spokojnie zignorować. ;-)

**Przykład:**
```python
names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
print(name_sorter(names))
```

```
{'female': ['Alicja', 'Barbara'], 'male': ['Andrzej', 'Cezary', 'Henryk']}
```

#### Zadanie 3 (3pkt).

Napisz funkcję `validate_password`, która sprawdzi, czy hasło przekazane do funkcji jako parametr jest bezpieczne i zwróci `True` jeśli jest, `False` jeśli nie jest.

**Jak sprawdzić siłę hasła?**

1. hasło powinno być dłuższe niż 8 znaków,
2. funkcja powinna sprawdzać, czy każda kolejna litera w haśle zawiera się w zbiorze liter wielkich, liter małych, cyfr i znaków specjalnych. Możesz w swoim zadaniu wykorzystać poniższy zbiór znaków:

```python
valid_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[{]}\|;:?/>.<,'
```

#### Zadanie 4. (2pkt)

Napisz funkcję `div`, która przyjmie dwa argumenty liczbowe: `a` i `b`. Funkcja ma zwrócić `True`, jeśli `a` dzieli się przez `b` bez reszty, w przeciwnym przypadku &ndash; `False`

#### Zadanie 5. (4pkt)

Napisz funkcję `find_longest_word`, która przyjmie napis w postaci łańcucha tekstowego i zwróci najdłuższe słowo z tego łańcucha. W przypadku, gdy kilka słów jest tej samej długości zwróć pierwsze z nich.

**Przykład:**
```python
print(find_longest_word("I find your lack of faith disturbing"))
```
```
disturbing
```

#### Zadanie 6. (4pkt)
Napisz funkcję `poker_hand`, która wylosuje i **wyświetli** na ekranie 5 kart z puli gart do gry. Listę z kartami znajdziesz w pliku **answers.py**. Pamietaj, że musisz usunąć kartę z puli, gdy ją wylosujesz.

<!-- Links -->
[forking]: https://guides.github.com/activities/forking/
[ref-clone]: http://gitref.org/creating/#clone
[ref-commit]: http://gitref.org/basic/#commit
[ref-push]: http://gitref.org/remotes/#push
[pull-request]: https://help.github.com/articles/creating-a-pull-request
[ref-multiple-forms]: http://stackoverflow.com/a/14071321
