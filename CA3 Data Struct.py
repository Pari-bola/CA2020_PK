# TASK THREE: DATA STRUCTURES

# 1. Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.
list1 = [1,"Deepen",10+20j,1.2,2,"patel",1+4j,2.1,9,10]


# 2. Create a list of size 5 and execute the slicing structure.
list2 = [1,2,3,4,5]

slicing_list2 = list2[2:5]
print(slicing_list2)

reverse_list2=list2[::-1]
print(reverse_list2)
# 3.Write a program to get the sum and multiply of all the items in a given list.
sum_of_elements = sum(list2)
print("Sum of all the elements is : ", sum_of_elements)


def mul_of_elements(a):
    result = 1
    for i in a:
        result = result * i
    return result


product = mul_of_elements(list2)
print("Multiplication of all elements is : ", product)

# 4.   Find the largest and smallest number from a given list.
list3 = [5, 6, 8, 9, 10, 11, 12, 3]


def find_smallest_num(List):
    smallest = List[0]
    for i in List:
        if i < smallest:
            smallest = i
    return smallest


def find_largest_num(List):
    largest = List[0]
    for i in List:
        if i > largest:
            largest = i
            return largest

smallest_num = find_smallest_num(list3)
print("Smallest number in the list is :", smallest_num)

largest_num = find_largest_num(list3)
print("Largest number in the list is :", largest_num)

# 5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
new_list = []
for i in list4:
    if i % 2 != 0:
        new_list.append(i)
print(new_list)

# 6. Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

first_list = []
last_list = []
for i in range(1, 31):
    if i <= 5:
        first_list.append(i ** 2)
    if i >= 26:
        last_list.append(i ** 2)

final_list = first_list + last_list
print("list of first and last 5 elements where the values are square of numbers between 1 and 30 :", final_list)

# 7. Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]

list5 = [1, 3, 5, 7, 9, 10]
list6 = [2, 4, 6, 8]

list5[5] = list6
print(list5)

# 8. Create a new dictionary by concatenating the following two dictionaries:
# a={1:10,2:20}
# b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40}

a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
a.update(b)
print("New dictionary by concatenating the following two dictionaries:", a)

# 9 Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
# Sample data (n=5)
# Expected Output: {1:1,2:4,3:9,4:16,5:25}

dict1 = {}
n = 6

for i in range(1, n):
    dict1[i] = i * i
print("Dictionary that contains a number (between 1 and n) in the form(x,x*x)", dict1)

# 10. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# The output should be:
# [‘34’,’67’,’55’,’33’,’12’,’98’]
# (‘34’,’67’,’55’,’33’,’12’,’98’)

user_input = input("Enter numbers seperated with comma's")
list7 = user_input.split(",")
print(list7)

tuple1 = tuple(user_input.split(","))
print(tuple1)