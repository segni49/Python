x= input("Enter first number: ")
y = input("Enter second number: ")

choice = input("Enter operation (+, -, *, /): ")
if choice == '+':
    result = float(x) + float(y)
elif choice == '-':
    result = float(x) - float(y)
elif choice == '*':
    result = float(x) * float(y)
elif choice == '/':
    if float(y) != 0:
        result = float(x) / float(y)
    else:
        result = "Division by zero error"
else:
    result = "Invalid input"

print("Result:", result)