"""
[Pythonでmultisetの代用ができるデータ構造 - Tsuboの競プロブログ](https://tsubo.hatenablog.jp/entry/2020/06/15/124657)
"""

import heapq


class HeapDict:
    def __init__(self, h=[]):
        self.h = []
        self.d = dict()
        for e in h:
            self.insert(e)

    def insert(self, x):
        heapq.heappush(self.h, x)
        if x not in self.d:
            self.d[x] = 1
        else:
            self.d[x] += 1

    def erase(self, x):
        if x not in self.d or self.d[x] == 0:
            print(x, "is not in HeapDict")
            raise
        else:
            self.d[x] -= 1

        while len(self.h) != 0:
            if self.d[self.h[0]] == 0:
                heapq.heappop(self.h)
            else:
                break

    def is_exist(self, x):
        if x in self.d and self.d[x] != 0:
            return True
        else:
            return False

    def get_min(self):
        return self.h[0]


N, K, Q = map(int, input().split())

a = [0 for _ in range(N)]  # 数列A
s = HeapDict([0 for _ in range(K)])  # 上位の集合
t = HeapDict([0 for _ in range(N - K)])  # 下位の集合
# tは最大値を取り出したいため適宜反転させる
ans = 0
for _ in range(Q):
    # 入力
    x, y = map(int, input().split())
    x -= 1
    # 追加
    s.insert(y)  # sに追加
    ans += y
    min_v = s.get_min()
    t.insert(-min_v)  # sの最小値をtに追加
    ans -= min_v
    s.erase(min_v)  # sから最小値を削除
    # 削除
    if s.is_exist(a[x]):
        # sに存在する
        s.erase(a[x])  # sから削除
        ans -= a[x]
        max_v = -t.get_min()  # tから最大の値を取得
        s.insert(max_v)  # sに追加
        ans += max_v
        t.erase(-max_v)  # tから最大の値を削除
    else:
        # tに存在する
        t.erase(-a[x])  # tから削除
    # 更新
    a[x] = y
    # 出力
    print(ans)
