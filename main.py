# initialise calculator file which will include functionalities
# this is executable py file only
import add, subtract, divide, multiply

width = 50
print("Welcome to Calculator App".center(width,"-"))

x = int(input("\n\nEnter first number: "))
y = int(input("Enter second number: "))

operation = str(input("\nEnter operation to perform: "))

if operation == "add":
    result = add.add(x,y)

elif operation == "sub":
    result = subtract.subtract(x,y)

elif operation == "mul":
    result = multiply.multiply(x,y)

elif operation == "div":
    result = divide.divide(x,y)

else:
    result = "Invalid operation or error"

print("\n")
print(("Your result is: " + str(result)).center(width,"-"))