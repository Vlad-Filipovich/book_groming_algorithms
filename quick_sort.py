def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    greater = [i for i in arr if i > pivot]
    less = [i for i in arr if i < pivot]
    return quick_sort(less) + [pivot] * arr.count(pivot) + quick_sort(greater)


my_list = [1, 2, 7, 78, 41, 77, 78, 11, 2, 15, 1]
print(quick_sort(my_list))
