def add (num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1*num2
def divide(num1, num2):
    return num1 / num2

num1 = int(input("enter the first number:  "))
num2 = int(input("Enter the second number:  "))

print("Choose your operator")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")

choice = int(input("enter you choice (1-4):  "))

#subroutine recollection
if choice == 1:
    result = add(num1, num2)
    print(f"The result of adding {num1} and {num2} is {result}")
elif choice == 2:
    result = subtract(num1, num2)
    print(f"The result of subtracting {num1} and {num2} is {result}")
elif choice == 3:
        result = mutiply (num1, num2)
        print(f"The result of multiplication {num1} and {num2} is {result}")
elif choice ==4:
    result= divide(num1, num2)
    print(f"The result of division {num1} and {num2} is {result}")
else: print("Invalid Choice...")