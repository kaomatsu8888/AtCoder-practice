n, k = map(int,input().split()) # nは要素数、kは最大値
a = list(map(int,input().split())) # aはリスト
b = list(map(int,input().split())) # bはリスト

num = 0 # numを初期化
for i in range(n): 
    num += abs(a[i] - b[i]) 

if abs(num - k) % 2 == 0 and num <= k:
    print("Yes")
else:
    print("No")
