N, M = map(int, input().split())
L = [int(x) for x in input().split()]


def f(w):
    line = 0  # 必要な行数
    rem = 0  # 残りの列数
    for i in range(N):
        if L[i] + 1 <= rem:
            # まだ単語を追加できる場合
            rem -= L[i] + 1  # 1は空白の分
        else:
            # 単語を追加できない場合
            line += 1  # 必要な行数を1つ増やす(改行する)
            rem = w - L[i]  # 最初の単語の文字数分減らす
            if rem < 0:
                # 1単語が最大列数を超えていた場合、その時点で失敗
                return False
    return line <= M  # M以下であれば条件を満たす


wa = 0
ac = 1e15

# 単調増加であるため2分探索が使える
while abs(ac - wa) > 1:  # 条件を満たす場合と満たさない場合の境界を求める
    wj = (ac + wa) // 2
    if f(wj):
        ac = wj
    else:
        wa = wj
print(int(ac))
