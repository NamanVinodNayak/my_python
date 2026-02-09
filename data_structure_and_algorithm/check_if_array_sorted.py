list1 = [1,2,3,4,5,7,8]
n = len(list1)
mark = True
for i in range(0,n-1):
    if list1[i] > list1[i+1]:
        mark = False

print(mark)