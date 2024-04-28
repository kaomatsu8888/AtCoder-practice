#特定のデータを抽出して別のファイルに書き出す
import pandas as pd #pandasをインポート
df = pd.read_excel("店舗別売上リスト.xlsx",sheet_name="Sheet1") #ブックを読み込み
df = df[df.店名 == "新宿店"] #新宿店のみ取得
#シートごとにエクセルブックに書き出し
with pd.ExcelWriter("新宿店売上リスト.xlsx",date_format='YYYY/MM/DD',datetime_format='YYYY/MM/DD') as writer:
    df.to_excel(writer, sheet_name="新宿店",index=False)