print("Saksham's Calculator:")
print("ENTER 1 for Addition of a and b")
print("ENTER 2 for Subtraction of a and b")
print("ENTER 3 for Multiplication of a and b")
print("ENTER 4 for Division of a and b")
print("Any other number to exit the program")

while True:
    key = int(input("\nENTER KEY: "))
    if key < 1 or key > 4:
        print("Exiting...")
        break

    a = int(input("ENTER VALUE OF a: "))
    b = int(input("ENTER VALUE OF b: "))

    if key == 1:
        result = a + b
        print("ADDITION OF a AND b:", result)
    elif key == 2:
        result = a - b
        print("SUBTRACTION OF a AND b:", result)
    elif key == 3:
        result = a * b
        print("MULTIPLICATION OF a AND b:", result)
    elif key == 4:
        if b != 0:
            result = a / b
            print("DIVISION OF a AND b:", result)
        else:
            print("Error: Division by zero is not possible ")
