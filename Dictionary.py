'''
Dictionary allows user to write the data in the form of key and value
-> Dictionary are enclosed inside curly brackets {}
-> Keys and Value are represented by colon
-> Every key value pair is separated by comma {','}

CODE:
Employee_Data = {"name":"john","age":10,"gender":"male"}
print(Employee_Data["gender"])
'''
#Iteration in Dictionaries
'''
Students = {"name":"JOhn","Class":"6th","Roll_no":23}
#printing all the key names one by one
for x in Students:
    print(Students["Roll"])

#printing all the value names one by one
for x in Student:
    print(Student[x])
'''
#Dictionary Funtions
#get
'''
Get particular key ke value lekar deta hy
Students = {"name":"JOhn","Class":"6th","Roll_no":23}
x = Students.get("name")
print(x)
'''
#keys
'''
b.Student.keys()
print(b)
'''
#values
'''
b.Student.values()
print(b)
'''
#copy
'''
b.Student.copy()
print(b)
'''
#Nested Dictionary
'''
Employee = {
    1:{"Name":"John","age":23,"Gender":"male"}
    2:{"Name":"Lisa","age":25,"Gender":"Female"}
    3:{"Name":"Abrar","age":23,Gender":"Male"}
}
print(Empoyee[1]["Gender"])
'''
#PROBLEM SOLVE
'''
write a python program to sort a dictionary by value.
A = {"a":12,"b":23,"c":6,"d":91."e":45}
a = sorted(A.values())
print(a)
Write a python script to print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys.
a = {}
for i in range(1,16):
    a[i] = i**2
print(a)

Write a program to multiply all the items in a dictionary.
A = {1:12,2:23,3:6,4:91,5:45}
product = 1
for i in A :
     product *=A[i]
print(A)
Write a python program to sort a dictionary by key.
A = {1:12,2:23,3:6,4:91,5:45}
a = sorted(a.keys())
print(a)
'''