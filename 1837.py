a, b = map(int, input().split())

quotient = 0
reminder = 0

for r in range(abs(b)):
    q = (a - r) // b
    if a == b * q + r:
        quotient = q
        reminder = r
        break

print(f"{quotient} {reminder}")




























# a, b = map(int, input().split())

# quotient = 0
# reminder = 0

# for r in range(abs(b)):
#     q = (a - r) // b
#     if a == b * q + r:
#         quotient = q
#         reminder = r
#         break

# print(f"{quotient} {reminder}")
