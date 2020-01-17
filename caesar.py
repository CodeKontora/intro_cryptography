import random


# Генерируем рандомный ключ от 3 до 7
# На это значение будем сдвигать символы
def generate_key():
    key = random.randint(3, 7)
    return key


# Функция-шифровальщик
def encrypt(message, key):
    # В этом списке будем хранить зашифрованный текст
    encrypted_message = []
    # Пробегаемся по каждому символу исходного текста
    for char in message:
        # Переводим символ в десятичное число
        # Увеличваем его на значение ключа
        # Переводим новое значение обратно в символ
        encrypted_char = chr(ord(char) + key)
        # Добавляем символ в зашифрованный текст
        encrypted_message.append(encrypted_char)
    # Переводим список символов в одну строку и возвращаем
    return ''.join(encrypted_message)


# Функция-дешифровальщик
def decrypt(encrypted_message, key):
    # В этом списке будем хранить расшифрованный текст
    decrypted_message = []
    # Пробегаемся по каждому символу зашифрованного текста
    for char in encrypted_message:
        # Переводим символ в десятичное число
        # Уменьшаем его на значение ключа
        # Переводим новое значение обратно в символ
        decrypted_char = chr(ord(char) - key)
        # Добавляем символ в расшифрованный текст
        decrypted_message.append(decrypted_char)
    # Переводим список символов в одну строку и возвращаем
    return ''.join(decrypted_message)


# Этот блок выполняется только когда мы запускаем файл как испольняемый
# А не как модуль
if __name__ == "__main__":
    # Генерируем ключ
    key = generate_key()
    # Шифруем строку Код Контора
    encrypted_message = encrypt('Код Контора', key)
    # Зашифрованный текст – Схл'Схфщхчз
    # С разным ключами, зашифрованный текст тоже будет разный
    print(encrypted_message)
    # Расшифровываем текст с помощью ключа
    decrypted_message = decrypt(encrypted_message, key)
    # Получаем исходную строку – Код Контора
    print(decrypted_message)
