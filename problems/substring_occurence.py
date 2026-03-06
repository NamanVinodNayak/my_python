a = "uoieabcgaeioughaeiou"
str1 = "aeiou"

temp = list(str1)
count = 0

for char in a:
    if char in temp:
        temp.remove(char)

        if len(temp) == 0:
            count += 1
            temp = list(str1)

    else:
        temp = list(str1)

print(count)