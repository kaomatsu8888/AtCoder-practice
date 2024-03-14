import sys
sys.setrecursionlimit(10**6)

def func(N, depth=0):
    indent = "  " * depth  # インデントを追加して、再帰の深さを視覚化
    if N == 0:
        print(f"{indent}{N}: 終わったぜ")
        return 0
    
    print(f"{indent}{N}: を呼び出したぜ")
    result = func(N - 1, depth + 1)  # 再帰呼び出し
    print(f"{indent}{N} + {result} = {N + result}")  # 結果の加算を表示
    
    return N + result  # 再帰呼び出しの結果を返す

N = int(input("Nを入力してください: "))
print(f"合計: {func(N)}")
