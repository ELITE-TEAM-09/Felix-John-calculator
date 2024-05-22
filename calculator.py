print("Enter first number")
first_number = float(input())
print("Enter an operator")
operator = input()
print("Enter second number")
second_number = float(input())
if operator == "+" :
    result = first_number + second_number
elif operator == "-" :
    result = first_number - second_number
elif operator == "*" :
    result = first_number * second_number
elif operator == "/" :
    result = first_number / second_number
elif operator == "%" :
    result = first_number % second_number
else:
    print("INVALID OPERATOR")


print(result)

