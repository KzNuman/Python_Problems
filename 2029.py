# while True:
#     try:

#         volume = float(input())
#         diameter = float(input())
#         n = 3.14

#         redius = diameter/2


#         area =  n*redius*redius
#         hight = volume/area

#         print(f"ALTURA = {hight:.2f}")
#         print(f"AREA = {area:.2f}")

#     except EOFError:
#         break
    






















while True:
    try:

        volume = float(input())
        diameter = float(input())
        n = 3.14


        radius = diameter / 2

        area = n * radius * radius

        height = volume / (n* radius * radius)

        print(f"ALTURA = {height:.2f}")
        print(f"AREA = {area:.2f}")

    except EOFError:
        break

    