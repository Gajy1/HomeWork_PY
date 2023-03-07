#Первая задача:
#Задаем длину списка наполненного рандомными числами от 1 до 100.
#Вводим искомое число X
#Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
#которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
import random
c = 0
x = 0
list = [random.randint(1, 100) for _ in range(20)]
X = int(input('Введите число: '))

for i in range(20):
    if list[i] == X:
        c += 1

n = abs(X - list[0])
for i in range(20):
    if list.count(X) == 0 and  n > abs(X - list[i]):
        n = abs(X - list[i])
        x = list[i]


print(list)
if c != 0:
    print(c)
else:
    print(f'Число {X} не сушествует, {x}')    