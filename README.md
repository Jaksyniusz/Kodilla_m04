# Kodilla_m04
4th module tasks

### Zadanie 4.2

Zadanie: palindromy<br>
Pamiętaj, że wszystkie zadania, które wysyłasz Mentorowi powinny być umieszczone w Twoim zdalnym repozytorium, jako osobne projekty. W czasie pracy zapisuj więc kolejne commity i prześlij całość na serwer w serwisie GitHub.<br>
Twoim zadaniem będzie napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem. Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.<br>
Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False, mówiącą czy podany tekst jest palindromem.
Podpowiedź<br>
Pamiętaj, że string/tekst, to kolekcja znaków. Znasz już funkcje kolekcji, które pozwalają odnosić się do elementów indeksowanych od początku i od końca.<br>

### Zadanie 4.4

Zadanie: kalkulator<br>
Czas na duże, poważne zadanie! Dojrzewasz jako programista, więc mamy coś odpowiedniego – stworzymy własny kalkulator, oczywiście nieco uproszczony. Załóżmy, że będzie przyjmował zawsze dwie liczby do obliczeń.<br>
Docelowo chcielibyśmy uzyskać taki efekt:<br>
<prep>
    Po uruchomieniu programu jesteśmy pytani o typ obliczenia

    >> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:

    Następnie pobieramy dwie wartości liczbowe.

    Korzystając z biblioteki logging, informujemy użytkownika, jakie działanie wykonamy i jakie będą jego argumenty (np. Dodaję 1 i 3).

    Następnie wykonujemy obliczenie i drukujemy rezultat z print.
</prep>
Do pobierania wartości użyj input. Nie ma potrzeby sprawdzania, czy podane argumenty są liczbami, przewidujemy poprawne uzupełnienie.<br>
Przykładowe wywołanie razem z wartościami wybranymi przez użytkownika może wyglądać tak:<br>
<prep>
>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: 1
Podaj składnik 1. 2.3
Podaj składnik 2. 5.4
Dodaję 2.30 i 5.40
Wynik to 7.70
</prep>
Dla chętnych<br>
Jeśli chcesz usprawnić swoje zadanie, możesz dodać dwa rozszerzenia:<br>
<prep>
    Sprawdzaj, czy podana wartość na pewno jest liczbą.
    W wypadku mnożenia i dodawania daj użytkownikowi możliwość wpisania większej ilości argumentów niż tylko dwa, np. możesz dodać do siebie trzy i więcej liczb.
</prep>


### Zadanie 4.X

Ćwiczenie<br>
Żeby dobrze sobie to przećwiczyć, zadeklaruj trzy funkcje z pustą implementacją, czyli z komendą pass.<br>
Pierwsza z nich, fun_default, powinna przyjmować argumenty pozycyjne albo nazwane. Druga, fun_positional, tylko pozycyjne. Trzecia, fun_keyword, tylko nazwane. Testem na to, czy druga i trzecia funkcja jest dobrze zadeklarowana będzie próba podstawienia argumentów odwrotnie, niż było w planie, czyli np. do fun_keyword, próba podania argumentów pozycyjnych.<br>


Ćwiczenie<br>
Do powyższego przykładu implementacji funkcji count_them_alldopisz sprawdzenie ilości argumentów nazwanych. Wypisz go w linijce z wykorzystaniem print. Następnie przetestuj czy takie wywołanie<br>
<prep>
count_them_all(1, 2, 3, "A", a=1, b=2)
</prep>
poprawnie zidentyfikuje dwa argumenty nazwane.<br>
To, że argumenty nazwaliśmy args i kwargs jest przyjętą konwencją. Tak naprawdę moglibyśmy zrobić to dowolnie. Jeśli jednak użyjesz tych nazw, to żaden programista Pythona nie będzie miał wątpliwości, o co Ci chodziło.<br>


Ćwiczenie<br>
Wywołaj help() na kilku funkcjach, które już znasz, np. print(). Czy teraz jest już dla Ciebie jasne, dlaczego dobrze jest pozostawić dobrą dokumentację swojego kodu?
Z tej samej beczki<br>
W internecie znajdziemy mnóstwo projektów, z których możemy korzystać. Na najbardziej popularnym portalu do przechowywania kodu — GitHub — ludzie zwykle dołączają plik README.md, który jest pokazywany jako “strona domowa” dla projektu. To dobre miejsce, by umieścić w nim dokumentację.<br>
W Pythonie możesz zdefiniować dokumentację dla swojej funkcji w bardzo łatwy sposób. Po prostu zadeklaruj tekst na jej początku. Teraz każdy, kto będzie chciał się dowiedzieć, jak działa Twoja funkcja i jak interpretować jej argumenty, będzie mógł się tego dowiedzieć dzięki funkcji help().c
<prep>
def customized_hello(first_name, last_name, gender_prefix='Mr'):
    """
        Prints hello, based on arguments passed
        Arguments:
        first_name,
        last_name
        Optional arguments:
        gender_prefix:  Mr/Ms based on sex of person
    """
    print("Hello %s %s %s" % (gender_prefix, first_name, last_name))
</prep>