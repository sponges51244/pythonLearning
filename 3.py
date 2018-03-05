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



