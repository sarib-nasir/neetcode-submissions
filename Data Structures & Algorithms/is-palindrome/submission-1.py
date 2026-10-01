class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        i = 0
        j = len(s)-1
        while i <= len(s):            
            while j >= 0:                
                if  s[i] != s[j]:
                    return False
                else :
                    i +=1
                    j -=1
            return True
