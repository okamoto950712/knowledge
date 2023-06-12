"""
自分がすなおに実装したDP
"""
import math

# 入力
X, Y, Z = map(int, input().split())
S = input()

# DPの初期化
dp = [[math.inf for _ in range(2)] for _ in range(len(S) + 1)]
dp[0][0] = 0  # 0文字入力するのにかかる時間

# DPを回す
for i, s in enumerate(S):
    # キー入力をする
    if s == "a":  # aを入力する場合
        # CapsLockがOFFの状態でaを押す
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + X)
        # CapsLockがONの状態でCapsLockとaを押す
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][1] + Z + X)
        # CapsLockがONの状態でShift+aを押す
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + Y)
        # CapsLockがOFFの状態でCapsLockとShift+aを押す
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][0] + Z + Y)
    else:  # Aを入力する場合
        # CapsLockがOFFの状態でshift+aを押す
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + Y)
        # CapsLockがONの状態でCapsLockとShift+aを押す
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][1] + Z + Y)
        # CapsLockがONの状態でaを押す
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + X)
        # CapsLockがOFFの状態でCapsLockとaを押す
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][0] + Z + X)

# 出力
print(min(dp[-1][0], dp[-1][1]))
