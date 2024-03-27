W, B = map(int, input().split())

# 無限に長いピアノの鍵盤の白鍵と黒鍵を表す文字列Sを生成する
S = ("wb" * 50) + ("bw" * 50)  # 長さ200の文字列

# Sの中からW個のwとB個のbからなる部分文字列を探す
found = False
for i in range(len(S) - W - B + 1):
    substring = S[i : i + W + B]
    if substring.count("w") == W and substring.count("b") == B:
        found = True
        break

if found:
    print("Yes")
else:
    print("No")
