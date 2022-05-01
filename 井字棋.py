import random

s = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  # 创建一个列表用来存储数据


def board():  # 输出最初的空白棋盘及修改后的棋盘
    for i in range(0, 3):
        for j in range(0, 3):
            print(' {} '.format(s[i][j]), end='')
            if j < 2:
                print('|', end='')
        print()
        if i < 2:
            print('---|---|---')
    print('Σσ(・Д・；)我我我什么都没做!!!!!!!!!!!!!')


def game_man(s1):  # 玩家落子,标记为*
    while True:
        x, y = eval(input('请输入你要下的坐标（形如1,1）：'))
        if 1 <= x <= 3 and 1 <= y <= 3:
            if s[x - 1][y - 1] == ' ':
                s[x - 1][y - 1] = '*'
                board()
                break
            else:
                print('你输入的坐标已被占用，请重新输入')
        else:
            print('你输入的坐标有误，请重新输入')


def game_computer(s2):  # 智障电脑落子，标记为#，俺不会人工智能，所以他是个智障
    while True:
        x1 = random.randint(0, 2)
        y1 = random.randint(0, 2)
        if s[x1][y1] == ' ':
            s[x1][y1] = '#'
            board()
            break
        elif is_full(s2):  # 没这玩意，填最后一个元素的时候就死循环了，找了半个小时错误，我服了，找bug太痛苦了
            break


def is_win(s3):  # 很简单，通过这个函数返回的值判断谁赢了
    while True:
        game_man(s3)
        game_computer(s3)
        for i in range(0, 3):
            if s3[i][0] == s3[i][1] == s3[i][2] and s3[i][1] != ' ':
                return s3[i][0]
            elif s3[0][i] == s3[1][i] == s3[2][i] and s3[1][i] != ' ':
                return s3[0][i]
            elif (s3[0][0] == s3[1][1] == s3[2][2] or s3[2][0] == s3[1][1] == s3[0][2]) and s3[1][1] != ' ':
                return s3[1][1]
        if (' ' not in s3[0]) and (' ' not in s3[1]) and (' ' not in s3[2]):
            return 'C'
        else:
            return 'D'


def is_full(s4):
    if (' ' not in s4[0]) and (' ' not in s4[1]) and (' ' not in s4[2]):
        return 1


print('*' * 25)
print('1->玩游戏'.center(23, '*'))
print('0->退出'.center(24, '*'))
print('*' * 25)
a = 0
while a != 1:
    a = eval(input('请选择是否玩游戏:'))
    if a == 1:
        while True:
            board()
            t = is_win(s)
            if t == '*':
                print('能赢没什么好骄傲的，因为它是个智障')
                break
            elif t == '#':
                print('这都能输，你个废物')
                break
            elif t == 'C':
                print('你真是个天才，能下成平局')
                break
            elif t == 'D':
                print('速度解决，和他下棋是浪费时间')
    elif a == 0:
        print('再见')
        exit()
    else:
        print('输入错误，请重新选择')
