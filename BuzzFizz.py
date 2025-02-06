def buzzfizz():
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            i = "FizzBuzz"
        elif i % 5 == 0:
            i = "Buzz"
        elif i % 3 == 0:
            i = "Fizz"
        print(i)

buzzfizz()

def palindromenumber():
    for i in range(101):
        i = str(i)
        if i == i[::-1]:
            print(f"{i} Palindrome")
        else :
            print(i, "Pas palindrome")

palindromenumber()


import random

def MaxiNumber():
    MyArray = []
    for _ in range(100):
            New = random.randint(1,100)
            MyArray.append(New)
    print(max(MyArray))
    

MaxiNumber()

def Vowel(quote):
    Vowel = ['a','e','i','o','u']
    VowelCount = 0
    for letter in quote:
        if letter in Vowel:
            VowelCount += 1
    print(VowelCount)

Vowel("James Bond")