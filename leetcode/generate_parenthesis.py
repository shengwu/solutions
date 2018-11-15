class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def gen(leftRem, rightRem):
            if leftRem > rightRem: return []
            if rightRem == 1 and leftRem == 0: return [')']
            result = []
            if leftRem > 0:
                for opt in gen(leftRem-1, rightRem):
                    result.append('(' + opt)
            if rightRem > leftRem:
                for opt in gen(leftRem, rightRem-1):
                    result.append(')' + opt)
            return result
        return gen(n, n)


s = Solution()
print s.generateParenthesis(3)
print s.generateParenthesis(10)
print s.generateParenthesis(20)
