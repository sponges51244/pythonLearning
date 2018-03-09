#coding=utf-8
# 字典
info = {"name":"sun", "addr":"shandong...", "age":18}

print("%s %d %s" %(info["name"], info["age"], info["addr"]))

#===============字典的增删改查=================
'''增'''
info['qq'] = 10010
'''改'''
info["name"] = "li"

print(info)	# {'name': 'li', 'addr': 'shandong...', 'age': 18, 'qq': 10010}

'''删'''
del info['qq']
print(info)	#{'name': 'li', 'addr': 'shandong...', 'age': 18}

'''查 : get()不会让程序崩溃如果没有key的话
直接info['key']如果没这个key的话会报错
'''
print(info.get('qq'))	#None
print(info.get('name')) #li

print(len(info))	# 3

#得到所有的键
print(info.keys())	# dict_keys(['name', 'addr', 'age'])

#得到所有的值
print(info.values())	# dict_values(['li', 'shandong...', 18])

if "name" in info.keys():
	print("有name这个key")	#有name这个key

#遍历键
for temp in info.keys():
	print(temp)

print("="*10)

#遍历value
for temp in info.values():
	print(temp)

print("="*10)

#把key和value分装到元组中
print(info.items())	# dict_items([('name', 'li'), ('addr', 'shandong...'), ('age', 18)])

#遍历key和value, 三种遍历方式
for temp in info.items():
	print(temp)

for temp in info.items():
	print("key=%s, value=%s" %(temp[0],temp[1]))

for A, B in info.items():
	print("key=%s, value=%s" %(A,B))

print("="*10)


#============元组=============

nums = (11,22,33)
print(type(nums))	# <class 'tuple'>

#列表和元组大致一样，但元组不能改里面的元素，元组只能查询

a = (11,22)
b = a
print(b)	#(11, 22)

#拆包过程
c,d = a

print(c)	#11
print(d)	#22






