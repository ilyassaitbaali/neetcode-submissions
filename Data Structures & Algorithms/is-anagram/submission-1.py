# class Solution: # 2 + \(2O(n \log n)\)
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):  #1
#             return False

#         sorted_string_s = ''.join(sorted(s))   #\(O(n \log n)\) #o(n)
#         sorted_string_t = ''.join(sorted(t))  #\(O(n \log n)\) #o(n)

#         if sorted_string_s == sorted_string_t : #1
#             return True  
#         else:
#             return False 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
            
        count_s = {}
        count_t = {}
        
        
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
            
        
        return count_s == count_t   