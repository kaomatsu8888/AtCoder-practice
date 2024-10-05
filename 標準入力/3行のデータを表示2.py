"""
入力例
a a a
"""

"""
出力例
a
a
a
"""

# 1行の文字列を取得
s = input()

# スペース区切りの整数の入力
a, b = map(int, input().split())

# 文字列の入力
s = input()

# 出力
print(s)
# 出力
print(a, b)

"""
# 上のコードは以下のように書き換えることができる
s = input()
t = s.split()
print(t[0])
print(t[1])
print(t[2])
"""

# スペース区切りの整数と文字列の入力
a, s = input().split()


