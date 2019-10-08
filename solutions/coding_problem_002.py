'''

This problem was asked by Uber.

Given an array of integers, return a new array such that
each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
 If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

'''
from functools import reduce

input = [1, 2, 3, 4, 5]


# i = 18


def solution_1(lst_input):
    # n complexity solution with divide
    multiplied_result = reduce(lambda x, y: x * y, lst_input)
    print([multiplied_result // element for element in lst_input])


solution_1(input)


def solution_2(lst_input):
    # n*n complexity solution without divide
    multiplied_result = reduce(lambda x, y: x * y, lst_input)
    result = []
    for element in lst_input:
        temp_multiplied_result = multiplied_result
        count = 0
        while (True):
            # replace divide with multiple subtract
            temp_multiplied_result = temp_multiplied_result - element
            count = count + 1
            if temp_multiplied_result <= 0:
                break

        result.append(count)
    print(result)


solution_2(input)
