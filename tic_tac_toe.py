a = int(input('Введите размерность доски: '))


# Создание доски
def create_board(a):
    count = 1
    z = [[] for _ in range(a)]
    for q in range(a):
        for s in range(a):
            z[q].append(count)
            count += 1
    return z


while True:
    board = create_board(a)  # Создаем новую доску на каждой итерации
    # Вывод доски
    print(board)

    # Ввод чисел для замены
    q = int(input('Введите число, которое заменить на "x": '))
    for row in board:
        for i, elem in enumerate(row):
            if elem == q:
                row[i] = 'x'

    z = int(input('Введите число, которое заменить на "0": '))
    for row in board:
        for i, elem in enumerate(row):
            if elem == z:
                row[i] = '0'

    print(board)