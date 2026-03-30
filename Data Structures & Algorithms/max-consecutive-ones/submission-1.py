class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_con=[]
        for i in nums:
            if i == 1:
                count +=1
            else:
                max_con.append(count)
                count = 0
        max_con.append(count)
        result = max(max_con)
        return result