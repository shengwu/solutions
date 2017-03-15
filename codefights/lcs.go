func longestCommonSubstring(s string, t string) int {
    slen := len(s) + 1
    tlen := len(t) + 1
    grid := make([][]int, slen)
    for i := 0; i < slen; i++ {
        grid[i] = make([]int, tlen)
    }
    max := 0
    for i := 1; i < slen; i++ {
        for j := 1; j < tlen; j++ {
            if s[i-1] == t[j-1] {
                grid[i][j] = grid[i-1][j-1] + 1
                if grid[i][j] > max {
                    max = grid[i][j]
                }
            }
        }
    }
    return max
}
