def count_substring(string, sub_string):
    count = 0
    #abcdcdc i = c
    #cd      j = c
    for i in range(len(string)):
        for j in range(len(sub_string)):
            if string[i+j] == sub_string and j==(len(sub_string)-1):
                count = count+1
            if string[i+j]!=sub_string[j]:
                break
        if i==len(string)-len(sub_string):
            break
    return count


string = input().strip()
sub_string = input().strip()    
count = count_substring(string, sub_string)
print(count)