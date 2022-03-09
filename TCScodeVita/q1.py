#LEXI_STRING
#P is dictionary
#S is sub string to find according to dict p

test = int(input())

while (test>0):
    p = input()
    s = input()

    list = []
    for i in s:
        list.append(p.find(i))

    list.sort()
    for i in list:
        print(p[i], end = "")
    if test>1:
        print()
    test -=1