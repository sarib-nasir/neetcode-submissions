class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l +=1
            while l < r and not s[r].isalnum():
                r -=1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

        # s = s.replace(" ","")
        # s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        # i , j = 0, len(s)-1
        # while i < j:                         
        #     if s[i] != s[j]:
        #         return False
        #     i +=1
        #     j -=1
        # return True
