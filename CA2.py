# 1. Write a program in Python to perform the following operation:

# ● If a number is divisible by 3 it should print “Consultadd” as a string

# ● If a number is divisible by 5 it should print “c” as a string

# ● If a number is divisible by both 3 and 5 its should print “Consultadd

# # Python Training” as a string

count = 15
if count % 3 == 0:
    print("Consultadd")
if count % 5 == 0:
    print("c")
if (count % 3 == 0) and count % 5 == 0:
    print("Consultadd Python Training")


# 2. Write a program in Python to perform the following operator based task:
# ● Ask the user to choose the following option first:
# ○ If User Enter 1 - Addition
# ○ If User Enter 2 - Subtraction
# ○ If User Enter 3 - Division
# ○ If USer Enter 4 - Multiplication
# ○ If User Enter 5 - Average
# ● Ask the user to enter the 2 numbers in a variable for first and second for
# the first 4 options mentioned above.
# ● Ask the user to enter two more numbers as first1 and second2 for
# calculating the average as soon as the user chooses an option 5.
# ● In the end, if the answer of any operation is Negative print a statement
# saying “Zsa”
# ● NOTE: At a time users can perform one action at a time.
action = int(input("choose the following option first 1 - Addition, 2 - Subtraction, 3 - Division,  4 - Multiplication, 5 - Average"))
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number"))

if action == 1:
    answer = num1+num2
    print(f'Addition of two numbers is {answer}')
if action == 2:
    answer = num1-num2
    print(f'Subtraction of two numbers is {answer}')
if action == 3:
    answer = num1/num2
    print(f'Division of two numbers is {answer}')
if action == 4:
    answer = num1*num2
    print(f'Multiplication of two numbers is {answer}')
if action == 5:
    first1 = int(input('Enter a number'))
    second2 = int(input('Enter another number'))
    answer = (num1+num2+first1+second2)/4
    print(f'Average of all numbers is {answer}')
if answer < 0 :
    print("Zsa")

# 3. Write a program in Python to implement the given flowchart:


a = 10
b = 20
c = 30
avg = (a+b+c)/3
print("avg = ",avg)

if avg > a and avg > b and avg > c :
    print('Average is higher than a, b , c')
else:
    if avg > a and avg > b :
        print('Average is higher than a, b')
    elif avg > a and avg > c :
        print('Average is higher than a, c')
    elif avg > b and avg > c :
        print('Average is higher than b, c')
    else:
        if avg > a :
            print('Average is just higher than a')
        elif avg > b :
            print('Average is just higher than b')
        elif avg > c :
            print('Average is just higher than c')


# 4. Write a program in Python to break and continue if the following cases occurs:

# If user enters a negative number just break the loop and print “It’s Over”

# ● If user enters a positive number just continue in the loop and print “Good Going

while True:
    x = int(input("Enter a number"))
    if x < 0:
        print("It's over")
        break
    else:
        print("Good Going")
        continue


#5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.

numbers=[]
print("numbers which are divisible by 7 but are not a multiple of 5 are : ")
for i in range(2000,3200):
    if (i % 7 == 0) and (i % 5 != 0) :
        numbers.append(i)
print(numbers)

#3
#7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.

# Expected output: 0 1 2 4 5

# Note: Use ‘continue’ statement

for i in range(6):
    if i == 3 or i == 6:
        continue
    else:
        print(i)


# 8. Write a program that accepts a string as an input from user and calculate the number of digits and letters.

# Expected output: consul12

# Letters 6

# Digits 2
x = input("Enter a string: ")
digits=0
letters=0
for ch in x:
    if ch.isdigit():
        digits+=1
    else:
        letters+=1
print("Letters = ",letters)
print("Digits = ",digits)


# 9. Read the two parts of the question below:

# ● Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.
'''
lucky_number = 3

while True:
    guess= int(input("guess the Lucky number "))
    if guess == lucky_number:
        print('You guessed it right!')
        break
    else :
        continue
'''

# ● Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed the correct number)
number = 3

while True:
    guess= int(input("guess the Lucky number "))
    if guess == number:
        print('You guessed it right!')
        break
    else :
        answer = input('Do you want to continue guessing ? ')
        if answer != 'no':
            continue
        else:
            print('Better luck next time. Good-Bye!')
            break



# counter=1

# While counter <= 5:

# print(“Type in the”, counter, “number”

# counter=counter+1

# The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.
number = 3
counter = 1

while counter <=5:
    print('Type in the', counter, 'number')
    guess= int(input("guess the Lucky number "))
    if guess == number:
        counter+=1
        print('Good Guess!')
    elif counter ==5:
        print("Game Over!")
        break
    else :
        print('Try again!')
        counter+=1
        continue

# 11. In the previous question, insert “break” after the “Good guess!” print statement. “break” will terminate the while loop so that users do not have to continue guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”.
number = 3
counter = 1

while counter <=5:
    print('Type in the', counter, 'number')
    guess= int(input("guess the Lucky number "))
    if guess == number:
        print('Good Guess!')
        break
    elif counter ==5:
        print("Sorry but that was not very successful")
        print("Game Over!")
        break
    else :
        print('Try again!')
        counter+=1
        continue

# Guess output

x=123

for i in x:

    print(i)

    i = 0

    while i < 5:

        print(i)

        i += 1

        if i == 3:

            break

        else:

            print(“error”)

    count = 0

while True:

    print(count)

    count += 1

if count >= 5:

    break