# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([j for i, j in enumerate(my_list) if i != 0 and j > my_list[i - 1]])

# Вариант
my_list = [15, 16, 2, 3, 1, 7, 5, 4, 10]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num]]
print(more_then)

# Вариант
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [j for i, j in zip(my_list, my_list[1:]) if j > i]
print(new_list)
