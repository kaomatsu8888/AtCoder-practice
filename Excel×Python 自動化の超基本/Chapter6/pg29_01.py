#グラフをグラフシートに追加する
import openpyxl
from openpyxl.chart import BarChart, Reference,Series
workBook = openpyxl.load_workbook("日別店舗別クロス集計表.xlsx") #エクセルブックを開く
sheet = workBook.active #アクティブなワークシートを選択
chartSheet = workBook.create_chartsheet("日別店舗別売上グラフ")#グラフシートの作成
#グラフの描画対象になるセル範囲を設定
values = Reference(sheet, min_col=2, min_row=1,max_col=4, max_row=32)
chart = BarChart() #棒グラフを作成
chart.title = "日別店舗別売上グラフ" #タイトルの追加
chart.x_axis.title = '日付' #ラベルの追加
#先頭行をグラフのラベルにしてデータを追加
chart.add_data(values,titles_from_data=True)
chartSheet.add_chart(chart)
#グラフシートにグラフを描画
workBook.save("日別店舗別クロス集計表(グラフ)2.xlsx") #ファイルの保存
