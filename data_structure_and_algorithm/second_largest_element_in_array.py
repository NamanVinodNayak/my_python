list1 = [10, -1, 5, 0, -3, 8]

largest = float('-inf')
second_largest = float('-inf')

for i in list1:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print(f"The second largest element in the array is: {second_largest}")