import random

a = []
for i in range(0, 10000):
    a.append(random.randint(1, 100000))

operations = 0

for i in range(len(a)):
    for j in range(len(a) - i - 1):
        operations += 1
        operations += 1
        
        if a[j + 1] < a[j]:
            a[j], a[j + 1] = a[j + 1], a[j]
            operations += 3
            
    operations += 1
operations += 1

print(f"Всего операций: {operations}")