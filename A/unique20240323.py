def main():
    # 整数 N を入力
    N = int(input())
    # 整数列 A を入力し、整数のリストに変換
    A = list(map(int, input().split()))

    # 結果を格納するリスト B を初期化
    B = []

    # Bi を計算し、リスト B に追加
    for i in range(N - 1):
        B.append(A[i] * A[i + 1])

    # B の要素を空白区切りで出力
    print(" ".join(map(str, B)))


if __name__ == "__main__":
    main()
