class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums != list(set(nums)):
          return True 
        else:
          return False