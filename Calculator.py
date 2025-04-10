print("Calculator")
while True:
    num1 = float(input("\nEnter first number: "))

    op = input("Enter operation {Addition(+), Subtraction(-), Multiplication(*), Division(/), Exponent(**)}\n→ ")

    num2 = float(input("Enter second number: "))

    result = None

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Go back to basics, a number can't be divided by 0!")
    elif op == "**":
        result = num1 ** num2
    else:
        print("Kya bhai, bhand-vand ho kya? Invalid operation entered.")

    if result is not None:
        print("Result is:", result)

    again = input("\nCalculate again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Adios!")
        break

