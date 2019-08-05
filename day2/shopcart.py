#!/user/bin/env python
# coding:utf-8

product_list = [
    ('iphone',5800),
    ('mac',9800),
    ('huawei',3800),
    ('ns',2800),
    ('ps4',3200),
    ('xbox',2600),
]
cart = []
salary = input("输入金额：")
if salary.isdigit():
    salary = int(salary)
    while True:
        #打印商品列表
        for index,item in enumerate(product_list):
            print(index,item)
        your_choice = input("选择购买商品编号>>>:")
        if your_choice.isdigit():
            your_choice = int(your_choice)
            #判断输入的编号是否正确
            if your_choice < len(product_list) and your_choice >-1:
                pic = product_list[your_choice]
                if salary >= pic[1]:
                    cart.append(pic)
                    salary -= pic[1]
                    print("添加 %s 到你的购物清单，有的余额是 \033[31;1m%s\033[0m" %(pic,salary))
                else:
                    print("你的余额只剩 \033[31;1m%s\033[0m ，无法购买，输入q退出" %(salary))
            else:
                print("输入的编号错误或者商品不存在")
        elif your_choice == 'q':
            print("-------购买商品列表--------")
            for p in cart:
                print(p)
            print("你的余额剩余 %s" %(salary))
            exit()
        else:
            print("输入的错误请输入编号")
else:
    print("输入的金额必须是数字")
