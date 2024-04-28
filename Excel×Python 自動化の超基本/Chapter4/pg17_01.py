#列の幅と行の高さを変更する1
import openpyxl #openpyxlをインポート
workBook = openpyxl.Workbook() #空のワークブックを作成
sheet = workBook.active #アクティブなワークシートを選択
sheet['A1'] = "日付" #セルに値を入力
sheet['B1'] = "店名"
sheet['C1'] = "売上金額"
sheet.title = "新宿店" #シート名を設定
sheet.row_dimensions[1].height = 30 #行の高さを設定 (ピクセル)
sheet.column_dimensions["A"].width = 20 #列の幅を設定 (文字数)
sheet.column_dimensions["B"].width = 60
sheet.column_dimensions["C"].width = 30
workBook.save('店別売上表.xlsx') #ファイル名を指定して保存
