a = int(input('введи на какой доске хочешь сыграть\n',))
def board(a):
    count = 1
    z = [[] for i in range(a)]
    for q in range(a):
        for s in range(a):
            z[q].append(count)
            count += 1
    return z
print(board(a))