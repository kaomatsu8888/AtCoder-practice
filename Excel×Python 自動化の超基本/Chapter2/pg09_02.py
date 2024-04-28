import pandas as pd #Excelのブックを操作するライブラリの読み込み
item_list = [] #Excelに出力するデータを格納するリスト
item_no = input("商品番号を入力して下さい 終了は-1:") 
while(int(item_no) != -1): #商品番号に-1が入力されるまで5行目から9行目までを繰り返します
    item_name = input("商品名を入力して下さい:") 
    item_price = input("価格を入力して下さい:") 
    item_sales = input("売上額を入力して下さい:") 
    item_list.append([item_no,item_name,item_price, item_sales]) #入力したデータをリスト形式で追加
    item_no = input("商品番号を入力して下さい 終了は-1:")
df = pd.DataFrame(item_list,columns=['商品番号', '商品名', '価格', '売上額'])#列名
with pd.ExcelWriter("商品リスト.xlsx") as writer:
    df.to_excel(writer,index=False)#エクセルファイルに書き出し
print("プログラム終了")