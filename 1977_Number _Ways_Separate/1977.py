class Solution(object):
    def numberOfCombinations(self, num):
        """
        :type num: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(num)
        if num[0] == '0':
            return 0
        lcp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if num[i] == num[j]:
                    lcp[i][j] = lcp[i+1][j+1] + 1
                else:
                    lcp[i][j] = 0
        dp = [[0] * (n+2) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for l in range(n - i, 0, -1):
                if num[i] == '0':
                    dp[i][l] = 0
                else:
                    j = i + l
                    if j == n:
                        dp[i][l] = 1
                    else:
                        if j + l <= n:
                            common = lcp[i][j]
                            if common >= l or num[i+common] <= num[j+common]:
                                dp[i][l] = dp[j][l]
                            else:
                                dp[i][l] = dp[j][l+1]
                        else:
                            dp[i][l] = 0
                dp[i][l] = (dp[i][l] + dp[i][l+1]) % MOD
        return dp[0][1] % MOD