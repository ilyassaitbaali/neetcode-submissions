class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0 
        i = len(s)-1

        while i >= 0 :
            if s[i] == " " :
                if length > 0:
                    break   
                i = i - 1
            elif s[i] != " ":
                length += 1 
                i -= 1
            
        return length 




        