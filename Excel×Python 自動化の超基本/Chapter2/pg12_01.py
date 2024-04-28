#売上リストから店舗別に売上を集計し別のブックに出力する
import pandas as pd #pandasをインポート
#指定したブックのすべてのシートを読み込み
df = pd.read_excel("店舗別売上リスト.xlsx",sheet_name="統合表")
shopDictionary = {} #店舗と売上を保存する辞書 
total = 0 #全店舗の売上を保存する変数
for index,rows in df.iterrows(): #行ループ
    if rows["店名"] not in shopDictionary:
        shopDictionary[rows["店名"]] = rows["売上金額"]
    else:
        shopDictionary[rows["店名"]] = shopDictionary[rows["店名"]] + rows["売上金額"]
    total = total + rows["売上金額"]
shopDictionary["全店合計"] = total #全店合計を辞書に格納
df2 = pd.DataFrame(list(shopDictionary.items()),columns=["店名","売上合計"])#集計表に店舗別の売上データを追加
#新しいエクセルブックに書き出し
with pd.ExcelWriter("店舗別売上集計リスト.xlsx",date_format='YYYY/MM/DD',datetime_format='YYYY/MM/DD') as writer:
    df2.to_excel(writer, sheet_name="集計表",index=False)
