# TO-DO: Complete the selection_sort() function below
# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
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


# print(selection_sort(arr1))
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    length = len(arr)
    for i in range(0, length):
        for j in range(1, length - i):
            if (arr[j-1] > arr[j]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


# print(bubble_sort(arr1))
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
