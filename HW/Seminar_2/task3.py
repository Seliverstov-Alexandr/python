# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
n = int(input())
lis = []
sum = 0
for i in range (1, n+1):
    res = round((1+1/i)**i, 3)
    lis.append (res)
    sum += res
print (lis)
print (sum)
