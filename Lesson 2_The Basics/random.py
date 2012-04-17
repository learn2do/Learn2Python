__author__ = 'Nathan'

# File: random.py
# This is a basic program designed to demonstrate a chaotic system

def main():
    print("This program demonstrates the output of a chaotic function.")
    x = eval(input("Please input a number between 0 and 1: "))
    for i in range(10):
        x = 3.8*x*(1-x)
        print(x)
main()
