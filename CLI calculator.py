def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2 if num2 != 0 else "Error: Division by zero"
print("please select operation\n"
"1.add\n"
"2.sub\n"
"3.mul\n"
"4.div\n")
op=input("select operation:")
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
#using if else for programming a calculator
if op=="1" :
    print("result:", add(num1,num2))
elif op=="2" :
    print("result:", subtract(num1, num2))
elif op=="3" :
    print("result:", multiply(num1, num2))
elif op=="4" :
    print("result:", divide(num1, num2))
else:
    print("invalid input")
