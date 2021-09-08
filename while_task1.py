#Напишите функцию hello_user(), которая с помощью функции input() спрашивает #пользователя “Как дела?”, пока он не ответит “Хорошо”

def hello_user(user_answer):
    while True:
        if user_answer == 'Хорошо':
            print('Наконец-то!')
            break
        else:
            user_answer = input('Как дела? ')

user_answer = input('Как дела? ')
hello_user(user_answer)

        