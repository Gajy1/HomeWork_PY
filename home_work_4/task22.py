#Задача 22: 
#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
#m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
list_n = []
list_m = []
n = int(input('Size 1: '))
m = int(input('Size 2: '))

for i in range(n):
    list_n.append(int(input('Введите число: ')))
print(" ")    
print(list_n)
print()


for i in range(n):
    list_m.append(int(input('Введите число: ')))
print(' ')    
print(list_m)
print()

newlist = []

for i in range(n):
    if newlist.count(list_n[i]) == 0:
        newlist.append(list_n[i])

for i in range(m):
    if newlist.count(list_m[i]) == 0:
        newlist.append(list_m[i])        
print()        

#while i < len(newlist) - 1:
    #j = 1
    #c = 0
    #if newlist[i] > newlist[j]:
       #c, newlist[j], newlist[i] = newlist[j], newlist[i], c
    #j += 1
    #if j == len(newlist):
        #j = 1
       # i +=1
newlist.sort()
print(newlist)