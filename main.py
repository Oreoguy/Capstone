# initialise calculator file which will include functionalities
# this is executable py file only
import add

width = 50
print("Welcome to Calculator App".center(width,"-"))

x = int(input("\n\nEnter first number: "))
y = int(input("Enter second number: "))

operation = str(input("\nEnter operation to perform: "))

if operation == "add":
    result = add.add(x,y)

print("\nYour result is: ", result)