#  DAY 9 CODES:-

# # # # # # class Solution:
def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x

        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x // 10

        if temp == rev:
            print("number is palindrome")
            return True
        else:
            print("number is not palindrome")
            return False







# # # # class Solution:
def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        
        for i in accounts:
            total = 0
            for j in range(len(i)):
                total = total + i[j]
            wealth.append(total)
        
        return max(wealth)




n = int(input())
arr = list(map(int, input().split()))
MOD = 1000000007
result = 1
for num in arr:
    result = (result * num) % MOD

# Output result
print(result)







# # # #!/bin/python3
# # # import sys
# # # #
# # # # Complete the 'miniMaxSum' function below.
# # # #
# # # # The function accepts INTEGER_ARRAY arr as parameter.

def miniMaxSum(arr):
    total = sum(arr)
    
    min_val = min(arr)
    max_val = max(arr)
    
    min_sum = total - max_val
    max_sum = total - min_val
    
    print(min_sum, max_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)









# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# # Complete the 'timeConversion' function below.
# # The function is expected to return a STRING.
# # The function accepts STRING s as parameter.

def timeConversion(s):
    period = s[-2:]          # AM or PM
    time_part = s[:-2]       # hh:mm:ss
    hour = int(time_part[:2])
    
    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    
    return f"{hour:02d}{time_part[2:]}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()










# # #!/bin/python3

# # import math
# # import os
# # import random
# # import re
# # import sys


# # # Complete the 'birthdayCakeCandles' function below.
# # # The function is expected to return an INTEGER.
# # # The function accepts INTEGER_ARRAY candles as parameter.

def birthdayCakeCandles(candles):
    max_height = max(candles)
    count = candles.count(max_height)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()





# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# # Complete the 'timeConversion' function below.
# # The function is expected to return a STRING.
# # The function accepts STRING s as parameter.

def timeConversion(s):
    period = s[-2:]          # AM or PM
    time_part = s[:-2]       # hh:mm:ss
    hour = int(time_part[:2])
    
    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    
    return f"{hour:02d}{time_part[2:]}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()