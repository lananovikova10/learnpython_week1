# Перепишите функцию discounted(price, discount, max_discount=20) из урока про функции так,
# чтобы она перехватывала исключения, когда переданы некорректные аргументы.
# Первые два нужно приводить к вещественному числу при помощи float(),
# а третий - к целому при помощи int() и перехватывать исключения ValueError и TypeError, если приведение типов не сработало.

def discounted(price, discount, max_discount=20):
    try:
        price = float(abs(price))
        discount = float(abs(discount))
        max_discount = int(abs(max_discount))
    except (TypeError, ValueError):
        print('Не удалось привести типы')
        return None

    try:
        if max_discount >= 100:
            raise ValueError
    except ValueError:
        print('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

discounted('fvfvfv', 50, 200)

