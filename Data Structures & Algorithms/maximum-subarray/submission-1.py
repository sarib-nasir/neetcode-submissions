class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_num = 0
        # if len(nums) == 1:
        #     return nums[0]
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         # print(nums[i],nums[j])
        #         max_num = max(nums[i]+nums[j], max_num )
        # # print(max_num) 
        # return max_num

        max_sum = nums[0]
        current = 0

        for i in nums:
            if current < 0:
                current = 0
            current += i
            max_sum = max(max_sum, current )
        return max_sum
