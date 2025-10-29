#количество операций этим методом ~100.000.000
import random

a = []
for i in range(0, 10000):
    a.append(random.randint(1, 100000))

operations = 0
for i in range(1, len(a)):
    start_value = a[i]
    operations += 1
    j = i - 1
    while j >= 0 and a[j] > start_value:
        operations += 3 
        a[j + 1] = a[j]
        j -= 1
        operations += 1
    if j >= 0:
        operations += 2 
    else:
        operations += 1
    a[j + 1] = start_value
    operations += 1

print(f"Всего операций: {operations}")

print(f"Проверка сортировки: {a == sorted(a)}")
