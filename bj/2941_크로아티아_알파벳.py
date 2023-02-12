raw_data = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
word_cnt = 0

index = 0

while index < len(word):
    if word[index:index+2] in raw_data:
        index+=1
    if word[index:index+3] in raw_data:
        index +=2
    word_cnt+=1
    index+=1

print(word_cnt)