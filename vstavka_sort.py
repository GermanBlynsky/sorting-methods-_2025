import random

def insert_sort(arr):
    if not arr:
        raise ValueError("empty array")
    
    comparision = 0
    temp = []
    temp.append(arr[0])
    
    for i in range(1, len(arr)):
        inserted = False
        for j in range(len(temp)):
            comparision += 1
            if arr[i] < temp[j]:
                temp.insert(j, arr[i])
                inserted = True
                break
        if not inserted:
            temp.append(arr[i])
    
    print(f"Количество операций: {comparision}")
    return temp

# Создаем массив
arr = []
for i in range(0, 10000):
    arr.append(random.randint(1, 100000))

sorted_arr = insert_sort(arr)
print(f"Проверка сортировки: {sorted_arr == sorted(arr)}")

