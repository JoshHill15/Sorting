# TO-DO: Complete the selection_sort() function below
arr1 = [1, 1, 5, 2, 4]
arr2 = ['Bob', 'Slack', ['reddit', '89', 101, [
    'alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]
#  - 10


def selection_sort(arr):
    # loop through n-1 elements
    length = len(arr)
    for i in range(length-1):
        cur_index = i
        # smallest_value_index = cur_index
        # ^^^ unnecessary - just use arr[i] in swap
    # TO-DO: find next smallest element
    # (hint, can do in 3 loc)
        for j in range(i+1, length):
            if arr[cur_index] > arr[j]:
                cur_index = j
    # TO-DO: swap
        arr[cur_index], arr[i] = arr[i], arr[cur_index]
    return arr


# print("selection", selection_sort(arr1))
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(1, length - i):
            if (arr[j-1] > arr[j]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


# print("bubble", bubble_sort(arr1))
# STRETCH: implement the Count Sort function below

# arr1 = [1, 1, 5, 2, 4]

def count_sort(array):

    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
    return output


print("count", count_sort(arr1))


# def nested_print(arr):
#     for element in arr:
#         if type(element) == list:
#             nested_print(element)
#         else:
#             print(element)

# def nested_print(arr):
#     for element in arr:
#         # if element == list:
#         #     print('list')
#         while type(element) == list and element.length > 1:
#             for i in element:
#                 print(i)
#         else:
#             print(element)


# print("nest", nested_print(arr2))
