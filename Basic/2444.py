import sys

a = int(sys.stdin.readline())

for i in range(a):
    print(" "*(a-1-i)+"*"*(2*(i+1)-1))

for i in range(1,a):
    print(" "*i+"*"*(2*(a-i)-1))