#Loops
'''
A loop  means to repeat something in the exact same way.
Type of Loop are:
1) For Loop
2) While Loop
3) While True
4) Nested Loop 
'''
#For loop
'''
Theory
For loop is a loop that repeats something in a given range.
The Range  has  a starting  point, ending point and a step/gap  in it 
+ is  added  to the ending point while defining a range

CODE:
For i in range(1,6):
    print(i)

OUTPUT
1
2
3
4
5

CODE:
Create Table
n = int(input("Enter a number here: "))
for i in range(1,51):
    print(n,"x",i,"=",n*i)
'''
#While loop
'''
while loop executes till the given condition is true.
In while loop, the increment is done inside the loop

code:
n = 1
while n <= 5:
      print(n)
      n +=1
'''

#Break and Continue Statement
'''
Continue Statement:
Continue statement is used when you want to skip a particular.
Condition:
Break statement:
break statement is used when you want to  destroy a loop  at a certain  condition  and come  out of loop.

CONTINUE CODE:
for i in range(1,5):
    if i == 3:
       continue:
    else:
       print(i)
OUTPUT:
1
2
4

BREAK CONDITION:
for i in range (1,11):
    if i == 7:
       break
    else:
        print(i)

output:
1
2
3
4
5
6
'''
#PROBLEM SOLVING
'''

1) Write a program to find a sum of all the even numbers up to 50.
2) Write a program to write first 20 numbers and their squared numbers.
3) Write a program to find sum of first 10 odd numbers using while loop.
4) Write a program to check if a number is divisible by 8 and 100 numbers.
5) Write a program to create a billing system at supermarket.


1) Write a program to find a sum of all the even numbers up to 50.
# Sum of even numbers up to 50
sum_even = 0
for i in range(2, 51, 2):
    sum_even += i
print("Sum of even numbers up to 50 =", sum_even)


OUTPUT:

Sum of even numbers up to 50 = 650

2) Write a program to write first 20 numbers and their squared numbers.
# First 20 numbers and their squares
for i in range(1, 21):
    print(i, "squared is", i*i)


OUTPUT (first few):

1 squared is 1
2 squared is 4
3 squared is 9
...
20 squared is 400

3) Write a program to find sum of first 10 odd numbers using while loop.
# Sum of first 10 odd numbers using while loop
count = 1
num = 1
sum_odd = 0
while count <= 10:
    sum_odd += num
    num += 2
    count += 1
print("Sum of first 10 odd numbers =", sum_odd)


OUTPUT:

Sum of first 10 odd numbers = 100

4) Write a program to check if a number is divisible by 8 within 100 numbers.
# Numbers divisible by 8 from 1 to 100
for i in range(1, 101):
    if i % 8 == 0:
        print(i, "is divisible by 8")


OUTPUT (few numbers):

8 is divisible by 8
16 is divisible by 8
24 is divisible by 8
...
96 is divisible by 8

5) Write a program to create a billing system at supermarket.
# Simple supermarket billing system
total = 0
while True:
    price = int(input("Enter item price (0 to finish): "))
    if price == 0:
        break
    total += price
print("Total Bill =", total)


Sample OUTPUT:

Enter item price (0 to finish): 100
Enter item price (0 to finish): 50
Enter item price (0 to finish): 200
Enter item price (0 to finish): 0
Total Bill = 350
'''