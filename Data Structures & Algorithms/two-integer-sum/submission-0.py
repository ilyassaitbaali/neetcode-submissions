class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for j, val in enumerate(nums):
            num2 = target - val 
            if num2 in num:
                i = num[num2]
                return [i, j] 
            num[val] = j