# -*- coding:utf-8 -*-
# Author:wizard_wang

# python2.X需要在首行声明字符编码

#name = raw_input()  2.X 中使用
# input 2.X 不带引号是变量 带引号是字符串

name = input('uname:')
pwd = input('pwd:')
#强制转换为整形 默认输入都是字符串
age = int(input('age:'))
print(type(age),type(str(age)))

print(name,pwd)

#字符串格式化 建议不使用 + 拼接
# 占位符 %s字符串 %d数字
info1 = '''
-----------------info of %s-----------------
name:%s
pwd:%s
age:%d
''' % (name,name,pwd,age)

print(info1)

info2 = '''
-----------------info of {_name1}-----------------
name:{_name}
pwd:{_pwd}
age:{_age}
'''.format(_name1 = name,
           _name = name,
           _pwd = pwd,
           _age=age)
print(info2)


info3 = '''
-----------------info of {0}-----------------
name:{0}
pwd:{1}
age:{2}
'''.format(name,pwd,age)
print(info3)