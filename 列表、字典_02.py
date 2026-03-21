# 定义施工机械列表（含重复）
machinery_list = ["挖掘机", "推土机", "装载机", "挖掘机", "推土机", "挖掘机"]

# 方法1：字典统计每种机械数量
machinery_count = {}
for machine in machinery_list:
    if machine in machinery_count:
        machinery_count[machine] += 1
    else:
        machinery_count[machine] = 1

print("施工机械数量统计（方法1）:")
for machine, count in machinery_count.items():
    print(f"{machine}: {count} 台")

# 方法2：使用 dict.get 简洁统计
machinery_count2 = {}
for machine in machinery_list:
    machinery_count2[machine] = machinery_count2.get(machine, 0) + 1      #有点难懂，问ai理解

print("\n施工机械数量统计（方法2）:")
for machine, count in machinery_count2.items():
    print(f"{machine}: {count} 台")

# 使用集合查看不同机械类型（去重）
unique_machinery = set(machinery_list)
print("\n施工机械种类（去重）:", unique_machinery)
