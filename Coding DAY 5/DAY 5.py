#DAY 5 CODES:-
# # # #accept 4 numbers anf find max numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
max = a
if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d
print("Maximum number is:", max)


# # #Find minimum and maximum element
arr=[5,3,2,7]
max = arr[0]
for i in range(1,len(arr)):
    if max<arr[i]:
        max=arr[i]

print(max)

arr=[5,3,2,7]
min = arr[0]
for i in range(1,len(arr)):
    if min>arr[i]:
        min=arr[i]

print(min)

# #CHECK LEAP YEAR
year=int(input("Enter year:"))
if year%100!=0:
    if year%4==0:
        print("Non century leap year")
    else:
        print("Not leap year")
else:
    if year%400==0:
        print("century leap year")
    else:
        print("Not leap year")


#FIND LARGEST
no=2025
n1=no%100
n2=no//100
sum=n1+n2
sq=sum**2
if sq==no:
    print("tech no")
else:
    print("not tech no")
