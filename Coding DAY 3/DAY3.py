#nested loop 
#inner loop for rows
#outer loop for rows
    #j1 j2 j3 j4
#i=1 1   1  1  1
#i=2 2   2  2  2
#i=3 3   3  3  3
#i=4 4   4  4  4
#---------------
#i=3 j=4
#o/p
# 1111
# 2222
# 3333
# 4444
for i in range(1,5):
    for j in range(1,5):
        print(j,end="")
    print()


#2    o/p
n=65
for i in range(1,5):
    for j in range(1,5):
        print(chr(n),end="")
        n=n+1
    print()

#ascii values
    #A-65 a=97
    #B=66 b=98
    #C=67 c=99
    

#3 
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()

#4
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end="")
    print()

#5
for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()


#LISTS
ls=[]
print(type(ls))
print(ls)

#4
ls=[12,3,4,55,77,99]
print(ls)


#5    
ls=[12,3,4,55,77,99]
print(ls)
for i in range(len(ls)):
    print(ls[i])


#6
ls=[12,3,4,55,77,99]
print(ls)
for i in range(len(ls)):
    print(ls[i])
for i in ls:
    print(i)

#7
ls=[12,3,4,55,77,99]
print(ls)
ls.append(66)
ls.append(69)
ls[7]=99
print(ls)


#8
ls=[12,3,4,55,77,99]
print(ls)
ls.append(66)
ls.pop(3)
print(ls)
  
#9
ls=[12,3,4,55,77,99]
print(ls)
print(ls[4])
print(ls[0])
print(ls[-1])

#10    [: means Slicing]
ls=[12,3,4,55,77,99,66,48,40,15]
print(ls[1:5])
print(ls[0:4])
print(ls[4:])
print(ls[:5])
print(ls[:])
print(ls[::])
print(ls[0:4:7])
print(ls[4:5:2])
print(ls[::-1])

#11
s="arya"
print(s)
print(s[3])
print(s[::-1])


  #CDPC TRAINING folder 
        #DAY1
        #DAY2
        #DAY3