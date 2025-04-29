import random

number = random.randint(1, 10)

guess = 0

count = 0

while True:
    guess = int(input("猜猜看是多少？(1-10): "))
    if guess == number:
        print("恭喜你猜中了！") 
        count += 1
        print(f"你總共猜了{count}次")
        print(f"命中率為{100//count}%")
        break
    elif guess < number:
        print("猜大一點") 
        count += 1
    else:
        print("猜小一點") 
        count += 1