# n = int(input())

# g = {}

# for _ in range(n):
#     lol,c = map(float, input().split())
#     g[lol] = c

    
# max_key = max(g, key = g.get)

# if c < 8:
#     print("Minimum note not reached")
    
# else:
#     print(int(max_key))

# print(int(max_key))





n = int(input())

m = 0.0

al = 0

while(n > 0):
    n -= 1
    a,b = input().split()
    if float(b) > m:
        m = float(b)
        al = int(a)

if m >= 8:
    print(al)
else:
    print("Minimum note not reached")





















# n = int(input())
# m = 0.0
# al = 0

# while(n > 0):
#     n -= 1
#     a, b = input().split()
#     if float(b) > m:
#         m = float(b)
#         al = int(a)

# if m >= 8:
#     print(al)
# else:
#     print("Minimum note not reached")

























# num_entries = int(input())

# data = {}

# for _ in range(num_entries):
#     key, value = map(int, input().split())
#     data[key] = value


# max_key = max(data, key = data.get)
# print(max_key)