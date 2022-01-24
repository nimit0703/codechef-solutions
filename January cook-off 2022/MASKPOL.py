for i in range(int(input())):
    n,a=map(int,input().split())
    na=n-a
    print(min(na,a))
