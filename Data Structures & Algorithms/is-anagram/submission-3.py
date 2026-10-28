class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     return True
        # else :
        #     return False
        s_count = {}
        t_count = {}
        if len(s) != len(t):
            return False

        for cha in s :
            if cha in s_count:
                s_count[cha] += 1 
            else :
                s_count[cha] = 1

        for cha in t:
            if cha in t_count:
                t_count[cha] += 1
            else :
                t_count[cha] = 1
        
        return s_count == t_count 

