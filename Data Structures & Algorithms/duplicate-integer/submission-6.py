class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = []
        seen = set()
        # duplicate_bool = False
        for i, value in enumerate(nums):
            if value in seen:
                return True
            # seen.append(nums[i])
            seen.add(nums[i])
        return False

