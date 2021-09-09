# Написать функцию, которая принимает на вход две строки
# Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
# Если строки одинаковые, вернуть 1
# Если строки разные и первая длиннее, вернуть 2
# Если строки разные и вторая строка 'learn', возвращает 3
# Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты

def compare_strings(string1, string2):

    if type(string1) != str or type(string2) != str:
        return 0
    elif string1 == string2:
        return 1
    elif len(string1) > len(string2):
        return 2
    elif string1 != string2 and string2 == 'learn':
        return 3
    else:
        print('Ни одно из условий не сработало')


compare = compare_strings('love', 'learn')
print(compare)
