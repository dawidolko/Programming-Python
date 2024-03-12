#Zad. 2
ex1 = lambda x: sum([i**2 for i in range(1, x+1)])
print(ex1(14))

#Zad. 3
nums = [1, 2, 3, 5, 8, 3, 0, 7]
filtered = list(filter(lambda x: x<=4, nums))
print(filtered)

#Zad. 4
def spamWord():
    word = 'spam'
    for i in range(1, len(word)+1):
        yield word[0:i]

print(list(spamWord()))

#Zad. 5
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

#Zad. 6
def newton(n, k):
    if k==n or k==0:
        return 1
    else:
        return newton(n-1,k-1)+newton(n-1,k)

print(newton(5,3))

#Zad. 7
def ex7(set1, set2):
    print(set1 | set2)
    print(set1 & set2)
    print(set1 - set2)
    print(set1 ^ set2)

set1 = set([1,4,7,9])
set2 = set([1,2,4,5,6,7])
ex7(set1, set2)