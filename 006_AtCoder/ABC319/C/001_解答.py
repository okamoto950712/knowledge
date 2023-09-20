import itertools

C = []
for _ in range(3):
    C += list(map(int, input().split()))

ROWS = (
    (0, 1, 2),  # 上から1行目
    (3, 4, 5),  # 上から2行目
    (6, 7, 8),  # 上から3行目
    (0, 3, 6),  # 左から1列目
    (1, 4, 7),  # 左から2列目
    (2, 5, 8),  # 左から3列目
    (0, 4, 8),  # 左上から右下
    (2, 4, 6),  # 右上から左下
)

not_disappoint = 0  # がっかりしない開け方の総数
all = 0  # 開け方の総数
for order in itertools.permutations([i for i in range(9)]):
    disappoint_flg = False  # がっかりするか判定するフラグ
    for a, b, c in ROWS:
        if C[a] == C[b] and order[a] < order[c] and order[b] < order[c]:
            disappoint_flg = True
            break
        elif C[a] == C[c] and order[a] < order[b] and order[c] < order[b]:
            disappoint_flg = True
            break
        elif C[b] == C[c] and order[b] < order[a] and order[c] < order[a]:
            disappoint_flg = True
            break
    if not disappoint_flg:
        not_disappoint += 1
    all += 1
print(not_disappoint / all)
