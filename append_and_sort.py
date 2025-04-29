def get_sorted_numbers():
    numbers = list(map(int, input("輸入一串數字，以空格分隔: ").split()))
    numbers.sort()
    print("排序後的數字:", numbers)
    
    while True:
        choice = input("是否要繼續新增數字？(y/n): ").strip()
        if choice == 'y':
            new_numbers = list(map(int, input("輸入數字，以空格分隔: ").split()))
            for num in new_numbers:
                numbers.append(num)
            numbers.sort()
            print("更新後排序的數字:", numbers)
        elif choice == 'n':
            print("排序結果:", numbers)
            break
        else:
            print("請輸入 'y' 或 'n'!")

get_sorted_numbers()
