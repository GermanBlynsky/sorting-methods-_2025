#htpe
import random

operations = 0

def quicksort_simple(arr, low, high):
    global operations
    if low < high:
        operations += 1
        
        pi = partition_simple(arr, low, high)
        
        quicksort_simple(arr, low, pi - 1)
        quicksort_simple(arr, pi + 1, high)

def partition_simple(arr, low, high):
    global operations
    pivot = arr[high]
    operations += 1  
    
    i = low - 1
    operations += 1  
    
    for j in range(low, high):
        operations += 1 
        
        operations += 1  
        if arr[j] <= pivot:
            i += 1
            operations += 1 
            arr[i], arr[j] = arr[j], arr[i]
            operations += 3
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    operations += 3
    
    return i + 1

a = []
for i in range(0, 10000):
    a.append(random.randint(1, 100000))

a_copy = a.copy()

operations = 0

quicksort_simple(a, 0, len(a) - 1)

print(f"Всего операций: {operations}")
print(f"Проверка правильности сортировки (сравнением со встроенной сортировкой) : {a == sorted(a_copy)}")