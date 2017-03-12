def is_palindrome(n):
    return n == n[::-1]

def palindromic_decompositions(n):
    if len(n) == 0:
        return []
    if len(n) == 1:
        return [[n]]
    result = []
    for i in xrange(1, len(n)+1):
        prefix = n[:i]
        if is_palindrome(prefix):
            suffixes = palindromic_decompositions(n[i:])
            if suffixes:
                for suffix in suffixes:
                    result.append([prefix] + suffix)
            else:
                # n[i:] must have been empty
                result.append([prefix])
    return result

print palindromic_decompositions('0204451881')
assert ['020', '44', '5', '1', '88', '1'] in palindromic_decompositions('0204451881')
assert ['020', '44', '5', '1881'] in palindromic_decompositions('0204451881')
