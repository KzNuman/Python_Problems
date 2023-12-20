# i = 3

# while i > 0:
#     print(i)
#     i -= 1


# i = 5
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("Displayed Successfully!")




n = int(input("Please enter the number of layers...."))
i = 1

while i <= n:
    j = 1
    while j <= n - i:
        print(".",end="")
        j = j + 1
    j = 1
    while j <= 2*i - 1:
        print("*",end="")
        j = j + 1
    print()
    i = i + 1
    