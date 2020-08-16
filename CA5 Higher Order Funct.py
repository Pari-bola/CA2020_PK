# TASK FIVE: HIGHER ORDER FUNCTIONS, GENERATORS, LIST COMPREHENSION

# 1. Write a program to Python find the values which is not divisible 3
# but is should be a multiple of 7. Make sure to use only higher order function.

print(list(filter(lambda i:i%3!=0 and i%7==0,[j for j in range(30)])))

# 2. Write a program in Python to  multiple the element of list by itself
# using a traditional function and pass the function to map to complete the operation.

list1=[1,2,3,4,5]
def sq_elements(a):
    res=a*a
    return res
print(list(map(sq_elements,list1)))

# 3. Write a program to Python find out the character in a string which is uppercase using list comprehension.

string1='Hello World'
list1=[i for i in string1 if i.isupper()==True]
print(list1)

# 4. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects.
# The dictionary should maps the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also

student = ['Pari', 'Fluffy', 'Droid']

capital = ['Python', 'AWS', 'Operating System']

dict1 = {i: j for i, j in zip(student, capital)}
print(dict1)

# 5.  Learn More about Yield, next and Generators

# 6. Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”

str ='Consultadd Training'
print(str[::-1])


def deco(func):
    def inner():
        print('***Decorator starts here***')
        func()
        print('--- Decorator ends here ---')

    return inner


@deco
def func():
    print('|  This is real function   |')


func()

