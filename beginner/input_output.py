# input & output

greet = input("What your name? ")
print(greet)

age = int(input("What your age? "))
age_abs = abs(age)

# String concatentaion
print("Nice to meet you "+greet + str(age))

# formated stringn

print(f"Name : {greet} age: {age_abs}")