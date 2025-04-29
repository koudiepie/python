number = (input("請輸入數字: "))

if number.isdigit() and int(number) >= 0: #isdigit()判斷是否為全數字
    number = int(number)
    
    def factorial(n):
        result = 1
        if number == 0:
            return 1

        for i in range(1, n+1):
            result *= i
        return result

    print(f"{number} 的階乘是: {factorial(number)}")
else:
    print("無效數字，重新輸入")