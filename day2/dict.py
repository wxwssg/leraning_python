#!/user/bin/env python
# coding:utf-8

info = {
    'stu1001':'lao si ji',
    'stu1002':'biao che xia',
    'stu1003':'kai che',

}

print(info)


#查找
print(info.get('stu1003')) #查找取值 存在则取  否则不取

print('stu1003' in info) #判断是否存在键


info['stu1004'] = 'add stu'

new_info = {
    'stu1002':'super man',
    1:'hkjhkhkj',
    'hkjhkj':4654564
}

#合并字典
info.update(new_info)
print(info)

#字典转列表
print(info.items())

#删除
info.pop('stu1003')
del info['stu1001']
print(info)

#初始化一个新字典 多个key共享一个值  如果值是字典改变值 其他多项也会改变；如果是纯值只会修改单独的值不会修改其他值
c = dict.fromkeys([3,8,6],['test','hehehe'])
d = dict.fromkeys([1,5,9],'ceshi')

print(c)
print(d)
c[8][0] = 'hahaha'
d[9] = 'hahaha'
print(c)
print(d)



menu = {
    'm1':{
      'm1-1':{
          'baidu':['搜索','广告']
      }
    },
    'm2':{
      'm2-1':{
          'alibaba':['购物','支付']
      }
    },
    'm3':{
      'm3-1':{
          'tencent':['微信','qq']
      }
    },
    'm4':{
      'm4-1':{
          'qihu':['安全','系统']
      }
    }
}

menu['m4']['m4-1']['qihu'][1] = '测试'

#查找数据 如果没有就插入一条
menu.setdefault('m3',{'m3-2':{'zifu':['新闻','抖音']}})

print(menu)

menu.setdefault('m5',{'m3-2':{'zifu':['新闻','抖音']}})


print(menu)

#循环输出

#速度快
for i in menu:
    print(i,menu[i])

#速度慢
for k,v in menu.items():
    print(k,v)