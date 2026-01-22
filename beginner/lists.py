color = ["red","black","orange"]

print(color)

print("Index**************")
print(color[1])
print(color[0])

print("Pop**************")
print(color.pop(1))

print("Append**************")
color.append("Blue")
print(color)
color.append(1)
print(color)

print("Remove**************")
color.remove(1)
print(color)
color.remove("Blue")
print(color)

print("Insert**************")
color.insert(2, "Yellow")
print(color)

print("Slicing**************")
print(color[0:2])
print(color[0:1])

print("Sort**************")
rnum = num = [1,56,552,52,46,64614,674,6545,165,4654,64,163,54,154,4,64,61,5]
print(num)
num.sort()
print(num)
rnum.sort(reverse=True)
print(rnum)

print("Copy**************")
new_num = num.copy()
print(new_num)

print("Copy**************")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

print("Comprehension**************")
#newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "b" in x:
    newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]



print(newlist)

print(newlist)