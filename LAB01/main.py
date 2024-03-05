# ️1. Podstawowe obliczenia w Pythonie:
print("\n"+"=============")
print(1, "ZADANIE.")
print("============="+"\n")

# Dodawanie
print(5 + 3)

# Odejmowanie
print(10 - 7)

# Mnożenie
print(4 * 6)

# Dzielenie
print(15 / 3)

# 2. Skrypt pytający użytkownika o imię i wyświetlający powitanie:
print("\n"+"=============")
print(2, "ZADANIE.")
print("============="+"\n")

imie = input("Podaj swoje imię: ")
print("Witaj,", imie + "!")

# 3. Skrypt obliczający sumę liczb całkowitych wprowadzonych przez użytkownika i wyświetlający wynik jako liczbę zmiennoprzecinkową:
print("\n"+"=============")
print(3, "ZADANIE.")
print("============="+"\n")

print(float(sum(int(x) for x in input("Podaj liczby oddzielone spacją: ").split())))

# 4. Obliczenie sumy liczb naturalnych od 8 do 80:
print("\n"+"=============")
print(4, "ZADANIE.")
print("============="+"\n")

suma = sum(range(8, 81))
print(suma)

# 5. Skrypt obliczający liczbę dni od zadanej daty do daty aktualnej:
print("\n"+"=============")
print(5, "ZADANIE.")
print("============="+"\n")

from datetime import datetime

data = input("Podaj datę w formacie rrrr-mm-dd: ")
data_zadana = datetime.strptime(data, "%Y-%m-%d")
dzis = datetime.now()
roznica = dzis - data_zadana
print("Liczba dni od zadanej daty do dzisiaj:", roznica.days)

# 6. Prosty kalkulator z menu wyboru działania dla dwóch liczb:
print("\n"+"=============")
print(6, "ZADANIE.")
print("============="+"\n")

def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y == 0:
        return "Nie można dzielić przez zero!"
    else:
        return x / y

print("Wybierz działanie:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Potegowanie")

wybor = input("Podaj numer działania (1/2/3/4/5): ")

num1 = float(input("Podaj pierwszą liczbę: "))
num2 = float(input("Podaj drugą liczbę: "))

if wybor == '1':
    print("Wynik dodawania:", dodawanie(num1, num2))
elif wybor == '2':
    print("Wynik odejmowania:", odejmowanie(num1, num2))
elif wybor == '3':
    print("Wynik mnożenia:", mnozenie(num1, num2))
elif wybor == '4':
    print("Wynik dzielenia:", dzielenie(num1, num2))
elif wybor == '5':
    print("Wynik potegowania:", pow(num1, num2))
else:
    print("Niepoprawny wybór działania.")
