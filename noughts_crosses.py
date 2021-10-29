def new_game():
    print("-------------------")
    print("  Крестики-нолики  ")
    print("-------------------")
    print("Введите: x и y, где")
    print("x - номер строки   ")
    print("y - номер столбца  ")


def show_field():
    print('  0 1 2')
    for i, j in enumerate(field):
        print(f"{i} {' '.join(j)}")


def user_input():
    while True:
        move = input(f"Ваш ход, {user}: ").split()

        if len(move) != 2:
            print("Введите 2 значения!")
            continue

        x, y = move

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа!")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне игрового поля!")
            continue

        if field[x][y] != "-":
            print("Ячейка занята!")
            continue

        return x, y


def game_over():
    win_positions = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for position in win_positions:
        values = []
        for i in position:
            values.append(field[i[0]][i[1]])
        if values == ["X", "X", "X"]:
            print("Победа X!")
            return True
        if values == ["0", "0", "0"]:
            print("Победа 0!")
            return True
    return False


new_game()
field = [['-'] * 3 for _ in range(3)]
count = 0
while True:
    count += 1
    show_field()
    if count % 2 == 1:
        user = 'X'
    else:
        user = '0'

    x, y = user_input()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if game_over():
        show_field()
        break

    if count == 9:
        print("Победила дружба!")
        show_field()
        break
