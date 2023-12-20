n = float(input())
ar = "{:E}".format(n)

if ar[0] != '-':
    print("+",end='')

print("{:.4E}".format(n))