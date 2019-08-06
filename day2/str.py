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

#删除2端空格和换行
print('\nremove lfet sapce'.lstrip())
print('remove right sapce\n'.rstrip())
print('\nremove  sapce\n'.strip())

#字符串替换 适用于加密替换
p = str.maketrans('abcdefg','1234567')
print('print account'.translate(p))

#字符串以某个值转换成列表
print('1,2,3,4,5'.split(','))

#大小写相互转换
print('Test The Python 3.5.5'.swapcase())

#把字符串转换成英文标题格式
print('test the python'.title())
