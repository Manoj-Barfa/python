# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"


# One Value to Multiple Variables
x = y = z = "Orange"

# extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

# Output Variables
print(x)
print(x, y, z) # add space between values
print(x + y + z) # no space, 