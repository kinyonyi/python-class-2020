#list
info = ["david","david","micheal", 1, 2, 3]
second_list = ["cows","goats","buffallo"]
print(info)
#string methods
info.append("isaac")
print(info)
info.insert(0,"name 1")
print(info)
indexed = info.index("micheal")
print(indexed)
info.pop()
print(info)
info.pop(indexed)
print(info)
list2 = info + second_list
info.extend(second_list)
print(info)
print(list2)
print(info.count("david"))
copied = info.copy()
print(copied)
sorted_list = sorted(second_list)
print(sorted_list)
sorted_reversed = sorted(second_list, reverse=True)
print(sorted_reversed)
info.clear()
print(info)

length = len(sorted_list) - 1
new_list = []
while length >= 0:
    new_list.append(sorted_list[length])
    length -= 1
print(new_list)

name = "i am going to school, i was sick"
list_names = ["ivan was sick","isaac","david"]
