'''

Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
 In other words, find the lowest positive integer that does not exist in the array.
  The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

'''

lst_input = [-1, 3, 4, -1, 1, -11, 5, -38, 7, 3, -1, -2, -3, -4, -5]
lst_input = [2, 3, 7, 6, 8, -1, -10, 15]
lst_input = [2, 3, -7, 6, 8, 1, -10, 15]
lst_input = [1, 1, 0, -1, -2]


def solution_1(lst_input):
    neg_element_index = -1

    # shift negitive elements at first and +ve elements at last with n complexity
    for index, element in enumerate(lst_input):
        if element <= 0:
            lst_input[neg_element_index + 1], lst_input[index] = lst_input[index], lst_input[neg_element_index + 1]
            neg_element_index = neg_element_index + 1

    for i, element in enumerate(lst_input[neg_element_index + 1:]):
        try:
            lst_input[neg_element_index + element] = -lst_input[neg_element_index + element]
        except:
            pass
    if min(lst_input[neg_element_index + 1:]) > 0:
        print(max(lst_input[neg_element_index + 1:]) + 1, 'missing number')
        return
    for i, element in enumerate(lst_input[neg_element_index + 1:]):
        if element < 0:
            print(i, 'missing number')
            return


solution_1(lst_input)
