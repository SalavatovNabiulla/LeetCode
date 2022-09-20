from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index,value in enumerate(nums):
            x = target - value
            temp = nums.copy()
            temp.remove(temp[index])
            if x in temp:
                return [index,temp.index(x)+1]

obj = Solution()
answer = obj.twoSum([2,7,11,15],9)
print(answer)