#Print Statement
#To call a print function in python we just need to wrtite print followed by parenthesis() and values written inside quotation marks
#INPUT-
print("Hello World")
#OUTPUT
#-------Hello World
print("This is my first program")

#Single Multiple Lines IN Print Statement
'''
Theory
There are two methods to write a statement in multiple lines:
    To print multiple lines in python, Triple Quotations are used.
    \n (Backslash) is used to insert something in the next line

CODE:
print("""This is me Abrar!
      We are here!
      We Can help you!""")
'''

#Single Line Comments

'''Single Line Comments
To Add Single Line Comments, #Hash is used.
Python Completely Ignores anything written after #
'''

#Variables
'''
Theory:
Variables are placeholder, which can store a value.
In Simple words, Variable is container that holds data inside it as a Value

Code:
a =  "Hello"
Print(a)

Rules of Variable Name
1) Make Sure to not use Spaces while creating a variable.
one can use (_) underscore to separate the names while writing a variable

2) A variable name should never start with a number or special symbol
'''

#Data Types and User-Input
'''
DataTypes:
Text-Type: String(str)
Numeric Types: integer(int), floating point(float), complex
Sequence Types: List, Tuple, and Range
Mapping Type: Dictionaries(dict)
Set Types: Set, Frozenset
Boolean Type: Bool
Binary Types: Bytes, bytearray, memoryview

To Ask for the input from the user, Default datatype is string

CODE: 
name = input("Enter Your NAME Here: ")
print(name)

OUTPUT:
Enter Your NAME Here

age = int(input('Enter Your Age Here: '))
print(age)

OUTPUT:
Enter Your Age Here

exp1 =  eval(input("Enter Any Equation here: "))
print(exp1)

OUTPUT:
2+5 
7
This eval evalution the any mathamatication Operation, 
'''

#Type Casting and SubTypes
'''
Type Casting
Conversion of one datatype to another is called as type-casting.

There are two types of type-casting:
1)Implicit Type Conversion: Where python itself converts one datatype to another.

2) Explicit Type Conversion: Where the user converts one data type to another 

CODE: 
A = 123
B = 1.23
print(type(A))
print(type(B))
Integer
Float

A = 123
B = 1.23
IMPLICIT TC:
C = A+B
print(C)
print(type(C))
124.23
TYPE float (Python Automatic Conversion means Implicit use we give in integer and decimal python conversion it in float)
'''

#Problem Solving
'''
1) Write a program to display a person's name . age and address in three different lines
2) Write a Program to swap two variables
3) Write a program to Convert  a float into Integer.
4) Write a program to take details from a student for ID-CARD and then print it in different lines
5) Write a Program to take an user Input as Integer then Convert to float

# Program 1: Display person's details
name = "Abrar Khan"
age = 24
address = "Karachi, Pakistan"

print("Name:", name)
print("Age:", age)
print("Address:", address)

# Program 2: Swap two variables
temp = a
a = b
b = temp

print("After Swap:", a, b)

# Program 3: Convert float to integer
num = 12.75
converted = int(num)

print("Float Value:", num)
print("Integer Value:", converted)

# Program 4: Student ID Card
name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
program = input("Enter Program: ")
department = input("Enter Department: ")
university = input("Enter University: ")

print("\n===== Student ID Card =====")
print("Name:", name)
print("Roll No:", roll)
print("Program:", program)
print("Department:", department)
print("University:", university)

# Program 5: Convert integer input into float
num = int(input("Enter an integer: "))
converted = float(num)

print("Integer Value:", num)
print("Float Value:", converted)
'''

#Operators and Operands
'''
Operators indicates what operation is to be performed while operands indicates on waht the action or the operation should be performed
x+y = 0
In the given expression , x,y and O are Operands 

Types of Operators:
Operators can be further divided into 6 Categories:
1) Arithmetic Operators
2) Comprasion Operators
3) Logical operators
4) Assignment Operators
5) Identity Operators 
6) Membership Operators
7) Bitwise Operators
'''
#Arthmetic Operators
'''
Operation are like addition, substraction, modulus, division etc
Print(8%3)
Modules Division sy pehly ke value deta hy!
print(8//3) This use for Floor Division
print(2**10) To ke power 10 so Answer (1024)
'''
#Comparison Operators
'''
Is like <,>, <=, >=,!=  etc
print(3>=3)
OUTPUT:
True
'''

#Logical Operators
'''
and, or, not
print(3>4 or 3<4)
True
'''
#Assignement Operators
'''
Assignment operators are used in python to assign values to variables.
a =  6 is a simple assignment operators that assign the value 6 on the right to the variable a on the left.

Operator    Example      Equivalent to
 =           x=6           x= 6
 +=          x+=6          x=x+6
 -=          x-=6          x=x-6
 *=          x*=6          x=x*6
'''

#Identity Operators
'''
Identity operators are used to compare items to see if they are the same object with the same memory address
Types:
1) Is
2) Is not

CODE:
A = 1234
B = 1234
print(a is b)
True

print(a is not b)
False
'''

#Bitwise Operators
'''
These Operators are used to compare the binary numbers
Types:
1) AND (&) Operator
2) OR (|) Operator
3) XOR (^) Operator
4) << Zero Fill left shift
5) >> zero  Fill right shift

'''

#MemberShip Operators
'''
Membership Operators:
Membership Operators are used to check the presence of a sequence in an object.
Types:
1) In 
2) Not in

CODE:
a = "hello"
print("p",not in a)
OUTPUT:
True
'''
