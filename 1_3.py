n = int(input('Введите число: '))
result = 0
while n != 0:
	last_digit = n % 10
	result += last_digit
	n = n // 10
print(result)