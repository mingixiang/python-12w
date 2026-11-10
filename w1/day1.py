
#定义 5 个变量，分别存整数、小数、字符串、布尔、列表，用 type() 打印类型
A = 4
B = 3.14
C = False
D = "Hello"
E = [0,1,2,3,4]
print(type(A), type(B), type(C),type(D), type(E))


#用 f-string 输出一行自我介绍（姓名 / 年龄 / 城市），要求冒号对齐、宽度 10
print(f'姓名:{"Ming":<10}' )
print(f'年龄:{"26":<10}')
print(f'城市:{"HangZhou":<10}')


#输入两个数，输出和、差、积、商，结果保留 2 位小数
a = float(input())
b = float(input())
print(f'和: {a + b:.2f}')
print(f'差: {a - b:.2f}')
if b == 0:
    print("商不能为0")
else:
    print(f'商: {a / b:.2f}')
print(f'积: {a * b:.2f}')

#摄氏转华氏，输出格式如 25.0C = 77.0F
tempure_a = float(input())
tempure_b = tempure_a * 9 / 5 + 32
print(f'{tempure_a:.1f}C = {tempure_b:.1f}F')

#读一个字符串，输出：长度、首字符、末字符、反转后的字符串
verb = input()
if verb == "":
    print("输入为空")
else:
    print(f'长度: {len(verb)} \n首字符: {verb[0]} \n末字符: {verb[-1]} \n反转后的字符串: {verb[::-1]}')