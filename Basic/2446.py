import sys

a = int(sys.stdin.readline())

for i in range(a):
    print(" "*i+"*"*(2*a-1-2*i))
for i in range(1,a):
    print(" "*(a-i-1)+"*"*(2*i+1))