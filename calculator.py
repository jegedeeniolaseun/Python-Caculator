print("=" * 40)
print("      ENIOLA TECH CALCULATOR")
print("=" * 40)

while True:

    print()

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        answer = num1 + num2

    elif operator == "-":
        answer = num1 - num2

    elif operator == "*":
        answer = num1 * num2

    elif operator == "/":
        if num2 == 0:
            print("❌ Error! Division by zero.")
            continue
        answer = num1 / num2

    else:
        print("❌ Invalid operator.")
        continue

    print("-" * 40)
    print("Answer =", answer)
    print("-" * 40)

    again = input("Do another calculation? (yes/no): ")

    if again.lower() != "yes":
        print()
        print("Thank you for using ENIOLA TECH CALCULATOR!")
        print("Goodbye!")
        break