#指定したブック、セル範囲間でコピーアンドペーストするプログラム
import openpyxl #Excelのブックを操作するライブラリの読み込み
workBook = openpyxl.load_workbook("商品リスト.xlsx") #指定したファイル名のExcelブックを開く
workSheet = workBook["Sheet1"] #指定したシート名の シートを取得する
workSheet["A10"] = workSheet["A1"].value #セルA10に セルA1の値をコピーアンドペースト
workBook.save("商品リスト.xlsx")