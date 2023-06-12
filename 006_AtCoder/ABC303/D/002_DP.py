"""
下記を参考にして作成したDP
[AtCoder ABC 303 D - Shift vs. CapsLock (茶色, 400 点) - けんちょんの競プロ精進記録](https://drken1215.hatenablog.com/entry/2023/05/28/213500)
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
    # CapsLockを押す場合を試す
    dp[i][0] = min(dp[i][0], dp[i][1] + Z)
    dp[i][1] = min(dp[i][1], dp[i][0] + Z)

    # キー入力をする
    if s == "a":
        # aを入力する場合
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + X)  # CapsLockがOFFの状態でaを押す
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + Y)  # CapsLockがONの状態でShift+aを押す
    else:
        # Aを入力する場合
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + Y)  # CapsLockがOFFの状態でShift+aを押す
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + X)  # CapsLockがONの状態でaを押す

# 出力
print(min(dp[-1][0], dp[-1][1]))
