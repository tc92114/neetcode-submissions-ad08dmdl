class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      nums.sort()
      for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
          if nums[j] == nums[i]:
            return True
      return False
        