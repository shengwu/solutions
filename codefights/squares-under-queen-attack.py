def squaresUnderQueenAttack(n, queens, queries):
    # O(n) memory
    x = set()
    y = set()
    upper_diag = set()
    lower_diag = set()

    # O(|queens|) time
    for queen in queens:
        x.add(queen[0])
        y.add(queen[1])
        upper_diag.add(queen[1] + queen[0])
        lower_diag.add(queen[1] - queen[0])

    # O(|queries|) time
    result = []
    for query in queries:
        result.append(query[0] in x or
                      query[1] in y or
                      (query[1] + query[0]) in upper_diag or
                      (query[1] - query[0] in lower_diag))

    return result
