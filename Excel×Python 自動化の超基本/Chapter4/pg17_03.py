#データを抽出して書き出し、列の幅を変える
import openpyxl #openpyxlをインポート 
import pandas as pd #pandasをインポート
df = pd.read_excel("店舗別売上リスト.xlsx",sheet_name="Sheet1") #ブックを読み込み
df = df[df.店名 == "新宿店"] #新宿店のみ取得
#シートごとにエクセルブックに書き出し
with pd.ExcelWriter("新宿店売上リスト(完成).xlsx",date_format='YYYY/MM/DD',datetime_format='YYYY/MM /DD') as writer:
    df.to_excel(writer, sheet_name="新宿店",index=False)
workBook = openpyxl.load_workbook("新宿店売上リスト(完成).xlsx") #エクセルブックを開く
sheet = workBook.active #アクティブなワークシートを選択 
sheet.column_dimensions["A"].width = 12 #列の幅を設定(文字数) 
workBook.save('新宿店売上リスト(完成).xlsx') #ファイル名を指定して保存