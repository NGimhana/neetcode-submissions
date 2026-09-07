class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ## nums = [2,3,6,7]
        ## target = 7

        result = []
        
        ## which candidates we are allowed to use i
        def dfs(i, current, total):
            if total == target:
                result.append(current.copy())
                return
            
            if i >= len(nums) or total > target:
                 return
            
            ## include nums[i]
            current.append(nums[i])
            dfs(i, current, total + nums[i])
            
            current.pop()
            ## can't include nums[i], total does not include because did not add anythingl just current combination
            dfs(i+1, current, total)

        dfs(0,[],0)
        return result
