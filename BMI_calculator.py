height = float(input("請輸入身高: "))
weight = float(input("請輸入體重: "))

BMI = weight / (height / 100) ** 2

BMI = round(BMI, 4)

print("BMI是:", BMI)

if BMI < 18.5:
    print("過輕")
elif 18.5 <= BMI < 24:
    print("標準")
elif 24 <= BMI < 27:
    print("過重")
elif 27 <= BMI:
    print("肥胖")