def area(a, b, c):
	p = a + b + c
	p2 = p / 2
	area = (p2 * (p2 - a) * (p2 - b) * (p2 - c))**0.5
	return area


print(area(int(input('Введите сторону a: ')), int(input('Введите сторону b: ')),int(input('Введите сторону c: '))))
