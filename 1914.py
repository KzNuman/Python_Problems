# x = int(input())
# for i in range(x):

#     aa, bb, cc, dd = input().split()
#     c , d = map(int, input().split())

#     a = c+d

#     if bb[0] == 'P':
#         if a%2==0:
#             print(aa)
#         else:
#             print(cc)

#     else:
#         if a % 2 == 0:
#             print(cc)
#         else:
#             print(aa)
































x = int(input())

for i in range(x):
    
    aa, bb, cc, dd = input().split()
    c , d = map(int,input().split())
    e = c+d

    if bb[0]=='P':
        if e%2 == 0:
            print(aa)
        else:
            print(cc)
    else:
        if e%2 == 0:
            print(cc)
        else:
            print(aa)
    


