class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0 :
            return True 
        elif x < 0 or x % 10 == 0 :
            return False 
        
        
        rev_str = int(str(x)[::-1])

        return rev_str == x
      
        


     