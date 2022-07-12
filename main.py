print("This is a simple calculator. Only two numbers can be used at this time. \n Thank you for using this calculator.")


num1 = int(input("Please enter your first number here: "))

num2 = int(input("Enter your second number here: "))

operator = input("Please enter your operator here: ")

low_oper = operator.lower()

if low_oper == "multiply" or low_oper == "*":
    print(num1 * num2)

elif low_oper == "divided" or low_oper == "/":
    print(num1 / num2)

elif low_oper == "add" or low_oper == "+":
    print(num1 + num2)

elif low_oper == "subtract" or low_oper == "-":
    print(num1 - num2)

else:
    print("I can't do that!")
