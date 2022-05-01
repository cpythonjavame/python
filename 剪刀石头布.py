from random import *
i = 1
while i == 1:
    a = int(input("请输入0（剪刀)、1（石头）或2（布）："))
    print('用户输入的是:', a)
    b = randint(0, 2)
    print('电脑输入的是:', b)
    if a == b:
        print('再来一把')
    elif a - b == 1 or a - b == -2:
        print('你赢了')
    else:
        print('你输了')
    c = int(input('请输入0（退出）或1（再来一把）:'))
    i = 1 if c == 1 else 0
print('游戏结束')
