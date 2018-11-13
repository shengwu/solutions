class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # each square contains the number of consecutive 1s seen going right
        right = []
        for row in matrix:
            count = 0
            curr = []
            for item in row:
                if item == '0':
                    count = 0
                else:
                    count += 1
                curr.append(count)
            right.append(curr)
        #print right

        # then evaluate the matrix again
        # let's say we see a 3. if there are 3s in the two entries
        # above it, then it's a square with area 9
        #
        # if we just see a 2 directly above, then at most it's a 2x2 square
        #
        # for n rows and m columns, I think this is O(n^2 m^2)
        # since each spot can scan the entire column. There are O(nm) spots.
        # maybe it's just O(n^2m)

        def max_sq_here(i, j):
            # if we're at a square with 4, we need to look up a max of 4 steps anyway
            # but not past the bounds of the square
            end_pt = max(-1, i-right[i][j]-1)
            # look upwards
            run_len = 0
            max_val = right[i][j]
            max_sq = 0
            for k in range(i, end_pt, -1):
                #print 'coords', i, j, k, run_len, max_val, min(run_len, max_val)**2
                if right[k][j] != 0:
                    run_len += 1
                    # it can only get smaller; otherwise we let the preceding square
                    # handle itself
                    max_val = min(right[k][j], max_val)
                    cand = min(run_len, max_val)**2
                    if cand > max_sq:
                        max_sq = cand
                else:
                    #print ' returning', run_len, max_val, max_sq
                    return max_sq
            #print ' returning', run_len,max_val,  max_sq
            return max_sq

        # NOTE
        # honestly, we could probably store these values to not
        # have to look backwards up the entire column
        #
        # if we look up one cell and it has a 16, we know that there must have been a
        # 4x4 square with lower right corner at the 16
        #
        # if right[i][j] has a 3, and there's a 4 in each of the cells (in this latest matrix)
        # to the left, upwards, and left-upwards, then we must be at the lower
        # right hand corner of a 3x3 square
        # that makes building this last matrix O(nm)
        maxsq = 0
        for i in range(len(matrix)):
            #print
            for j in range(len(matrix[0])):
                ms = max_sq_here(i, j)
                #print  ms,
                curr_max = ms
                if curr_max > maxsq:
                    maxsq = curr_max
        #print
        return maxsq




s = Solution()
sq1 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#print s.maximalSquare(sq1)
assert s.maximalSquare(sq1) == 4


sq = ['11', '11']
assert s.maximalSquare(sq) == 4

sq = ['11', '10']
assert s.maximalSquare(sq) == 1

sq = ['111', '101']
assert s.maximalSquare(sq) == 1

sq = ['011', '011']
assert s.maximalSquare(sq) == 4

sq = ['110', '111']
assert s.maximalSquare(sq) == 4

sq = ['111', '111', '111']
assert s.maximalSquare(sq) == 9

sq = ['111', '101', '111']
assert s.maximalSquare(sq) == 1

sq = ['111', '011', '111']
assert s.maximalSquare(sq) == 4

sq = ['110', '111', '111']
assert s.maximalSquare(sq) == 4

sq = ['1111'] * 4
assert s.maximalSquare(sq) == 16

sq = ['11111'] * 5
assert s.maximalSquare(sq) == 25

sq = ['00000'] * 5
assert s.maximalSquare(sq) == 0

sq = [["0","0","0","1"],
        ["1","1","0","1"],
        ["1","1","1","1"],
        ["0","1","1","1"],
        ["0","1","1","1"]]
assert s.maximalSquare(sq) == 9

sq = [["0","0","0","1"],
        ["1","1","0","1"],
        ["1","1","1","1"],
        ["0","1","1","1"],
        ["0","1","1","0"]]
assert s.maximalSquare(sq) == 4

sq = [["0","0","1","1"],
        ["1","1","1","1"],
        ["1","1","1","1"],
        ["0","1","1","1"],
        ["0","1","1","0"]]
assert s.maximalSquare(sq) == 9

sq = [["1","1","1","1"],
        ["1","1","1","0"],
        ["1","1","1","1"],
        ["0","1","1","1"],
        ["0","1","1","0"]]
assert s.maximalSquare(sq) == 9
