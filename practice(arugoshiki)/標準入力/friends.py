
N, A, B = map(int, input().split()) # N, A, B を取得
S = [input() for i in range(N)] # N 個の文字列を取得

# 出力
print('Yes' if S[A][B] == 'o' else 'No') # 出力

# 出力結果
# Yes
