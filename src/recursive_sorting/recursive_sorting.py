# TO-DO: complete the helpe function below to merge 2 sorted arrays
arr1 = [1, 2, 8, 5, 78]
arr2 = [3, 5, 9, 34]


def merge(arrA, arrB):
    merged_arr = [None] * (len(arrA) + len(arrB))
    # TO-DO
    # Initalize pointers
    first, second, third = 0, 0, 0
    # while first is smaller than first array and second is smaller than second array
    while first < len(arrA) and second < len(arrB):
        # if element in first array is smaller than element in second array
        if arrA[first] < arrB[second]:
            merged_arr[third] = arrA[first]
            first += 1
            third += 1
        # if element in second array is smaller than element in first array
        else:
            merged_arr[third] = arrB[second]
            third += 1
            second += 1
    # if second array is larger than first, add the remaining values in second array to merged_arr
    if first >= len(arrA):
        while second < len(arrB):
            merged_arr[third] = arrB[second]
            third += 1
            second += 1
    # if first array is larger than second, add the remaining values in first array to merged_arr
    elif second >= len(arrB):
        while first < len(arrA):
            merged_arr[third] = arrA[first]
            third += 1
            first += 1
    return merged_arr


# print("merge", merge(arr1, arr2))

# TO-DO: implement the Merge Sort function below USING RECURSION


# arr1 = [1, 2, 8, 5,78]
def merge_sort(arr):
    # TO-DO
    # if length of array is 1 or 0, return it
    if len(arr) <= 1:
        return arr
    # keep slicing array in the middle, until one element per array done via recursion
    middle = len(arr) // 2
    rhs = arr[middle:]
    lhs = arr[:middle]
    # build sorted array out of arrays with length of one with merge function
    return merge(merge_sort(lhs), merge_sort(rhs))


# merge(lhs, rhs)
print("merge_sort", merge_sort(arr1))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


def quicksort(arr):
    # Base case: arr len 0 or 1 is sorted
    if len(arr) <= 1:
        return arr
    # Pick a pivot
    pivot = arr[0]
    # Separate all vals smaller and larger than pivot
    smaller = []
    larger = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            larger.append(arr[i])
    # Sort smaller and larger
    # Concatenate smaller + pivot + larger
    return quicksort(smaller) + [pivot] + quicksort(larger)
