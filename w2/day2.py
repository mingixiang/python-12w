#10 个数字的列表：最大、最小、总和、平均
numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6, 0]
maximum = max(numbers)
minimum = min(numbers)
total = sum(numbers)
average = total / len(numbers)
print(f'最大值: {maximum}, 最小值: {minimum}, 总和: {total}, 平均值: {average:.2f}')

#切片：前 3、后 3、中间 4、整体反转
first_three = numbers[:3]
last_three = numbers[-3:]
middle_four = numbers[3:7]
reversed_numbers = numbers[::-1]
print("reversed_numbers:", reversed_numbers)

# append / insert / remove / pop / index / sort / reverse 各用一次
numbers.append(10)  # append: 在列表末尾添加元素
numbers.insert(0, -1)  # insert: 在指定位置插入元素
numbers.remove(5)  # remove: 删除指定元素
numbers.pop()  # pop: 删除并返回最后一个元素
index = numbers.index(3)  # index: 获取元素的索引
numbers.sort()  # sort: 对列表进行排序
numbers.reverse()  # reverse: 反转列表
print("numbers:", numbers)
print("index of 3:", index)
print("first three:", first_three)
print("last three:", last_three)
print("middle four:", middle_four)
print("reversed_numbers:", reversed_numbers)

#列表推导式：1–20 的平方，只保留偶数
squares = [x * x for x in range(2, 21, 2) ]
print("squares:", squares)

#两个列表合并、去重、排序
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
combined = list1 + list2
unique = list(set(combined))
unique.sort()
print("unique:", unique)