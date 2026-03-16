# # # DAY 6 CODES:-

# 1 
# Complete the 'compareTriplets' function below.
def compareTriplets(a, b):
    alice = 0
    bob = 0

    for i in range(3):
        if a[i] > b[i]:
           alice += 1
        elif a[i] < b[i]:
            bob += 1
    return [alice,bob]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# 2
# Complete the 'aVeryBigSum' function below.
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
def aVeryBigSum(ar):
    total = 0
    for i in ar:
        total += i
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

# # # #
# n=int(input())
# ------------
# a=int(input())
# b=int(input())
# -------------
# a,b=map(int,input().split())
# --------------
# a,b,c=map(int,input().split())
# -----------------------
# arr=list(map(int,input().split))
# -----------------------
# arr=eva1(input())

# 3
# Complete the 'diagonalDifference' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
def diagonalDifference(arr):
    n = len(arr)
    sum1 = 0
    sum2 = 0
    
    for i in range(n):
        sum1 += arr[i][i]
        sum2 += arr[i][n-i-1]
    
    return abs(sum1 - sum2)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# 4
# Complete the 'plusMinus' function below.
def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zero = 0
    
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1

    print(pos/n)
    print(neg/n)
    print(zero/n)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)




