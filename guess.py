# Author:wizard_wang
real_age = int(input("输入要猜的数字"))

#while 猜数字
count = 0
while count <3:
    guess_age = int(input("猜数字:"))
    if guess_age == real_age:
        print("猜对了")
        break
    elif guess_age>real_age:
        print("猜大了")

    elif guess_age<real_age:
        print("猜小了")
    count +=1
    if count == 3:
        continue_confirm = input("是否继续 y/n")
        if continue_confirm == 'y':
            count = 0
else:
    print('猜数超过3次了')

#for 循环猜数字
for i in range(3):
    guess_age = int(input("猜数字:"))
    if guess_age == real_age:
        print("猜对了")
        break
    elif guess_age > real_age:
        print("猜大了")

    elif guess_age < real_age:
        print("猜小了")
else:
    print('猜数超过3次了')