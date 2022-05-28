first_number = int(input("Enter first integer: "))
second_number = int(input("Enter second integer: "))


print("What operation would you like to perform?")
operation = str(input("Press A for addition, B for subtraction, C for multiplication,"
                      "D for division, and E for modulo: "))


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b



def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def modulo(a, b):
    return a % b


if operation.lower() == "a":
    print(addition(first_number, second_number))
elif operation.lower() == "b":
    print(subtraction(first_number, second_number))
elif operation.lower() == "c":
    print(multiplication(first_number, second_number))
elif operation.lower() == "d":
    print(division(first_number, second_number))
elif operation.lower() == "e":
    print(modulo(first_number, second_number))
