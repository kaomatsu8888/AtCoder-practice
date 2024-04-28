#エクセルブックを翻訳
import datetime
import openpyxl
from googletrans import Translator
translator = Translator()#翻訳の準備
workBook = openpyxl.load_workbook("旅行スケジュール.xlsx") #ブックを開く
sheet = workBook.active #アクティブなワークシートを選択
for row in sheet:
    for cell in row:
        #空白セルは翻訳しない 
        if cell.value is None:
            continue
        #セルが数値の場合は翻訳しない
        if isinstance(cell.value,int):
            continue
        #時刻は翻訳しない
        if isinstance(cell.value,datetime.time): 
            cell.number_format = "h:mm" 
            continue
        #日付は翻訳しない
        if isinstance(cell.value,datetime.datetime):
            cell.number_format = "yyyy/m/d"
            continue
        cell.value = translator.translate(str(cell.value), dest="en").text
workBook.save("旅行スケジュール(翻訳).xlsx") #ファイル名を指定して保存