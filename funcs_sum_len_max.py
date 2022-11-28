def summa(arr):
    if arr == []:
        return 0
    return arr[0] + summa(arr[1:])


def lenght(arr):
    if arr == []:
        return 0
    return 1 + lenght(arr[1:])

def maximum(arr):
    if lenght(arr) == 1:
        return arr[0]
    if lenght(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_maximum = maximum(arr[1:])
    return arr [0] if arr[0] > sub_maximum else sub_maximum


my_list = [1]
print(f'Summa = {summa(my_list)}')
print(f'Lenght = {lenght(my_list)}')
print(f'Max elem = {maximum(my_list)}')
