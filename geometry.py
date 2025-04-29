def area_1(length, width):
    return length * width

def area_2(radius):
    return 3.14159 * radius ** 2

def area_3(base, height):
    return 0.5 * base * height

def area_4(base1, base2, height):
    return 0.5 * (base1 + base2) * height

while True:
    print("選擇要計算面積的幾何圖形種類:")
    print("1. 長方形")
    print("2. 圓形")
    print("3. 三角形")
    print("4. 梯形")
    print("5. 退出")

    choice = input("請輸入選擇 (1/2/3/4/5): ")

    if choice == '1':
        length = float(input("請輸入長: "))
        width = float(input("請輸入寬: "))
        print(f"面積 = {area_1(length, width)}")

    elif choice == '2':
        radius = float(input("請輸入半徑: "))
        print(f"面積 = {area_2(radius):.2f}")

    elif choice == '3':
        base = float(input("請輸入底: "))
        height = float(input("請輸入高: "))
        print(f"面積 = {area_3(base, height)}")

    elif choice == '4':
        base1 = float(input("請輸入上底: "))
        base2 = float(input("請輸入下底: "))
        height = float(input("請輸入高: "))
        print(f"面積 = {area_4(base1, base2, height)}")
    
    elif choice == '5':
        print("再見")
        break