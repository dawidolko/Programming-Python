from array import array
import random
import numpy as np
import itertools

# 1. Wypróbuj kody z listingów znajdujących się w instrukcji i sprawdź ich działanie.

my_array = array('i', [1, 2, 3, 4, 5])
for i in my_array:
    print(i)

# Dodawanie elementu do tablicy przy użyciu append
my_array_append = array('i', [1, 2, 3, 4, 5])
my_array_append.append(6)
print("Po dodaniu 6 metodą append:", my_array_append)

# Dodawanie elementu na konkretnym indeksie przy użyciu insert
my_array_insert = array('i', [1, 2, 3, 4, 5])
my_array_insert.insert(0, 0)  # Dodanie 0 na początku tablicy
print("Po dodaniu 0 na początku metodą insert:", my_array_insert)

# Rozszerzanie tablicy o inną tablicę przy użyciu extend
my_array_extend = array('i', [1, 2, 3, 4, 5])
my_extend_array = array("i", [6, 7, 8, 9, 10])
my_array_extend.extend(my_extend_array)
print("Po rozszerzeniu tablicy metodą extend:", my_array_extend)

# Usuwanie elementu z tablicy przy użyciu remove
my_array_remove = array('i', [1, 2, 3, 4, 5])
my_array_remove.remove(4)

# Usuwanie ostatniego elementu z tablicy metodą pop
my_array_pop = array('i', [1, 2, 3, 4, 5])
my_array_pop.pop()

# Odwracanie tablicy przy użyciu reverse
my_array_reverse = array('i', [1, 2, 3, 4, 5])
my_array_reverse.reverse()

(my_array_remove, my_array_pop, my_array_reverse)

# Sprawdzanie informacji o tablicy (adres i długość) przy użyciu buffer_info
my_array_info = array('i', [1, 2, 3, 4, 5])
print("Informacje o tablicy:", my_array_info.buffer_info())

# Zliczanie wystąpień elementu w tablicy przy użyciu count
my_array_count = array('i', [1, 2, 3, 3, 5])
print("Liczba wystąpień elementu '3':", my_array_count.count(3))

# Konwersja tablicy do listy przy użyciu tolist
my_array_to_list = array('i', [1, 2, 3, 4])
converted_list = my_array_to_list.tolist()
print("Konwersja tablicy do listy:", converted_list)



# 2. Napisz skrypt wypełniający tablicę znakami, a następnie wyświetl znaki w kolejności odwrotnej
# do wprowadzania. Dane wprowadzane z klawiatury.

# Pobranie ciągu znaków od użytkownika
user_input = input("Wprowadź ciąg znaków: ")

# Utworzenie tablicy typu 'u' (dla znaków Unicode) i dodanie do niej znaków z ciągu wprowadzonego przez użytkownika
char_array = array('u', user_input)

# Odwrócenie kolejności elementów w tablicy
char_array.reverse()

# Wyświetlenie odwróconych znaków
print("Odwrotna kolejność znaków:", ''.join(char_array))

# 3. Wypełniający tablicę liczbami losowymi rzeczywistymi z przedziału (-5,5). Wartość tablicy zapisz do pliku _result.txt_

# Utworzenie tablicy typu 'f' dla liczb zmiennoprzecinkowych
random_numbers = array('f', [random.uniform(-5, 5) for _ in range(10)])  # Generowanie 10 liczb losowych

# Otworzenie pliku result.txt w trybie zapisu
with open("result.txt", "w") as file:
    # Zapis wartości tablicy do pliku, każda liczba w nowej linii
    for number in random_numbers:
        file.write(f"{number}\n")


# 4. Napisz funkcję tworzącą tablicę dwuwymiarową (5x5) która zostanie wypełniona kwadratami liczb z komórek z wiersza wcześniejszego. Pierwszy wiersz wypełniony wartościami 2,3,4,5,6. Do utworzenia tablicy dwuwymiarowej wykorzystaj bibiotekę NumPy. Bibliotekę można zainstalować przy pomocy polecenia:
# python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
import numpy as np

# Utworzenie pierwszego wiersza tablicy
first_row = np.array([2, 3, 4, 5, 6])

# Utworzenie tablicy dwuwymiarowej 5x5
array_2d = np.zeros((5, 5), dtype=int)

# Wypełnienie pierwszego wiersza wartościami
array_2d[0] = first_row

# Iteracja przez kolejne wiersze i wypełnienie ich
for i in range(1, 5):
    array_2d[i] = array_2d[i-1] ** 2

# Wydrukowanie utworzonej tablicy
print(array_2d)


# 5. Napisz funkcję, która jako parametr przyjmuje lokalizację pliku tekstowego który zawiera dowolny tekst i zwraca histogram znaków występujących w tym napisie (czyli pary znak-liczba wystąpień). Wynikiem powinien być słownik. Przykład:
# >>> histogram("document.txt") dokument zawiera tekst: Ala ma kota {'t': 1, 'a': 3, 'l': 1, 'A': 1, 'k': 1, 'm': 1, 'o': 1}
def histogram(file_path):
    # Słownik do przechowywania histogramu znaków
    char_histogram = {}

    # Otwarcie pliku do odczytu
    with open(file_path, 'r') as file:
        # Odczytanie całego tekstu z pliku
        text = file.read()

        # Przejście przez każdy znak w tekście
        for char in text:
            # Aktualizacja licznika wystąpień znaku w słowniku
            if char in char_histogram:
                char_histogram[char] += 1
            else:
                char_histogram[char] = 1

    # Zwrócenie histogramu
    return char_histogram

# Przykładowe wywołanie funkcji
histogram_result = histogram("document.txt")
print(histogram_result)


# 6. Napisz następujące funkcje niezbędne do implementacji gry w pokera pięciokartowego dobieranego:
#
# deck() - zwraca listę reprezentującą talię kart w kolejności od najmłodszej do najstarszej. Każda karta posiada 2 atrybuty, będące łańcuchem tekstowym:
# rangę - możliwe wartości: '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A' (karty od 2 do 10 oraz walet, dama, król, as)
#
# kolor - możliwe wartości:
#
# 🔹c - ♣ trefl (clubs)
#
# 🔹d - ♦ karo (diamonds)
#
# 🔹h - ♥ kier (hearts)
#
# 🔹s - ♠ pik (spades)
#
# Każdym elementem listy powinna być krotka, będąca parą (ranga, kolor). Przykładowo as pik:
#
# 🂡
# reprezentowany będzie jako ('A', 's'). Lista powinna zawierać 52 elementy (13 rang * 4 kolory).
#
# shuffle_deck(deck) - przyjmuje listę kart, zwraca karty potasowane (permutacja). Skorzystaj z:
#
# deal(deck, n) - przyjmuje talię kart (deck) oraz liczbę graczy (n), zwraca n-elementową listę 5-elementowych list z kartami rozdanymi graczom. Każda 5-elementowa lista kart gracza zawiera 5 krotek reprezentujących kartę.
def deck():
    families = ['c', 'd', 'h', 's']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    cards = []
    for i in itertools.product(values, families):
        cards.append(i)
    return cards


def shuffle_deck(deck):
    random.shuffle(deck)


def deal(deck, n):
    if n > 10:
        print("Mozna grac maksymalnie w 10 osob.")
    else:
        mainDeal = []
        for i in range(n):
            playerDeck = []
            for j in range(5):
                index = random.randint(0, len(deck) - 1)
                playerDeck.append(deck[index])
                deck.remove(deck[index])
            mainDeal.append(playerDeck)
        return mainDeal


mainDeck = deck()
print(mainDeck)
shuffle_deck(mainDeck)
print(mainDeck)
print(deal(mainDeck, 3))
