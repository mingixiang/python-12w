#「城市 → 人口」字典，遍历打印
city_population = {
    "北京": 21540000,
    "上海": 24280000,
    "广州": 15300000,
    "深圳": 17560000
}

for city, population in city_population.items():
    print(f"{city}: {population}")

#统计一句话里每个字符出现的次数
sentence = "hello world"
for char in sentence:
    count = sentence.count(char)
    print(f"'{char}': {count}")

#嵌套字典：3 个学生 × 3 门课，算每人平均分
students_scores = {
    "Alice": {"Math": 90, "English": 85, "Science": 92},
    "Bob": {"Math": 78, "English": 82, "Science": 88},
    "Charlie": {"Math": 95, "English": 90, "Science": 94}
}

for student, subjects in students_scores.items():
    total = sum(subjects.values())
    average = total / len(subjects)
    print(f"{student}: {average:.2f}")

#按分数排序输出前 3 名
top_students = sorted(students_scores.items(), key=lambda x: sum(x[1].values()) / len(x[1]), reverse=True)[:3]
print("前 3 名学生:")
for student, _ in top_students:
    print(student)

#合并两个字典，重复的 key 求和
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
merged_dict = dict1.copy()
for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] += value
    else:
        merged_dict[key] = value
print(merged_dict)