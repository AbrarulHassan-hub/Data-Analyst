#------------------Condition Statements----------------
'''
Conditional Statement allows computer to execute a certain condition only if it is true
Types of Conditional Statements:
1) If the Statement
2) if-else Statement
3) if-elif-else statement
4) Nested Statement
5) Short Hand If Statement
'''
# If Statement
'''The If Statement is the most fundamental decision-making statement. The if Statement in python has the subsequent syntax:
    if expression:
        statement
CODE:
marks = 97
if marks >= 90:
   print('You will ge a mobile phone')
print("Thank You")

OUTPUT:
you will get a mobile phone 
Thank You
'''

#if-else Statement
'''
if-else statement is used when you want to give two different condition to the computer.
Here if one condition is false, program executes the another condition.
if condition:
      #will execute this block if the condition is true
else:
      #WILL execute this block if the condition is false
      
CODE:
marks =  97
if marks >= 90:
   print("You will gget a phone")
else: 
    print("no phone for 1 week")
print("Thank you")
      
OUTPUT:
you will get a phone 
Thank you
'''
#if-elif-else statement
'''
In this case, the if condition is evaluated first. if it is false, the elif statement will be executed, if it also comes false then else statement will be executed.
For multiple Condition, MOre elif statement are added.
if condition:
   body of if
elif condition:
   body of elif
else:

CODE:
marks = 50

if marks >= 90:
    print("You can go to a trip")
elif marks >= 80 and marks < 90:
    print("You will get a new phone")
elif marks >= 70 and marks < 80:
    print("You will get a new book")
else:
    print("You will not get your phone back")

OUTPUT:
You will not get your phone back
'''
# problems
'''
1) Write a Program to check if a number is positive 
2) Write a program to check whether a number is odd or even
3) write a program to create area calculator 
4) write a program check whether the passed letter is a vowel or not 
5) Write a program to check if a number is a single digit number , 2 - digits number and so on up to 5 digits
'''
#Solution
'''
1) Write a Program to check if a number is positive 
num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

2) Check whether a number is odd or even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

3) write a program to create area calculator 
print("Area Calculator")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    radius = float(input("Enter radius: "))
    area = 3.1416 * radius * radius
    print("Area of Circle:", area)

elif choice == 2:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print("Area of Rectangle:", area)

elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of Triangle:", area)

else:
    print("Invalid Choice!")

4) write a program check whether the passed letter is a vowel or not 
letter = input("Enter a single letter: ").lower()

if letter in ['a', 'e', 'i', 'o', 'u']:
    print("It is a Vowel")
else:
    print("It is not a Vowel")

5) Write a program to check if a number is a single digit number , 2 - digits number and so on up to 5 digits
num = int(input("Enter a number up to 5 digits: "))

if num >= 0 and num <= 9:
    print("It is a single digit number")

elif num >= 10 and num <= 99:
    print("It is a double digit number")

elif num >= 100 and num <= 999:
    print("It is a three digit number")

elif num >= 1000 and num <= 9999:
    print("It is a four digit number")

elif num >= 10000 and num <= 99999:
    print("It is a five digit number")

else:
    print("Number is more than 5 digits")


'''