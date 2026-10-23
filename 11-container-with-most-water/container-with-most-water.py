class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        x = 0

        while i < j:
            mn = min(height[i], height[j])
            y = (j - i) * mn

            if y > x:
                x = y

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return x
          