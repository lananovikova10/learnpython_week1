#Написать функцию, которая принимает на вход две строки
#Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
#Если строки одинаковые, вернуть 1
#Если строки разные и первая длиннее, вернуть 2
#Если строки разные и вторая строка 'learn', возвращает 3
#Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты

def compare_strings(string1, string2):
    if type(string1) == str and type(string2) == str:
#        print('Это строки!')
        if string1 == string2:
            return 1
        elif len(string1) > len(string2):
            return 2
        elif string1 != string2 and string2 == 'learn':    
            return 3
    else:
        return 0

compare = compare_strings('learn',3)
print(compare)