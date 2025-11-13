num1 = float(input("Enter First Number: "))
op = input("Enter Operator: ")
num2 = float(input("Enter Second Number: "))

if op == "+" or op == "add":
    print(num1 + num2)
elif op == "-" or op == "subtract":
    print(num1 - num2)
elif op == "*" or op == "multiply":
    print(num1 * num2)
elif op == "/" or op == "divide":
    print(num1 / num2)
else:
    print("Invalid Operator")