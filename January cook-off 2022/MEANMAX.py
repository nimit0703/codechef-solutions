for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    print(l[n-1] + (sum(l[:n-1])/(n-1)))
