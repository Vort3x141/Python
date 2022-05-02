def mutate_string(string, position, character):
    final_string = ""
    split_list = []
    for char in string:
        split_list.append(char)
    split_list[position] = character
    final_string ="".join(split_list)
    return final_string


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)