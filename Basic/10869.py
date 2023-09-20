# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
a= int(input())

if a >= 90:
    print("A",end="")
elif a >= 80:
    print("B",end="")
elif a >= 70:
    print("C",end="")
elif a >= 60:
    print("D",end="")
else:
    print("F", end="")