
li = [ i+1 for i in range(20)]

for _ in range(10):
    a,b = map(int,input().split(" "))
    li1 = li[:a-1]
    li2 = li[b:]
    li3 = li[a-1:b][::-1]
    li = li1+li3+li2

for i in li:
    print(i, end=" ")