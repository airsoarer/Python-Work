import sys
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def exponent(num1, num2):
    return num1 ** num2

def slope(y1, y2, x1, x2):
    return (y2 - y1) / (x2 - x1)

def calculate():
    print("Welcome to the Calculator, choose what your would like to do: ") 
    print("0 = addition")
    print("1 = subtraction")
    print("2 = multiplication")
    print("3 = division")
    print("4 = exponent")
    print("5 = slope")

    chocie = input("What operation would you like to do?: ")

    if chocie == "0":
        num1 = input("enter your first number: ")
        num1 = int(num1)
        num2 = input("enter your second number: ")
        num2 = int(num2)
        print(addition(num1, num2))
        yesNo = input("Would you like to use The Calculator again? Y/N: ")
        if yesNo == "Y" or yesNo == "y":
            calculate()
        elif yesNo == "N" or yesNo == "n":
            exit()

    elif chocie == "1":
        num1 = input("enter your first number: ")
        num1 = int(num1)
        num2 = input("enter your second number: ")
        num2 = int(num2)
        print(subtraction(num1, num2))
        yesNo = input("Would you like to use The Calculator again? Y/N")
        if yesNo == "Y" or yesNo == "y":
            calculate()
        elif yesNo == "N" or yesNo == "n":
            exit()

    elif chocie == "2":
        num1 = input("enter your first number: ")
        num1 = int(num1)
        num2 = input("enter your second number: ")
        num2 = int(num2)
        print(multiplication(num1, num2))
        yesNo = input("Would you like to use The Calculator again? Y/N")
        if yesNo == "Y" or yesNo == "y":
            calculate()
        elif yesNo == "N" or yesNo == "n":
            exit()

    elif chocie == "3":
        num1 = input("enter your first number: ")
        num1 = int(num1)
        num2 = input("enter your second number: ")
        num2 = int(num2)
        print(division(num1, num2))
        yesNo = input("Would you like to use The Calculator again? Y/N")
        if yesNo == "Y" or yesNo == "y":
            calculate()
        elif yesNo == "N" or yesNo == "n":
            exit()

    elif chocie == "4":
        num1 = input("enter your first number")
        num1 = int(num1)
        num2 = input("enter your second number")
        num2 = int(num2)
        print(exponent(num1, num2))
        yesNo = input("Would you like to use The Calculator again? Y/N")
        if yesNo == "Y" or yesNo == "y":
            calculate()
        elif yesNo == "N" or yesNo == "n":
            exit()

    elif chocie == "5":
        y1 = input("enter the value for y1")
        y1 = int(y1)
        y2 = input("enter the value for y2")
        y2 = int(y2)
        x1 = input("enter the value for x1")
        x1 = int(x1)
        x2 = input("enter the value for x2")
        x2 = int(x2)
        print(slope(y1, y2, x1, x2))
        yesNo = input("Would you like to use The Calculator again? Y/N")
        if yesNo == "Y" or yesNo == "y":
            calculate()
        elif yesNo == "N" or yesNo == "n":
            exit()
    
    else:
        print("You did not enter anything.")
        calculate()

calculate()
          



    
