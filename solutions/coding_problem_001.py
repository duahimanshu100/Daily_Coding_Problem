'''

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

'''

input = [10, 15, 3, 7]
k = 18


def solution_1(lst_input, k):
    # n*n complexity solution
    for index, item in enumerate(lst_input):
        for inner_item in lst_input[index:]:
            if item + inner_item == k:
                print('found the pair', item, inner_item)
                break


def solution_2(lst_input, k):
    # n complexity solution with extra space
    dict = {}
    for index, item in enumerate(lst_input):
        if index == 0:
            dict[item] = index
            continue
        if (k - item) in dict:
            print('Found the pair', item, k - item)
            break
        dict[item] = index


solution_2(input, k)
