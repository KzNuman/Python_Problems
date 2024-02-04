# hora = input().split(':')
# n = int(hora[0])*60 + int(hora[1]) - 420
# if n < 0:
#     n = 0
# print('Atraso maximo: %d' % n)






# while True:
#     try:
#         a, c, b = map(int, input().split())

#         A = a - 7
#         B = b

#         if A < 0:
#             print("Atraso maximo: 0")

#         else:
#             print(f"Atraso maximo: {A * 60 + B}")
        
#     except EOFError:
#         break



















while True:
    try:
        a, b = map(int, input().split(':'))

        A = a - 7
        B = b

        if A < 0:
            print("Atraso maximo: 0")
        else:
            print(f"Atraso maximo: {A * 60 + B}")

    except EOFError:
        break


















# hora = input().split(':')
# for _ in range()
# n = int(hora[0])*60 + int(hora[1]) - 420
# if n < 0:
#     n = 0

# print(f"Atraso maximo: %d" % n)