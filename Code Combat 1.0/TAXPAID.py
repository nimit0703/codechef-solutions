for i in range(int(input())):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    print(int(n*(m*(m+1)/2))%1000000007)
