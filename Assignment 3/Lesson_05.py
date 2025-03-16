# Lwesson:05 Control Flow and Decision Making in Python

# Comparison Operators

x: int = 15
y: int = 30

print("x == y = ", x == y)  
print("x != y = ", x != y) 
print("x > y  = ", x > y)   
print("x < y  = ", x < y)   
print("x >= y = ", x >= y) 
print("x <= y = ", x <= y)  

# Logical Operator

age: int = 18
is_student: bool = True

# Check if age is greater than equal to 18 AND is_student is True
if age >= 18 and is_student:
    print("You are eligible for a student discount.")

# Check if age is less than 12 OR greater than 60
if age < 12 or age > 60:
    print("You qualify for a special discount.")

# Check if the person is NOT a student
if not is_student:
    print("You are not a student.")

#The if Statement

age: int = 18

if age > 15:
    print("You can enroll in this course.")    

#The else Statement


age: int = 12

if age > 15:
    print("You can enroll in this course.")  
else:
    print("You can not enroll in this course")    

#The elif Statement    

num: int = 0

if num > 0: 
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Nested if Statements

num: int = 12
#num: int = -10

if num > 0: # check wather the number is positive or negative

    if num % 2 == 0: # Modulus operator, remainder 0 = even_number,
        print("The number is positive and even.")
    else: # remainder 1 = odd_number,
        print("The number is positive and odd.")

else:
    print("The number is negative.")



