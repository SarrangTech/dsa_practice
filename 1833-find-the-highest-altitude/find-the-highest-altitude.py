class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        j = 1
        mx = max(0, gain[0])
        x = gain[0]

        while j < len(gain):
            x = x + gain[j]

            if x > mx:
                mx = x

            j += 1

        return mx
        