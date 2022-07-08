def vklad(x, y, p):
    count = 0
    while x < y:
        x = int(x + x * (p /100))
        count += 1
    return count

print(vklad(int(input('Размер вклада: ')), int(input('Целевая сумма: ')), float(input('Ставка: '))))
