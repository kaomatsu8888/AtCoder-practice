import sys
sys.setrecursionlimit(10**6)

# 再帰関数
def func(N):
    # 終了条件
    if N == 0:
        print(f"{N}終わったぜ")
        return 0
    
    # 再帰呼び出し
    print(f"{N}を呼び出したぜ") # ここで再帰呼び出しをする前に出力する
    return N + func(N - 1) # 再帰呼び出しをする


# 入力
N = int(input())

# 出力
print(func(N))
