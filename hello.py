
# Question 1: Hello, User!
# name = input ("Enter your name: ")
# print ("Hello, " + name + "!")

# Question 2: Simple Arithmetic Operations
a = 10
b = 20
sum = a + b 
print ("The sum of", a, "and", b, "is", sum)

# Question 3: Type Conversion and Operations
aa = 15
bb = '25'
print (aa + int(bb))

# Question 4: Division and Power Operations
a1 = 15 
b1 = 4 
print ("The division of this programe when the operator is single : - ", a1 / b1)
print ("The division of this programe is : - ", a1 // b1)
print("The power :" , 2 ** 3)

# Question 5: User Input and Calculations
number = input ("Enter your number: ")
print("Square of the number is: ", int(number) ** 2)
print("Cube of the number is: ", int(number) ** 3)

# Question 6: Time Conversion
number = input ("Enter your time into seconds: ")
print("Time in minutes and hours is: ", int(number) / 60 , "Minutes and ", int(number) / 3600 , "Hours")

# Question 7: Average Speed Calculation
km = 120
time = 3 
average_speed = km / time
print("The average speed is: ", average_speed , "km/h")


# Question 8: Even or Odd Check
firstNo = input("Enter first number: ")
secondNo = input("Enter second number: ")
isNoisMultipleOfSecondNo = int(firstNo) % int(secondNo) == 0
print("Is first number multiple of second number? ", isNoisMultipleOfSecondNo)

# Question 9: Simple Interest Calculation
p = input("Enter the principal amount: ")
r = input("Enter the rate of interest: ")
t = input("Enter the time in years: ")
simple_interest = (int(p) * float(r) * int(t)) / 100
print("The simple interest is: ", simple_interest)

# Question 10: Rounded quotient
num1 = input("Enter first number: ")    
num2 = input("Enter second number: ")
quotient = int(num1) / int(num2)
print("The rounded quotient is: ", quotient.__round__())