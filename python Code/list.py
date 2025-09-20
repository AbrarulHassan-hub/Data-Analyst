'''
Lists are the collection of order and mutable data
. List are written inside the sqaure brackets.
. The Value inside a list  is prepared by coma (,)
. Mutable MEANS once created they can not be changed
. Multiple datatype can be written inside a list

CODE:
fruits = ["Apple","mango","banana",12,14,45.10]
print(fruits)
print(type(fruits))

OUTPUT:
['Apple','mango','banana',12,14,45.10]
<Class 'LIST'>
'''

#ITERATION LOOP
'''
a =  ["Hulk","Thor","Ironman","Captain America"]
for i in a:
    print(i)
    
#Anohter Way
for i in range(len(a)):
    print(a[i])
'''

#List Functions-1
'''
a =  ["Hulk","Thor","Ironman","Captain America"]
#To find the length  of a list
print(len(a))
#To Count an occurence of a particular  Element
print(a.count("Thor"))
#To add to the list
a.append("SpiderMan") --- Insert in list at the end of list
#To Add to specific location 
a.insert(1,"Spjcoder") --- add element at the specific location
#to remove from a list
a.remove("Hulk")
#to remove from a certain location 
print(a.pop(1) )
'''

#List Functions-2
'''
a = ["Thor","Hulk","Ironman", "Captain America"]
#to create a copy of a list
CODE:
b =  a.copy()
print(b)
#to access an element
print(a.index("Ironman"))
#to entend the list
c = ["vision","spiderman"]
a.extend(c)
print(c)
#to reverse the list
a.reverse()
print(a)
#to sort the list
a.sort()
print(a)
#to clear all the data from the list
a.clear()
'''
#List Comprehensive
'''
List Comprehensive tab use karte hain, Jab Ek list ka data dusre list mei copy karna ho ga tab!
a = [3,23,44,12]
L3 = [i for i in a if i >10 ]
print(L3)
'''
#PROBLEM SOLVING LIST
'''
For List A: A = ["Ross", "Rachel", "Monica", "Joe"]
Write a program to swap first and forth element.
CODE:
A[0],A[3] = A[3],A[0]
print(A)
A = ["Joe", "Rachel", "Monica", "Ross"]
Write a program to add a new value at second position.
CODE:
A.insert(1,"Phoebe")
print(A)
Write a program to delete a value from 3rd position.
CODE
A.pop(3)
print(A)
For List B: B = [13, 7, 12, 10]
Write a program to multiply all the numbers in the list.
CODE
Mul = 1
for i in (B)
    Mul*=i
print(Mul)
Write a program to get the largest number from the list.\
CODE
B=[13,7,12,10]
B.sort()
print("largest element: ",B[-1])
Write a program to get the smallest number from the list.
CODE
print("Smallest element: ",B[0])
'''