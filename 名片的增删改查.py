def add_person(n_a, s_a, q_a):
    x = {'name': n_a, 'tel': s_a, 'qq': q_a}
    return x


list_person = []
while True:
    print('-' * 20)
    s = '名片管理系统 V1.0'
    print(s.rjust(15, ' '))
    print('1:添加名片：\n2:删除名片：\n3:修改名片：\n4:查询名片：\n5:显示所有名片：\n6:退出系统')
    print('-' * 20)
    n = eval(input('请输入要进行的操作（数字）：'))
    if n == 1:
        name1 = input('请输入姓名：')
        for item in list_person:
            if item['name'] == name1:
                print('此用户名已被占用，请重新输入')
                break
        else:
            tel1 = eval(input('请输入手机号：'))
            qq1 = eval(input('请输入QQ号：'))
            s1 = add_person(name1, tel1, qq1)
            list_person.append(s1)
            print(list_person)
    elif n == 2:
        name_2 = input('请输入姓名：')
        for item in list_person:
            if item['name'] == name_2:
                list_person.remove(item)
                break
        print(list_person)
    elif n == 3:
        k = eval(input('请输入要修改的序号是：'))
        print('你要修改的信息是：')
        print(list_person[k])
        list_person[k]['name'] = input('请输入新的姓名：')
        list_person[k]['tel'] = input('请输入新的手机号：')
        list_person[k]['qq'] = input('请输入新的QQ：')
        print(list_person)
    elif n == 4:
        name_4 = input('请输入要查询的名片姓名：')
        for item4 in list_person:
            if item4['name'] == name_4:
                print(item4)
                break
        else:
            print('没有您要找的信息...')
    elif n == 5:
        print(list_person)
    elif n == 6:
        print('亲，你确定要退出吗ヾ(●´∀｀●) （yes or no）')
        if input() == 'yes':
            exit()
