def merge_sorted_list_without_duplicate(list1, list2):
    i, j = 0, 0
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            result.append(list2[j])
            j += 1
        else:  # equal case → avoid duplicate
            result.append(list1[i])
            i += 1
            j += 1

    # Add remaining elements (if any)
    result.extend(list1[i:])
    result.extend(list2[j:])

    return result

list1 = [1, 2, 3, 5]
list2 = [2, 3, 4, 6]

merged_list = merge_sorted_list_without_duplicate(list1, list2)
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]


