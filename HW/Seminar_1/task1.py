day = int(input ('Введите день недели цифрой от 1 до 7'))
if day < 1 or day > 7:
    print ('Вы ввели некорректную цифру')
elif day == 6 or day ==7:
    print ('Да')
else:
    print ('Нет')