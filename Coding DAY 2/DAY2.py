## DAY 2 CODES:-

#Reverse oF Number
no=int(input("Enter no: "))
rev=0
while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10
print("Reverse no is",rev)

#Count number of Digits
#Count number of digits using while loop
no = int(input("Enter number: "))
count = 0
while no > 0:
    no=no//10
    count=count+1
print("Number of digits =", count)

#Sum of Digits
#Sum of digits using while loop
no=int(input("Enter number: "))
sum=0
while no > 0:
    digit=no%10
    sum=sum+digit
    no=no // 10

print("Sum of digits =", sum)

# Check no is Palidrome
no=int(input("Enter no: "))
rev = 0
temp = no

while no > 0:
    rem = no % 10
    rev = rev * 10 + rem
    no = no // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
#Check No is ArmStrong
no=int(input("Enter number: "))
sum=0
temp=no
count=0
while no > 0:
  no=no//10
  count=count+1
while no>0:
    rem=no%10
    sum=sum+rem**count
    no=no//10
if temp==sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")

# Check Armstrong No. From 1 to 100000
# Armstrong numbers from 1 to 100000
for num in range(1, 100001):
    temp = num
    sum = 0
    n = len(str(num))   # number of digits

    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** n
        temp = temp // 10

    if sum == num:
        print(num)



#Peterson Number a number is said to be Peterson if the sum of factorials of each digit is equal to the sum of number itself.Suppose, we have to check the number (n) 145 is Peterson or not.
# Not Solved
