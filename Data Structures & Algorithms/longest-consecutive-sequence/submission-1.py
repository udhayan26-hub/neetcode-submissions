class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        lon = 1
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                count += 1
            else:
                lon = max(lon, count)
                count = 1
        lon = max(lon, count)
        return lon        

        
        
        