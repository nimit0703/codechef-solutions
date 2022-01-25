s=input()
for i in range(int(input())):
    n=int(input())
    c=s[n-1]
    print(s[:n-1].count(c))
