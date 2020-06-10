
remaining_times = 3
tr_password = "12345b"
while True: 
	password = input("請輸入密碼: ")
	if password == tr_password:
		print("登入成功")
		break
	else:
		remaining_times = remaining_times -1
		if remaining_times == 0:
			print("你已無法登入")
			break
		print("請再試一次! 你還有", remaining_times, "次機會")
		
