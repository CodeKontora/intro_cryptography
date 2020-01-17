from prime_numbers import search_prime_number
from gcd_extended import gcd_extended


# Функция-шифровальщик
def encrypt(message):
    # Функция для чтения публичного ключа из файла
    def read_public_key():
        # Открываем файл
        with open('public.txt', 'r') as public:
            # Читаем файл
            # Руками закрывать файл не нужно
            # После считывания, файл автоматически закроет with
            file = public.read()
        # Разбиваем прочитанный ключ на две переменные
        open_exp, module = file.split(' ')
        return (int(open_exp), int(module))
    # В этом списке будем хранить зашифрованный текст
    encrypted_message = []
    # Получаем публичный ключ для шифрования
    open_exp, module = read_public_key()
    # Проходим по каждому символу в исходном сообщении
    for char in message:
        # Переводим символ в десятичное число 
        # Возводим в степень open_exp
        # И делим всё это по модулю module
        encrypted_message.append(pow(ord(char), open_exp, module))
    return encrypted_message


# Функция-дешифровальщик
def decrypt(encrypted_message):
    # Функция для чтения приватного ключа из файла
    # Всё тоже самое, что и при чтении публичного ключа
    def read_private_key():
        with open('private.txt', 'r') as private:
            file = private.read()
        closed_exp, module = file.split(' ')
        return (int(closed_exp), int(module))
    # В этом списке будем хранить расшифрованный текст
    decrypted_message = []
    # Получаем приватный ключ для дешифрования
    closed_exp, module = read_private_key()
    # Пробегаемся по каждому значению шифрованного текста
    for number in encrypted_message:
        # Возводим значение в степень closed_exp
        # Делим по модулю module
        # И переводим получвшиеся число в символ
        decrypted_message.append(chr(pow(number, closed_exp, module)))
    # Переводим список символов в одну строку и возвращаем
    return ''.join(decrypted_message)


# Функция для генерации ключей
# По умолчанию ищем простые 1024-битные числа
def generate_key(bit_size=1024):
    # Ищем простое 1024-битное число p
    prime_p = search_prime_number(bit_length=bit_size)
    # Ищем простое 1024-битное число q
    prime_q = search_prime_number(bit_length=bit_size)
    # Вычисляем модуль – произведение простых p и q
    module = prime_p * prime_q
    # Вычисляем функцию Эйлера
    Euler_function = (prime_p - 1) * (prime_q - 1)
    # Устанавливаем открытую экспоненту
    # Для ускорения вычислений лучше брать простые числа в форме n^4 + 1
    open_exp = 65537
    # Вычисляем закрытую экспоненту через расширенный алгоритм Евклида
    closed_exp, _, _ = gcd_extended(open_exp, Euler_function)

    # Записываем публичный и приватный ключ в файлы
    with open('public.txt', 'w') as public:
        public.write(f'{open_exp} {module}')
    with open('private.txt', 'w') as private:
        private.write(f'{closed_exp} {module}')


# Функция для проверки существования ключей
# Чтобы каждый раз не генерировать новые
def is_valid_keys():
    try:
        public = open('public.txt')
        public.close()
        prviate = open('private.txt')
        prviate.close()
    except FileNotFoundError:
        # Если файлов с ключами нет, то возвращаем False
        return False
    else:
        # Если файлы есть, то True
        return True


# Этот блок выполняется только когда мы запускаем файл как испольняемый
# А не как модуль
if __name__ == "__main__":
    # Проверяем существование ключей
    if not is_valid_keys():
        # Если их нет, то генерируем новые
        generate_key()
    # Шифруем строку Код Контора
    encrypted_message = encrypt('Код Контора')
    # Зашифрованное сообщение – список из огромных чисел
    print(encrypted_message)
    # Расшифровываем текст
    decrypted_message = decrypt(encrypted_message)
    # Получаем исходную строку – Код Контора
    print(decrypted_message)
