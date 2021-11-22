# https://leetcode.com/problems/flood-fill/
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image

        current_color = image[sr][sc]

        if current_color == newColor:
            return image

        def fill(r, c):
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
                return

            if image[r][c] == current_color:
                image[r][c] = newColor
            else:
                return

            fill(r + 1, c)
            fill(r, c + 1)
            fill(r - 1, c)
            fill(r, c - 1)

        fill(sr, sc)

        return image
