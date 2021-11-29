from typing import List


class Solution:
    @staticmethod
    def num_islands(grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0

        def _explode(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]) or grid[x][y] == '0':
                return

            grid[x][y] = '0'
            _explode(x + 1, y)
            _explode(x - 1, y)
            _explode(x, y + 1)
            _explode(x, y - 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                c = grid[i][j]
                if c == '0':
                    continue

                count += 1
                _explode(i, j)

        return count