account = 'admin'
password  = '10160013'

for i in range(3):
    input_account = input("請輸入帳號：")
    input_password = input("請輸入密碼：")
    if input_account == 'admin' and input_password == '10160013':
        print("登入成功！")
        break
    elif input_account == 'admin' and input_password != '10160013':
        print("密碼錯誤！")
    elif input_account != 'admin' and input_password == '10160013':
        print("帳號錯誤！")
    else:
        print("帳號密碼錯誤！")