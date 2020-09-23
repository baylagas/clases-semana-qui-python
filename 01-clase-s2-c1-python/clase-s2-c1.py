# -- clase 01 -------------------------------------
# casting
#   int()
#   float()
#   str()
# integer casting:
x = int(1)  # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3
print(x, y, z)
# float casting:
x = float(1)  # x will be 1.0
y = float(2.8)  # y will be 2.8
z = float("3")  # z will be 3.0
w = float("4.2")  # w will be 4.2
print(x, y, z, w)
# string casting:
x = str("s1")  # x will be 's1'
y = str(2)  # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x, y, z)


# -- clase 02 -------------------------------------
# string literals
print("Hello")
# print('Hello') tambien es valido
# Assign String to a Variable
a = "Hello"
print(a)
# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Strings are Arrays
a = "Hello, World!"
print(a[1])
# Slicing
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
# Negative Indexing
# Get the characters from position 5 to position 1 (not included), starting the count from the end of the string:
b = "Hello, World!"
print(b[-5:-1])
# String Length
a = "Hello, World!"
print(len(a))
# String Methods
#   The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"
#   The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
#   The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
#   The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
#   The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']
# Check String
# To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
# Check if the phrase "ain" is NOT present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)
# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)
# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)
# String Format
# age = 36
# txt = "My name is John, I am " + age  # this gives an error
# print(txt)

# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
# Escape Character
# The escape character allows you to use double quotes when you normally would not be allowed:
txt = 'We are the so-called "Vikings" from the north.'
print(txt)
# String Methods
# Python has a set of built-in methods that you can use on strings.


# -- clase 03 -------------------------------------
# operators
# Arithmetic operators
x = 5
y = 2
print(x + y)  # +	Addition 7
print(x - y)  # -	Subtraction 3
print(x * y)  # *	Multiplication 10
print(x / y)  # /	Division 2.5
print(x % y)  # %	Modulus 1
print(x ** y)  # **	Exponentiation 25
print(x // y)  # //	Floor division 2

# Assignment operators
x = 5
print(x)
x = 5
x += 3  # equal to x = x + 3
print(x)
x = 5
x -= 3  # equal to x = x - 3
print(x)
x = 5
x *= 3  # equal to x = x * 3
print(x)
x = 5
x /= 3  # equal to x = x / 3
print(x)
x = 5
x %= 3  # equal to x = x % 3
print(x)
x = 5
x //= 3  # equal to x = x // 3
print(x)
x = 5
x **= 3  # equal to x = x ** 3
print(x)
x = 5
x &= 3  # equal to x = x & 3
print(x)
x = 5
x |= 3  # equal to x = x | 3
print(x)
x = 5
x ^= 3  # equal to x = x ^ 3
print(x)
x = 5
x >>= 3  # equal to x = x >> 3
print(x)
x = 5
x <<= 3  # equal to x = x << 3
print(x)

# Comparison operators
x = 5
y = 2
print("Comparison operators:")
print(x == y)  # ==	Equal
print(x != y)  # !=	Not equal
print(x > y)  # >	Greater than
print(x < y)  # <	Less than
print(x >= y)  # >=	Greater than or equal to
print(x <= y)  # <=	Less than or equal to

# Logical operators
print("Logical operators:")
print(x < 5 and x < 10)  # and
print(x < 5 or x < 4)  # or
print(not (x < 5 and x < 10))  # not

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
print("Identity operators:")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)  # returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print(x is not z)  # returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

# Membership operators are used to test if a sequence is presented in an object:
print("Membership operators:")
x = "banana split is delicious"
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list
x = "banana split is delicious"
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list


# -- clase 04 -------------------------------------
# Boolean Values
# You can evaluate any expression in Python, and get one of two answers, True or False.
print("Boolean Values:")
print(10 > 9)
print(10 == 9)
print(10 < 9)
# Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))  # string
print(bool(15))  # number

# Evaluate two variables:
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
x = 0
y = []
print(bool(x))
print(bool(y))
