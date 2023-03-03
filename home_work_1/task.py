#Найдите сумму цифр трехзначного числа.

a = int(input('Введите трехзначное число: '))
b= a // 100
c = a % 10
d = a // 10 % 10
print(a)
print(b)
print(d)
print(c)
print(b+d+c)