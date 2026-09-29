class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        var_1 = "".join(sorted(s))
        var_2 = "".join(sorted(t))
        
        if var_1 == var_2:
            return True

        return False