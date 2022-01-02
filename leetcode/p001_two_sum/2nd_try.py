# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def two_sum_1(self, nums: List[int], target: int) -> List[int]:
        initial_dict = dict()
        for i, v in enumerate(nums):
            if target - v in initial_dict:
                return [initial_dict[target - v], i]

            initial_dict[v] = i
        return None


sol = Solution()
print(sol.two_sum_1([1, 2, 5, 4], 5))
