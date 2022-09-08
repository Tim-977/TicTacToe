def g1():
    grid[0][0] = stat
def g2():
    grid[0][1] = stat
def g3():
    grid[0][2] = stat
def g4():
    grid[1][0] = stat
def g5():
    grid[1][1] = stat
def g6():
    grid[1][2] = stat
def g7():
    grid[2][0] = stat
def g8():
    grid[2][1] = stat
def g9():
    grid[2][2] = stat
grid = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]
stat = 1
hods = set()
n = 9
win = False

for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(grid[i][j], end=' ')
    print()
while n > 0:
    print('Ход игрока: ' + str(stat))
    hodf = True
    while hodf:
        hod = input()
        if hod not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']: print("Чё, еблан?"); continue
        hod = int(hod)
        if hod in hods: print("Чё, еблан?")
        else:
            hodf = False
            hods.add(hod)
    print()
    if hod == 1:
        g1()
    elif hod == 2:
        g2()
    elif hod == 3:
        g3()
    elif hod == 4:
        g4()
    elif hod == 5:
        g5()
    elif hod == 6:
        g6()
    elif hod == 7:
        g7()
    elif hod == 8:
        g8()
    elif hod == 9:
        g9()
    if grid[0][0] == grid[0][1] == grid[0][2] != '-' or grid[1][0] == grid[1][1] == grid[1][2] != '-' or grid[2][0] == grid[2][1] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][0] == grid[2][0] != '-' or grid[0][1] == grid[1][1] == grid[2][1] != '-' or grid[0][2] == grid[1][2] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][1] == grid[2][2] != '-' or grid[0][2] == grid[1][1] == grid[2][0] != '-':
        win = True
        break
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=' ')
        print()
    n -= 1
    stat += 1
    stat %= 2

if win:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=' ')
        print()
    print("Игра окончена! Победил: " + "Игрок 1" if stat == 1 else "Игра окончена! Победил: " + 'Игрок 2')
else: print('ПОБЕДИЛА ДРУЖБА УРАА')