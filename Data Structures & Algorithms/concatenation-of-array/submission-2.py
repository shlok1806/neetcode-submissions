class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums = nums + nums
        # return nums
        ans = []

        for x in range(2):
            for x in nums:
                ans.append(x)
        return ans