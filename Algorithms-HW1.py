                                                #1)  Data Structures

#   -Create a list of integers and add 5 elements to it.
my_list = [1, 2, 3, 4, 5]
print(my_list)

#   -Create a dictionary with string keys and integer values, and add 5 key-value pairs to it.
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
print(my_dict)

#   -Create a queue of integers and add 5 elements to it.
from collections import deque
queue = deque([1, 2, 3, 4, 5])
print(queue)

#   -Create a stack of integers and add 5 elements to it.
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

print(stack)
#-----------------------------------------------------------------------------------------------------------------------

                                        #2)Operations on Data Structures

#   -Calculate and print the sum of all elements in the list.
my_list = [1, 2, 3, 4, 5]
total_sum = sum(my_list)

print(total_sum)


#   -Calculate and print the sum of all values in the dictionary.
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
total_sum = sum(my_dict.values())

print(total_sum)


#   -Remove 2 elements from the queue and print the remaining elements.
from collections import deque

queue = deque([1, 2, 3, 4, 5])
queue.popleft()
queue.pop()

print(queue)

#   -Remove 2 elements from the stack and print the remaining elements.

stack = [1, 2, 3, 4, 5]
stack.pop()
stack.pop()

print(stack)

#-----------------------------------------------------------------------------------------------------------------------
                                            #3)Additional Tasks

#   -Print all elements of the list.
my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print(element)

#   -From a three-digit number (e.g., 124), print the largest digit.

number = 950

number_str = str(number)
largest_digit = max(int(digit) for digit in number_str)

print(largest_digit)

#   -From a three-digit number (e.g., 124), print the smallest digit.

number = 185

number_str = str(number)
largest_digit = min(int(digit) for digit in number_str)

print(largest_digit)

#   -From an array, find all even values and print their sum.

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_values = [num for num in array if num % 2 == 0]
sum_of_even_values = sum(even_values)

print(sum_of_even_values)


#   -Calculate and print the average of all elements in the array.

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total_sum = sum(array)
num_elements = len(array)
average = total_sum / num_elements

print(average)
