class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #solution 1 :
        # if sorted(s) == sorted(t):
        #     return True
        # else :
        #     return False

        #solution 2 :
        if len(s) != len(t):
            return False 
        s_count={}
        t_count={}

        for cha in s:
            if cha in s_count:
                s_count[cha] += 1 
            else:
                s_count[cha]= 1

        for cha in t:
            if cha in t_count:
                t_count[cha] += 1
            else:
                t_count[cha] = 1
        
        if t_count == s_count :
            return True 
        else :
            return False 


  
