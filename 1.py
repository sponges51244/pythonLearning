#在代码第一行写入执行时的Python 解释路径，编辑完后需要对此python文件添加‘x'权限

#用 $ which python3 来得到Python 解释路径

#!/usr/bin/python         让其变为executable file,可以使用./1.python,

#coding=utf-8		汉语显示

#chmod u+x file_name

#单行注释

'''
多行注释
多行注释
'''

'''文档注释'''

#============变量定义==============
name = "dongge"

age = 100

print(name)		# dongge

'''变量类型： Numbers; boolean; String; List; Tuple; Dictionary '''

print(type(name))	# type() 能测变量类型

# input - get input from terminal, by default all value received is string
# in python2, can use raw_input, python3 use input, try to input 1+2 to see the difference

high = input("please enter you heigh: ")

age = 18

print("age is %d" %age)	# age is 18

name = "Dong"

print("name is %s" %name)

#输出多个变量
print("name is %s ; age is %d"%(name,age))

#=========== if ================

age = input("please enter your age: ")
age_num = int(age)		

if age_num > 18 and age_num < 70:
	print("work")
elif age_num == 18 or age_num == 70:
	print("reflection year")
else:
	print("not work")

a = 90

if not (a >= 0 and a <= 50):
	print("a < 0 or a > 50")

#============================

5/2		#2.5
5//2	#2
5%2		#1

2**2	#4  次方
2**3	#8
2**10	#1024
2**16	#65536

"H"*10	# 'HHHHHHHHHH'

#==========while + for================
num = 1
print(num)

while num < 10:
	num = num+1
	print(num)

name = "laowang"

for temp in name:
	print('-'*5)
	print(temp)



