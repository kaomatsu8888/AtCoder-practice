# split()でスペース区切りの複数の整数をリストとして受け取り、map()でint型に変換して複数の変数に代入
A, B = map(int, input().split())
print(A+B)

# 処理の順番
# 1. 標準入力からスペース区切りの複数の整数を受け取る
# 2. 受け取った整数をint型に変換して複数の変数に代入.例えば5,10の場合、A=5, B=10
# 3. A+Bを計算して出力する.
"""
さらに分解
入力の分割: 最初にユーザーから受け取った文字列"5 10"をsplit()メソッドを使って
スペースで区切ります。この結果、['5', '10']というリストが得られます
このリストには2つの要素があり、それぞれ文字列'5'と'10'です

整数への変換: 次に、map(int, split_input)を使って、
リスト内の文字列を整数に変換します。
map()関数は、第一引数に指定した関数（この場合はint）をリストの各要素に適用します。
この結果として得られるのは[5, 10]という整数のリストです。

変数への代入: この整数のリストを2つの変数AとBに展開して代入します。
ここでは、Aが5、Bが10になります。

まとめ
入力:5 10 → ['5', '10'] → [5, 10] → A=5, B=10

"""
