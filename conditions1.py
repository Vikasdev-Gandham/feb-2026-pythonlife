#1. if statement
#syntax
# if condition:
#     statement . 1
#     statement . 2
#     statement . n


# age = 35
# if age >= 18: #True
#     print(f"you are eligible to vote age is {age}")
#     num_1 = 10
#     num_2 = 5
#     result = num_1 - num_2
#     print(result)

# if condition moves to next line if condition is true otherwise it will skip the block of code and move to next line of code

# age = 17
# if age >= 18: #False
#     print(f"you are eligible to vote age is {age}")
#     num_1 = 10
#     num_2 = 5
#     result = num_1 - num_2
#     print(result)

# user_name = "vivek"
# if user_name == "vivek": #True
#     print(f"login success")
#     print(f"welcome {user_name}")

#block of code will execute only when condition is true otherwise it will skip the block of code and move to next line of code

# user_name = input("enter username: ")
# if user_name == "vivek": #true
#     print(f"login success")
#     print(f"welcome {user_name}")
    
# print("sample statement")

# number = 6
# if number > 5: #True
#     #calculate square
#     print(number * number)
# print('Next lines of code')

# 4.else statement
#syntax
# if conditin:
#     # code block execute if condition is true
# else:
#     # code block execute if condition is false

# age = 35
# if age > 18: #true
#     print(f"now you are eligible to vote age is {age}")
# else:
#     print(f"not eligible to vote age is {age}")

# age = 17
# if age > 18 :#false
#     print(f'now you are eligible to vote age is {age}')
# else:
#     print(f"not eligible to vote age is {age}")

# age = int(input("enter your age: "))
# if age > 18: 
#     print(f"now you are eligible to vote age is {age}")
# else:
#     print(f"now eligible to vote age is {age}")

# user_name = input("enter username: ")
# password = input("enter password: ")
# if user_name == "vikas" and password == "vikas1234" :
#     print(f"Login success")
#     print(f"welcom {user_name}.....")
# else:
#     print(f"invalid Login credentials...")


#syntax 
#GRADING SYSTEM
# marks = int(input("enter your marks: "))
# if marks >= 90 and marks <= 100:
#     print(f"you got A grade obtained marks {marks}")
# elif marks>=80 and marks<=89:
#     print(f"you got B grade obtained marks {marks}")
# elif marks>=70 and marks<=79:
#     print(f"you got C grade obtained marks {marks}")
# elif marks>=60 and marks<=69:
#     print(f"you got D grade obtained marks {marks}")
# elif marks>=35 and marks<=59:
#     print(f"Pass you obtained marks {marks}")
# elif marks >= 0 and marks<=34:
#     print(f"failed.... your marks {marks}")
# else:
#     print(f"invalid marks {marks}...")

# or we can write like this
# marks = int(input("enter your marks: "))
# if marks > 100 or marks < 0:
#     print(f"invalid inputs, marks should be between 0 to 100")
# elif marks >= 90:
#     print(f"you got A grade obtained marks {marks}")
# elif marks >= 80:
#     print(f"you got B grade obtained marks {marks}")
# elif marks >= 70:
#     print(f"you got C grade obtained marks {marks}")
# elif marks >= 35:
#     print(f"Pass you obtained marks {marks}")
# else :
#     print(f"failed.... your marks {marks}")


# Syntax:
# if condition1:
# # code block for condition1
# if condition2:
# # code block for condition2
# else:
# # code block for condition2 being false
# else:
# # code block for condition1 being false

user_name = input("enter username: ")
password = input("enter password: ")
if user_name == "vikas":
    if password == "12345":
        print(f"Login success")
        print(f"welcome {user_name}.....")
    else:
        print(f"invalid password...")
else:
    print(f"invalid username...")