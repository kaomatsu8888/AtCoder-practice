# 長い文章
LONG_SENTENCE = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum"

# ここからコードを書いてください
cnt = 0 # 単語の数をカウントする変数.これがないと最後の単語がカウントされない
for character in LONG_SENTENCE: # 文字列を1文字ずつ取り出す
    if character == " ": # スペースがあれば
        cnt += 1 # カウントを1増やす

print(cnt + 1) # 最後の単語の後にスペースがないので、1を足す
