# 1. Wypróbuj kod z listingów znajdujących się w instrukcji i sprawdź ich działanie.
print("\n\nZADANIE ", "1.","\n\n")

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

def pure_function(x, y):
    temp = x + 2 * y
    return temp / (2 * x + y)

some_list = []

def impure(arg):
    some_list.append(arg)

def my_func(f, arg):
    return (f(arg))

print(my_func(lambda x: 2 * x * x, 5))

# nzawana funkcja
def polynomial(x):
    return x ** 2 + 5 * x + 4

print(polynomial(-4))

# lambda
print((lambda x: x ** 2 + 5 * x + 4)(-4))

double = lambda x: x * 2
print(double(7))

def decor(func):
    def wrap():
        print("==================")
        func()
        print("==================")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

def decor(func):
    def wrap():
        print("==================")
        func()
        print("==================")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

nums = {1, 2, 1, 3, 4, 5, 1}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

# 2. Napisz funkcję z wykorzystaniem wyrażenia lambda która dla przyjętego argumentu x wyznaczy listę kwadratów kolejnych liczb naturalnych od 1 do x
print("\n\nZADANIE ", "2.","\n\n")

ex1 = lambda x: [i**2 for i in range(1, x+1)]
print(ex1(14))

# 3. Z podanej poniżej listy odfiltruj elementy które są większe od 4 wykorzystując funkcję filter.
print("\n\nZADANIE ", "3.","\n\n")
nums = [1, 2, 3, 5, 8, 3, 0, 7]
filtered = list(filter(lambda x: x>4, nums))
print(filtered)

# 4. Napisz funkcję z wykorzystaniem generatora która wygeneruje poniższe elementy listy
print("\n\nZADANIE ", "4.","\n\n")
def spamWord():
    word = 'spam'
    for i in range(1, len(word)+1):
        yield word[0:i]

print(list(spamWord()))

# 5. Napisz funkcję obliczającą dowolne równanie a następnie napisz funkcję dekorującą która przed wynikiem wstawi pierwotny wzór funkcji.
print("\n\nZADANIE ", "5.","\n\n")
def decor(showing):
    def evaluate():
        a = 4
        b = 5
        showing(a, b)
        print(a+b)
    return evaluate

def printing(a, b):
    print(str(a) + " + " + str(b))

decorated = decor(printing)
decorated()

# 6. Napisz rekurencyjną funkcję przyjmującą 2 parametry która z podanych wartości obliczy wartość symbolu Newtona.
print("\n\nZADANIE ", "6.","\n\n")
def newton(n, k):
    if k==n or k==0:
        return 1
    else:
        return newton(n-1,k-1)+newton(n-1,k)

print(newton(5,3))

# 7. Napisz funkcję w której przetestujesz wszystkie omawiane operacje na zbiorach.
print("\n\nZADANIE ", "7.","\n\n")
def ex7(set1, set2):
    print(set1 | set2)
    print(set1 & set2)
    print(set1 - set2)
    print(set1 ^ set2)

set1 = set([1,4,7,9])
set2 = set([1,2,4,5,6,7])
ex7(set1, set2)
