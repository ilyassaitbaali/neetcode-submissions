class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0 :
            return True 
        elif x < 0 or x % 10 == 0 :
            return False 
        
        
        rev_str = int(str(x)[::-1])

        if rev_str == x:
            return True
        else :
            return False
        


     