N = int(input("Enter amount of numbers:"))
maxOdd = 1.5
sumEven = 0
if N <= 0:
    print("Not valid count!")
else:
    for i in range(N):
        num = int(input("Enter a number:"))
        if num % 2 == 0:
            sumEven += num
        elif num > maxOdd:
            maxOdd = num 
    print("The sum of the even numbers is:", sumEven)
    if maxOdd == 1.5:
        print("There are no odd numbers")
    else:
        print("The highest odd number is:", maxOdd)
