#输入分数（0–100），输出等级
score = int(input("请输入分数（0–100）："))
if score < 0 or score > 100:
    print("输入无效，请输入0到100之间的分数。")
if score >= 90:
    print("等级为A")
elif score >= 80:
    print("等级为B")
elif score >= 70:
    print("等级为C")
elif score >= 60:
    print("等级为D")
elif score >= 0:
    print("不合格")
else:
    print("输入无效")

#FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#猜数字游戏
import random
number = random.randint(1, 100)
print("猜数字游戏开始！请在1到100之间猜一个数字。")
for i in range(7):  # 给玩家7次机会
    guess = int(input("请输入你的猜测："))
    if guess < number:
        print("太小了，请再试一次。")
    elif guess > number:
        print("太大了，请再试一次。")
    else:
        print("恭喜你，猜对了！")
        break
else:
    print(f"很遗憾，你没有猜对。正确答案是 {number}。")

#九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i*j}", end="\t")
    print()


#输入一个整数，判断是否是质数
num = int(input("请输入一个整数："))
if num <= 1:
    print(f"{num} 不是质数")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} 不是质数")
            break
    else:
            print(f"{num} 是质数")