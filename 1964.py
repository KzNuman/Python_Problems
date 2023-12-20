tst = int(input())

while tst > 0:
    dif = int(input())

    if dif < 2015:
        year = 2015 - dif
        print(f"{year} D.C.")
    else:
        year = dif - 2014
        print(f"{year} A.C.")

    tst -= 1