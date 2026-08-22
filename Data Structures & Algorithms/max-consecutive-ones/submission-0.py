class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        max_co = 0
        for num in nums:
            if num == 1:
                count += 1 
                if count > max_co:
                    max_co = count
            else :
                count = 0
        return max_co

 



            

        