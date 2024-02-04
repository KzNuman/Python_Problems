# cnt = 0

# while True:
#     try:
#         n = int(input())
#         cnt += 1
#         num = 1 + (n * (n+1) // 2)

#         if n == 0:
#             print(f"Caso {cnt}: {num} numero")

#         else:
#             print(f"Caso {cnt}: {num} numeros")

#         print("0", end="")

#         for i in range(1, n+1):
#             for j in range(1, i+1):
#                 print(f" {i}",end="")

#         print("\n")

#     except EOFError:
#         break


























cnt = 0

while True:
    try:
        n = int(input())
        cnt += 1
        num = 1 + (n * (n+1) // 2)

        if n == 0:
            print(f"Caso {cnt}: {num} numero")
        else:
            print(f"Caso {cnt}: {num} numeros")


        print("0",end="")
        

        for i in range(1, n+1):
            for j in range(1, i+1):
                print(f" {i}",end='')


        print("\n")
    except EOFError:
        break