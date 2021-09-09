# Перепишите функцию hello_user() из задания про while, чтобы она перехватывала KeyboardInterrupt, 
# писала пользователю "Пока!" и завершала работу при помощи оператора break

def hello_user(user_answer):
    while True:
        if user_answer == 'Хорошо':
            print('Наконец-то!')
            break
        else:
            try:
                user_answer = input('Как дела? ')
            except KeyboardInterrupt:
                print('Пока!')
                break

user_answer = input('Как дела? ')
hello_user(user_answer)