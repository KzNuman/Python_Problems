decimel = int(input())

hexa = ""

while decimel > 0:
    mod = decimel % 16
    decimel //= 16

    if mod <=9:
        hexa += str(mod)
    else:
        hexa += chr(ord('A')+ mod - 10)
    
hexa = hexa[::-1]
print(hexa)
        

