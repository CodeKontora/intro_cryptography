from math import log2
from random import randint


def Miller_Rabin_test(number):
	# Функция для разложения number - 1 в 2^s * t
	def decomposition(s, t):
		while (s % 2 == 0):
			s //= 2
			t += 1
		return s, t
	# Проверяем простые случаи
	# Если число равно 2 или 3, то оно простое
	if number == 2 or number == 3:
		return True
	# Если число меньше 2 или чётное, то оно не просто
	elif number < 2 or number % 2 == 0:
		return False
	# Если число больше трёх и нечётное, то начинаем вычисления
	else:
		# Раскладываем number - 1 на t и s
		t, s = decomposition(number - 1, 0)
		# Вычисляем количество раундов
		# Для этого алгоритма лучше брать log2(number) раундов
		rounds_amount = int(log2(number))
		# Начинаем раунды
		for _ in range(rounds_amount):
			random_number = randint(2, number - 2)
			# Возводим случайное число в степень t по модулю number
			x = pow(random_number, t, number)
			# Если получившиеся значение равно 1 или number - 1
			if x == 1 or x == number - 1:
				# То переходим на следующий раунд
				continue
			# Иначе проверяем x на равенство 1 или number - 1 s-1 раз
			for _ in range(s - 1):
				x = pow(x, 2, number)
				# Если x равен 1, то число составное
				if x == 1:
					return False
				# Если х равен number - 1, то число возможно простое
				elif x == number - 1:
					# Выходим во внешний цикл и начинаем новый раунд
					break
			# Если цикл от 0 до s - 1 полностью прокрутился и x не равен number - 1, то число составное
			if x != number - 1:
				return False
		# Если проверки прошли в каждом раунде – число простое с вероятностью 1/4^количество_раундов
		# Например, для проверки числа 107 нужно 6 раундов
		# 107 простое число с вероятностью 1/4^6 или же 0.02%
		return True
