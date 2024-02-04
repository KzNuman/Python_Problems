n = int(input())
s = 0.0
for _ in range(n):
    a,b = map(int,input().split())
    
    if a == 1001:
        a = 1.50
    if a == 1002:
        a = 2.50
    if a == 1003:
        a = 3.50
    if a == 1004:
        a = 4.50
    if a == 1005:
        a = 5.50
    s = s+a*b


print(f"{s:.2f}")
