class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        ml = len(matrix)
        from_sides = 0
        while from_sides < (ml/2):
            for i in range(from_sides, ml-from_sides-1):
                matrix[from_sides][i], matrix[i][ml-from_sides-1], matrix[ml-from_sides-1][ml-i-1], matrix[ml-i-1][from_sides] = matrix[ml-i-1][from_sides], matrix[from_sides][i], matrix[i][ml-from_sides-1], matrix[ml-from_sides-1][ml-i-1]
            from_sides += 1
