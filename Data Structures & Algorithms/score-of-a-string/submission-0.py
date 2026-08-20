class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0 #O(1)
        for i in range(len(s) - 1): #O(n)
            a = ord(s[i]) #O(1)
            b = ord(s[i+1]) #O(1)            ==> O(n)

            diff = abs(a - b) #O(1)
            score = score + diff #O(1)
        return score 



            #s = code 
            #a = c= 11
            #b = o = 12 





