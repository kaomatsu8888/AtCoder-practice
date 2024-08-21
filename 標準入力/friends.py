
N, A, B = map(int, input().split()) # N, A, B を取得
S = [input() for i in range(N)] # N 個の文字列を取得

# 出力
print('Yes' if S[A][B] == 'o' else 'No') # 出力

# 処理の順番
# 1. N, A, B を取得
# 2. N 個の文字列を取得
# 3. S[A][B] が 'o' かどうかで条件分岐
# 4. 入力と出力結果の例: 3 1 1 → xox → Yes
