example_inp = '''
Before: [3, 1, 2, 0]
5 1 2 0
After:  [0, 1, 2, 0]

Before: [3, 3, 0, 2]
10 2 0 1
After:  [3, 0, 0, 2]

Before: [3, 3, 1, 1]
7 3 3 3
After:  [3, 3, 1, 0]

Before: [1, 3, 2, 0]
8 0 2 2
After:  [1, 3, 0, 0]

Before: [3, 0, 0, 2]
12 2 3 2
After:  [3, 0, 1, 2]

Before: [0, 3, 1, 1]
1 2 3 1
After:  [0, 2, 1, 1]

Before: [1, 1, 0, 2]
2 0 2 2
After:  [1, 1, 0, 2]

Before: [3, 1, 3, 3]
0 1 2 0
After:  [0, 1, 3, 3]

Before: [3, 0, 2, 1]
10 1 0 3
After:  [3, 0, 2, 0]

Before: [2, 1, 3, 0]
14 0 3 0
After:  [1, 1, 3, 0]

Before: [1, 0, 0, 3]
2 0 2 1
After:  [1, 0, 0, 3]

Before: [2, 1, 3, 0]
0 1 2 3
After:  [2, 1, 3, 0]

Before: [2, 1, 0, 0]
14 0 3 0
After:  [1, 1, 0, 0]

Before: [2, 1, 2, 1]
4 3 1 2
After:  [2, 1, 0, 1]

Before: [1, 0, 1, 1]
7 3 3 1
After:  [1, 0, 1, 1]

Before: [0, 1, 0, 1]
7 3 3 2
After:  [0, 1, 0, 1]

Before: [0, 1, 3, 2]
0 1 2 1
After:  [0, 0, 3, 2]

Before: [1, 1, 2, 2]
8 0 2 3
After:  [1, 1, 2, 0]

Before: [2, 0, 2, 2]
10 1 0 0
After:  [0, 0, 2, 2]

Before: [2, 1, 3, 1]
0 1 2 3
After:  [2, 1, 3, 0]

Before: [1, 1, 2, 2]
8 0 2 1
After:  [1, 0, 2, 2]

Before: [0, 0, 2, 1]
11 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 0, 2, 0]
3 2 2 0
After:  [4, 0, 2, 0]

Before: [1, 0, 0, 0]
2 0 2 3
After:  [1, 0, 0, 0]

Before: [2, 0, 0, 1]
4 0 1 1
After:  [2, 1, 0, 1]

Before: [2, 0, 3, 3]
10 1 0 3
After:  [2, 0, 3, 0]

Before: [0, 1, 3, 2]
0 1 2 0
After:  [0, 1, 3, 2]

Before: [2, 1, 3, 3]
0 1 2 3
After:  [2, 1, 3, 0]

Before: [0, 1, 2, 1]
11 3 2 3
After:  [0, 1, 2, 1]

Before: [0, 2, 2, 3]
13 0 2 1
After:  [0, 0, 2, 3]

Before: [0, 2, 3, 2]
13 0 1 3
After:  [0, 2, 3, 0]

Before: [1, 1, 2, 2]
4 3 2 1
After:  [1, 0, 2, 2]

Before: [1, 1, 2, 1]
11 3 2 2
After:  [1, 1, 1, 1]

Before: [0, 2, 1, 0]
13 0 1 1
After:  [0, 0, 1, 0]

Before: [2, 1, 2, 2]
9 2 0 0
After:  [1, 1, 2, 2]

Before: [1, 1, 1, 1]
1 2 0 3
After:  [1, 1, 1, 2]

Before: [3, 3, 0, 2]
12 2 3 2
After:  [3, 3, 1, 2]

Before: [0, 1, 2, 2]
3 3 2 1
After:  [0, 4, 2, 2]

Before: [0, 2, 2, 3]
13 0 3 0
After:  [0, 2, 2, 3]

Before: [1, 3, 1, 0]
1 2 0 0
After:  [2, 3, 1, 0]

Before: [0, 1, 1, 3]
15 1 3 3
After:  [0, 1, 1, 0]

Before: [3, 2, 3, 0]
12 3 2 3
After:  [3, 2, 3, 1]

Before: [1, 0, 1, 3]
1 2 0 3
After:  [1, 0, 1, 2]

Before: [3, 1, 2, 1]
11 3 2 2
After:  [3, 1, 1, 1]

Before: [0, 0, 0, 2]
6 0 0 3
After:  [0, 0, 0, 0]

Before: [1, 0, 0, 1]
2 0 2 3
After:  [1, 0, 0, 0]

Before: [0, 3, 0, 2]
6 0 0 0
After:  [0, 3, 0, 2]

Before: [1, 1, 3, 0]
0 1 2 0
After:  [0, 1, 3, 0]

Before: [3, 1, 0, 3]
15 1 3 0
After:  [0, 1, 0, 3]

Before: [3, 2, 0, 2]
10 2 0 1
After:  [3, 0, 0, 2]

Before: [0, 2, 0, 2]
6 0 0 1
After:  [0, 0, 0, 2]

Before: [0, 3, 3, 1]
6 0 0 1
After:  [0, 0, 3, 1]

Before: [0, 1, 2, 0]
3 2 2 3
After:  [0, 1, 2, 4]

Before: [3, 0, 0, 0]
4 0 2 1
After:  [3, 1, 0, 0]

Before: [0, 2, 2, 1]
11 3 2 3
After:  [0, 2, 2, 1]

Before: [2, 0, 3, 3]
9 3 2 0
After:  [1, 0, 3, 3]

Before: [2, 1, 2, 2]
5 1 2 2
After:  [2, 1, 0, 2]

Before: [1, 1, 2, 2]
5 1 2 2
After:  [1, 1, 0, 2]

Before: [0, 1, 0, 1]
6 0 0 3
After:  [0, 1, 0, 0]

Before: [1, 3, 2, 2]
3 2 2 1
After:  [1, 4, 2, 2]

Before: [3, 0, 2, 2]
3 2 2 2
After:  [3, 0, 4, 2]

Before: [2, 1, 2, 1]
3 2 2 0
After:  [4, 1, 2, 1]

Before: [1, 3, 2, 3]
8 0 2 2
After:  [1, 3, 0, 3]

Before: [2, 1, 1, 3]
4 2 1 0
After:  [0, 1, 1, 3]

Before: [2, 0, 1, 1]
1 2 3 0
After:  [2, 0, 1, 1]

Before: [3, 0, 0, 3]
10 1 0 0
After:  [0, 0, 0, 3]

Before: [1, 1, 3, 1]
0 1 2 1
After:  [1, 0, 3, 1]

Before: [0, 0, 1, 2]
6 0 0 2
After:  [0, 0, 0, 2]

Before: [3, 3, 0, 2]
10 2 0 2
After:  [3, 3, 0, 2]

Before: [2, 3, 2, 1]
11 3 2 0
After:  [1, 3, 2, 1]

Before: [1, 0, 0, 1]
2 0 2 0
After:  [0, 0, 0, 1]

Before: [0, 2, 2, 0]
6 0 0 3
After:  [0, 2, 2, 0]

Before: [1, 1, 2, 0]
8 0 2 0
After:  [0, 1, 2, 0]

Before: [2, 3, 2, 0]
9 2 0 2
After:  [2, 3, 1, 0]

Before: [1, 3, 0, 2]
2 0 2 0
After:  [0, 3, 0, 2]

Before: [3, 0, 0, 0]
10 1 0 3
After:  [3, 0, 0, 0]

Before: [0, 1, 0, 1]
6 0 0 0
After:  [0, 1, 0, 1]

Before: [0, 1, 3, 0]
12 3 2 2
After:  [0, 1, 1, 0]

Before: [2, 3, 1, 0]
14 0 3 2
After:  [2, 3, 1, 0]

Before: [0, 1, 2, 1]
11 3 2 1
After:  [0, 1, 2, 1]

Before: [3, 1, 1, 3]
4 2 1 0
After:  [0, 1, 1, 3]

Before: [0, 3, 0, 2]
6 0 0 2
After:  [0, 3, 0, 2]

Before: [0, 3, 2, 1]
11 3 2 3
After:  [0, 3, 2, 1]

Before: [2, 2, 2, 1]
3 1 2 3
After:  [2, 2, 2, 4]

Before: [2, 1, 0, 0]
14 0 3 1
After:  [2, 1, 0, 0]

Before: [0, 3, 3, 3]
9 3 2 2
After:  [0, 3, 1, 3]

Before: [0, 3, 3, 1]
13 0 1 2
After:  [0, 3, 0, 1]

Before: [0, 1, 1, 1]
13 0 3 1
After:  [0, 0, 1, 1]

Before: [2, 0, 2, 1]
3 2 2 2
After:  [2, 0, 4, 1]

Before: [0, 2, 2, 1]
9 2 1 1
After:  [0, 1, 2, 1]

Before: [2, 1, 0, 1]
7 3 3 3
After:  [2, 1, 0, 0]

Before: [0, 0, 1, 3]
13 0 3 0
After:  [0, 0, 1, 3]

Before: [3, 3, 1, 3]
15 2 3 3
After:  [3, 3, 1, 0]

Before: [0, 1, 3, 3]
0 1 2 0
After:  [0, 1, 3, 3]

Before: [3, 0, 3, 0]
12 3 2 0
After:  [1, 0, 3, 0]

Before: [1, 0, 2, 3]
8 0 2 1
After:  [1, 0, 2, 3]

Before: [2, 1, 3, 3]
0 1 2 1
After:  [2, 0, 3, 3]

Before: [2, 0, 3, 3]
4 2 0 1
After:  [2, 1, 3, 3]

Before: [0, 0, 2, 3]
13 0 3 1
After:  [0, 0, 2, 3]

Before: [1, 1, 3, 3]
9 3 2 0
After:  [1, 1, 3, 3]

Before: [0, 0, 0, 1]
6 0 0 2
After:  [0, 0, 0, 1]

Before: [0, 0, 3, 2]
13 0 2 3
After:  [0, 0, 3, 0]

Before: [1, 3, 2, 2]
8 0 2 1
After:  [1, 0, 2, 2]

Before: [0, 1, 0, 1]
13 0 1 2
After:  [0, 1, 0, 1]

Before: [2, 3, 0, 0]
14 0 3 2
After:  [2, 3, 1, 0]

Before: [2, 0, 2, 1]
7 3 3 1
After:  [2, 0, 2, 1]

Before: [3, 3, 2, 2]
7 3 3 2
After:  [3, 3, 0, 2]

Before: [0, 3, 1, 2]
6 0 0 3
After:  [0, 3, 1, 0]

Before: [1, 0, 1, 1]
1 2 0 2
After:  [1, 0, 2, 1]

Before: [2, 1, 1, 0]
14 0 3 1
After:  [2, 1, 1, 0]

Before: [3, 3, 3, 3]
9 3 0 3
After:  [3, 3, 3, 1]

Before: [1, 1, 1, 1]
1 2 3 0
After:  [2, 1, 1, 1]

Before: [3, 1, 3, 1]
0 1 2 2
After:  [3, 1, 0, 1]

Before: [1, 1, 2, 0]
5 1 2 2
After:  [1, 1, 0, 0]

Before: [1, 1, 2, 3]
5 1 2 2
After:  [1, 1, 0, 3]

Before: [2, 0, 0, 3]
10 1 0 1
After:  [2, 0, 0, 3]

Before: [1, 2, 0, 1]
7 3 3 3
After:  [1, 2, 0, 0]

Before: [0, 3, 1, 3]
6 0 0 1
After:  [0, 0, 1, 3]

Before: [2, 2, 3, 1]
4 2 0 3
After:  [2, 2, 3, 1]

Before: [3, 0, 2, 1]
11 3 2 2
After:  [3, 0, 1, 1]

Before: [0, 1, 2, 0]
5 1 2 2
After:  [0, 1, 0, 0]

Before: [2, 3, 1, 1]
1 2 3 2
After:  [2, 3, 2, 1]

Before: [0, 1, 1, 2]
13 0 3 3
After:  [0, 1, 1, 0]

Before: [3, 1, 2, 3]
5 1 2 0
After:  [0, 1, 2, 3]

Before: [1, 3, 3, 0]
12 3 2 0
After:  [1, 3, 3, 0]

Before: [2, 3, 0, 2]
12 2 3 2
After:  [2, 3, 1, 2]

Before: [3, 1, 0, 1]
10 2 0 1
After:  [3, 0, 0, 1]

Before: [0, 2, 0, 0]
13 0 1 0
After:  [0, 2, 0, 0]

Before: [0, 2, 2, 2]
13 0 1 2
After:  [0, 2, 0, 2]

Before: [3, 2, 2, 3]
15 2 3 2
After:  [3, 2, 0, 3]

Before: [2, 0, 2, 0]
14 0 3 1
After:  [2, 1, 2, 0]

Before: [2, 2, 0, 0]
14 0 3 2
After:  [2, 2, 1, 0]

Before: [1, 3, 2, 0]
8 0 2 0
After:  [0, 3, 2, 0]

Before: [3, 2, 3, 1]
9 2 3 1
After:  [3, 0, 3, 1]

Before: [0, 1, 1, 0]
4 2 1 1
After:  [0, 0, 1, 0]

Before: [0, 3, 2, 3]
13 0 3 0
After:  [0, 3, 2, 3]

Before: [3, 1, 0, 1]
7 3 3 3
After:  [3, 1, 0, 0]

Before: [1, 3, 3, 3]
9 3 2 3
After:  [1, 3, 3, 1]

Before: [2, 3, 3, 1]
4 2 0 2
After:  [2, 3, 1, 1]

Before: [0, 3, 3, 1]
7 3 3 0
After:  [0, 3, 3, 1]

Before: [1, 2, 1, 2]
1 2 0 1
After:  [1, 2, 1, 2]

Before: [0, 2, 2, 2]
13 0 2 2
After:  [0, 2, 0, 2]

Before: [1, 1, 3, 3]
0 1 2 1
After:  [1, 0, 3, 3]

Before: [2, 0, 3, 2]
4 0 1 0
After:  [1, 0, 3, 2]

Before: [3, 1, 3, 0]
12 3 2 2
After:  [3, 1, 1, 0]

Before: [0, 2, 1, 1]
1 2 3 3
After:  [0, 2, 1, 2]

Before: [2, 3, 1, 0]
14 0 3 3
After:  [2, 3, 1, 1]

Before: [2, 0, 1, 0]
14 0 3 0
After:  [1, 0, 1, 0]

Before: [0, 3, 1, 1]
7 3 3 3
After:  [0, 3, 1, 0]

Before: [2, 3, 3, 3]
9 3 2 3
After:  [2, 3, 3, 1]

Before: [2, 1, 2, 3]
15 2 3 1
After:  [2, 0, 2, 3]

Before: [2, 1, 3, 3]
0 1 2 2
After:  [2, 1, 0, 3]

Before: [3, 1, 2, 1]
7 3 3 0
After:  [0, 1, 2, 1]

Before: [1, 1, 0, 1]
7 3 3 1
After:  [1, 0, 0, 1]

Before: [2, 1, 2, 1]
5 1 2 2
After:  [2, 1, 0, 1]

Before: [3, 1, 3, 2]
0 1 2 1
After:  [3, 0, 3, 2]

Before: [2, 1, 1, 3]
15 1 3 3
After:  [2, 1, 1, 0]

Before: [3, 2, 0, 1]
10 2 0 3
After:  [3, 2, 0, 0]

Before: [1, 3, 0, 1]
2 0 2 2
After:  [1, 3, 0, 1]

Before: [1, 1, 3, 2]
0 1 2 2
After:  [1, 1, 0, 2]

Before: [1, 2, 2, 2]
7 3 3 0
After:  [0, 2, 2, 2]

Before: [1, 2, 2, 2]
8 0 2 0
After:  [0, 2, 2, 2]

Before: [3, 1, 0, 3]
9 3 0 3
After:  [3, 1, 0, 1]

Before: [1, 1, 0, 1]
2 0 2 2
After:  [1, 1, 0, 1]

Before: [2, 3, 3, 0]
14 0 3 0
After:  [1, 3, 3, 0]

Before: [3, 0, 2, 1]
11 3 2 1
After:  [3, 1, 2, 1]

Before: [2, 3, 3, 0]
14 0 3 3
After:  [2, 3, 3, 1]

Before: [0, 1, 2, 2]
5 1 2 2
After:  [0, 1, 0, 2]

Before: [3, 0, 2, 3]
10 1 0 3
After:  [3, 0, 2, 0]

Before: [1, 1, 2, 3]
8 0 2 2
After:  [1, 1, 0, 3]

Before: [0, 0, 0, 3]
6 0 0 1
After:  [0, 0, 0, 3]

Before: [1, 3, 2, 1]
11 3 2 2
After:  [1, 3, 1, 1]

Before: [0, 3, 1, 3]
13 0 3 1
After:  [0, 0, 1, 3]

Before: [2, 0, 3, 0]
14 0 3 1
After:  [2, 1, 3, 0]

Before: [0, 2, 0, 3]
13 0 3 3
After:  [0, 2, 0, 0]

Before: [1, 0, 2, 0]
8 0 2 2
After:  [1, 0, 0, 0]

Before: [1, 3, 2, 0]
8 0 2 1
After:  [1, 0, 2, 0]

Before: [1, 0, 2, 1]
11 3 2 1
After:  [1, 1, 2, 1]

Before: [1, 0, 0, 0]
2 0 2 1
After:  [1, 0, 0, 0]

Before: [2, 2, 2, 1]
11 3 2 1
After:  [2, 1, 2, 1]

Before: [3, 3, 0, 2]
7 3 3 1
After:  [3, 0, 0, 2]

Before: [2, 1, 3, 3]
15 1 3 0
After:  [0, 1, 3, 3]

Before: [0, 3, 3, 2]
13 0 1 1
After:  [0, 0, 3, 2]

Before: [0, 3, 3, 3]
6 0 0 1
After:  [0, 0, 3, 3]

Before: [1, 3, 2, 2]
8 0 2 2
After:  [1, 3, 0, 2]

Before: [1, 0, 0, 3]
2 0 2 3
After:  [1, 0, 0, 0]

Before: [2, 3, 2, 1]
9 2 0 2
After:  [2, 3, 1, 1]

Before: [1, 3, 1, 2]
1 2 0 0
After:  [2, 3, 1, 2]

Before: [2, 1, 3, 0]
0 1 2 0
After:  [0, 1, 3, 0]

Before: [3, 2, 2, 1]
9 2 1 2
After:  [3, 2, 1, 1]

Before: [2, 1, 3, 1]
0 1 2 2
After:  [2, 1, 0, 1]

Before: [0, 2, 1, 0]
6 0 0 1
After:  [0, 0, 1, 0]

Before: [1, 1, 0, 3]
15 1 3 1
After:  [1, 0, 0, 3]

Before: [0, 3, 3, 3]
9 3 2 3
After:  [0, 3, 3, 1]

Before: [3, 1, 3, 1]
7 3 3 3
After:  [3, 1, 3, 0]

Before: [2, 2, 2, 1]
11 3 2 3
After:  [2, 2, 2, 1]

Before: [3, 2, 2, 3]
9 3 0 1
After:  [3, 1, 2, 3]

Before: [3, 2, 2, 0]
3 1 2 1
After:  [3, 4, 2, 0]

Before: [2, 3, 2, 0]
14 0 3 1
After:  [2, 1, 2, 0]

Before: [0, 1, 3, 0]
0 1 2 2
After:  [0, 1, 0, 0]

Before: [2, 2, 3, 0]
4 2 0 3
After:  [2, 2, 3, 1]

Before: [2, 0, 0, 0]
14 0 3 1
After:  [2, 1, 0, 0]

Before: [1, 1, 0, 0]
2 0 2 0
After:  [0, 1, 0, 0]

Before: [0, 2, 3, 2]
6 0 0 1
After:  [0, 0, 3, 2]

Before: [2, 3, 2, 3]
3 2 2 0
After:  [4, 3, 2, 3]

Before: [1, 2, 2, 1]
3 2 2 0
After:  [4, 2, 2, 1]

Before: [2, 2, 2, 0]
14 0 3 0
After:  [1, 2, 2, 0]

Before: [1, 1, 2, 3]
5 1 2 0
After:  [0, 1, 2, 3]

Before: [3, 1, 3, 3]
9 3 2 0
After:  [1, 1, 3, 3]

Before: [1, 1, 0, 0]
2 0 2 2
After:  [1, 1, 0, 0]

Before: [1, 1, 2, 3]
8 0 2 3
After:  [1, 1, 2, 0]

Before: [3, 3, 2, 3]
3 2 2 1
After:  [3, 4, 2, 3]

Before: [3, 3, 1, 3]
15 2 3 2
After:  [3, 3, 0, 3]

Before: [0, 1, 0, 2]
6 0 0 1
After:  [0, 0, 0, 2]

Before: [1, 1, 3, 0]
12 3 2 0
After:  [1, 1, 3, 0]

Before: [2, 1, 2, 2]
3 3 2 2
After:  [2, 1, 4, 2]

Before: [1, 1, 3, 2]
0 1 2 1
After:  [1, 0, 3, 2]

Before: [3, 1, 2, 3]
5 1 2 1
After:  [3, 0, 2, 3]

Before: [0, 1, 3, 1]
0 1 2 1
After:  [0, 0, 3, 1]

Before: [3, 2, 2, 1]
7 3 3 1
After:  [3, 0, 2, 1]

Before: [0, 1, 2, 3]
5 1 2 2
After:  [0, 1, 0, 3]

Before: [1, 1, 0, 3]
2 0 2 1
After:  [1, 0, 0, 3]

Before: [2, 0, 2, 0]
14 0 3 0
After:  [1, 0, 2, 0]

Before: [0, 2, 1, 0]
6 0 0 2
After:  [0, 2, 0, 0]

Before: [0, 2, 0, 1]
13 0 1 0
After:  [0, 2, 0, 1]

Before: [2, 3, 0, 0]
14 0 3 0
After:  [1, 3, 0, 0]

Before: [3, 1, 1, 3]
15 1 3 3
After:  [3, 1, 1, 0]

Before: [1, 2, 1, 3]
15 2 3 3
After:  [1, 2, 1, 0]

Before: [3, 1, 2, 1]
5 1 2 1
After:  [3, 0, 2, 1]

Before: [1, 1, 0, 1]
2 0 2 1
After:  [1, 0, 0, 1]

Before: [1, 2, 2, 3]
8 0 2 0
After:  [0, 2, 2, 3]

Before: [0, 2, 2, 3]
15 2 3 2
After:  [0, 2, 0, 3]

Before: [1, 0, 2, 0]
8 0 2 0
After:  [0, 0, 2, 0]

Before: [0, 2, 2, 3]
3 2 2 0
After:  [4, 2, 2, 3]

Before: [3, 3, 2, 1]
11 3 2 2
After:  [3, 3, 1, 1]

Before: [0, 2, 2, 2]
6 0 0 2
After:  [0, 2, 0, 2]

Before: [1, 1, 2, 1]
5 1 2 3
After:  [1, 1, 2, 0]

Before: [2, 0, 2, 1]
11 3 2 1
After:  [2, 1, 2, 1]

Before: [0, 1, 2, 1]
5 1 2 3
After:  [0, 1, 2, 0]

Before: [1, 2, 2, 2]
3 1 2 0
After:  [4, 2, 2, 2]

Before: [1, 3, 2, 1]
11 3 2 3
After:  [1, 3, 2, 1]

Before: [0, 1, 1, 2]
13 0 1 2
After:  [0, 1, 0, 2]

Before: [1, 2, 2, 0]
3 1 2 1
After:  [1, 4, 2, 0]

Before: [1, 0, 0, 0]
2 0 2 0
After:  [0, 0, 0, 0]

Before: [1, 2, 1, 1]
1 2 0 3
After:  [1, 2, 1, 2]

Before: [3, 3, 2, 1]
11 3 2 1
After:  [3, 1, 2, 1]

Before: [0, 0, 2, 1]
11 3 2 0
After:  [1, 0, 2, 1]

Before: [1, 1, 1, 3]
4 2 1 3
After:  [1, 1, 1, 0]

Before: [2, 0, 2, 2]
7 3 3 1
After:  [2, 0, 2, 2]

Before: [0, 1, 2, 1]
5 1 2 0
After:  [0, 1, 2, 1]

Before: [3, 2, 0, 3]
10 2 0 0
After:  [0, 2, 0, 3]

Before: [1, 1, 2, 0]
5 1 2 1
After:  [1, 0, 2, 0]

Before: [2, 0, 3, 1]
9 2 3 2
After:  [2, 0, 0, 1]

Before: [1, 0, 2, 1]
8 0 2 1
After:  [1, 0, 2, 1]

Before: [0, 2, 0, 3]
15 1 3 3
After:  [0, 2, 0, 0]

Before: [0, 2, 2, 0]
6 0 0 0
After:  [0, 2, 2, 0]

Before: [0, 0, 1, 1]
1 2 3 2
After:  [0, 0, 2, 1]

Before: [1, 0, 1, 3]
15 2 3 3
After:  [1, 0, 1, 0]

Before: [2, 1, 2, 3]
15 1 3 2
After:  [2, 1, 0, 3]

Before: [1, 2, 2, 3]
8 0 2 2
After:  [1, 2, 0, 3]

Before: [2, 2, 3, 0]
12 3 2 2
After:  [2, 2, 1, 0]

Before: [3, 1, 3, 1]
9 2 3 3
After:  [3, 1, 3, 0]

Before: [3, 0, 3, 1]
7 3 3 1
After:  [3, 0, 3, 1]

Before: [0, 3, 0, 2]
6 0 0 3
After:  [0, 3, 0, 0]

Before: [1, 1, 2, 1]
5 1 2 0
After:  [0, 1, 2, 1]

Before: [1, 3, 3, 0]
12 3 2 3
After:  [1, 3, 3, 1]

Before: [3, 0, 1, 1]
1 2 3 0
After:  [2, 0, 1, 1]

Before: [2, 1, 2, 0]
14 0 3 3
After:  [2, 1, 2, 1]

Before: [2, 3, 2, 1]
11 3 2 2
After:  [2, 3, 1, 1]

Before: [0, 3, 3, 0]
6 0 0 3
After:  [0, 3, 3, 0]

Before: [0, 1, 3, 0]
12 3 2 3
After:  [0, 1, 3, 1]

Before: [1, 2, 3, 0]
12 3 2 3
After:  [1, 2, 3, 1]

Before: [2, 1, 0, 2]
12 2 3 3
After:  [2, 1, 0, 1]

Before: [0, 3, 0, 2]
7 3 3 3
After:  [0, 3, 0, 0]

Before: [3, 0, 3, 0]
12 3 2 2
After:  [3, 0, 1, 0]

Before: [2, 2, 0, 0]
14 0 3 3
After:  [2, 2, 0, 1]

Before: [1, 2, 0, 1]
2 0 2 1
After:  [1, 0, 0, 1]

Before: [0, 2, 3, 1]
9 2 3 2
After:  [0, 2, 0, 1]

Before: [2, 1, 2, 1]
11 3 2 1
After:  [2, 1, 2, 1]

Before: [3, 1, 3, 3]
0 1 2 3
After:  [3, 1, 3, 0]

Before: [0, 1, 2, 3]
5 1 2 3
After:  [0, 1, 2, 0]

Before: [1, 3, 1, 0]
1 2 0 2
After:  [1, 3, 2, 0]

Before: [0, 3, 3, 2]
13 0 1 3
After:  [0, 3, 3, 0]

Before: [1, 2, 0, 2]
2 0 2 0
After:  [0, 2, 0, 2]

Before: [2, 2, 0, 0]
14 0 3 0
After:  [1, 2, 0, 0]

Before: [3, 2, 0, 0]
10 2 0 0
After:  [0, 2, 0, 0]

Before: [1, 2, 2, 0]
8 0 2 0
After:  [0, 2, 2, 0]

Before: [2, 0, 2, 2]
3 3 2 1
After:  [2, 4, 2, 2]

Before: [1, 3, 0, 2]
12 2 3 1
After:  [1, 1, 0, 2]

Before: [0, 1, 1, 2]
7 3 3 3
After:  [0, 1, 1, 0]

Before: [0, 0, 1, 2]
7 3 3 1
After:  [0, 0, 1, 2]

Before: [0, 1, 1, 0]
6 0 0 1
After:  [0, 0, 1, 0]

Before: [2, 0, 2, 1]
11 3 2 0
After:  [1, 0, 2, 1]

Before: [2, 2, 3, 3]
15 1 3 1
After:  [2, 0, 3, 3]

Before: [0, 3, 2, 3]
13 0 2 3
After:  [0, 3, 2, 0]

Before: [0, 1, 2, 2]
13 0 3 3
After:  [0, 1, 2, 0]

Before: [2, 1, 2, 0]
5 1 2 0
After:  [0, 1, 2, 0]

Before: [3, 3, 0, 2]
7 3 3 3
After:  [3, 3, 0, 0]

Before: [0, 0, 1, 2]
13 0 3 2
After:  [0, 0, 0, 2]

Before: [1, 3, 1, 2]
1 2 0 3
After:  [1, 3, 1, 2]

Before: [0, 1, 3, 1]
13 0 3 1
After:  [0, 0, 3, 1]

Before: [2, 1, 3, 1]
4 2 0 0
After:  [1, 1, 3, 1]

Before: [1, 1, 2, 2]
8 0 2 2
After:  [1, 1, 0, 2]

Before: [3, 0, 0, 2]
10 1 0 3
After:  [3, 0, 0, 0]

Before: [0, 3, 1, 2]
7 3 3 2
After:  [0, 3, 0, 2]

Before: [3, 2, 2, 2]
9 2 1 2
After:  [3, 2, 1, 2]

Before: [0, 3, 2, 2]
4 3 2 1
After:  [0, 0, 2, 2]

Before: [0, 1, 2, 3]
5 1 2 0
After:  [0, 1, 2, 3]

Before: [1, 2, 0, 3]
2 0 2 3
After:  [1, 2, 0, 0]

Before: [0, 3, 2, 3]
13 0 2 0
After:  [0, 3, 2, 3]

Before: [1, 1, 2, 0]
8 0 2 2
After:  [1, 1, 0, 0]

Before: [1, 2, 0, 0]
2 0 2 2
After:  [1, 2, 0, 0]

Before: [0, 0, 2, 1]
11 3 2 2
After:  [0, 0, 1, 1]

Before: [3, 1, 3, 2]
0 1 2 2
After:  [3, 1, 0, 2]

Before: [1, 1, 1, 1]
4 3 1 1
After:  [1, 0, 1, 1]

Before: [0, 3, 3, 1]
13 0 3 1
After:  [0, 0, 3, 1]

Before: [1, 1, 3, 0]
12 3 2 1
After:  [1, 1, 3, 0]

Before: [2, 0, 0, 0]
14 0 3 0
After:  [1, 0, 0, 0]

Before: [0, 1, 3, 2]
0 1 2 3
After:  [0, 1, 3, 0]

Before: [1, 1, 2, 0]
8 0 2 3
After:  [1, 1, 2, 0]

Before: [3, 0, 2, 3]
15 2 3 2
After:  [3, 0, 0, 3]

Before: [1, 1, 1, 2]
1 2 0 0
After:  [2, 1, 1, 2]

Before: [3, 3, 2, 2]
3 2 2 2
After:  [3, 3, 4, 2]

Before: [0, 1, 0, 2]
7 3 3 2
After:  [0, 1, 0, 2]

Before: [0, 2, 2, 2]
13 0 2 0
After:  [0, 2, 2, 2]

Before: [3, 1, 0, 0]
10 2 0 3
After:  [3, 1, 0, 0]

Before: [2, 1, 3, 0]
0 1 2 1
After:  [2, 0, 3, 0]

Before: [1, 0, 2, 2]
8 0 2 1
After:  [1, 0, 2, 2]

Before: [2, 0, 1, 2]
10 1 0 1
After:  [2, 0, 1, 2]

Before: [2, 3, 2, 1]
11 3 2 1
After:  [2, 1, 2, 1]

Before: [2, 1, 1, 1]
4 2 1 3
After:  [2, 1, 1, 0]

Before: [2, 0, 2, 1]
11 3 2 2
After:  [2, 0, 1, 1]

Before: [2, 1, 3, 2]
0 1 2 1
After:  [2, 0, 3, 2]

Before: [2, 1, 2, 0]
5 1 2 3
After:  [2, 1, 2, 0]

Before: [0, 3, 2, 3]
13 0 1 3
After:  [0, 3, 2, 0]

Before: [1, 1, 2, 2]
5 1 2 0
After:  [0, 1, 2, 2]

Before: [1, 3, 1, 1]
1 2 3 3
After:  [1, 3, 1, 2]

Before: [2, 0, 2, 0]
14 0 3 2
After:  [2, 0, 1, 0]

Before: [3, 2, 2, 1]
11 3 2 1
After:  [3, 1, 2, 1]

Before: [1, 1, 3, 2]
0 1 2 0
After:  [0, 1, 3, 2]

Before: [0, 2, 2, 1]
11 3 2 1
After:  [0, 1, 2, 1]

Before: [2, 0, 0, 3]
10 1 0 3
After:  [2, 0, 0, 0]

Before: [2, 1, 0, 3]
15 1 3 1
After:  [2, 0, 0, 3]

Before: [3, 0, 2, 2]
4 3 2 1
After:  [3, 0, 2, 2]

Before: [3, 2, 2, 1]
11 3 2 2
After:  [3, 2, 1, 1]

Before: [2, 0, 0, 2]
12 2 3 2
After:  [2, 0, 1, 2]

Before: [0, 1, 2, 2]
6 0 0 0
After:  [0, 1, 2, 2]

Before: [2, 2, 2, 3]
3 2 2 1
After:  [2, 4, 2, 3]

Before: [2, 1, 2, 3]
5 1 2 3
After:  [2, 1, 2, 0]

Before: [0, 3, 3, 2]
6 0 0 0
After:  [0, 3, 3, 2]

Before: [3, 0, 3, 1]
7 3 3 0
After:  [0, 0, 3, 1]

Before: [0, 1, 1, 3]
15 1 3 1
After:  [0, 0, 1, 3]

Before: [0, 1, 3, 3]
15 1 3 3
After:  [0, 1, 3, 0]

Before: [2, 3, 2, 2]
4 3 2 0
After:  [0, 3, 2, 2]

Before: [0, 0, 2, 2]
7 3 3 2
After:  [0, 0, 0, 2]

Before: [2, 1, 1, 2]
4 2 1 1
After:  [2, 0, 1, 2]

Before: [1, 2, 0, 3]
2 0 2 0
After:  [0, 2, 0, 3]

Before: [3, 1, 2, 3]
9 3 0 3
After:  [3, 1, 2, 1]

Before: [0, 0, 0, 3]
13 0 3 0
After:  [0, 0, 0, 3]

Before: [1, 2, 2, 1]
8 0 2 2
After:  [1, 2, 0, 1]

Before: [3, 0, 1, 3]
9 3 0 3
After:  [3, 0, 1, 1]

Before: [1, 1, 2, 2]
5 1 2 1
After:  [1, 0, 2, 2]

Before: [1, 0, 2, 1]
11 3 2 0
After:  [1, 0, 2, 1]

Before: [0, 2, 3, 0]
12 3 2 3
After:  [0, 2, 3, 1]

Before: [3, 1, 3, 3]
0 1 2 1
After:  [3, 0, 3, 3]

Before: [3, 1, 0, 2]
7 3 3 0
After:  [0, 1, 0, 2]

Before: [1, 2, 0, 1]
2 0 2 3
After:  [1, 2, 0, 0]

Before: [1, 0, 2, 1]
8 0 2 3
After:  [1, 0, 2, 0]

Before: [2, 0, 2, 0]
10 1 0 1
After:  [2, 0, 2, 0]

Before: [3, 0, 3, 1]
10 1 0 2
After:  [3, 0, 0, 1]

Before: [3, 0, 3, 3]
9 3 0 1
After:  [3, 1, 3, 3]

Before: [0, 1, 3, 1]
13 0 2 1
After:  [0, 0, 3, 1]

Before: [0, 1, 1, 0]
6 0 0 3
After:  [0, 1, 1, 0]

Before: [0, 3, 3, 1]
13 0 3 3
After:  [0, 3, 3, 0]

Before: [1, 3, 0, 3]
2 0 2 0
After:  [0, 3, 0, 3]

Before: [2, 3, 3, 0]
12 3 2 2
After:  [2, 3, 1, 0]

Before: [3, 2, 1, 3]
15 1 3 0
After:  [0, 2, 1, 3]

Before: [1, 3, 2, 1]
8 0 2 2
After:  [1, 3, 0, 1]

Before: [3, 0, 3, 2]
10 1 0 1
After:  [3, 0, 3, 2]

Before: [3, 0, 2, 0]
10 1 0 2
After:  [3, 0, 0, 0]

Before: [2, 2, 3, 0]
14 0 3 1
After:  [2, 1, 3, 0]

Before: [3, 1, 2, 2]
5 1 2 1
After:  [3, 0, 2, 2]

Before: [1, 1, 2, 1]
5 1 2 1
After:  [1, 0, 2, 1]

Before: [1, 2, 2, 1]
11 3 2 2
After:  [1, 2, 1, 1]

Before: [3, 3, 2, 1]
11 3 2 0
After:  [1, 3, 2, 1]

Before: [0, 2, 0, 1]
6 0 0 3
After:  [0, 2, 0, 0]

Before: [2, 1, 2, 1]
11 3 2 2
After:  [2, 1, 1, 1]

Before: [1, 1, 3, 0]
0 1 2 1
After:  [1, 0, 3, 0]

Before: [3, 1, 2, 0]
5 1 2 2
After:  [3, 1, 0, 0]

Before: [0, 1, 2, 1]
5 1 2 2
After:  [0, 1, 0, 1]

Before: [0, 2, 3, 1]
13 0 1 1
After:  [0, 0, 3, 1]

Before: [1, 2, 3, 0]
12 3 2 1
After:  [1, 1, 3, 0]

Before: [1, 0, 3, 0]
12 3 2 0
After:  [1, 0, 3, 0]

Before: [2, 3, 0, 0]
14 0 3 1
After:  [2, 1, 0, 0]

Before: [0, 3, 1, 1]
7 3 3 1
After:  [0, 0, 1, 1]

Before: [3, 1, 3, 2]
0 1 2 3
After:  [3, 1, 3, 0]

Before: [0, 1, 3, 1]
9 2 3 1
After:  [0, 0, 3, 1]

Before: [3, 3, 0, 2]
12 2 3 3
After:  [3, 3, 0, 1]

Before: [1, 3, 2, 1]
11 3 2 0
After:  [1, 3, 2, 1]

Before: [0, 3, 1, 1]
7 3 3 0
After:  [0, 3, 1, 1]

Before: [1, 3, 3, 1]
7 3 3 3
After:  [1, 3, 3, 0]

Before: [2, 1, 2, 2]
5 1 2 3
After:  [2, 1, 2, 0]

Before: [2, 1, 3, 1]
9 2 3 1
After:  [2, 0, 3, 1]

Before: [0, 2, 2, 1]
13 0 1 0
After:  [0, 2, 2, 1]

Before: [0, 1, 2, 1]
11 3 2 0
After:  [1, 1, 2, 1]

Before: [0, 1, 3, 3]
0 1 2 3
After:  [0, 1, 3, 0]

Before: [1, 1, 3, 3]
0 1 2 0
After:  [0, 1, 3, 3]

Before: [1, 0, 1, 2]
1 2 0 1
After:  [1, 2, 1, 2]

Before: [1, 0, 1, 3]
1 2 0 2
After:  [1, 0, 2, 3]

Before: [2, 1, 2, 0]
3 0 2 3
After:  [2, 1, 2, 4]

Before: [3, 0, 2, 2]
7 3 3 0
After:  [0, 0, 2, 2]

Before: [3, 0, 0, 2]
10 1 0 0
After:  [0, 0, 0, 2]

Before: [2, 1, 3, 2]
7 3 3 3
After:  [2, 1, 3, 0]

Before: [2, 0, 2, 1]
4 0 1 1
After:  [2, 1, 2, 1]

Before: [3, 3, 3, 0]
12 3 2 1
After:  [3, 1, 3, 0]

Before: [1, 0, 2, 3]
8 0 2 0
After:  [0, 0, 2, 3]

Before: [0, 1, 1, 3]
15 1 3 0
After:  [0, 1, 1, 3]

Before: [2, 0, 3, 3]
9 3 2 2
After:  [2, 0, 1, 3]

Before: [2, 3, 0, 0]
14 0 3 3
After:  [2, 3, 0, 1]

Before: [2, 3, 2, 1]
11 3 2 3
After:  [2, 3, 2, 1]

Before: [2, 0, 0, 3]
4 0 1 2
After:  [2, 0, 1, 3]

Before: [0, 1, 1, 2]
6 0 0 0
After:  [0, 1, 1, 2]

Before: [1, 0, 3, 0]
12 3 2 1
After:  [1, 1, 3, 0]

Before: [2, 1, 1, 1]
1 2 3 2
After:  [2, 1, 2, 1]

Before: [1, 3, 2, 2]
3 2 2 3
After:  [1, 3, 2, 4]

Before: [0, 1, 1, 1]
1 2 3 1
After:  [0, 2, 1, 1]

Before: [2, 1, 3, 2]
0 1 2 0
After:  [0, 1, 3, 2]

Before: [1, 0, 2, 0]
8 0 2 3
After:  [1, 0, 2, 0]

Before: [0, 3, 2, 3]
3 2 2 2
After:  [0, 3, 4, 3]

Before: [1, 2, 1, 1]
1 2 3 3
After:  [1, 2, 1, 2]

Before: [2, 3, 2, 1]
3 2 2 3
After:  [2, 3, 2, 4]

Before: [3, 1, 1, 1]
1 2 3 2
After:  [3, 1, 2, 1]

Before: [2, 3, 2, 0]
9 2 0 1
After:  [2, 1, 2, 0]

Before: [2, 0, 2, 1]
11 3 2 3
After:  [2, 0, 2, 1]

Before: [1, 1, 2, 0]
3 2 2 2
After:  [1, 1, 4, 0]

Before: [2, 2, 2, 1]
11 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 0, 0, 2]
2 0 2 0
After:  [0, 0, 0, 2]

Before: [1, 0, 3, 0]
12 3 2 3
After:  [1, 0, 3, 1]

Before: [3, 1, 0, 3]
4 0 2 3
After:  [3, 1, 0, 1]

Before: [3, 2, 2, 1]
3 2 2 0
After:  [4, 2, 2, 1]

Before: [3, 1, 2, 3]
5 1 2 3
After:  [3, 1, 2, 0]

Before: [3, 1, 2, 2]
3 2 2 2
After:  [3, 1, 4, 2]

Before: [3, 0, 1, 1]
7 3 3 0
After:  [0, 0, 1, 1]

Before: [1, 0, 3, 0]
12 3 2 2
After:  [1, 0, 1, 0]

Before: [2, 3, 3, 0]
4 2 0 0
After:  [1, 3, 3, 0]

Before: [2, 2, 1, 0]
14 0 3 3
After:  [2, 2, 1, 1]

Before: [1, 2, 0, 3]
2 0 2 1
After:  [1, 0, 0, 3]

Before: [0, 2, 2, 1]
9 2 1 0
After:  [1, 2, 2, 1]

Before: [3, 1, 3, 1]
0 1 2 0
After:  [0, 1, 3, 1]

Before: [0, 1, 2, 3]
6 0 0 0
After:  [0, 1, 2, 3]

Before: [3, 0, 1, 2]
10 1 0 1
After:  [3, 0, 1, 2]

Before: [2, 2, 2, 1]
7 3 3 3
After:  [2, 2, 2, 0]

Before: [3, 0, 1, 3]
10 1 0 0
After:  [0, 0, 1, 3]

Before: [0, 0, 3, 0]
12 3 2 3
After:  [0, 0, 3, 1]

Before: [2, 1, 2, 0]
5 1 2 1
After:  [2, 0, 2, 0]

Before: [2, 2, 2, 3]
15 2 3 2
After:  [2, 2, 0, 3]

Before: [2, 0, 3, 0]
14 0 3 3
After:  [2, 0, 3, 1]

Before: [1, 1, 3, 3]
0 1 2 2
After:  [1, 1, 0, 3]

Before: [0, 1, 1, 2]
6 0 0 3
After:  [0, 1, 1, 0]

Before: [2, 2, 2, 3]
15 1 3 3
After:  [2, 2, 2, 0]

Before: [2, 3, 2, 0]
14 0 3 3
After:  [2, 3, 2, 1]

Before: [0, 1, 3, 3]
0 1 2 1
After:  [0, 0, 3, 3]

Before: [1, 3, 2, 2]
4 3 2 0
After:  [0, 3, 2, 2]

Before: [2, 1, 1, 3]
4 2 1 3
After:  [2, 1, 1, 0]

Before: [2, 1, 0, 0]
14 0 3 3
After:  [2, 1, 0, 1]

Before: [0, 2, 1, 3]
15 1 3 1
After:  [0, 0, 1, 3]

Before: [2, 1, 3, 0]
0 1 2 2
After:  [2, 1, 0, 0]

Before: [1, 2, 0, 2]
12 2 3 0
After:  [1, 2, 0, 2]

Before: [0, 3, 0, 3]
13 0 3 3
After:  [0, 3, 0, 0]

Before: [3, 3, 0, 1]
10 2 0 1
After:  [3, 0, 0, 1]

Before: [2, 1, 1, 0]
14 0 3 3
After:  [2, 1, 1, 1]

Before: [1, 2, 2, 0]
8 0 2 2
After:  [1, 2, 0, 0]

Before: [2, 0, 0, 3]
4 0 1 0
After:  [1, 0, 0, 3]

Before: [1, 1, 2, 1]
5 1 2 2
After:  [1, 1, 0, 1]

Before: [3, 0, 3, 3]
9 3 2 0
After:  [1, 0, 3, 3]

Before: [1, 2, 2, 3]
9 2 1 0
After:  [1, 2, 2, 3]

Before: [2, 3, 2, 0]
14 0 3 0
After:  [1, 3, 2, 0]

Before: [3, 2, 3, 1]
7 3 3 3
After:  [3, 2, 3, 0]

Before: [0, 1, 3, 0]
0 1 2 1
After:  [0, 0, 3, 0]

Before: [3, 3, 0, 3]
9 3 0 2
After:  [3, 3, 1, 3]

Before: [3, 1, 3, 2]
0 1 2 0
After:  [0, 1, 3, 2]

Before: [0, 0, 2, 1]
11 3 2 3
After:  [0, 0, 2, 1]

Before: [0, 2, 1, 3]
13 0 1 3
After:  [0, 2, 1, 0]

Before: [1, 2, 2, 2]
3 1 2 3
After:  [1, 2, 2, 4]

Before: [0, 1, 2, 3]
5 1 2 1
After:  [0, 0, 2, 3]

Before: [2, 0, 3, 2]
10 1 0 0
After:  [0, 0, 3, 2]

Before: [1, 1, 0, 2]
12 2 3 0
After:  [1, 1, 0, 2]

Before: [3, 3, 1, 1]
1 2 3 0
After:  [2, 3, 1, 1]

Before: [1, 1, 0, 3]
2 0 2 3
After:  [1, 1, 0, 0]

Before: [1, 3, 1, 1]
1 2 0 2
After:  [1, 3, 2, 1]

Before: [2, 1, 2, 0]
14 0 3 1
After:  [2, 1, 2, 0]

Before: [2, 0, 2, 1]
4 0 1 3
After:  [2, 0, 2, 1]

Before: [2, 0, 2, 0]
14 0 3 3
After:  [2, 0, 2, 1]

Before: [0, 1, 3, 1]
0 1 2 2
After:  [0, 1, 0, 1]

Before: [1, 1, 2, 2]
3 2 2 1
After:  [1, 4, 2, 2]

Before: [0, 2, 3, 1]
6 0 0 3
After:  [0, 2, 3, 0]

Before: [1, 3, 0, 2]
2 0 2 3
After:  [1, 3, 0, 0]

Before: [1, 0, 1, 1]
1 2 3 3
After:  [1, 0, 1, 2]

Before: [1, 3, 1, 1]
1 2 3 0
After:  [2, 3, 1, 1]

Before: [1, 2, 2, 2]
9 2 1 0
After:  [1, 2, 2, 2]

Before: [2, 1, 3, 0]
14 0 3 1
After:  [2, 1, 3, 0]

Before: [1, 2, 1, 3]
1 2 0 0
After:  [2, 2, 1, 3]

Before: [1, 0, 0, 0]
2 0 2 2
After:  [1, 0, 0, 0]

Before: [2, 0, 2, 2]
3 2 2 0
After:  [4, 0, 2, 2]

Before: [2, 0, 3, 2]
4 0 1 3
After:  [2, 0, 3, 1]

Before: [2, 1, 2, 1]
5 1 2 3
After:  [2, 1, 2, 0]

Before: [1, 2, 2, 3]
15 2 3 1
After:  [1, 0, 2, 3]

Before: [0, 3, 2, 1]
6 0 0 2
After:  [0, 3, 0, 1]

Before: [1, 0, 0, 3]
2 0 2 2
After:  [1, 0, 0, 3]

Before: [1, 3, 2, 2]
8 0 2 0
After:  [0, 3, 2, 2]

Before: [0, 2, 1, 1]
6 0 0 1
After:  [0, 0, 1, 1]

Before: [2, 0, 2, 3]
9 2 0 1
After:  [2, 1, 2, 3]

Before: [2, 1, 2, 0]
14 0 3 2
After:  [2, 1, 1, 0]

Before: [1, 0, 1, 2]
1 2 0 3
After:  [1, 0, 1, 2]

Before: [2, 2, 3, 0]
12 3 2 3
After:  [2, 2, 3, 1]

Before: [3, 3, 3, 3]
9 3 2 1
After:  [3, 1, 3, 3]

Before: [0, 2, 2, 2]
3 1 2 3
After:  [0, 2, 2, 4]

Before: [2, 2, 2, 1]
9 2 1 1
After:  [2, 1, 2, 1]

Before: [1, 3, 0, 0]
2 0 2 1
After:  [1, 0, 0, 0]

Before: [2, 1, 2, 0]
14 0 3 0
After:  [1, 1, 2, 0]

Before: [1, 3, 0, 1]
2 0 2 3
After:  [1, 3, 0, 0]

Before: [1, 3, 1, 1]
1 2 3 1
After:  [1, 2, 1, 1]

Before: [1, 3, 0, 3]
2 0 2 1
After:  [1, 0, 0, 3]

Before: [3, 1, 2, 3]
15 2 3 2
After:  [3, 1, 0, 3]

Before: [2, 3, 3, 3]
9 3 2 0
After:  [1, 3, 3, 3]

Before: [0, 1, 3, 1]
0 1 2 3
After:  [0, 1, 3, 0]

Before: [1, 0, 1, 1]
1 2 0 1
After:  [1, 2, 1, 1]

Before: [1, 0, 2, 1]
8 0 2 0
After:  [0, 0, 2, 1]

Before: [1, 2, 2, 2]
8 0 2 1
After:  [1, 0, 2, 2]

Before: [3, 2, 1, 3]
9 3 0 0
After:  [1, 2, 1, 3]

Before: [2, 1, 3, 2]
0 1 2 3
After:  [2, 1, 3, 0]

Before: [2, 2, 2, 0]
3 2 2 0
After:  [4, 2, 2, 0]

Before: [3, 3, 2, 3]
15 2 3 1
After:  [3, 0, 2, 3]

Before: [3, 0, 1, 1]
10 1 0 3
After:  [3, 0, 1, 0]

Before: [0, 1, 3, 3]
6 0 0 1
After:  [0, 0, 3, 3]

Before: [0, 0, 3, 3]
9 3 2 0
After:  [1, 0, 3, 3]

Before: [0, 2, 1, 1]
1 2 3 0
After:  [2, 2, 1, 1]

Before: [2, 3, 1, 0]
14 0 3 1
After:  [2, 1, 1, 0]

Before: [3, 0, 0, 3]
9 3 0 1
After:  [3, 1, 0, 3]

Before: [0, 0, 0, 2]
6 0 0 0
After:  [0, 0, 0, 2]

Before: [1, 3, 2, 0]
8 0 2 3
After:  [1, 3, 2, 0]

Before: [0, 3, 1, 1]
13 0 3 1
After:  [0, 0, 1, 1]

Before: [1, 2, 1, 1]
1 2 3 0
After:  [2, 2, 1, 1]

Before: [0, 1, 1, 2]
13 0 1 3
After:  [0, 1, 1, 0]

Before: [1, 2, 0, 0]
2 0 2 0
After:  [0, 2, 0, 0]

Before: [0, 0, 0, 0]
6 0 0 1
After:  [0, 0, 0, 0]

Before: [0, 0, 3, 0]
12 3 2 0
After:  [1, 0, 3, 0]

Before: [0, 3, 2, 2]
4 3 2 3
After:  [0, 3, 2, 0]

Before: [3, 3, 3, 2]
7 3 3 2
After:  [3, 3, 0, 2]

Before: [0, 2, 0, 1]
13 0 3 1
After:  [0, 0, 0, 1]

Before: [3, 1, 3, 1]
0 1 2 3
After:  [3, 1, 3, 0]

Before: [3, 1, 2, 0]
5 1 2 1
After:  [3, 0, 2, 0]

Before: [0, 1, 2, 0]
5 1 2 0
After:  [0, 1, 2, 0]

Before: [0, 1, 3, 3]
0 1 2 2
After:  [0, 1, 0, 3]

Before: [1, 0, 0, 2]
2 0 2 1
After:  [1, 0, 0, 2]

Before: [2, 3, 1, 3]
15 2 3 2
After:  [2, 3, 0, 3]

Before: [2, 2, 1, 2]
7 3 3 1
After:  [2, 0, 1, 2]

Before: [0, 1, 0, 2]
7 3 3 3
After:  [0, 1, 0, 0]

Before: [1, 1, 2, 2]
3 3 2 2
After:  [1, 1, 4, 2]

Before: [2, 0, 1, 1]
1 2 3 1
After:  [2, 2, 1, 1]

Before: [1, 2, 0, 1]
2 0 2 2
After:  [1, 2, 0, 1]

Before: [0, 1, 1, 0]
6 0 0 2
After:  [0, 1, 0, 0]

Before: [2, 0, 2, 3]
3 0 2 1
After:  [2, 4, 2, 3]

Before: [0, 1, 2, 0]
5 1 2 1
After:  [0, 0, 2, 0]

Before: [2, 2, 2, 3]
3 0 2 0
After:  [4, 2, 2, 3]

Before: [1, 1, 2, 3]
15 2 3 0
After:  [0, 1, 2, 3]

Before: [0, 1, 2, 1]
3 2 2 2
After:  [0, 1, 4, 1]

Before: [2, 1, 2, 3]
5 1 2 2
After:  [2, 1, 0, 3]

Before: [3, 3, 0, 2]
12 2 3 0
After:  [1, 3, 0, 2]

Before: [3, 1, 3, 1]
0 1 2 1
After:  [3, 0, 3, 1]

Before: [3, 0, 3, 0]
12 3 2 1
After:  [3, 1, 3, 0]

Before: [2, 2, 2, 0]
14 0 3 1
After:  [2, 1, 2, 0]

Before: [1, 1, 0, 1]
2 0 2 0
After:  [0, 1, 0, 1]

Before: [3, 3, 1, 1]
1 2 3 3
After:  [3, 3, 1, 2]

Before: [0, 3, 0, 2]
12 2 3 1
After:  [0, 1, 0, 2]

Before: [1, 1, 2, 2]
3 2 2 0
After:  [4, 1, 2, 2]

Before: [3, 2, 2, 1]
11 3 2 3
After:  [3, 2, 2, 1]

Before: [0, 1, 2, 1]
13 0 1 3
After:  [0, 1, 2, 0]

Before: [1, 1, 1, 2]
1 2 0 1
After:  [1, 2, 1, 2]

Before: [0, 3, 2, 1]
11 3 2 2
After:  [0, 3, 1, 1]

Before: [1, 1, 3, 3]
0 1 2 3
After:  [1, 1, 3, 0]

Before: [3, 1, 0, 2]
4 0 2 0
After:  [1, 1, 0, 2]

Before: [1, 1, 3, 0]
0 1 2 2
After:  [1, 1, 0, 0]

Before: [1, 2, 0, 2]
2 0 2 1
After:  [1, 0, 0, 2]

Before: [1, 0, 1, 2]
1 2 0 0
After:  [2, 0, 1, 2]

Before: [3, 1, 2, 1]
5 1 2 0
After:  [0, 1, 2, 1]

Before: [2, 2, 2, 1]
11 3 2 2
After:  [2, 2, 1, 1]

Before: [0, 1, 2, 0]
5 1 2 3
After:  [0, 1, 2, 0]

Before: [3, 3, 1, 2]
7 3 3 1
After:  [3, 0, 1, 2]

Before: [3, 1, 2, 2]
5 1 2 2
After:  [3, 1, 0, 2]

Before: [1, 3, 0, 3]
2 0 2 3
After:  [1, 3, 0, 0]

Before: [1, 1, 2, 0]
5 1 2 0
After:  [0, 1, 2, 0]

Before: [1, 1, 2, 2]
3 3 2 1
After:  [1, 4, 2, 2]

Before: [3, 0, 2, 1]
10 1 0 0
After:  [0, 0, 2, 1]

Before: [0, 0, 1, 1]
1 2 3 1
After:  [0, 2, 1, 1]

Before: [0, 3, 2, 1]
11 3 2 0
After:  [1, 3, 2, 1]

Before: [3, 3, 0, 3]
10 2 0 1
After:  [3, 0, 0, 3]

Before: [2, 2, 3, 1]
9 2 3 2
After:  [2, 2, 0, 1]

Before: [1, 1, 2, 1]
8 0 2 2
After:  [1, 1, 0, 1]

Before: [2, 1, 2, 1]
5 1 2 0
After:  [0, 1, 2, 1]

Before: [3, 1, 3, 0]
12 3 2 0
After:  [1, 1, 3, 0]

Before: [1, 0, 0, 2]
12 2 3 2
After:  [1, 0, 1, 2]

Before: [1, 3, 2, 1]
8 0 2 0
After:  [0, 3, 2, 1]

Before: [3, 2, 2, 3]
3 1 2 2
After:  [3, 2, 4, 3]

Before: [0, 2, 2, 2]
4 3 2 3
After:  [0, 2, 2, 0]

Before: [3, 1, 2, 1]
5 1 2 3
After:  [3, 1, 2, 0]

Before: [0, 2, 0, 2]
6 0 0 2
After:  [0, 2, 0, 2]

Before: [3, 1, 0, 3]
15 1 3 1
After:  [3, 0, 0, 3]

Before: [2, 2, 2, 0]
3 0 2 0
After:  [4, 2, 2, 0]

Before: [0, 0, 0, 2]
12 2 3 1
After:  [0, 1, 0, 2]

Before: [3, 1, 3, 3]
9 3 0 1
After:  [3, 1, 3, 3]

Before: [1, 0, 2, 1]
11 3 2 3
After:  [1, 0, 2, 1]

Before: [2, 1, 0, 0]
14 0 3 2
After:  [2, 1, 1, 0]

Before: [3, 0, 2, 2]
10 1 0 1
After:  [3, 0, 2, 2]

Before: [2, 2, 1, 1]
1 2 3 1
After:  [2, 2, 1, 1]

Before: [0, 2, 2, 3]
15 1 3 2
After:  [0, 2, 0, 3]

Before: [1, 3, 0, 3]
2 0 2 2
After:  [1, 3, 0, 3]

Before: [3, 1, 2, 1]
11 3 2 0
After:  [1, 1, 2, 1]

Before: [2, 1, 2, 1]
11 3 2 0
After:  [1, 1, 2, 1]

Before: [1, 1, 2, 3]
8 0 2 1
After:  [1, 0, 2, 3]

Before: [2, 1, 2, 3]
5 1 2 0
After:  [0, 1, 2, 3]

Before: [1, 1, 0, 2]
7 3 3 1
After:  [1, 0, 0, 2]

Before: [0, 0, 2, 3]
15 2 3 2
After:  [0, 0, 0, 3]

Before: [1, 3, 0, 0]
2 0 2 0
After:  [0, 3, 0, 0]

Before: [3, 2, 2, 2]
9 2 1 3
After:  [3, 2, 2, 1]

Before: [2, 3, 3, 0]
12 3 2 3
After:  [2, 3, 3, 1]

Before: [3, 0, 1, 1]
7 2 3 0
After:  [0, 0, 1, 1]

Before: [3, 1, 3, 0]
0 1 2 0
After:  [0, 1, 3, 0]

Before: [0, 2, 2, 1]
11 3 2 2
After:  [0, 2, 1, 1]

Before: [1, 1, 1, 3]
15 1 3 2
After:  [1, 1, 0, 3]

Before: [2, 3, 3, 1]
9 2 3 2
After:  [2, 3, 0, 1]

Before: [0, 2, 0, 3]
6 0 0 0
After:  [0, 2, 0, 3]

Before: [2, 3, 1, 0]
14 0 3 0
After:  [1, 3, 1, 0]

Before: [2, 3, 2, 0]
14 0 3 2
After:  [2, 3, 1, 0]

Before: [0, 3, 1, 1]
6 0 0 2
After:  [0, 3, 0, 1]

Before: [2, 0, 1, 1]
1 2 3 3
After:  [2, 0, 1, 2]

Before: [1, 2, 1, 3]
1 2 0 1
After:  [1, 2, 1, 3]

Before: [3, 1, 2, 1]
5 1 2 2
After:  [3, 1, 0, 1]

Before: [1, 3, 2, 3]
8 0 2 0
After:  [0, 3, 2, 3]

Before: [3, 1, 0, 1]
4 3 1 0
After:  [0, 1, 0, 1]

Before: [0, 3, 2, 1]
11 3 2 1
After:  [0, 1, 2, 1]

Before: [2, 1, 3, 2]
0 1 2 2
After:  [2, 1, 0, 2]

Before: [2, 2, 1, 0]
14 0 3 0
After:  [1, 2, 1, 0]

Before: [1, 2, 2, 1]
11 3 2 1
After:  [1, 1, 2, 1]

Before: [2, 2, 2, 0]
14 0 3 3
After:  [2, 2, 2, 1]

Before: [3, 1, 1, 1]
1 2 3 3
After:  [3, 1, 1, 2]

Before: [1, 2, 2, 1]
11 3 2 0
After:  [1, 2, 2, 1]

Before: [3, 3, 0, 2]
4 0 2 1
After:  [3, 1, 0, 2]

Before: [0, 1, 0, 1]
6 0 0 1
After:  [0, 0, 0, 1]

Before: [3, 3, 2, 3]
9 3 0 0
After:  [1, 3, 2, 3]

Before: [0, 2, 1, 3]
13 0 2 3
After:  [0, 2, 1, 0]

Before: [0, 2, 1, 1]
6 0 0 3
After:  [0, 2, 1, 0]

Before: [1, 2, 0, 0]
2 0 2 3
After:  [1, 2, 0, 0]

Before: [2, 1, 0, 2]
7 3 3 0
After:  [0, 1, 0, 2]

Before: [3, 1, 2, 1]
11 3 2 3
After:  [3, 1, 2, 1]

Before: [0, 2, 0, 1]
6 0 0 2
After:  [0, 2, 0, 1]

Before: [1, 2, 2, 1]
8 0 2 3
After:  [1, 2, 2, 0]

Before: [0, 0, 2, 2]
6 0 0 0
After:  [0, 0, 2, 2]

Before: [0, 2, 3, 1]
6 0 0 2
After:  [0, 2, 0, 1]

Before: [3, 2, 0, 2]
12 2 3 3
After:  [3, 2, 0, 1]

Before: [2, 1, 3, 0]
12 3 2 1
After:  [2, 1, 3, 0]

Before: [3, 1, 1, 0]
4 2 1 1
After:  [3, 0, 1, 0]

Before: [2, 1, 2, 1]
11 3 2 3
After:  [2, 1, 2, 1]

Before: [1, 0, 2, 0]
8 0 2 1
After:  [1, 0, 2, 0]

Before: [3, 0, 2, 0]
3 2 2 0
After:  [4, 0, 2, 0]

Before: [2, 2, 1, 3]
15 2 3 2
After:  [2, 2, 0, 3]

Before: [1, 0, 3, 1]
7 3 3 1
After:  [1, 0, 3, 1]

Before: [0, 1, 2, 1]
11 3 2 2
After:  [0, 1, 1, 1]

Before: [1, 0, 1, 0]
1 2 0 1
After:  [1, 2, 1, 0]

Before: [0, 1, 3, 3]
13 0 1 1
After:  [0, 0, 3, 3]

Before: [1, 3, 0, 0]
2 0 2 2
After:  [1, 3, 0, 0]

Before: [0, 1, 1, 1]
13 0 1 0
After:  [0, 1, 1, 1]

Before: [1, 0, 1, 2]
1 2 0 2
After:  [1, 0, 2, 2]

Before: [0, 3, 2, 1]
13 0 1 3
After:  [0, 3, 2, 0]

Before: [2, 0, 0, 0]
14 0 3 2
After:  [2, 0, 1, 0]

Before: [1, 1, 1, 1]
1 2 0 0
After:  [2, 1, 1, 1]

Before: [3, 0, 1, 3]
10 1 0 1
After:  [3, 0, 1, 3]

Before: [1, 2, 1, 2]
7 3 3 1
After:  [1, 0, 1, 2]

Before: [0, 1, 2, 2]
5 1 2 1
After:  [0, 0, 2, 2]

Before: [0, 0, 2, 1]
6 0 0 0
After:  [0, 0, 2, 1]

Before: [1, 1, 0, 2]
2 0 2 3
After:  [1, 1, 0, 0]

Before: [2, 2, 3, 0]
14 0 3 2
After:  [2, 2, 1, 0]

Before: [1, 1, 3, 1]
0 1 2 2
After:  [1, 1, 0, 1]

Before: [1, 3, 1, 1]
7 3 3 0
After:  [0, 3, 1, 1]

Before: [0, 0, 3, 0]
6 0 0 1
After:  [0, 0, 3, 0]

Before: [3, 1, 3, 0]
0 1 2 1
After:  [3, 0, 3, 0]

Before: [1, 2, 2, 1]
8 0 2 1
After:  [1, 0, 2, 1]

Before: [1, 2, 0, 3]
2 0 2 2
After:  [1, 2, 0, 3]

Before: [1, 1, 0, 2]
12 2 3 1
After:  [1, 1, 0, 2]

Before: [0, 0, 3, 0]
12 3 2 2
After:  [0, 0, 1, 0]

Before: [1, 2, 0, 2]
2 0 2 3
After:  [1, 2, 0, 0]

Before: [0, 2, 3, 1]
13 0 3 3
After:  [0, 2, 3, 0]

Before: [0, 2, 2, 1]
11 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 3, 2, 2]
8 0 2 3
After:  [1, 3, 2, 0]

Before: [1, 1, 1, 3]
1 2 0 1
After:  [1, 2, 1, 3]

Before: [3, 0, 0, 1]
10 1 0 0
After:  [0, 0, 0, 1]

Before: [2, 1, 1, 1]
7 2 3 0
After:  [0, 1, 1, 1]

Before: [0, 1, 2, 2]
5 1 2 0
After:  [0, 1, 2, 2]

Before: [0, 2, 1, 2]
6 0 0 1
After:  [0, 0, 1, 2]

Before: [0, 3, 3, 1]
7 3 3 2
After:  [0, 3, 0, 1]

Before: [1, 1, 2, 1]
8 0 2 1
After:  [1, 0, 2, 1]

Before: [1, 1, 2, 1]
11 3 2 3
After:  [1, 1, 2, 1]

Before: [0, 1, 1, 3]
13 0 2 2
After:  [0, 1, 0, 3]

Before: [2, 2, 2, 2]
3 1 2 0
After:  [4, 2, 2, 2]

Before: [0, 3, 1, 1]
1 2 3 0
After:  [2, 3, 1, 1]

Before: [1, 1, 0, 3]
2 0 2 2
After:  [1, 1, 0, 3]

Before: [2, 1, 3, 1]
0 1 2 0
After:  [0, 1, 3, 1]

Before: [1, 1, 0, 0]
2 0 2 1
After:  [1, 0, 0, 0]

Before: [3, 2, 1, 1]
1 2 3 2
After:  [3, 2, 2, 1]

Before: [2, 3, 2, 3]
9 2 0 3
After:  [2, 3, 2, 1]

Before: [0, 0, 0, 1]
6 0 0 3
After:  [0, 0, 0, 0]

Before: [2, 2, 3, 3]
15 1 3 3
After:  [2, 2, 3, 0]

Before: [1, 0, 2, 3]
8 0 2 3
After:  [1, 0, 2, 0]

Before: [1, 1, 0, 2]
2 0 2 0
After:  [0, 1, 0, 2]

Before: [1, 1, 0, 2]
2 0 2 1
After:  [1, 0, 0, 2]

Before: [0, 0, 0, 1]
6 0 0 1
After:  [0, 0, 0, 1]

Before: [1, 3, 2, 1]
8 0 2 1
After:  [1, 0, 2, 1]

Before: [2, 0, 1, 0]
10 1 0 2
After:  [2, 0, 0, 0]

Before: [1, 2, 0, 1]
2 0 2 0
After:  [0, 2, 0, 1]

Before: [0, 2, 2, 3]
15 1 3 3
After:  [0, 2, 2, 0]

Before: [2, 1, 2, 3]
5 1 2 1
After:  [2, 0, 2, 3]

Before: [1, 3, 2, 1]
8 0 2 3
After:  [1, 3, 2, 0]

Before: [1, 1, 2, 2]
5 1 2 3
After:  [1, 1, 2, 0]

Before: [0, 1, 2, 1]
4 3 1 1
After:  [0, 0, 2, 1]

Before: [3, 1, 3, 0]
0 1 2 2
After:  [3, 1, 0, 0]

Before: [2, 0, 2, 2]
3 0 2 0
After:  [4, 0, 2, 2]

Before: [0, 1, 3, 1]
0 1 2 0
After:  [0, 1, 3, 1]

Before: [2, 1, 2, 2]
5 1 2 1
After:  [2, 0, 2, 2]

Before: [1, 3, 0, 0]
2 0 2 3
After:  [1, 3, 0, 0]

Before: [1, 2, 2, 3]
3 2 2 0
After:  [4, 2, 2, 3]

Before: [0, 3, 2, 0]
6 0 0 2
After:  [0, 3, 0, 0]

Before: [0, 3, 2, 3]
13 0 3 3
After:  [0, 3, 2, 0]

Before: [3, 0, 0, 0]
4 0 2 3
After:  [3, 0, 0, 1]

Before: [2, 3, 2, 2]
4 3 2 1
After:  [2, 0, 2, 2]

Before: [2, 2, 2, 0]
3 0 2 2
After:  [2, 2, 4, 0]

Before: [3, 0, 3, 3]
9 3 0 3
After:  [3, 0, 3, 1]

Before: [0, 1, 2, 2]
13 0 1 3
After:  [0, 1, 2, 0]

Before: [1, 1, 1, 1]
1 2 3 3
After:  [1, 1, 1, 2]

Before: [2, 2, 3, 2]
4 2 0 0
After:  [1, 2, 3, 2]

Before: [3, 1, 3, 3]
15 1 3 0
After:  [0, 1, 3, 3]

Before: [0, 1, 1, 3]
6 0 0 1
After:  [0, 0, 1, 3]

Before: [0, 3, 1, 1]
6 0 0 1
After:  [0, 0, 1, 1]

Before: [3, 0, 0, 3]
9 3 0 2
After:  [3, 0, 1, 3]

Before: [0, 3, 3, 1]
9 2 3 2
After:  [0, 3, 0, 1]

Before: [2, 0, 1, 0]
14 0 3 3
After:  [2, 0, 1, 1]

Before: [0, 2, 3, 0]
6 0 0 3
After:  [0, 2, 3, 0]

Before: [1, 3, 0, 2]
2 0 2 1
After:  [1, 0, 0, 2]

Before: [1, 1, 2, 1]
11 3 2 0
After:  [1, 1, 2, 1]

Before: [1, 1, 2, 3]
8 0 2 0
After:  [0, 1, 2, 3]

Before: [3, 1, 2, 2]
5 1 2 3
After:  [3, 1, 2, 0]

Before: [1, 0, 0, 2]
2 0 2 2
After:  [1, 0, 0, 2]

Before: [2, 0, 3, 0]
12 3 2 3
After:  [2, 0, 3, 1]

Before: [1, 1, 2, 1]
8 0 2 3
After:  [1, 1, 2, 0]

Before: [1, 1, 2, 0]
8 0 2 1
After:  [1, 0, 2, 0]

Before: [3, 1, 2, 2]
5 1 2 0
After:  [0, 1, 2, 2]

Before: [1, 2, 2, 2]
8 0 2 3
After:  [1, 2, 2, 0]

Before: [3, 3, 0, 0]
10 2 0 2
After:  [3, 3, 0, 0]

Before: [0, 3, 2, 2]
6 0 0 2
After:  [0, 3, 0, 2]

Before: [3, 0, 3, 1]
10 1 0 0
After:  [0, 0, 3, 1]

Before: [2, 3, 1, 1]
7 2 3 1
After:  [2, 0, 1, 1]

Before: [3, 1, 2, 3]
3 2 2 1
After:  [3, 4, 2, 3]

Before: [0, 2, 2, 3]
15 1 3 1
After:  [0, 0, 2, 3]

Before: [0, 3, 2, 1]
6 0 0 0
After:  [0, 3, 2, 1]

Before: [0, 1, 3, 0]
6 0 0 3
After:  [0, 1, 3, 0]

Before: [1, 3, 2, 1]
7 3 3 1
After:  [1, 0, 2, 1]

Before: [1, 0, 0, 1]
2 0 2 1
After:  [1, 0, 0, 1]

Before: [3, 1, 0, 2]
12 2 3 3
After:  [3, 1, 0, 1]

Before: [3, 0, 2, 3]
10 1 0 0
After:  [0, 0, 2, 3]

Before: [3, 2, 2, 1]
11 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 1, 2, 3]
5 1 2 1
After:  [1, 0, 2, 3]

Before: [1, 1, 0, 1]
2 0 2 3
After:  [1, 1, 0, 0]

Before: [2, 1, 2, 2]
5 1 2 0
After:  [0, 1, 2, 2]

Before: [0, 3, 3, 1]
6 0 0 3
After:  [0, 3, 3, 0]

Before: [3, 2, 2, 3]
9 2 1 3
After:  [3, 2, 2, 1]

Before: [1, 1, 2, 1]
8 0 2 0
After:  [0, 1, 2, 1]

Before: [2, 2, 1, 0]
14 0 3 2
After:  [2, 2, 1, 0]

Before: [3, 2, 2, 3]
9 2 1 2
After:  [3, 2, 1, 3]

Before: [1, 2, 2, 2]
8 0 2 2
After:  [1, 2, 0, 2]

Before: [1, 0, 2, 2]
8 0 2 0
After:  [0, 0, 2, 2]

Before: [1, 3, 0, 1]
2 0 2 1
After:  [1, 0, 0, 1]

Before: [3, 2, 3, 3]
15 1 3 3
After:  [3, 2, 3, 0]

Before: [0, 2, 0, 3]
6 0 0 1
After:  [0, 0, 0, 3]

Before: [2, 1, 3, 1]
0 1 2 1
After:  [2, 0, 3, 1]

Before: [1, 3, 0, 1]
2 0 2 0
After:  [0, 3, 0, 1]

Before: [2, 1, 2, 1]
5 1 2 1
After:  [2, 0, 2, 1]

Before: [1, 3, 0, 2]
12 2 3 2
After:  [1, 3, 1, 2]

Before: [0, 3, 0, 1]
13 0 1 2
After:  [0, 3, 0, 1]

Before: [3, 3, 0, 1]
7 3 3 3
After:  [3, 3, 0, 0]

Before: [0, 3, 0, 0]
13 0 1 2
After:  [0, 3, 0, 0]

Before: [2, 1, 1, 0]
4 2 1 3
After:  [2, 1, 1, 0]

Before: [3, 0, 0, 3]
10 1 0 1
After:  [3, 0, 0, 3]

Before: [2, 0, 2, 3]
15 2 3 0
After:  [0, 0, 2, 3]

Before: [1, 0, 0, 2]
2 0 2 3
After:  [1, 0, 0, 0]

Before: [1, 1, 0, 3]
2 0 2 0
After:  [0, 1, 0, 3]

Before: [3, 0, 0, 0]
10 2 0 3
After:  [3, 0, 0, 0]

Before: [3, 0, 2, 1]
11 3 2 0
After:  [1, 0, 2, 1]

Before: [3, 0, 0, 3]
10 2 0 2
After:  [3, 0, 0, 3]
'''

test_program_inp = '''
13 0 0 0
3 0 2 0
8 3 0 1
13 0 0 3
3 3 1 3
4 0 1 0
13 0 1 0
1 2 0 2
8 2 1 3
8 1 2 0
13 0 0 1
3 1 0 1
2 0 3 1
13 1 3 1
13 1 3 1
1 2 1 2
11 2 0 0
8 3 0 2
8 3 2 1
8 0 0 3
12 3 2 2
13 2 2 2
13 2 1 2
1 0 2 0
11 0 3 1
8 3 1 3
8 0 2 2
8 0 3 0
0 3 2 3
13 3 1 3
1 1 3 1
11 1 1 3
8 3 1 0
8 0 2 1
13 3 0 2
3 2 2 2
4 2 0 1
13 1 3 1
1 3 1 3
11 3 2 1
8 0 2 3
8 1 0 0
15 3 2 2
13 2 3 2
1 1 2 1
11 1 2 3
8 3 0 1
8 2 0 2
11 0 2 2
13 2 3 2
1 2 3 3
11 3 2 0
13 2 0 2
3 2 3 2
8 3 1 3
0 3 2 3
13 3 1 3
1 3 0 0
11 0 3 1
8 2 2 3
8 2 1 2
8 3 0 0
4 2 0 3
13 3 1 3
1 3 1 1
11 1 0 2
8 3 3 3
8 2 2 0
13 1 0 1
3 1 0 1
5 3 0 3
13 3 1 3
1 2 3 2
11 2 3 1
8 1 1 0
8 0 2 3
8 2 0 2
11 0 2 3
13 3 1 3
1 3 1 1
13 2 0 3
3 3 3 3
8 2 3 0
13 2 0 2
3 2 3 2
7 0 2 3
13 3 3 3
1 3 1 1
8 2 0 2
13 3 0 3
3 3 1 3
2 3 0 0
13 0 2 0
13 0 1 0
1 1 0 1
8 2 3 0
8 2 0 3
10 2 3 2
13 2 3 2
13 2 3 2
1 2 1 1
11 1 1 0
8 0 1 1
8 1 0 3
13 2 0 2
3 2 0 2
3 3 1 3
13 3 3 3
1 0 3 0
11 0 2 2
8 2 0 3
13 0 0 0
3 0 2 0
9 0 3 0
13 0 1 0
13 0 2 0
1 2 0 2
8 3 1 1
8 3 2 3
8 2 1 0
5 1 0 0
13 0 1 0
1 2 0 2
11 2 1 3
8 2 3 0
13 1 0 2
3 2 2 2
8 1 2 1
2 1 0 2
13 2 3 2
1 3 2 3
11 3 3 2
8 1 3 0
8 3 0 3
1 1 0 3
13 3 3 3
1 2 3 2
11 2 2 1
8 3 3 3
8 2 2 2
11 0 2 0
13 0 2 0
13 0 3 0
1 0 1 1
11 1 1 0
8 2 3 3
8 2 1 1
10 1 3 3
13 3 2 3
1 0 3 0
11 0 2 2
8 1 2 0
8 3 2 3
1 0 0 3
13 3 2 3
13 3 1 3
1 2 3 2
11 2 2 0
8 1 1 1
13 2 0 2
3 2 2 2
13 2 0 3
3 3 0 3
15 3 2 1
13 1 1 1
13 1 2 1
1 1 0 0
11 0 0 3
8 1 1 2
13 0 0 1
3 1 2 1
8 3 3 0
0 0 2 0
13 0 1 0
13 0 2 0
1 3 0 3
11 3 0 0
8 1 3 1
8 2 0 3
8 0 1 2
13 1 2 3
13 3 1 3
1 3 0 0
13 1 0 3
3 3 0 3
8 3 0 2
8 0 2 1
12 3 2 3
13 3 1 3
13 3 2 3
1 0 3 0
11 0 3 2
8 0 0 3
13 1 0 0
3 0 1 0
8 2 1 1
10 1 3 1
13 1 2 1
1 1 2 2
11 2 1 3
8 2 0 2
8 2 3 1
11 0 2 2
13 2 2 2
13 2 2 2
1 2 3 3
11 3 3 2
8 1 0 3
13 0 0 1
3 1 0 1
3 3 1 3
13 3 1 3
1 3 2 2
11 2 3 1
8 2 1 2
8 2 3 3
11 0 2 2
13 2 1 2
1 2 1 1
11 1 2 2
8 1 0 3
13 3 0 0
3 0 2 0
8 0 1 1
14 0 3 1
13 1 3 1
1 1 2 2
11 2 2 1
8 1 1 0
8 3 1 2
1 0 0 0
13 0 1 0
1 0 1 1
13 2 0 0
3 0 3 0
13 3 0 2
3 2 1 2
8 0 3 3
0 0 2 2
13 2 1 2
1 1 2 1
11 1 3 0
8 1 1 3
8 2 1 2
8 3 3 1
3 3 1 3
13 3 2 3
1 3 0 0
8 1 0 2
8 2 1 1
8 0 3 3
10 1 3 1
13 1 1 1
1 0 1 0
11 0 3 3
8 3 0 1
8 1 1 0
8 0 1 2
3 0 1 2
13 2 1 2
1 2 3 3
13 2 0 2
3 2 3 2
8 2 2 0
5 1 0 2
13 2 2 2
1 3 2 3
11 3 0 0
8 2 2 2
8 2 1 3
5 1 3 3
13 3 1 3
1 3 0 0
11 0 1 1
8 3 0 2
8 1 2 0
8 0 1 3
8 2 3 3
13 3 3 3
1 3 1 1
8 2 3 2
8 3 3 0
8 1 3 3
6 2 0 0
13 0 2 0
13 0 1 0
1 1 0 1
11 1 3 3
8 1 2 0
13 2 0 1
3 1 3 1
4 2 1 2
13 2 1 2
1 2 3 3
8 3 0 0
8 2 3 2
4 2 0 1
13 1 1 1
1 3 1 3
11 3 1 0
8 2 3 1
8 0 1 3
15 3 2 1
13 1 1 1
13 1 1 1
1 1 0 0
11 0 1 1
8 0 3 0
15 3 2 3
13 3 2 3
13 3 3 3
1 1 3 1
13 3 0 0
3 0 2 0
8 0 2 2
13 1 0 3
3 3 1 3
13 3 2 0
13 0 3 0
1 1 0 1
8 0 0 3
8 3 2 0
7 2 0 0
13 0 3 0
1 0 1 1
11 1 1 2
8 1 0 0
8 1 1 3
8 1 2 1
1 3 0 3
13 3 3 3
1 3 2 2
11 2 1 3
8 0 2 1
8 0 3 2
13 0 2 1
13 1 1 1
13 1 1 1
1 3 1 3
11 3 1 1
8 3 3 2
8 0 3 3
8 2 0 0
10 0 3 3
13 3 2 3
1 3 1 1
11 1 0 3
8 2 2 1
8 2 2 2
8 3 1 0
4 2 0 2
13 2 1 2
1 3 2 3
8 1 0 0
13 2 0 2
3 2 0 2
8 1 1 1
1 0 0 0
13 0 1 0
1 3 0 3
11 3 3 1
8 2 2 3
8 2 2 0
9 0 3 3
13 3 2 3
13 3 2 3
1 1 3 1
11 1 3 3
8 1 3 0
8 3 1 1
8 2 3 2
11 0 2 0
13 0 1 0
1 0 3 3
11 3 1 0
8 3 2 3
13 0 0 1
3 1 2 1
8 1 3 2
0 3 2 2
13 2 3 2
13 2 2 2
1 2 0 0
11 0 0 1
8 3 1 0
8 2 0 3
8 0 0 2
7 2 0 2
13 2 3 2
13 2 2 2
1 1 2 1
11 1 3 3
8 2 1 2
8 1 2 0
8 0 2 1
11 0 2 0
13 0 2 0
1 3 0 3
11 3 3 2
8 2 2 0
8 0 0 3
10 0 3 0
13 0 1 0
1 2 0 2
11 2 1 3
8 2 2 0
8 1 1 1
8 3 3 2
13 1 2 0
13 0 3 0
13 0 3 0
1 0 3 3
11 3 0 1
8 1 0 3
8 2 3 0
7 0 2 0
13 0 1 0
1 1 0 1
11 1 3 2
8 2 1 0
13 2 0 1
3 1 3 1
14 0 3 3
13 3 1 3
1 3 2 2
11 2 0 0
8 2 2 1
13 0 0 2
3 2 0 2
13 0 0 3
3 3 2 3
12 2 3 2
13 2 1 2
13 2 2 2
1 2 0 0
11 0 0 1
13 2 0 3
3 3 1 3
8 3 3 2
8 2 2 0
14 0 3 2
13 2 1 2
13 2 2 2
1 2 1 1
11 1 0 0
8 3 1 3
13 1 0 2
3 2 3 2
13 0 0 1
3 1 2 1
6 1 2 1
13 1 1 1
1 0 1 0
11 0 1 2
8 2 1 0
8 1 1 3
8 0 2 1
2 3 0 0
13 0 2 0
13 0 1 0
1 0 2 2
11 2 3 0
8 3 1 3
8 3 1 1
8 2 2 2
4 2 1 3
13 3 2 3
13 3 3 3
1 3 0 0
8 3 3 2
13 0 0 3
3 3 3 3
8 1 3 1
13 1 2 2
13 2 2 2
13 2 2 2
1 0 2 0
11 0 3 2
8 2 2 0
13 0 0 1
3 1 2 1
8 2 2 3
10 0 3 1
13 1 2 1
1 1 2 2
11 2 3 3
13 3 0 0
3 0 3 0
8 0 1 2
8 3 2 1
7 2 0 1
13 1 2 1
1 3 1 3
13 2 0 1
3 1 1 1
7 2 0 0
13 0 1 0
13 0 3 0
1 3 0 3
11 3 3 1
8 2 1 2
8 3 2 3
13 0 0 0
3 0 3 0
4 2 0 0
13 0 2 0
1 1 0 1
11 1 3 3
8 1 3 2
8 2 3 0
8 3 3 1
5 1 0 0
13 0 1 0
1 0 3 3
8 2 0 2
8 1 0 0
8 0 0 1
11 0 2 2
13 2 3 2
1 3 2 3
11 3 0 1
13 0 0 0
3 0 2 0
8 2 1 3
8 3 2 2
9 0 3 3
13 3 2 3
1 3 1 1
11 1 1 3
8 3 3 1
8 2 2 2
13 2 0 0
3 0 1 0
4 2 1 0
13 0 3 0
1 3 0 3
11 3 0 1
13 1 0 3
3 3 1 3
13 0 0 2
3 2 3 2
8 1 2 0
13 0 2 3
13 3 1 3
13 3 3 3
1 1 3 1
11 1 3 0
8 0 2 1
8 0 1 3
8 2 3 2
13 2 1 2
1 2 0 0
13 3 0 2
3 2 2 2
13 2 0 1
3 1 3 1
4 2 1 1
13 1 3 1
1 0 1 0
11 0 0 1
8 1 2 2
8 2 3 0
8 3 0 2
13 2 2 2
1 2 1 1
11 1 1 0
8 1 0 1
8 1 1 2
8 1 3 3
1 3 3 2
13 2 2 2
1 0 2 0
11 0 1 1
8 3 2 0
8 2 3 2
8 0 0 3
4 2 0 3
13 3 3 3
1 1 3 1
11 1 0 0
8 3 2 2
8 0 0 1
8 3 0 3
8 2 3 3
13 3 1 3
1 3 0 0
11 0 0 2
13 2 0 0
3 0 2 0
8 1 0 1
8 2 1 3
9 0 3 1
13 1 1 1
13 1 2 1
1 2 1 2
11 2 2 0
8 3 0 1
8 1 0 2
0 1 2 2
13 2 3 2
13 2 3 2
1 2 0 0
8 2 2 1
8 2 1 2
8 0 0 3
15 3 2 3
13 3 1 3
1 3 0 0
11 0 2 3
8 3 3 0
8 3 3 2
8 0 1 1
0 0 2 0
13 0 2 0
13 0 2 0
1 3 0 3
11 3 1 1
8 2 0 0
8 3 2 3
7 0 2 2
13 2 2 2
1 1 2 1
11 1 1 0
8 0 3 3
13 1 0 2
3 2 2 2
8 0 0 1
15 3 2 1
13 1 3 1
1 0 1 0
11 0 0 1
8 3 3 0
13 3 0 2
3 2 1 2
8 1 1 3
1 3 3 0
13 0 2 0
1 0 1 1
11 1 1 0
8 3 0 3
13 0 0 2
3 2 3 2
8 2 2 1
8 2 3 1
13 1 2 1
1 1 0 0
11 0 0 2
8 2 2 0
8 1 2 1
8 1 2 3
2 3 0 3
13 3 2 3
1 3 2 2
8 3 0 1
13 1 0 3
3 3 2 3
9 0 3 1
13 1 2 1
13 1 2 1
1 1 2 2
8 1 3 0
8 2 3 1
10 1 3 3
13 3 1 3
1 2 3 2
11 2 1 1
8 2 1 3
8 3 3 2
1 0 0 2
13 2 3 2
1 1 2 1
8 2 2 0
13 3 0 2
3 2 2 2
9 0 3 3
13 3 1 3
1 3 1 1
8 2 2 3
8 1 2 2
13 0 0 0
3 0 1 0
2 0 3 2
13 2 1 2
1 1 2 1
8 0 1 0
8 3 3 2
8 3 0 2
13 2 1 2
1 2 1 1
11 1 1 2
8 3 0 0
8 0 1 1
5 0 3 1
13 1 1 1
13 1 1 1
1 1 2 2
11 2 0 1
13 2 0 0
3 0 1 0
8 3 0 2
8 0 2 3
12 3 2 0
13 0 1 0
1 0 1 1
11 1 2 0
8 3 0 1
13 1 0 2
3 2 0 2
8 3 2 3
8 2 1 1
13 1 3 1
13 1 3 1
1 1 0 0
11 0 3 1
8 0 3 3
8 3 2 2
8 1 1 0
12 3 2 2
13 2 3 2
13 2 2 2
1 2 1 1
11 1 0 3
13 0 0 0
3 0 0 0
8 1 2 1
13 1 0 2
3 2 0 2
8 2 1 0
13 0 2 0
1 0 3 3
11 3 1 0
13 0 0 3
3 3 0 3
8 3 3 1
13 3 0 2
3 2 2 2
15 3 2 2
13 2 2 2
13 2 2 2
1 0 2 0
8 1 0 1
8 0 3 2
8 2 2 3
2 1 3 1
13 1 2 1
1 1 0 0
11 0 2 1
8 2 2 2
8 2 3 0
9 0 3 0
13 0 1 0
13 0 3 0
1 1 0 1
8 0 2 0
13 3 0 2
3 2 0 2
12 2 3 2
13 2 3 2
13 2 1 2
1 2 1 1
11 1 2 0
13 3 0 2
3 2 1 2
8 2 1 1
8 0 0 3
10 1 3 2
13 2 1 2
13 2 2 2
1 0 2 0
11 0 3 3
8 1 1 1
8 3 2 0
8 3 0 2
13 1 2 0
13 0 2 0
1 3 0 3
11 3 3 0
8 2 0 1
8 0 2 3
6 1 2 2
13 2 2 2
1 2 0 0
11 0 2 2
8 0 0 1
8 2 1 0
8 3 0 0
13 0 1 0
13 0 2 0
1 0 2 2
11 2 3 3
8 3 3 2
8 3 0 1
8 2 1 0
4 0 1 2
13 2 3 2
1 3 2 3
11 3 2 2
8 2 2 3
13 1 0 1
3 1 2 1
10 1 3 3
13 3 3 3
1 2 3 2
11 2 3 3
8 0 3 0
8 0 1 2
8 3 3 1
0 1 2 1
13 1 1 1
13 1 2 1
1 1 3 3
11 3 1 2
8 1 1 1
13 2 0 3
3 3 2 3
2 1 3 1
13 1 2 1
13 1 2 1
1 2 1 2
11 2 1 3
8 2 2 2
13 2 0 1
3 1 0 1
8 3 3 0
6 2 0 2
13 2 1 2
13 2 3 2
1 3 2 3
11 3 2 0
13 0 0 3
3 3 0 3
8 3 0 2
8 3 2 1
12 3 2 1
13 1 3 1
13 1 2 1
1 0 1 0
11 0 2 2
8 1 2 1
8 2 0 0
10 0 3 3
13 3 2 3
1 3 2 2
11 2 1 1
8 2 1 3
8 3 0 2
6 0 2 3
13 3 1 3
13 3 2 3
1 3 1 1
11 1 1 2
13 2 0 3
3 3 1 3
8 0 2 1
14 0 3 0
13 0 1 0
1 2 0 2
11 2 3 0
8 1 0 2
8 2 3 3
8 1 3 3
13 3 2 3
13 3 2 3
1 3 0 0
11 0 0 3
8 3 1 2
13 0 0 0
3 0 2 0
7 0 2 2
13 2 1 2
1 2 3 3
11 3 1 1
8 2 0 2
8 0 0 0
8 1 1 3
8 3 0 2
13 2 1 2
1 1 2 1
11 1 0 0
8 2 0 3
8 1 1 1
13 1 0 2
3 2 3 2
2 1 3 2
13 2 2 2
1 2 0 0
8 3 2 1
8 0 0 2
5 1 3 2
13 2 3 2
1 0 2 0
11 0 2 3
8 2 2 2
8 2 1 0
8 1 3 1
2 1 0 0
13 0 1 0
1 3 0 3
11 3 0 1
8 2 1 3
13 0 0 2
3 2 1 2
8 1 1 0
1 0 0 3
13 3 3 3
1 3 1 1
8 2 0 0
8 2 3 3
13 2 0 2
3 2 0 2
9 0 3 0
13 0 3 0
1 0 1 1
11 1 3 0
8 2 2 2
8 0 3 3
8 0 1 1
15 3 2 2
13 2 3 2
1 0 2 0
11 0 2 3
8 3 2 0
13 3 0 2
3 2 2 2
6 2 0 0
13 0 1 0
1 0 3 3
11 3 3 0
8 3 3 3
8 0 3 2
8 2 2 1
5 3 1 2
13 2 3 2
13 2 1 2
1 0 2 0
11 0 0 1
8 2 0 0
8 0 0 3
8 0 0 2
10 0 3 3
13 3 1 3
1 3 1 1
11 1 2 3
8 3 3 2
8 0 1 1
8 2 1 1
13 1 1 1
13 1 1 1
1 3 1 3
11 3 1 0
'''

insts = [
    'addr',
    'addi',
    'mulr',
    'muli',
    'banr',
    'bani',
    'borr',
    'bori',
    'setr',
    'seti',
    'gtir',
    'gtri',
    'gtrr',
    'eqir',
    'eqri',
    'eqrr',
]
naive_translate = dict(enumerate(insts))

def exec_cmd(cmd, regs, translate):
    proccmd = translate[cmd[0]]
    a, b, c = cmd[1:]
    # make a copy
    result = list(regs)
    if proccmd == 'addr':
        result[c] = result[a] + result[b]
    elif proccmd == 'addi':
        result[c] = result[a] + b
    elif proccmd == 'mulr':
        result[c] = result[a] * result[b]
    elif proccmd == 'muli':
        result[c] = result[a] * b
    elif proccmd == 'banr':
        result[c] = result[a] & result[b]
    elif proccmd == 'bani':
        result[c] = result[a] & b
    elif proccmd == 'borr':
        result[c] = result[a] | result[b]
    elif proccmd == 'bori':
        result[c] = result[a] | b
    elif proccmd == 'setr':
        result[c] = result[a]
    elif proccmd == 'seti':
        result[c] = a
    elif proccmd == 'gtir':
        if a > result[b]:
            result[c] = 1
        else:
            result[c] = 0
    elif proccmd == 'gtri':
        if result[a] > b:
            result[c] = 1
        else:
            result[c] = 0
    elif proccmd == 'gtrr':
        if result[a] > result[b]:
            result[c] = 1
        else:
            result[c] = 0
    elif proccmd == 'eqir':
        if a == result[b]:
            result[c] = 1
        else:
            result[c] = 0
    elif proccmd == 'eqri':
        if result[a] == b:
            result[c] = 1
        else:
            result[c] = 0
    elif proccmd == 'eqrr':
        if result[a] == result[b]:
            result[c] = 1
        else:
            result[c] = 0
    return result

def possibilities(example):
    cmd, before, after = example
    return [t for t in xrange(len(insts)) if exec_cmd([t] + cmd[1:], before, naive_translate) == after]

def possibility_count(example):
    return len(possibilities(example))

def count_that_behave_like_three_or_more(examples):
    return sum(possibility_count(example) >= 3 for example in examples)

def only(set_with_one_elem):
    assert len(set_with_one_elem) == 1
    return list(set_with_one_elem)[0]

def derive_commands_for_opcodes(examples):
    '''Returns a dict from int -> cmd'''
    basic_mapping = {}
    for example in examples:
        cmd, _, _ = example
        if cmd[0] not in basic_mapping:
            basic_mapping[cmd[0]] = set(possibilities(example))
        else:
            basic_mapping[cmd[0]] &= set(possibilities(example))
    # run a stupid topsort
    # for each key, if there's exactly one value in the set,
    # that's what instruction it is
    while any(len(v) > 1 for v in basic_mapping.itervalues()):
        for k, v in basic_mapping.iteritems():
            if len(v) == 1:
                resolved = only(v)
                for k2, child in basic_mapping.iteritems():
                    if k != k2 and resolved in child:
                        child.remove(resolved)
    final_mapping = {k: insts[only(v)] for k, v in basic_mapping.iteritems()}
    return final_mapping

def parse_examples(example_inp):
    example_rows = example_inp.strip().split('\n\n')
    # tuples of cmd, before, after
    examples = []
    for row in example_rows:
        before_raw, cmd_raw, after_raw = row.split('\n')
        examples.append((map(int, cmd_raw.split()),
                         map(int, before_raw.split(': ')[1][1:-1].split(', ')),
                         map(int, after_raw.split(':  ')[1][1:-1].split(', '))))
    return examples

def parse_test_program(test_program_inp):
    program = []
    for row in test_program_inp.strip().split('\n'):
        program.append(map(int, row.split()))
    return program

# part 1
examples = parse_examples(example_inp)
print count_that_behave_like_three_or_more(examples)

# part 2
translator = derive_commands_for_opcodes(examples)
program = parse_test_program(test_program_inp)
regs = [0, 0, 0, 0]
for cmd in program:
    regs = exec_cmd(cmd, regs, translator)
print regs[0]
