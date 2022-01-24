ans=[1,2]
for i in range(250):
    ans.append(ans[len(ans)-1] + 3)
    ans.append(ans[len(ans)-1] + 1)
for i in range(int(input())):
    n=int(input())
    print(*ans[:n])
