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