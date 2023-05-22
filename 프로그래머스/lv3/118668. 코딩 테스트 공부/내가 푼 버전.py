def solution(alp, cop, problems):

    target_alp, target_cop = 0, 0

    for p in problems:
        target_alp = max(target_alp, p[0])
        target_cop = max(target_cop, p[1])

    dp = [[10 ** 9] * (target_cop + 1) for _ in range(target_alp + 1)]
    alp = min(alp, target_alp)
    cop = min(cop, target_cop)
    dp[alp][cop] = 0

    for i in range(alp, target_alp + 1):
        for j in range(cop, target_cop + 1):
            if i < target_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < target_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for p in problems:
                if i >= p[0] and j >= p[1]:
                    new_ap = min(target_alp, i + p[2])
                    new_cp = min(target_cop, j + p[3])
                    dp[new_ap][new_cp] = min(dp[new_ap][new_cp], dp[i][j] + p[4])

    return dp[target_alp][target_cop]