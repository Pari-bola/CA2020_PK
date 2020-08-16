# ASSIGNMENTS
# TASK ONE: NUMBERS AND VARIABLES
# 1.	Create three variables in a single a line and assign different values to them and make sure their data types are different. Like one is int, another one is float and the last one is a string

var1 = 123
var2 = 34

var3 = 'Pari'

print (var3)

#2. 	Create a variable of value type complex and swap it with another variable whose value is an integer.
var4 = 3.14j
var2 = var4
var4 = var1
var1 = var2

print (var4)
print (var1)

#3. 	Swap two numbers using the third variable as the result name and do the same task without using any third variable.

a=1
b=2
result = a
a = b
b = result

print('a = ',a ,'b =', b)

#4. 	Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.
#python 2.x
# name = raw_input('enter your name ')
# print 'name'

#python 3.x
name = input("Enter Employee Name ")
salary = input("Enter salary ")
company = input("Enter Company name ")

print("\n")
print("Printing Employee Details")
print("Name", "Salary", "Company")
print(name, salary, company)

#5. 	Write a program to complete the task given below:
# Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
z = 0
for i in range (2):
	num = int(input('Enter any number between  1-10 : '))
	z = z + num
	i+=1
print(f'sum of two number is z = {z}')

# Use z for adding 50 into it and print the final result by using variable result.
z+=50
print(f'Value of Z after adding 50 is {z}')

# 6. 	Write a program to check the data type of the entered values. HINT: Printed output should say -  The input value data type is: int/float/string/etc
user_input = input('enter value to check the data type')
print(f'The input data type is:{type(user_input)}')


# 7. 	Create Variable using CamelCase, LadderCase and UPPERCASE. (Refer:   https://capitalizemytitle.com/camel-case/) - Variable Conventions to write
Var = 10
var = 12
VAR = 14

print (Var, var, VAR)