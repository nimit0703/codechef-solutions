#time limit problem
for i in range(int(input())):
    lower_value, upper_value=map(int,input().split())
    sum1=0
    for number in range (lower_value, upper_value + 1):  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            sum1+=number
    print(sum1)
