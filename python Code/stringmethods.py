'''
Strings are the combination of number, Symbol and letters enclosed inside qoutations

Creating of string: String can be created by enclosing numbers,
letters or special  symbols inside double quotation 
it means assigning  a string value to a variable.

a = "hello world"
print(a)

Types of String Functions
1) length
2) count
3) upper
4) lower
5) index
6) capitilization 
7) Casefold
8) find 
9) format
'''
#SLICING PYTHON
'''
Slicing means extracting a portion of a sequence (string, list, tuple) using indexes.
sequence[start : stop : step]
start → index where slicing begins (default = 0)
stop → index where slicing ends (but it is exclusive, not included)
step → gap/jump between elements (default = 1)

CODE:
text = "PythonProgramming"
print(text[0:6])   # Python
print(text[:6])    # Python
print(text[6:])    # Programming
print(text[:])     # PythonProgramming
print(text[0:12:2])   # Pto rgam (takes every 2nd char)
print(text[-1])     # g  (last character)
print(text[-5:])    # mming
print(text[:-5])    # PythonProgram
Reverse a String
print(text[::-1])   # gnimargorPnohtyP
nums = [10, 20, 30, 40, 50, 60]

print(nums[1:4])    # [20, 30, 40]
print(nums[:3])     # [10, 20, 30]
print(nums[::2])    # [10, 30, 50]
print(nums[::-1])   # [60, 50, 40, 30, 20, 10]
'''
#PROBLEM SOLVING
'''
Write a program to get Fibonacci series up to 10 numbers.
Write a program to check if a number is prime or not.
Write a program to find a palindrome of integers.
Write a program to create an area calculator.

CODE:
1) Fibonacci Series up to 10 numbers
# Fibonacci series up to 10 numbers
a, b = 0, 1
print("Fibonacci series:")
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b


OUTPUT:

Fibonacci series:
0 1 1 2 3 5 8 13 21 34

2) Check if a number is Prime or Not
# Prime number check
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


Sample OUTPUT:

Enter a number: 17
17 is a prime number

3) Palindrome of Integers

 A number is palindrome if it remains same when reversed.

# Palindrome check for integer
num = int(input("Enter a number: "))
reverse = int(str(num)[::-1])

if num == reverse:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")


Sample OUTPUT:

Enter a number: 121
121 is a palindrome

4) Area Calculator

 Let's make a simple menu-based program.

# Area Calculator
print("Choose shape to calculate area:")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    area = 3.14159 * r * r
    print("Area of Circle =", area)

elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    area = l * w
    print("Area of Rectangle =", area)

elif choice == 3:
    side = float(input("Enter side: "))
    area = side * side
    print("Area of Square =", area)

elif choice == 4:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = 0.5 * b * h
    print("Area of Triangle =", area)

else:
    print("Invalid choice")


Sample OUTPUT:

Choose shape to calculate area:
1. Circle
2. Rectangle
3. Square
4. Triangle
Enter your choice: 2
Enter length: 10
Enter width: 5
Area of Rectangle = 50.0
'''

#STRING ANOTHE PROBLEM SOLVE
'''

Take an input from a user as a string then, reverse it.

Write a program to check if a string contains only digits.

Write a program to check if a string is palindrome.

Write a program to find number of vowels in a string.

Write a program to check if every word in a string begins with a capital letter.

CODE:
1) Take an input from a user as a string then, reverse it.
a = input("Enter anything here: ")
print(a[::-1])

OUPUT:
Hello
olleH

2) Write a program to check if a string contains only digits.
a =  input("Enter anything here: ")
print(a.isdigit())

3) Write a program to check if a string is palindrome.
a = input("Enter anything here: ")
rev =  a[::-1]
if a == rev:
   print("it is valid")
else: 
  print("Its not valid")

OUTPUT:
hello 
its not valid

4) Write a program to find number of vowels in a string.
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count = count + 1

print("Number of vowels:", count)

5) Write a program to check if every word in a string begins with a capital letter.
a = input("Enter anything here: ")
print(a.istitle())

OUTPUT:
Abrar here
True
'''
