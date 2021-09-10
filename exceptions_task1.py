# Перепишите функцию hello_user() из задания про while, чтобы она перехватывала KeyboardInterrupt, 
# писала пользователю "Пока!" и завершала работу при помощи оператора break



def hello_user():
    try:
        while True:
            user_answer = input('Как дела? ')
            if user_answer != 'Хорошо':
                pass
            else: 
                print('Наконец-то!')  
                break

    except KeyboardInterrupt:
        print('Пока!')

hello_user()
