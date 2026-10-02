class Solution:
    def isValid(self, s: str) -> bool:
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        # return s == ''


        stack = []
        bracket_hashmap = { "]":"[", "}":"{", ")":"("}

        for i in s:
            if i in bracket_hashmap:
                if stack and stack[-1] == bracket_hashmap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False
            
        