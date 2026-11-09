
#定义 5 个变量，分别存整数、小数、字符串、布尔、列表，用 type() 打印类型
A = int
B = float
C = bool
E = list[0,1,2,3,4]
print(type(A), type(B), type(C), type(E))


#用 f-string 输出一行自我介绍（姓名 / 年龄 / 城市），要求冒号对齐、宽度 10
print(f'姓名:{"Ming":<12}' )
print(f'年龄:{"26":<12}')
print(f'城市:{"HangZhou":<12}')
#输入两个数，输出和、差、积、商，结果保留 2 位小数
a = input()
b = input()
A = float(a) + float(b)
B = float(a) - float(b)
C = float(a) * float(b)
D = float(a) / float(b)
print(f'和: {A:.2f} \n差: {B:.2f} \n积: {C:.2f} \n商: {D:.2f}')

#摄氏转华氏，输出格式如 25.0C = 77.0F
tempure_a = input()
tempure_b = float(tempure_a) * 9 / 5 + 32
print(f'{tempure_a}C = {tempure_b}F')

#读一个字符串，输出：长度、首字符、末字符、反转后的字符串
verb = input()
print(f'长度: {len(verb)} \n首字符: {verb[0]} \n末字符: {verb[-1]} \n反转后的字符串: {verb[::-1]}')