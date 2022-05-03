# 6. Реализовать два небольших скрипта:
# a) итератор, генерирующий целые числа, начиная с указанного;
# b) итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения. # Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие,
# при котором повторение элементов списка прекратится.
from itertools import count, cycle

print('Программа генерирует целые числа, начиная с указанного. Для выхода из программы - "q"')
for i in count(int(input('Введите стартовое число: '))):
    print (i, end='')
    quit = input()
    if quit == 'q':
        break

# Вар без break
from itertools import count, cycle

my_count = count(7)
my_cycle = cycle("abc")

for _ in range(5):
    print("(my_count, my_cycle) = ({}, {})".format(next(my_count), next(my_cycle)))

# Вар
from itertools import count, cycle

a = 10
my_list = [b for b in range(8)]
counter = count()
cycler = cycle(my_list)

print([next(counter) for b in range(a)])
print([next(cycler) for b in range(a)])
