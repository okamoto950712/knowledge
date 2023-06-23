import sys

sys.setrecursionlimit(10**6)


def dfs(g, v, parent, root, S, ans, seen):
    seen[v] = True  # 訪問済みにする
    for next in g[v]:
        if seen[next]:
            # 訪問済みならスキップ
            continue
        dfs(g, next, v, root, S, ans, seen)
    if v == root:  # 根の処理
        assert len(g[v]) == 1  # 隣接ノードは1つのみ
        next = g[v][0]
        if ans[next] == "":
            # 子が未定
            ans[next] = S[v]
            ans[v] = S[next]
        elif S[v] == ans[next]:
            # 変換前の根の色と変換後の子の色が一致
            ans[v] = S[next]
        else:
            raise
        return
    w_cnt_child = 0  # 子のWの数
    b_cnt_child = 0  # 子のBの数
    for next in g[v]:
        if next == parent:
            # 親はスキップ
            continue
        if ans[next] == "":
            # 子の色が未定
            ans[next] = S[v]  # 自身の変換前の色にする
        if ans[next] == "W":
            w_cnt_child += 1
        elif ans[next] == "B":
            b_cnt_child += 1

    cnt_child = w_cnt_child + b_cnt_child  # 子の合計
    if cnt_child == 0:
        # 自身が葉だった場合
        if ans[parent] == "":
            ans[parent] = S[v]
            ans[v] = S[parent]
        elif ans[parent] != S[v]:
            # 親の条件を満たせない
            raise
        else:
            ans[v] = S[parent]
        return

    # 葉でなかった場合
    target_cnt_child = w_cnt_child if S[v] == "W" else b_cnt_child
    if cnt_child // 2 == target_cnt_child:
        # WとB同数だった場合
        if ans[parent] == "":
            ans[parent] = S[v]
        elif ans[parent] != S[v]:
            # 親の条件が満たせない
            raise
    elif cnt_child // 2 < target_cnt_child:
        # 多い場合は親の親が決定する
        pass
    else:
        # 少ない場合は条件を満たさない
        raise


def solve():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].append(b)
        graph[b].append(a)
    S = input()
    seen = [False for _ in range(N)]  # 訪問済みのリスト
    ans = ["" for _ in range(N)]  # 答えとなる色のリスト
    for i, g in enumerate(graph):
        if len(g) == 1:
            root = i  # 葉を根とする
            break

    try:
        dfs(graph, root, None, root, S, ans, seen)
    except:
        print("-1")
        return
    print("".join(ans))


T = int(input())
for _ in range(T):
    solve()
