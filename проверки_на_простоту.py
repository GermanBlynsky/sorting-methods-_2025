import random
import math

def ferma(n, iterations=5):
    if n <= 0: 
        raise ValueError("Число должно быть положительным")
    if n >= 0 and n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(iterations):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    
    return True

def test_soloveia_shtrassena(number, k=10):
    if number <= 0: 
        raise ValueError("Число должно быть положительным")
    if number == 1 or number == 3:
        return False
    
    if number % 2 == 0:
        return False
    
    for i in range(k):
        a = random.randint(2, number - 2)
        
        if math.gcd(a, number) > 1:
            return False
        
        mod_result = pow(a, (number - 1) // 2, number)
        if mod_result != number - 1 and mod_result != 1:
            return False
    
    return True

def test_millera_rabina(number, k=5):
    if number <= 0: 
        raise ValueError("Число должно быть положительным")
    if number >= 0 and number < 2:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False
    
    s = 0
    d = number - 1
    
    while d % 2 == 0:
        d //= 2
        s += 1
    
    for _ in range(k):
        a = random.randint(2, number - 2)
        
        x = pow(a, d, number)
        
        if x == 1 or x == number - 1:
            continue
        
        for _ in range(s - 1):
            x = pow(x, 2, number)
            
            if x == 1:
                return False
            
            if x == number - 1:
                break
        else:
            return False
    
    return True

print("Выберите, какой алгоритм проверки на простоту числа будете использовать")
print("Введите 1 если хотите использовать алгоритм Ферма")
print("Введите 2 если хотите использовать алгоритм Соловея-Штрассена")
print("Введите 3 если хотите использовать тест Миллера-Рабина")
input_value = input()
if input_value == '1':
    try:
        print("Введите число, чтобы узнать простое оно или составное с помощью алгоритма Ферма")
        n = int(input())
        if ferma(n):
            print(f"Число {n} - простое число")
        else:
            print(f"Число {n} - составное число")
    except ValueError:
        print("Ошибка! Введите целое число")
    except Exception as e:
        print(f"Ошибка: {e}")

elif input_value == '2':
    try:
        print("Введите число, чтобы узнать простое оно или составное с помощью алгоритма Соловея-Штрассена")
        n = int(input())
        if test_soloveia_shtrassena(n):
            print(f"Число {n} - простое число")
        else:
            print(f"Число {n} - составное число")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")

elif input_value == '3':
    try:
        print("Введите число, чтобы узнать простое оно или составное с помощью алгоритма Миллера-Рабина")
        n = int(input())
        if test_millera_rabina(n):
            print(f"Число {n} - простое число")
        else:
            print(f"Число {n} - составное число")
    except ValueError:
        print("Ошибка! Введите целое число")
    except Exception as e:
        print(f"Ошибка: {e}")

else:
    print("Неверный выбор. Пожалуйста, введите 1, 2 или 3")