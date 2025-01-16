
sec = int(input("Choose the operation (1: Addition, 2: Subtraction, 3: Division, 4: Multiplication): "))

if sec not in [1, 2, 3, 4]:
    print("Error: Invalid operation")
else:
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))

    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def division(a, b):
        if b == 0:
            return "A number cannot be divisible by zero!"
        return a / b

    def multiplication(a, b):
        return a * b

    if sec == 1:
        print("Result:", addition(a, b))
    elif sec == 2:
        print("Result:", subtraction(a, b))
    elif sec == 3:
        print("Result:", division(a, b))
    elif sec == 4:
        print("Result:", multiplication(a, b))
