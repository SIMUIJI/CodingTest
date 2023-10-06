import sys

a = int(sys.stdin.readline())

for _ in range(a):
    m, n = map(int, sys.stdin.readline().split())
    print(m+n)