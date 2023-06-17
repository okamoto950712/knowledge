"""
メモ化再帰
"""

import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)

# 入力
X, Y, Z = map(int, input().split())
S = input()


@lru_cache(maxsize=len(S) * 2 + 10)  # メモの最大数は文字列数*2存在する。10は遊び
def f(i, isCapsLockOn):
    if i == len(S):
        return 0
    if S[i] == "a":  # aを入力する場合
        if isCapsLockOn:  # CapsLockがONの状態
            # CapsLockとaを押す
            cost1 = f(i + 1, False) + Z + X
            # Shift+aを押す
            cost2 = f(i + 1, True) + Y
        else:  # CapsLockがOFFの状態
            # aを押す
            cost1 = f(i + 1, False) + X
            # CapsLockとShift+aを押す
            cost2 = f(i + 1, True) + Z + Y
    else:  # Aを入力する場合
        if isCapsLockOn:  # CapsLockがONの状態
            # CapsLockとShift+aを押す
            cost1 = f(i + 1, False) + Z + Y
            # aを押す
            cost2 = f(i + 1, True) + X
        else:  # CapsLockがOFFの状態
            # shift+aを押す
            cost1 = f(i + 1, False) + Y
            # CapsLockとaを押す
            cost2 = f(i + 1, True) + Z + X
    return min(cost1, cost2)


print(f(0, False))  # 0文字目、CapsLockはOFFでスタート
