from collections import defaultdict

# this isn't great
# might be O(p^3)
#
# more efficient: check for diagonals pairwise; check the other two corners
# are in the set of points
# would be O(p^2)

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # get the smallest rectangle with left coordinate at x
        # get the smallest rectangle with bottom coordinate at y
        # search x and y for smallest overall rectangle
        #
        # do you even need to go through y?
        x_sides = sorted(set(pt[0] for pt in points))
        #y_sides = sorted(set(pt[1] for pt in points))
        via_x = defaultdict(set)
        #via_y = defaultdict(set)
        for pt in points:
            via_x[pt[0]].add(pt[1])
            #via_y[pt[1]].add(pt[0])
        smallest_x = {}
        #smallest_y = {}
        for i in range(len(x_sides)-1):
            for j in range(i+1, len(x_sides)):
                x1 = x_sides[i]
                x2 = x_sides[j]
                # any overlap at the other side?
                common = sorted(via_x[x1] & via_x[x2])
                #print x1, x2, common
                if len(common) < 2:
                    continue
                # find the pair with the smallest difference in common
                minpair = []
                mindiff = float('inf')
                for k in range(len(common)-1):
                    if common[k+1] - common[k] < mindiff:
                        mindiff = common[k+1] - common[k] 
                        minpair = [common[k+1], common[k]]
                curr_area = (x2-x1) * abs(minpair[0] - minpair[1])
                if x1 not in smallest_x or curr_area < smallest_x[x1]:
                    smallest_x[x1] = curr_area
        #print smallest_x
        if len(smallest_x.values()) == 0:
            return 0
        return min(smallest_x.values())



s = Solution()
print s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]) == 4
print s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]) == 2
print s.minAreaRect([[0,0],[0,10],[10,10],[10,0]]) == 100
print s.minAreaRect([[0,0],[0,10],[10,10],[10,9]]) == 0
print s.minAreaRect([[0,0],[0,10],[10,10],[10,0],[0,5],[5,5],[5,0]]) == 25
print s.minAreaRect([[0,0],[0,10],[10,10],[10,0],[1,1],[1,5],[5,5],[5,1]]) == 16
