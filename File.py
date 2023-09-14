a=int(input())
b=int(input())

for i in range(a,b+1):
    div = []
    k = 0
    for n in range(1,i+1):
        if i % n ==0:
            k = k+1
            div.append(n)
    if k == 4:
        print(i)
        print(div)


