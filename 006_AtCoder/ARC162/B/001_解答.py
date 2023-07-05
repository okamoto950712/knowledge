import sys


def cnt_inversion(x):
    # 転倒数を求める
    cnt = 0
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[j] < x[i]:
                cnt += 1
    return cnt


def diff_idx(x):
    # インデックスと値が異なる箇所を特定する
    for i, v in enumerate(x):
        if i != v:
            return i
    return -1  # ソート済み


def operate(p, i, j):
    q = p[:i] + p[i + 2 :]
    p = p[i : i + 2]
    # print(f"{p=}, {q=}, {i=}, {j=}")
    assert len(p) == 2
    return q[: j + 1] + p + q[j + 1 :]


N = int(input())
p = list(map(lambda x: int(x) - 1, input().split()))
c = cnt_inversion(p)
if c % 2 == 1:
    # 転倒数が奇数の場合はソートできない
    print("No")
    sys.exit()


ope = []
while (m := diff_idx(p)) != -1:
    k = p.index(m)  # mの位置にもってきたい数の位置
    if k < N - 1:
        # kの位置にある値をmに持ってくる
        i = k
        j = m - 1
    else:
        # 末尾にあると困るので手前にずらす
        i = N - 2
        j = N - 4
    ope.append((i, j))
    p = operate(p, i, j)
    # print(f"{p=}")

print("Yes")
print(len(ope))
for o in ope:
    print(f"{o[0]+1} {o[1]+1}")
