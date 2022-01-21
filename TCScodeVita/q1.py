test = int(input("Enter number of Test Cases"))

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