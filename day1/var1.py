# -*- coding:utf-8 -*-
# Author:wizard_wang

name1 = 'wizard'
name2 = name1
print('My name is',name1,name2)
#内存指向 name1 指向被修改 但是值改了但是name2还是指向‘wizard’
name1 = 'old wang'
print(name1,name2)

#变量 奇葩使用 中文做变量 只有python3支持
名字 = '奇葩的中文变量'
print(名字)

#python没有常量 大写表示声明常量
NAME = '声明是常量'
print(NAME)