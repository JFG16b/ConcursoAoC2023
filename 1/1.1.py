with open('input1.1.txt', 'r') as f:
    word_list = f.readlines()
result = 0
digit_1 = 0
digit_2 = 0
for i in range(len(word_list)):
    k = len(word_list[i]) -1
    x = 0
    for j in range(len(word_list[i])):
        try:
            digit_1 = str(int(word_list[i][x]))
        except ValueError:
            x += 1
        try:
            digit_2 = str(int(word_list[i][k]))
        except ValueError:
            k -= 1
    result += int(digit_1+digit_2)
print(digit_1)
print(digit_2)     
print(result)      

