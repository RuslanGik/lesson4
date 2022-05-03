# 4. Представлен список чисел. Определите элементы списка, не имеющие повторений. Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите в порядке их следования в исходном списке. Для выполнения задания обязательно используйте генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
from random import randint

my_list = [randint(-10, 10) for _ in range(20)]
uniq_list = [el for el in my_list if my_list.count(el) ==1]
print(f"Source list\n{my_list}\nNo repetition list\n{uniq_list}")

# Вар
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [src[i] for i in range(len(src)) if src[i] not in src[i + 1:] and src[i] not in src[:i]]

# Вар одна стр.
print(a := [randint(0, 9) for j in range(20)], '\n,', [i for i in a if a.count(i) == 1], sep='')

# Вариант со словарем оптимизации
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
d = {}
for j in src:
    if j in d:
        d[j] += 1
    else:
        d[j] = 1
result = [el for el in src if d[el] == 1]
print(result)

# Вариант collections.Counter
from collections import Counter

lst = [1, 2, 3, 4, 5, 6, 2, 5, 2]
counter = Counter(lst)
unique = list(counter)
single = [x for x, n in counter.items() if n == 1]
print(single)

# Вар с одним множеством
from random import randint

orig_list = [randint(1, 30) for i in range(20)]
print(orig_list)

repeated_nums = orig_list[:]
for i in set(repeated_nums):
    repeated_nums.remove(i)

print([el for el in orig_list if el not in repeated_nums])

# Вар с генератором
def filter_generator(arr):
    dict_ = {}
    for a in arr:
        if a in dict_:
            dict_[a] += 1
        else:
            dict_[a] = 1
    filtered = [k for k in dict_ if dict_[k] == 1]
    for f in filtered:
        yield f

def main():
    arr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    for value in filter_generator(arr):
        print(value)


if __name__ == '__main__':
    main()
    