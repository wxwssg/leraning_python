#!/user/bin/env python
# coding:utf-8
import copy

msg = "测试数据"

#字符串和bytes相互转换
print(msg.encode(encoding='utf-8'))
print(msg.encode(encoding='utf-8').decode(encoding='utf-8'))

#元组 只能读取 和统计 不允许改变
alllist = ("1111","222","333")
alllist[2]
alllist.count("333")

#列表
names = ["ceshi","zhangsan","lisi","wangwu","zhaoerma"]


names.append("zhuijia") #追加

names.insert(3,"charu") #插入

names[2] = "tihuan" #替换

names.remove("tihuan") #删除数据

#删除数据
del names[1]
names.pop(1)


print(names)
print(names[1:3])#切片 顾头不顾尾
print(names[-2:])#取最后2个
print(names[:3])#取前2个
print(names[0:-1:2])#隔1个切片
print(names.index("wangwu"))#取值下标
print(names.count("zhaoerma"))#统计值数量


names = ["ceshi","zhangsan","lisi",["haha","ceshi"],"wangwu","zhaoerma"]
#浅复制 几种方式
names2 = names.copy()
names3 = copy.copy(names)
names4 = names[:]
names5 = list(names)


names[3][1] = "同步改变"
names[2] = "同步不变"
print(names)
print(names2)

#完全复制
names = ["ceshi","zhangsan","lisi",["haha","ceshi"],"wangwu","zhaoerma"]
names2 = names
names[3][1] = "同步改变"
names[2] = "同步改变"
print(names)
print(names2)
