a=int(input())
b=int(input())
for i in range(a,b+1):
    print(i)
    if(i%2==0):
        c=i**0.5
        d=int(c)
        if(d*d)==i:
            break
