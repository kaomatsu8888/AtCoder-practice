#ヘッダーとフッターを設定する
import openpyxl #openpyxlをインポート
import datetime #日付を扱うライブラリをインポート 
now_date = datetime.datetime.now() #今日の日付を取得 
workBook = openpyxl.load_workbook("新宿店売上リスト.xlsx") #エクセルブックを開く
sheet = workBook["新宿店"] #シート「新宿店」を選択
sheet.oddHeader.center.text = "新宿店売上リスト"
#ヘッダーの中心に表示
sheet.oddHeader.right.text = now_date.strftime('%Y/%m/%d') #ヘッダーの右側に今日の日付を表示
workBook.save('新宿店売上リスト(完成)3.xlsx') #ファイル名を指定して保存