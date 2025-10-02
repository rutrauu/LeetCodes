from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num

        return xor
    
nums = [4,1,2,1,2]
# nums = [2,2,1]
sol = Solution()
print(sol.singleNumber(nums))