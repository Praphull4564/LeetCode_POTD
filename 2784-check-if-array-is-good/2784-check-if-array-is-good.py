class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        nums.sort()

        for i in range(len(nums)):
            if i!=len(nums)-1:
                if i+1 != nums[i]:
                    return False

            else:
                if i!=nums[i]:
                    return False
        
        return True
