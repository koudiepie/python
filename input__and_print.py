schedule = {
    "星期一": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 20: None, 30: None, 40: None, 50: None, 60: None, 70: None},
    "星期二": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 20: None, 30: None, 40: None, 50: None, 60: None, 70: None},
    "星期三": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 20: None, 30: None, 40: None, 50: None, 60: None, 70: None},
    "星期四": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 20: None, 30: None, 40: None, 50: None, 60: None, 70: None},
    "星期五": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 20: None, 30: None, 40: None, 50: None, 60: None, 70: None},
}

def show_schedule():
    print("\n目前的課表：")
    for day, periods in schedule.items():
        print(f"\n{day}：")
        for period in sorted(periods.keys()):
            course = periods[period] if periods[period] else "空堂"
            print(f"  第{period}堂：{course}")

def add_course():
    day = input("請輸入星期幾：")
    if day not in schedule:
        print("輸入錯誤，請重新輸入！")
        return
    try:
        period = int(input("請輸入第幾堂："))
        if period not in schedule[day]:
            print("無效的節數，請輸入 1-70 節！")
            return
        if schedule[day][period]:
            print(f"衝堂！第{period}堂已經有課程：{schedule[day][period]}")
            return
        course_name = input("請輸入課程名稱：")
        schedule[day][period] = course_name
        print(f"已新增課程：{day} 第{period}堂 {course_name}")
    except ValueError:
        print("請輸入有效的數字！")

def delete_course():
    day = input("請輸入星期幾：")
    if day not in schedule:
        print("無效的星期！")
        return
    try:
        period = int(input("請輸入要刪除的堂數："))
        if period not in schedule[day] or not schedule[day][period]:
            print("該堂沒有課程！")
            return
        print(f"已刪除課程：{schedule[day][period]}")
        schedule[day][period] = None
    except ValueError:
        print("請輸入有效的數字！")

def update_course():
    day = input("請輸入星期幾：")
    if day not in schedule:
        print("無效的星期！")
        return
    try:
        period = int(input("請輸入要更新的堂數："))
        if period not in schedule[day] or not schedule[day][period]:
            print("該堂沒有課程！")
            return
        new_course = input("請輸入新課程名稱：")
        print(f"已更新課程：{schedule[day][period]} → {new_course}")
        schedule[day][period] = new_course
    except ValueError:
        print("請輸入有效的數字！")

while True:
    print("\n課表管理系統")
    print("1. 查看課表")
    print("2. 新增課程")
    print("3. 刪除課程")
    print("4. 更新課程")
    print("5. 退出")

    choice = input("請選擇操作（1-5）：")

    if choice == "1":
        show_schedule()
    elif choice == "2":
        add_course()
    elif choice == "3":
        delete_course()
    elif choice == "4":
        update_course()
    elif choice == "5":
        print("再見！")
        break
    else:
        print("輸入錯誤，請重新選擇！")