
# # 問題文
# 英小文字と | のみからなる文字列 S が与えられます。S は | をちょうど2 個含むことが保証されます。
# 2 つの | の間にある文字および | を S から削除した文字列を出力してください。

# ## 制約
# - S は英小文字および | のみからなる長さ 2 以上
# - 100 以下の文字列S は | をちょうど 2 個含む

# ## 入力
# - 入力は以下の形式で標準入力から与えられる。
# S

# ## 出力
# 答えを出力せよ。

# ## 入力例 1
# atcoder|beginner|contest

# ## 出力例 2
# atcodercontest

# ## 入力例 2
# |spoiler|

# ## 出力例 2
# 全ての文字が削除されることもあります。

# ## 入力例 3
# ||xyz

# ## 出力例 3
# xyz

def remove_text_between_pipes(S): # 文字列 S を引数として受け取り、その中の '|' とその間の文字を削除した文字列を返す関数
    # 最初と最後の '|' の位置を見つけます。
    first_pipe = S.find('|') # find() は文字列の中で指定した文字列が最初に現れる位置を返します。
    last_pipe = S.rfind('|') # rfind() は文字列の中で指定した文字列が最後に現れる位置を返します。
    
    # '|' とその間の文字を削除し、残りの部分を返します。
    return S[:first_pipe] + S[last_pipe+1:] # S[:first_pipe] は S の最初から first_pipe までの文字列を返します。S[last_pipe+1:] は S の last_pipe+1 から最後までの文字列を返します。

# 入力例
examples = [
    "atcoder|beginner|contest",
    "|spoiler|",
    "||xyz"
]

# 各入力例に対して関数を呼び出し、結果を出力します。
for example in examples:
    result = remove_text_between_pipes(example)
    print(f"Input: {example}\nOutput: {result}\n")


    def remove_text_between_pipes(S):
    # 最初と最後の '|' の位置を見つけます。
    first_pipe = S.find('|')
    last_pipe = S.rfind('|')
    
    # '|' とその間の文字を削除し、残りの部分を返します。
    return S[:first_pipe] + S[last_pipe+1:]

# 標準入力から文字列 S を受け取ります。
if __name__ == "__main__":
    S = input().strip()  # 入力の前後の空白を削除
    result = remove_text_between_pipes(S)
    print(result)

