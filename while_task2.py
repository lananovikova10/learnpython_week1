"""
Создайте словарь типа "вопрос": "ответ", например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее.
Напишите функцию ask_user() которая с помощью функции input() просит пользователя ввести вопрос, а затем, 
если вопрос есть в словаре, программа давала ему соотвествующий ответ. 
"""

q_and_a = {'Как дела': 'Пока не родила!',
           'Что делаешь': 'Сплю', 'Часто тут бываешь': 'Нет'}
input_question = input('Введите вопрос ')


def ask_user(input_question):
    while True:
        if input_question in q_and_a:
            print(q_and_a[input_question])
            return True
        else:
            print('я такого вопроса не знаю')
            return False


ask_user(input_question)
# q_and_a.get('input_question')
