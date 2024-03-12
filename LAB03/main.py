from array import array
import random
import numpy as np
import itertools

# Ex. 2, 3
counter = int(input("Podaj ilosc: "))
chars = array('i', [])

for i in range(counter):
    chars.append(random.randint(-5, 5))

chars.reverse()

with open("result.txt", "w") as file:
    for i in chars:
        print(i, end=" ")
        file.write(str(i) + " ")

print()

# Ex. 4
matrix = np.zeros((5, 5), dtype="uint64")
matrix[0] = [2, 3, 4, 5, 6]

for x in range(1, 5):
    for y in range(0, 5):
        matrix[x][y] = matrix[x - 1][y] ** 2

print(matrix)
print()


# Ex. 5
def histogram(url):
    charsCounter = dict()
    with open(url) as file:
        line = file.readline()
        line = line.split()
        for x in line:
            for y in x:
                if y not in charsCounter:
                    charsCounter[y] = 1
                else:
                    charsCounter[y] += 1
        return charsCounter


print(histogram("histogram.txt"))
print()


# Ex. 6
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
