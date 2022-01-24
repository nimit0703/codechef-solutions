for i in range(int(input())):
    x,y,z=map(int,input().split())
    if y<=x:
        print("PIZZA")
    elif y>x and z<=x:
        print("BURGER")
    else:
        print("NOTHING")
