# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
num = float(input())
sum= 0
num *= 10 ** (len(str(num)) - 2)
while num:
    sum += num % 10
    num //= 10
print(int(sum))