class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        rst = []
        for i in nums:
            rst.append(i)
        for i in nums:
            rst.append(i)
        return rst

