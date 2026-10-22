class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [ch.lower() for ch in s if ch.isalnum()]
        rev_str = s_list[::-1]
        if s_list == rev_str:
            return True 
        else :
            return False 


        