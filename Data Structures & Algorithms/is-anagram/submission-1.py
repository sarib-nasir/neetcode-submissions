class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # var_1 = "".join(sorted(s)) # this was fast (my solution)
        # var_2 = "".join(sorted(t))
        
        # if var_1 == var_2:
        #     return True
        # return False

        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1+ count_s.get(s[i],0)
            count_t[t[i]] = 1+ count_t.get(t[i],0)
        
        for c in count_s:
            if count_s[c]!= count_t.get(c,0):
                return False
        return True
            
