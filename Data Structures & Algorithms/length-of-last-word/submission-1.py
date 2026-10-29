class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lenght = 0
        i = len(s)-1

        while i >= 0 :
            if s[i] == " ":
                if lenght > 0 :
                    break
                i = i -1
            elif s[i] != " ":
                lenght += 1
                i = i -1 
        return lenght 