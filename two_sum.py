# Two Sum
# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.


from typing import List

class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num 
            if diff in seen :
                return [seen[diff],i]
            seen[num] = i 