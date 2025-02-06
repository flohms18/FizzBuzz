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