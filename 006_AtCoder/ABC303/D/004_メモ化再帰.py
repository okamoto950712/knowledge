"""
メモ化再帰
"""

import sys

sys.setrecursionlimit(10**6)

# 入力
X, Y, Z = map(int, input().split())
S = input()
cache = [[-1 for _ in range(2)] for _ in range(len(S) + 1)]


def f(i, c):  # iは文字列Sのインデックス、cはCapsLockの状態
    if i == len(S):
        return 0
    if cache[i][c] != -1:
        return cache[i][c]
    if S[i] == "a":  # aを入力する場合
        if c:  # CapsLockがONの状態
            # CapsLockとaを押す
            cost1 = f(i + 1, 0) + Z + X
            # Shift+aを押す
            cost2 = f(i + 1, 1) + Y
        else:  # CapsLockがOFFの状態
            # aを押す
            cost1 = f(i + 1, 0) + X
            # CapsLock+Shift+aを押す
            cost2 = f(i + 1, 1) + Z + Y
    else:  # Aを入力する場合
        if c:  # CapsLockがONの状態
            # CapsLockとShift+aを押す
            cost1 = f(i + 1, 0) + Z + Y
            # aを押す
            cost2 = f(i + 1, 1) + X
        else:  # CapsLockがOFFの状態
            # shift+aを押す
            cost1 = f(i + 1, 0) + Y
            # CapsLockとaを押す
            cost2 = f(i + 1, 1) + Z + X
    cost = min(cost1, cost2)
    cache[i][c] = cost
    return cost


print(f(0, 0))  # 0文字目、CapsLockはOFFでスタート
