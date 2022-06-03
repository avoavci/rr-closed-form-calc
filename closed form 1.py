za0 = input("input a0 ")
zan1 = input("input an1 ")
zan2 = input("input an2 ")
a0 = int(za0)
an1 = int(zan1)
an2 = int(zan2)
if a0 == 1: 
    print("1")
else:
    a1 = an1 * a0 + an2
    b0 = a1 - a0
    an3 = "x " + str(an1) + "^n"
    bn = b0 + an1
    an4 = an1 - 1
    an5 = (b0 / an4)
    an6 = str(an5)
    an7 = (an2 / an4)
    an8 = str(an7)
    if an7 >= 0:
        an9 = " - "
    else:
        an9 = " + "
    an10 = an6 + " " + an3 + an9 + an8
    print(an10)
