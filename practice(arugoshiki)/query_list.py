"""
10 個の整数 3,1,4,1,5,9,2,6,5,3 が一列に与えられます。

このデータ構造に対して、Q 回のクエリが与えられます。それぞれのクエリに答えてください。 各クエリは、次のいずれかです。

    Output(k)：整数値 k が与えられるので、左から k 番目の値を答えてください
    Write(k,v)：整数値 k,v が与えられるので、左から k 番目の値を v に書き換えてください。このとき、何も出力しなくてよいです

ただし、最も左の数字は左から 0 番目であると数えることにします。"""
# 配列を宣言

A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# 入力
Q = int(input())

for _ in range(Q):
    # クエリを行ごとに受け取る
	query = list(map(int, input().split()))
	print(query)
    # query の先頭が種類を表す
	query_type = query[0]
	print(query_type)
	if query_type == 0:
        # Output クエリ
		k = query[1]
		print(A[k])
	else:
        # Write クエリ
		k, v = query[1], query[2]
		print(k, v)
		A[k] = v
