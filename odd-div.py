n = int(input("Enter a number:"))
div = 1
while div < n:
    if n % div == 0:
        print(div)
    div += 2
