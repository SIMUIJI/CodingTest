import sys

a = int(sys.stdin.readline())

for i in range(1,a+1):
    print("*"*i+" "*2*(a-i)+"*"*i)
for i in range(1,a):
    print("*"*(a-i)+" "*2*i+"*"*(a-i))