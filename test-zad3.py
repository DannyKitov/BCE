while(1):
    n = int(input("Enter a number:"))
    if n > 0:
        break
m = n
rev = 0
digitSum = 0
while n > 0:
    rev = rev*10 + n%10 
    digitSum += n%10
    n = n//10
print("The sum of the digits is:", digitSum)
print("The reversed number is:", rev)
if rev == m:
    print("The number is palindrom!")
else:
    print("The number is not palinrom!")
