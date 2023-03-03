#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть
import random
count = 0
count2 = 0

n = int(input('Введите число: '))
i = 0
while i < n:
    x = random.randint(0, 1)
    print(x, end = " ")
    if x == 0:
        count += 1
    if x == 1:
        count2 += 1    
    i += 1

print(" ")    

if count < count2:
    print(count)
if count2 < count:
    print(count2)    
if count2 == count:
    print(count)


              