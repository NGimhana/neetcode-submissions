class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums: # O(n)
            if num in hashmap: # O(1)
                hashmap[num] = hashmap[num] + 1 # O(1)
            else:
                hashmap[num] =  1 # O(1)
        for key in hashmap: # O(n)
            if hashmap[key] > 1: # O(1)
                return True # O(1)
        return False # O(1)
        