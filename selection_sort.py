def find_index_smallest_elem(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr [i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_index_smallest_elem(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

my_list = [8,9,7,5,3,7,4,6,6]
print(selection_sort(my_list))
