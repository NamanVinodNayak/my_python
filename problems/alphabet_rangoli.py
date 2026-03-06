import string
# 3 -> 9 -> 3*4 -3
# 5 -> 17 -> 5*4 -3

def alphabet_rangoli(size):
    alpha = string.ascii_lowercase
    total_width = (size*4)-3
    first_half=[]
    
    for i in range(size):
        left_side = "-".join(alpha[size-1:i:-1])
        right_side = "-".join(alpha[i:size])
        row = left_side+("-" if left_side else "") + right_side
        new=row.center(total_width,"-")
        first_half.append(new)
    
    pattern = first_half[::-1] + first_half
    my_pattern = "\n".join(pattern)
    print(my_pattern)
    
    
n = 5
alphabet_rangoli(n)