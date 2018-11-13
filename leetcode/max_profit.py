class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minsofar = float('inf')
        maxprofit = 0
        for p in prices:
            if p < minsofar:
                minsofar = p
            if p - minsofar > maxprofit:
                maxprofit = p - minsofar
        return maxprofit



s = Solution()
assert s.maxProfit([7,1,5,3,6,4]) == 5
assert s.maxProfit([7,6, 4, 3, 1]) == 0
assert s.maxProfit([1, 2, 3, 4, 5]) == 4
assert s.maxProfit([1, 5, 3, 4, 9]) == 8
assert s.maxProfit([1, 5, 3, 4, 9, 8, 7, 6]) == 8
assert s.maxProfit([]) == 0
assert s.maxProfit([1]) == 0
assert s.maxProfit([1, 2]) == 1
assert s.maxProfit([2, 1]) == 0


