class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)

        dp = [[False]*(n+1) for _ in range(m+1)]

        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m and j == n:
                    continue  
                match_inicial = (i < m) and (j < n) and (s[i] == p[j] or p[j] == '.')
                
                if j+1 < n and p[j+1] == '*':
                    if j+2 <= n:
                        dp[i][j] = dp[i][j+2] or (match_inicial and (i+1 <= m and dp[i+1][j]))
                else:
                    if match_inicial and i+1 <= m and j+1 <= n:
                        dp[i][j] = dp[i+1][j+1]
        
        return dp[0][0]