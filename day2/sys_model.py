import os

#cmd_res = os.system("dir") #执行命令 直接显示 不保存结果
cmd_res = os.popen("dir").read() #执行命令保存结果

print("-->",cmd_res)


#import sys
#@print(sys.path) #打印环境变量
#print(sys.argv)
#print(sys.argv[2])





