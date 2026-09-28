class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        duplicate_bool = False
        for i, value in enumerate(nums):
            if value in seen:
                return True
            else:
                seen.append(nums[i])
        
        return duplicate_bool