# Question 1: FizzBuzz
# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz";


for a in range(1, 101):
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    elif a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    else:
        print(a)



