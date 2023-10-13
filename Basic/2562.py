import sys

max = 0
count = 0
for i in range(9):
    a = int(sys.stdin.readline())
    if a > max:
        max = a
        count = i+1
print(max)
print(count)