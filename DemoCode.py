print("Calculator Demo Code")

no1 = int(input("Enter first number : "))
no2 = int(input("Enter second number : "))

operator = input("Enter the operator (+, - *, /) : ")

if operator == '+':
    ans = no1 + no2
    print(ans)
elif operator == '-':
    ans = no1 - no2
    print(ans)
elif operator == '*':
    ans = no1 * no2
    print(ans)
elif operator == '/':
    ans = no1 / no2
    print(ans)
else:
    print("Please enter valid operator....")