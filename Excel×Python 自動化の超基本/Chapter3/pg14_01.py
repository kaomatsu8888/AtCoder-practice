#情報を並び替えて別のファイルに書き出す
import pandas as pd #pandasをインポート 
df = pd.read_excel("店舗別売上リスト.xlsx",sheet_name=None) #ブックを読み込み
df = df["Sheet1"].sort_values(['日付', '売上金額'],ascending=[False, False]) #日付、売上金額の降順に並び替え
#シートごとにExcelブックに書き出し
with pd.ExcelWriter("並び替え店舗別売上リスト.xlsx",date_format='YYYY/MM/DD',datetime_format='YYYY/MM/DD') as writer:
    df.to_excel(writer, sheet_name="統合表",index=False)
