from miller_rabin import Miller_Rabin_test
from random import getrandbits


# Функция для генерации простого числа
# По умолчанию, размер числа равен 170 бит
def search_prime_number(bit_length = 170):
    # Флаг простоты числа
    is_prime = False
    # Простое случайное число размером bit_length бит
    random_prime_number = None
    # Пока не получим простое число
    while not is_prime:
        # Создаём случайное число размером bit_length бит
        random_prime_number = getrandbits(bit_length)
        # Проверяем его на простоту
        is_prime = Miller_Rabin_test(random_prime_number)
    # Возвращаем случайное простое число
    return random_prime_number
