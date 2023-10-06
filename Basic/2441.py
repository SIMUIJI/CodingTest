# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
import sys

a = int(sys.stdin.readline())
for i in range(a):
    print(' '*i+'*'*(a-i))