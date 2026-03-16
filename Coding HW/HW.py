# Write a program to check whether a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Write a program to find the largest of three numbers.

x= int(input("Enter a number: "))
y= int(input("Enter a number: "))
z= int(input("Enter a number: "))

if x>y>z:
    print("The greatest nmuber is",x)
elif y>x>z:
    print("The greatest nmuber is",y)
else:
   print("The greatest nmuber is",z)


# Check whether a number is positive, negative, or zero.
x=int(input('enter the number'))
if x>0:
    print(x,"is positive number")
elif x<0:
    print(x,"is negative number")
else:
    print("number is zero")



# Write a program to check whether a number is divisible by both 3 and 5.
x=int(input('enter the number'))
if x%3==0 and x%5==0:
     print("The number is divisible by both 3&5")
else: print("The number is not divisible by both 3&5")

 
  
# Write a program to print numbers from 1 to N.
n=int(input('enter the number'))
i=0
for n in  range(n):
    n=n+1
    print(n)


# Write a program to print all even numbers from 1 to N.
n=int(input('enter the number'))
i=0
for n in  range(n):
    n=n+1
    if n%2==0:
        print(n)

# Write a program to calculate the sum of first N natural numbers.

n=int(input('enter the numbers'))
sum=0
for i in range (1,n+1):
    sum=sum+i
print(sum)


# Write a program to calculate the factorial of a number.

n=int(input('enter the numbers'))
fac=1
for i in range(1,n+1):
    fac=fac*i

print("Factorial =", fac)

# Write a program to print the multiplication table of a number.


N=int(input('enter the numbers'))
n=N
t=1
for i in range(1,11):
    n=N*t
    print(N,"*",t,"=",n)
    t=t+1

# Write a program to count the number of digits in a number.
n=int(input('enter the numbers'))
count=0
while (n>0):
    n=n//10
    count=count+1
print(count)


# Write a program to reverse a number.
n=int(input('enter the numbers'))
rev=0
while (n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)



# Write a program to check whether a number is palindrome.

n=int(input('enter the numbers'))
rev=0
temp=n
while (n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if (temp==n):
    print("number is palindrome number")
else:print("number is not palindrome number")

# Write a program to find the sum of digits of a number.
n=int(input('enter the numbers'))
rev=0
sum=0
while (n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)

# Write a program to check whether a number is an Armstrong number.
x=int(input("enter the number"))
sum=0
temp=x
count=0
while x>0:
	
	x=x//10
	count=count+1
x=temp
while x>0:
	rem=x%10
	sum=sum+rem**count
	x=x//10
	
if temp==sum:
    print("number is armstrong number")
else:
    print("number is not armstrong number")

# Write a program to print numbers divisible by 7 between 1 and N.
n=int(input("enter the number"))
for i in range(1,n+1):
    if (i%7==0):
        print(i)