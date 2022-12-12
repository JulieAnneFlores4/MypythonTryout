def Multiplication(num1, num2):
    return num1 * num2

def Addition(num1, num2):
    return num1 + num2

def Subtraction(num1, num2):
    return num1 - num2

def Division(num1, num2):
    return num1 / num2

print("--------------------------------")
print("          Calculator            ")
print("--------------------------------")

value1 = int(input("Enter 1st value: "))
value2 = int(input("Enter 2nd value: "))

print("\nSelect Operation:\n"
      "1.Division\n"
      "2.Multiplication\n"
      "3.Addition\n"
      "4.Subtraction\n")
operation = int(input("Enter your chosen Operator: "))

if operation == 1:
    print(value1, "/", value2, "=", Division(value1, value2))

elif operation == 2:
   print(value1, "*", value2, "=", Multiplication(value1, value2))

elif operation == 3:
   print(value1, "+", value2, "=", Addition(value1, value2))
elif operation == 4:
   print(value1, "-", value2, "=", Subtraction(value1, value2))
else:
   print("Invalid Operator!")
