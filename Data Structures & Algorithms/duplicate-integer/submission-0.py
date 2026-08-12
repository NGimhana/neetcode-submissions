class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums.sort()
        length = len(nums)
        for i in range(0,length-1):
            if nums[i] == nums[i+1]:
                return True
        return False

