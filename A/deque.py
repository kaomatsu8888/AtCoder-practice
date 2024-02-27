"""
t = 1 ... xを上に入れる
t = 2 ... xを下に入れる
t = 3 ... 上からx番目のカードを出力
"""

Q = int(input()) # Qを整数として取得
from collections import deque # dequeモジュールをインポート/ dequeモジュールは双方向キューを提供する

q = deque() # qを初期化
for i in range(Q): # Qの数だけ繰り返す
    t, x = map(int, input().split()) # t, xを整数として取得
    if t == 1:
        q.appendleft(x) # xを左に追加
    elif t == 2:
        q.append(x) # xを追加
    elif t == 3:
        print(q[x - 1]) # x番目の要素を出力

