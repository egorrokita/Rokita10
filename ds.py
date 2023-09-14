i = int(input())
binar = bin(i)
binar = str(binar)
binar = "".join(binar.split("0",1))
binar = "".join(binar.split("b",2))
leng = len(binar)
if i % 3 == 0:
    binar1 = binar + binar[leng-3]
    binar2 = binar1 + binar[leng - 2]
    binar3 = binar2 + binar[leng-1]
    bres = int(binar3)
if i % 3 != 0:
    ost = bin(i%3*3)
    print(ost)


