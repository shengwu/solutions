# this one is slow

from collections import Counter, defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < 1: return ''
        if s == t: return t
        def contains_all(a, b):
            for key in b:
                if key not in a or a[key] < b[key]: return False
            return True
            
        minsize = float('inf')
        min_start = None
        min_end = None
        start = 0
        end = 1
        d = defaultdict(int)
        d[s[0]] = 1
        target = Counter(t)

        while end < len(s):
            while not contains_all(d, target):
                d[s[end]] += 1
                end += 1
                if end >= len(s): break
            while contains_all(d, target):
                d[s[start]] -= 1
                start += 1
            if start == 0: break
            newsize = end - start + 1
            if newsize < minsize:
                minsize = newsize
                min_start = start - 1
                min_end = end

        if min_start is None or min_end is None: return ''
        return s[min_start:min_end]
        
