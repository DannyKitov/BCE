n = int(input("Enter a number:"))
a = 1
b = 1
c = 0
while True:
    c = a + b
    a = b
    b = c
    if c > n:
        break
    print(c) 
