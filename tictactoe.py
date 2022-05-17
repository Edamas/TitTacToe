def show():
    global cells
    print('---------')
    for row in range(1, 4):
        print('|', end=' ')
        for key in cells:
            if row == key[0]:
                print(cells[key], end=' ')
        print('|')
    print('---------')

def turn(player):
    global cells
    while True:
        row, col = [value for value in input('Enter the coordinates:').split(' ')]
        if not row.isnumeric() or not col.isnumeric():
            print('You should enter numbers!')
        else:
            row, col = [int(value) for value in [row, col]]
            if not 1 <= row <= 3 or not 1 <= col <= 3:
                print('Coordinates should be from 1 to 3!')
            else:
                print(cells[(row, col)])
                if cells[(row, col)] in 'XO':
                    print('This cell is occupied! Choose another one!')
                else:
                    cells[(row, col)] = player
                    break
                    
cells = {}
combinations = [[(1, 1), (2, 2), (3, 3)], [(1, 3), (2, 2), (3, 1)]]  # diagonals
for row in range(1, 4):
    horizontals, verticals = [], []
    for col in range(1, 4):
        cells[(row, col)] = ' '
        horizontals.append((row, col))
        verticals.append((col, row))
    combinations.append(horizontals)
    combinations.append(verticals)

turns = 1
finished = False
while not finished:
    if turns % 2 == 0:
        player = 'X'
    else:
        player = 'O'
    turn(player)
    show()
    
    for a, b, c in combinations:
        if cells[a] == cells[b] == cells[c] and cells[a] != ' ':
            print(cells[a], 'wins')
            finished = True
            break
    else:
        if turns == 9:
            print('Draw')
            finished = True
            break
    turns += 1
