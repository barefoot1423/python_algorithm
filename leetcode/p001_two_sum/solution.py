# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = dict()
        for i, x in enumerate(nums):
            if target - x in index_map:
                return [index_map[target-x], i]

            index_map[x] = i

        return None


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([1,2,3,1,4,7,2,3], 11))