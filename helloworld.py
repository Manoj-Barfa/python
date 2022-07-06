A = 55
a = 22
b = 11
B = 33
c = A

if a > b:
 print("M1")
 if b < a:
  print("A2")
  if A < a:
   print("B3")

print("-------------------------------------")

# Next topic: Play with variables
x = 5
y = "Hello, World!"

# Next topic: let's add comments.
#This is a comment.
print("Hello, World!")

# Next topic: multiple comments.
#This is a comment
#written in
#more than just one line
print("Hello, World!")

# Next topic: one more way to add comments
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

# Next topic: Print variables
x = 5
y = "John"
print(x)
print(y)

# Next topic: variable overriding 
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Next topic: Casting
# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Next Topic: Get the Type
x = 5
y = "John"
print(type(x))
print(type(y))

# Next Topic: single or double quotes is same.
x = "John"
# is the same as
x = 'John'

# Next Topic: Variable names are case-sensitive.
a = 4
A = "apple"
#A will not overwrite a
print(a)
print(A)

# Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#(age, Age and AGE are three different variables)

#Illegal variable names:
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""