#円グラフを作る
import openpyxl
from openpyxl.chart import Reference, Series,ProjectedPieChart,PieChart
workBook = openpyxl.load_workbook("店舗別売上集計表.xlsx") #エクセルブックを開く
sheet = workBook.active#アクティブなワークシートを選択
#グラフの描画対象になるセル範囲を設定 A2:B4
labels = Reference(sheet, min_col=1, min_row=2,max_col=1, max_row=4)
values = Reference(sheet, min_col=2, min_row=2,max_col=2, max_row=4)
chart = PieChart() #円グラフを作成
chart.add_data(values) 
chart.set_categories(labels)
sheet.add_chart(chart, "G1") #セルG1にグラフを描画
workBook.save("店舗別売上集計表(グラフ).xlsx") #ファイルの保存