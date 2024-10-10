m , d = input().split() 

if m == d or m[0] == d[0]:
    print("True")
else:
    print("False")


"""
# 月と日をスペース区切りで入力として受け取る
m, d = input().split()

# 月と日の文字列を結合する
combined = m + d

# すべての桁が同じであれば Yes、そうでなければ No を出力
if all(char == combined[0] for char in combined):
    print("Yes")
else:
    print("No")

改良点と解説
文字列の結合による判定
月と日を combined = m + d として一つの文字列に結合することで、すべての桁が同じかどうかを一括で確認できるようになります。

all() 関数の使用
all(char == combined[0] for char in combined) を使うことで、combined 内のすべての文字が combined[0]（最初の文字）と等しいかどうかを判定しています。

all() 関数は条件を全て満たす場合に True を返すので、各文字が最初の文字と同じなら Yes を出力します。
効率の向上
元のコードでは、月と日が同じかどうかのチェックや、各桁の比較を個別に行っていたため、複数の条件式を処理していました。結合して判定することで、よりシンプルに条件をチェックできます。

入力例と出力例
入力例 1
"""
