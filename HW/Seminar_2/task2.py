# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
number = int (input())
num = 1
for i in range (number):
    num*= i+1
    print (num, end=', ')

