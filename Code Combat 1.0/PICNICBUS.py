#error :wrong answer

n,m=map(int,input().split())
s1=set()
count=0
for i in range(m):
    a,b=map(int,input().split())
    if a in s1 or b in s1:
        # count+=1
        s1.add(a)
        s1.add(b)
    else:
        count =count + 1
        s1.add(a)
        s1.add(b)
# print(s1)
print(count)
