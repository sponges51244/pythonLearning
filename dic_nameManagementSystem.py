#1.打印功能提示

print("="*50)
print("	名片管理系统")
print(" 1:添加一个新的名字")
print(" 2:删除一个名字")
print(" 3：修改一个名字")
print(" 4:查询一个名字")
print(" 5:显示所有的名片")
print(" 6:退出系统")


cards_info = []	# 定义一个空的列表

while True:

	#2.获取用户的选择
	print("")
	num = int(input("请输入功能序号： "))
 
	#3.根据用户的选择，执行相应的功能

	if num == 1:
		new_name = input("请输入名字：")
		new_qq = input("请输入qq：")
		new_weixin = input("请输入微信：")
		new_addr = input("请输入住址：")

		#定义一个新的字典，存储名片
		new_info = {}
		new_info['name'] = new_name
		new_info['qq'] = new_qq
		new_info['weixin'] = new_weixin
		new_info['address'] = new_addr

		#将字典添加到列表中
		cards_info.append(new_info)

		#print(cards_info) #for test
	elif num == 2:
		pass

	elif num == 3:
		pass

	elif num == 4:
		find_name = input("请输入要查询的名字：")

		find_flag = 0 #默认表示没有找到

		for temp in cards_info:
			if temp["name"] == find_name:
				print("%s\t%s\t%s\t%s" %(temp["name"],temp["qq"],temp["weixin"],temp["address"]))
				find_flag = 1
				break
		#判断是否找到了
		if(find_flag == 0):
			print("查无此人......")

	elif num == 5:
		print("姓名\tqq\t微信\t住址")
		for temp in cards_info:
			print("%s\t%s\t%s\t%s" %(temp["name"],temp["qq"],temp["weixin"],temp["address"]))
	elif num == 6:
		break
	else:
		print("您的输入有误，请重新输入")
