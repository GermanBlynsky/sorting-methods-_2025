import random

def quick_sort(arr, counter):
    if not arr:
        return arr, counter
    
    pivot = arr[-1]
    arr = arr[:-1]
    
    lArr, counter = filter_arr(arr, pivot, True, counter)
    rArr, counter = filter_arr(arr, pivot, False, counter)
    
    sorted_lArr, counter = quick_sort(lArr, counter)
    sorted_rArr, counter = quick_sort(rArr, counter)
    
    result = combine(sorted_lArr, pivot, sorted_rArr)
    return result, counter

def filter_arr(arr, pivot, left, counter):
    part = []
    if left:
        for i in arr:
            counter += 1
            if i <= pivot:
                part.append(i)
    else:
        for i in arr:
            counter += 1
            if i > pivot:
                part.append(i)
    return part, counter

def combine(lArr, pivot, rArr):
    result = []
    for i in lArr:
        result.append(i)
    result.append(pivot)
    for i in rArr:
        result.append(i)
    return result

# Создаем массив
arr = []
for i in range(0, 10000):
    arr.append(random.randint(1, 100000))

counter = 0
sorted_arr, counter = quick_sort(arr, counter)
print(f"Количесто операций: {counter}")
print(f"Проверка сортировки: {sorted_arr == sorted(arr)}")
