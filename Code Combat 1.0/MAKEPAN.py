check="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
for i in range(int(input())):
    s=input()
    s.replace(" ", "")
    count=0
    l=list()
    for j in check:
        if j in s:
            count+=1
        else:
            l.append(j)
    if count == len(check):
        print("YES")
    else:
        print("NO")
        print(*l)
