# operator ---> symbol or keyword that performs an operation on one or more operands
# operand ---> value or variable acted upon by an operator to produce a result.

#1. Arithmetic operator: 
# (+) addition --> adds two operands
# num_1 = 10
# num_2 = 5
# result = num_1 + num_2
# print(result)

# num_1 = 10
# num_2 = 5
# result = num_2 + num_1
# print(result)

# num_1 = "vikasdev"
# num_2 = "gandham"
# result = num_1 + num_2
# print(result)

#(-) subtractions --> subtracts the right operand from the left operand.
# num_1 = 10
# num_2 = 5
# result = num_1 - num_2
# print(result)
# print(type(result))

# num_1 = 10
# num_2 = 5
# result = num_2 - num_1
# print(result)

#(*) Multiplication --> multiplication two operands
# num_1 = 10
# num_2 = 5
# result = num_1 * num_2
# print(result)
# print(type(result))

#(**) Exponentiation --> Raises the base (left operand) to the power of the exponent (right operand).
# num_1 = 4
# num_2 = 2
# result = num_1 ** num_2
# print(result)

# num_1 = 5
# num_2 = 2
# result = num_1 ** num_2
# print(result)

# num_1 = 5
# num_2 = 2
# result = num_2 ** num_1
# print(result)

# a = 10
# b = 2
# result = (a+b)**2
# print(result)


#(/) Division --> Divides the left operand by the right operand.
# num_1 = 10
# num_2 = 3
# result = num_1 / num_2
# print(result)

#(//) floor division --> Returns the quotent of the division, discarding the fractional part.
# num_1 = 10
# num_2 = 3
# result = num_1 // num_2
# print(result)

# (%) Modulus --> Returns the remainder of the division of the left operand by the right operand.
# num_1 = 9
# num_2 =4
# result = num_1 % num_2
# print(result)

# a = 10
# b = 3

# addition = a + b
# subctraction = a - b
# mulitplication = a * b
# division = a / b
# remainder = a % b
# floor_division = a // b
# exponentiation = a ** b

# print(addition, subctraction, mulitplication, division, remainder, floor_division, exponentiation)


#2. Assignment operator:
# rice = 1000
# rice += 10 #equal --> rice = rice + 10
# print(rice)

# rice = 1000
# rice -= 10 #substraction queal rice = rice - 10
# print(rice)

# task
# *=
# /=
# %=

# task
# rice = 1000
# rice *= 10 #multiplication equal rice = rice * 10
# print(rice)

# rice = 1000
# rice /= 10 #division equal rice = rice / 10
# print(rice)

# rice = 1000
# rice %= 10 #modulus equal rice = rice % 10
# print(rice)


#3. Comparison operator:
# (==) equal to --> checks if the values of two operands are equal, returns True if they are equal, otherwise returns False.
# product_cost = 1000
# product_cost2 = 1000
# product_cost3 = 900
# print(product_cost == product_cost2)
# print(product_cost < product_cost2)
# print(product_cost <= product_cost2)
# print(product_cost > product_cost2)
# print(product_cost >= product_cost2)
# print(product_cost != product_cost2)
# print(product_cost != product_cost3)

#4. Logical operator:
# and , or, not operators are used to combine conditional statements.
# user_name = "vikasdev"
# password = 12345
# otp = 123456
# print(user_name == "vikasdev" and password == 12345 and otp == 123456) #True and True --> True
# print(user_name == "vikasdev" or password == 123) #True or False --> True
# print(not user_name == "vikasev") #True and not False --> True

#5. identity operator:
# is and is not its used to compare the memory location of two objects, returns True if both operands refer to the same object in memory, otherwise returns False.
# sample = [1,2,3,4,5]
# sample1 = [1,2,3,4,5]
# print(sample is sample1) #false because they are different objects in memory

# num_1 = 245
# num_2 = 245
# print(num_1 is num_2) #true because small integers are cached by Python and refer to the same memory location

#6.Memebership operator:
# in and not in operators are used to test whether a value or variable is present in a sequence (like a list, tuple, or string).
# fruits = ["appple", "banana", "mango","orange","grapes"]
# print("banana" in fruits) #True
# print("kiwi" in fruits) #False
# print("kiwi" not in fruits) #True
# print("banana" not in fruits) #False

# sample = "vikasdev gandham"
# print("gandham" in sample) #True

# fruits = {"appple", "banana", "mango","orange","grapes"}
# print("banana" in fruits) #True
# print("kiwi" in fruits) #False

#finding the discount of a product
# product_cost = 10000
# discount = 10
# result = product_cost * (discount / 100)
# product_cost -= result 
# print(product_cost)

#7. output formatting: (f-string)

# product_cost = 10000
# discount = 10
# result = product_cost * (discount / 100)
# product_cost -= result
# print(f"discount given {discount}% and final discount {result} and total cost after discount {product_cost}/-")