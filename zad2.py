sum = 0
count = 0
count2 = 0
avr = 0
while(1):
    num = int(input("Enter a number:"))
    if num <= 0: 
        break
    count += 1
    if num > 9:
        count2 += 1
    sum += num
if count == 0:
    print("No data!")
else:  
    avr = float(sum / count)  
    print("The sum of the numbers is:", sum)
    print("The doble digit numbers are:", count2)            
    print("The average of the numbers is:", avr)
