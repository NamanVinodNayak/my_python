list1 = [10, -1, 5, 0, -3, 8]

largest = float('-inf')

for num in list1:
    largest = max(largest, num)

print(f"The largest element in the array is: {largest}")