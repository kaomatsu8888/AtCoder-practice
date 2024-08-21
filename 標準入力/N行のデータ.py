"""
入力例
3
aaaaa
bbbbbb
cccc
"""

"""
出力例
aaaaa
bbbbbb
cccc
"""

# Nを取得
N = int(input())
# N行の文字列を取得
S = [input() for i in range(N)]

# 出力

for i in range(N):
    print(S[i])

# 処理の順番
# 1. Nを取得
# 2. N行の文字列を取得
# 3. N行の文字列を出力
# 入力と出力結果の例: 
# 入力:3 → aaaaa → bbbbbb → cccc
# 出力:aaaaa → bbbbbb → cccc
