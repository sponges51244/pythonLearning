num = 100
str(num)	#'100'

name = "xiao"

len(name)	#4

lastName = "sun"

print("====%s=====" %(name + lastName))	# ====xiaosun=====

name = '012345678'

print(name[2:6])	# 2345

print(name[2:-1])	# 234567

print(name[2:])		# 2345678 默认取到最后一个

print(name[2:-1])	# 234567

print(name[2:-1:2])	# 246 跳着取 【start:end:step】

print(name[-1::-1])	# 876543210 逆序

#===========list==========

names = ["wang", "li", "liu", 11, 3.14]	# define a list

#增删改查

'''
增 ： append() / insert() / extend()
'''
names.append("zhao") # 加到最后

#names.insert(位置，要添加的内容)
names.insert(0, "bajie")

print(names)	# ['bajie', 'wang', 'li', 'liu', 11, 3.14, 'zhao']

names.insert(2, "wukong")

print(names) # ['bajie', 'wang', 'wukong', 'li', 'liu', 11, 3.14, 'zhao']

#combine two lists
names2 = ["sun", "hua"]

names3 = names2 + names
print(names3) # ['sun', 'hua', 'bajie', 'wang', 'wukong', 'li', 'liu', 11, 3.14, 'zhao']

#把names2合到names
names.extend(names2)

print(names) # ['bajie', 'wang', 'wukong', 'li', 'liu', 11, 3.14, 'zhao', 'sun', 'hua']

'''
删 ： pop() 删除最后一个/ remove() 根据内容删除/ del xx[下标] 根据下标删除
'''
print(names.pop())	# hua 
print(names) # ['bajie', 'wang', 'wukong', 'li', 'liu', 11, 3.14, 'zhao', 'sun']

del names[0]
print(names)	# ['wang', 'wukong', 'li', 'liu', 11, 3.14, 'zhao', 'sun']

names.remove("liu")
print(names)	# ['wang', 'wukong', 'li', 11, 3.14, 'zhao', 'sun']

'''
改： xxx[下标]
'''
names[3] = 'shawn'
print(names)	# ['wang', 'wukong', 'li', 'shawn', 3.14, 'zhao', 'sun']

'''
查：	in / not in
'''
if "li" in names:
	print("found")
if "zhou" not in names:
	print("not in")



