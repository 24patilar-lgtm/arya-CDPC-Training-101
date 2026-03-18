# DAY 8 CODES:-


# 
class Student:
    a=10
    def showA(self):   #instance function
        print("Im in showA")
    def showB(a):
        print("Im in showA")

if __name__ == '__main__':
    obj=Student()
    obj.showA(11,22)
    Student.showB(22)

# 1 Two sums
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            
# 2
# Given an integer n, return a string array answer (1-indexed) where:
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        
        return result


# 3
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums


        
