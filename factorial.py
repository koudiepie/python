#有bug，遇到小數點會爆掉
number = (input("請輸入數字: "))

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print(f"{number} 的階乘是: {factorial(number)}")