def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

main = True

def main_program():
    print("Welcome to the factorial calculator!")

def do_program():
    number = int(input("Enter a positive integer: "))
    factorial_result = factorial(number)
    print(f"The factorial of {number} is {factorial_result}.")
    print("Program execution completed.")
    choise = input("Do you want to continue? (true/flase): ")
    if choise.lower() == "true":
        do_program()
    else:
        print("Goodbye!")

import os

chois = input("Shut down the program? (true/false): ") 
if chois.lower() == "true":
    os.system("shutdown /s /t 0") 
else:
    do_program()
# main program execution
main_program()    
do_program()

