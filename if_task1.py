#Попросить пользователя ввести возраст при помощи input и положить результат в переменную
#Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: учиться в детском саду, школе, ВУЗе или работать
#Вызвать функцию, передав ей возраст пользователя, и положить результат работы функции в переменную
#Вывести содержимое переменной на экран

int_user_input = int(input('Введите ваш возраст:'))

def define_occupation(int_user_input):
    if int_user_input <= 6:
        result = 'иди в детский сад'
    elif 7 <= int_user_input <= 17:
        result = 'иди в школу'
    elif 17 < int_user_input <= 21:
        result = 'иди в  универ'
    else: 
        result = 'иди работай'
    return result

occupation = define_occupation(int_user_input)
print(occupation)