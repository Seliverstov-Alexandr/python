# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x = int(input ('Введите координату X не равную 0'))
y = int (input ('Введите координату Y не равную 0'))
if x>0 and y>0:
    print ('Точка в 1 четверти')
elif x>0 and y<0:
    print ('Точка в 2 четверти')
elif x<0 and y<0:
    print ('Точка в 3 четверти')
elif x<0 and y>0:
    print ('Точка в 4 четверти')
else:
    print ('Ошибка! Введен 0')
