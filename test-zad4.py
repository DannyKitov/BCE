a = int(input("a="))
b = int(input("b="))
if a and b <=0:
    print("Invalid numbers")
else:
    nok = 0
    nod = 0
    a1 = a
    b1 = b
    while(b != 0):
        temp = b
        b = a % b
        a = temp
    nod = a 
    nok = (a1*b1)//nod
    print("NOD:", nod)
    print("NOK:", nok)
    if nod == 1:
        print("Vzaimno prosti!")
    else:
        print("Ne sa vzaimno prosti!")    
