# 1. Write a program using function USINto reverse a string.
# Sample_data: '1234abcd'
# Expected Output: “dcba4321”

sample_data='1234abcd'

def reverse_string(string):
    reverse=string[::-1]
    return reverse

reverse_string(sample_data)


# 2. Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.

# Expected Output:

# No. of Upper case characters : 3

# No. of Lower case Characters : 12

def count_lower_upper_case(string):
    u = 0
    l = 0
    for i in string:
        if i.isdigit() != True:
            if i.islower() == True:
                l = l + 1
            else:
                u = u + 1
    print('No. of Upper case characters : ', u)
    print('No. of lower case characters : ', l)


count_lower_upper_case(sample_data)

# 3.        Create a function that takes a list and returns a new list with unique elements of the first list.

sample_list =[1,1,2,2,3,3,4,4,5,6,6,7]

def unique_list(list1):
    unique_list= set(list1)
    return (list(unique_list))

unique_list(sample_list)

# 4.        Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.


seq = 'hi-why-are-you-here'

list_seq = sorted(seq.split('-'))

print(list_seq)

sorted_string = ''
for word in list_seq:
    if word != list_seq[-1]:
        sorted_string += word + '-'
    else:
        sorted_string += word

print(sorted_string)


# Sample input:

# Hello world

# Practice makes perfect

# Expected Output:

# HELLO WORLD

# PRACTICE MAKES PERFECT

lines = []

while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break

for l in lines:
    print(l)



# 6.          Define a function that can receive two integral numbers in string form and compute their sum and print it in console.

num1='45'
num2='55'

def sum_string_num(string_num1,string_num2):
    list_num=[int(string_num1),int(string_num2)]
    return sum(list_num)
print('The sum of two integral string number is :',sum_string_num(num1,num2))

# 8.        Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.
list1=[]
for i in range(1,21):
    list1.append(i**2)
print(tuple(list1))

# 0 and limit with a label to identify the even and odd numbers.

# Example: If the limit is 3 , it should print:

# 0 EVEN

# 1 ODD

# 2 EVEN

# 3 ODD

def shownumbers(limit):
    for i in range(0,limit):
        if i%2==0:
            print(i,'EVEN')
        else:
            print(i,'ODD')

shownumbers(3)

# 10. Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)

list2=[x for x in range(0,21)]

filtered_list=filter(lambda x: (x%2==0),[x for x in range(0,21)])
print(list2)
print(list(filtered_list))

# 11. Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]

# Hints: Use map() to generate a list.

#           Use filter() to filter elements of a list

#             Use lambda to define anonymous functions

list3=[1,2,3,4,5,6,7,8,9,10]
filtered_list1=filter(lambda x:x%2==0,list3)
mapped_list=map(lambda x:x**2,filtered_list1)
print(list(mapped_list))

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions

while True:
    try:
        result = 5/0
        print(result)
    except:
        print('You cannot divide 5 by 0')
        break
    else:
        print('This is the result:',result)
        break

# 13. Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce

# Goal : Turn [1,2,3,4,5,6,7] to 1234567
from functools import reduce

lists=[[1,2,3],[4,5],[6,7,8]]
joined_list=reduce(lambda x,y:x+y,lists)
print(joined_list)


#  14.

def foo():
    try:
        return 1
    finally:
        return 2

k = foo()

print(k)


# # (ii)
# def a():
#     try:
#         f(x, 4)
#     finally:
#         print('after f')
#     print('after f?')

# a()