'''
Pattern 1
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5

CODE:
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

Pattern 2
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

CODE:
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

Pattern 3
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5

CODE:
for i in range(1, 6):
    for j in range(6-i):
        print(i, end=" ")
    print()

Pattern 4
*
**
***
****
*****


CODE:
for i in range(1, 6):
    print("*" * i)

Pattern 5
* * * * * 
* * * * 
* * * 
* * 
*

CODE:
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

Pattern 6 (Pyramid)
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

CODE:
rows = 5
for i in range(rows):
    # spaces
    for j in range(rows - i - 1):
        print(" ", end=" ")
    # stars
    for k in range(2*i + 1):
        print("*", end=" ")
    print()

'''