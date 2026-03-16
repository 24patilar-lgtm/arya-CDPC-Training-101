# #DAY 1 CODES :-

# Find Last Digit
no=int(input("Enter value: "))
res=no%25
print (res)

 #Sum of 2 Digit no
no=int(input("Enter value: "))
n1=no%10 #5
n2=no//10 #4
res=n1+n2
print(res)

 #Sum of 3 Digit no
no=int(input("Enter value: "))
n1=no%10 #5
no=no//10; #34
n2=no%10 #34
n3=no//10 #3
res=n1+n2+n3
print(res)

#Sum of 5 digits no
no=int(input("Enter value: "))
n1=no%10 #5
no=no//10; #34
n2=no%10 #34
no=no//10 #3
n3=no%10 #3
no=no//10
n4=no%10
n5=no//10
res=n1+n2+n3+n4+n5;
print(res)

#Reverse of 5 digit no
no=int(input("Enter value: "))
n1=no%10 #5
no=no//10; #34
n2=no%10 #34
no=no//10 #3
n3=no%10 #3
no=no//10
n4=no%10
n5=no//10
res=n1*10000+n2*1000+n3*100+n4*10+n5
print(res)

#Aceept 9 Digit NO. & Find sum of 1st & last digit (in 3 steps)
no = int(input("Enter 9 digit number: "))
last = no%10
first = no//100000000
sum = first+last
print("First digit:", first);
print("Last digit:", last);
print("Sum =", sum);

#Accept Basic Salary and Calculate Gross Salary where
bs=int(input("Enter salary"))
TA=bs * 20 / 100
DA=bs * 30 / 100
HRA=bs * 40 / 100
GS=bs+TA+DA+HRA

#Sum of 9 digit number and Reverse it
no = int(input("Enter value: "))
n1 = no % 10
no = no // 10
n2 = no % 10
no = no // 10
n3 = no % 10
no = no // 10
n4 = no % 10
no = no // 10
n5 = no % 10
no = no // 10
n6 = no % 10
no = no // 10
n7 = no % 10
no = no // 10
n8 = no % 10
n9 = no // 10
sum = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
rev = n1*100000000 + n2*10000000 + n3*1000000 + n4*100000 + n5*10000 + n6*1000 + n7*100 + n8*10 + n9
print("Sum =", sum)
print("Reverse =", rev)
