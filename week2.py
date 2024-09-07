my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
# [10,20,30,40]

my_list.insert(2, 15)
print(my_list)
# [10, 20, 15, 30, 40]
my_list.extend([50, 60, 70])
print(my_list)
# [10, 20, 15, 30, 30, 40, 50, 60, 70]
my_list.pop()
print(my_list) # [10, 20, 15, 30, 40, 50, 60]

my_list.sort()
print(my_list) 
# [10, 15, 20, 30, 40, 50, 60]

print(my_list.index(30)) # 3
