password = "a123456"
times = 3
while times > 0:
	times = times - 1
	pwd = input("請輸入密碼")
	if password == pwd:
		print('登入成功')
		break
	else:
		if times > 0:
			print('密碼錯誤,剩餘',times,'機會')
		else:
			print('密碼錯誤,帳號已鎖定')
