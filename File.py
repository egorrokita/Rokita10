a=int(input())
b=int(input())

for i in range(a,b+1):
    k = 0
    for n in range(1,a+1):
        if a % n ==0:
            k = k+1
    a=a+1
    if k == 4:
        div=[]
        x = 0
        print(i)
        for x in range(1,i+1):
            if i % x ==0:
                div.append(x)
        x = x + 1
        print(div)


