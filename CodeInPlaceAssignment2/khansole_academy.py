"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random

MIN = 10
MAX = 99

def main():
    #This line generates two random addends
    num1 = random.randint(MIN , MAX)
    num2 = random.randint(MIN , MAX)
    #Adds the total of the generated addends
    total = num1 + num2
    print("What is " + str(num1) + " + " + str(num2) + "?")
    #Asks the user to input their answer
    ans = input("Your answer: ")
    ans = int(ans)
    #Checks if user input is correct
    if ans == total:
        print("Correct!")
    else:
        print("Incorrect. The expected answer is " + str(total))


if __name__ == '__main__':
    main()