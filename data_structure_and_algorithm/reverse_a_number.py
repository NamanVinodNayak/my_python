num =int(input("Enter a number: "))
rev=0
new_num = num
while(new_num>0):
    temp=new_num%10
    rev=rev*10+temp
    new_num=new_num//10

print(f"Original Number : {num}")
print(f"Reversed number is: {rev}")