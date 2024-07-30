from string import ascii_letters, digits
from random import choice, sample

def isEven(integer):
    """Возвращает Boolean: True, если число четное, иначе False."""
    return integer % 2 == 0

def RandPass(size=8):
    """Генератор паролей"""
    s0 = ascii_letters  # Заглавные и строчные буквы
    s1 = digits  # Цифры
    s3 = "!$%^&*- _~"  # Специальные символы, включая пробел
    s = s0 + s1  # Все буквы и цифры
    s_full = s + s3  # Все буквы, цифры и специальные символы
    
    # Проверяем, что size - это положительное целое число
    if not isinstance(size, int) or size < 1:
        raise ValueError("Размер пароля должен быть положительным целым числом")

    passlen = size
    new_password = ""

    # Определяем размеры каждой части пароля
    if isEven(passlen):
        frnt = passlen // 3  # Длина первой части
    else:
        frnt = passlen // 2  # Длина первой части для нечетных размеров
    mid = 2  # Длина средней части (специальные символы)
    bck = passlen - (frnt + mid) - 1  # Длина последней части

    # Генерируем части пароля
    p0 = "".join(choice(s0))  # Первая часть: только буквы (без специальных символов)
    p1 = "".join(sample(s_full, frnt))  # Вторая часть: буквы, цифры и специальные символы
    p2 = "".join(sample(s3, mid))  # Третья часть: специальные символы
    p3 = "".join(sample(s, bck))  # Четвертая часть: буквы, цифры и специальные символы

    # Корректируем размер части p2, если общая длина не совпадает с ожидаемой
    if passlen != len(p0 + p1 + p2 + p3):
        p2 = "".join(sample(s3, passlen - (frnt + bck + 1)))

    # Обеспечиваем, что пробел не будет в конце пароля
    if p3 and p3[-1] == ' ':
        p3 = p3[:-1] + choice(s)  # Заменяем пробел на случайный символ

    # Объединяем все части в один пароль
    new_password = p0 + p1 + p2 + p3

    # Определяем силу пароля на основе его длины
    if passlen <= 8:
        msg = 'VERY WEAK'
        colorVal = "#6d0001"  # Цвет для очень слабого пароля
    elif passlen <= 10:
        msg = 'WEAK'
        colorVal = "#cc0000"  # Цвет для слабого пароля
    elif passlen <= 12:
        msg = 'DECENT'
        colorVal = "#fc8600"  # Цвет для приличного пароля
    elif passlen <= 14:
        msg = 'GOOD'
        colorVal = "#eae200"  # Цвет для хорошего пароля
    elif passlen <= 16:
        msg = 'STRONG'
        colorVal = "#9ff400"  # Цвет для сильного пароля
    elif passlen <= 18:
        msg = 'VERY STRONG'
        colorVal = "#007715"  # Цвет для очень сильного пароля
    else:
        msg = 'EXCELLENT'
        colorVal = "#001fef"  # Цвет для отличного пароля

    return new_password, msg, colorVal
