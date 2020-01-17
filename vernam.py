from random import getrandbits


# Функция-шифровальщик
def encrypt(message):
    # Вычисляем длину одного символа в тексте для шифрования
    # Латинские буквы занимают 8 бит, а кириллица – 16 бит
    char_bit_length = len(message.encode('utf-8')) // len(message) * 8
    # После шифрования строки здесь будет лежать ключ для расширофки
    key = []
    # В этом списке будем хранить зашифрованный текст
    encrypted_message = []
    # Начинаем шифровать
    for char in message:
        # Рандомим число на количество бит в символе
        key_part = getrandbits(char_bit_length)
        # Переводим символ из исходного текста в десятичный вид
        # Делаем XOR между исходным символом и рандомным числом
        # Добавляем получившиеся число в список
        encrypted_message.append(ord(char) ^ key_part)
        # Добавляем часть ключа
        key.append(key_part)
    # Возвращаем зашифрованный текст и полный ключ
    return (encrypted_message, key)


# Функция-дешифровальщик
def decrypt(encrypted_message, key):
    # В этом списке будем хранить расшифрованный текст
    decrypted_message = []
    # Через zip работаем одновременно с двумя значениями
    for enc, num in zip(encrypted_message, key):
        # Делаем XOR между зашифрованным текстом и ключом
        # Переводим получившиеся значение в символ
        # И добавляем получившийся символ в список
        decrypted_message.append(chr(enc ^ num))
    # Переводим список символов в одну строку и возвращаем
    return ''.join(decrypted_message)


# Этот блок выполняется только когда мы запускаем файл как испольняемый
# А не как модуль
if __name__ == "__main__":
    # Шифруем строку Код Контора
    encrypted_message, key = encrypt('Код Контора')
    # Зашифрованный текст – список чисел 
    # [1043, 1122, 1183, 6, 1241, 1134, 1090, 1263, 1230, 1174, 1024]
    print(encrypted_message)
    # Ключ тоже список чисел, только других
    # [9, 92, 171, 38, 195, 80, 127, 173, 240, 214, 48]
    print(key)
    # Расшифровываем текст с помощью ключа
    decrypted_message = decrypt(encrypted_message, key)
    # Получаем исходную строку – Код Контора
    print(decrypted_message)
