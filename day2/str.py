#!/user/bin/env python
# coding:utf-8

name = "test \t the {name} python version {vis} "

print(name.capitalize()) #首字母大写
print(name.count('e')) #统计位置
print(name.center(50,'-')) #前后输出 -
print(name.endswith('st')) #判断是否 以XX结尾
print(name.expandtabs(tabsize=20)) #设置tab空格长度
print(name.find('the')) #查找包含的字符串的开头的索引下标
print(name[name.find('the'):]) #字符串切片
print(name.format(name="local",vis="3.5.5")) #字符串变量设置
print(name.format_map({'name':'server','vis':'3.7'})) #字典值设置到变量
print(name.isalnum()) #判断是否只是英文和数字
print('hkjhkj11123'.isalnum()) #判断是否只是英文和数字