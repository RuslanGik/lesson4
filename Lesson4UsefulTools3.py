# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
# Подсказка: используйте функцию range() и генератор.
print([el for el in range(20, 241) if el % 21 == 0])

# Вариант
n_21 = [i for i in range(21, 241, 21)]
n_20 = [i for i in range(20, 241, 20)]
print(sorted(n_21 + n_20))


# Вариант генератором
def main():
    for i in range(20, 241):
        if i % 20 == 0 or i % 21 == 0: yield i

if __name__ == '__main__':

    for m in main():
        print(m)
