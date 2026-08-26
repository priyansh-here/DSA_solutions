class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = ans = 0

        for x in gain:
            curr += x
            ans = max(ans, curr)

        return ans