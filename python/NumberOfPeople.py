def peopleAwareOfSecret(n, delay, forget):
    MOD = 10**9 + 7
    dp = [0] * (n + 1)
    dp[1] = 1
    share = 0

    for day in range(2, n + 1):
        if day - delay >= 1:
            share = (share + dp[day - delay]) % MOD
        if day - forget >= 1:
            share = (share - dp[day - forget]) % MOD
        dp[day] = share

    return sum(dp[n - forget + 1: n + 1]) % MOD


n = 4
delay = 1
forget = 3

result = peopleAwareOfSecret(n, delay, forget)
print("Number of people who know the secret on day", n, ":", result)
