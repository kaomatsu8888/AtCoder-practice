#選択 ポイント 5行目と7行目はTabキーを押してずらします(インデント)
age = input("年齢を入力して下さい") #キーボードから入力を 受け付けます
age = int(age) #文字として扱われているデータを数値に変換します
if age >= 20: #入力されたageの値が20以上ならすぐ下の命 令が実行されます
    print("お酒を飲めます")
else: #20未満の場合は下の処理が実行されます。
    print("お酒を飲んではいけません")
print("プログラム終了")
