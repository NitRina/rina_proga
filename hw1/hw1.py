a=int(input())
b=int(input())
c=int(input())
if a%b==c and a*c+b==0:
    print("c - остаток a/b; c - решение уравнения ax+b=0")
elif a%b==c and a*c+b!=0:
    print("c - остаток a/b; c - не решение уравнения ax+b=0")
elif a%b!=c and a*c+b==0:
    print("c - не остаток a/b; c - решение уравнения ax+b=0")
else:
    print("c - не остаток a/b; c - не решение уравнения ax+b=0")
