# ### DAY 7 CODES:-

# # 1 To change profile photo 
L = int(input().strip())
N = int(input().strip())
for _ in range(N):
    W, H = map(int, input().split())
    if W < L or H < L:
        print("UPLOAD ANOTHER")
    elif W == H:
        print("ACCEPTED")
    else:
        print("CROP IT")


# # 2 Monk and Rotation
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    K = K % N  
    result = arr[-K:] + arr[:-K]
    print(*result)


# # 3 Toggle String
S = input()
result = ""

for x in S:
    if x.islower():
        result += x.upper()
    else:
        result += x.lower()

print(result)


# # 4 Array Rotation [Rotate an array to the right by giving no of steps:-]
def rotate_array(arr, n):
    n = n % len(arr)  # handle n > len(arr)
    return arr[-n:] + arr[:-n]

# Example 
arr = [1, 2, 3, 4, 5]

print(rotate_array(arr, 1))  # [5, 1, 2, 3, 4]
print(rotate_array(arr, 2))  # [4, 5, 1, 2, 3]
print(rotate_array(arr, 3))  # [3, 4, 5, 1, 2]

