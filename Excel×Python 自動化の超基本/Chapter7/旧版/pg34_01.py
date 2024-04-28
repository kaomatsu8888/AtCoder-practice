#Amazon ページの情報を取得する
import requests
import datetime
import pandas as pd 
import pyperclip
from bs4 import BeautifulSoup 
import tkinter as tk
from tkinter import messagebox
def pasteUrl(e): #テキストボックスがクリックされた時にURLを貼り付ける
    urlText.delete("1.0","end")
    urlText.insert("1.0",pyperclip.paste())
def getData(): #データを取得してExcelブックに追加する
    url = urlText.get("1.0","end")#1文字目から最後まで取得 
    html_contents = requests.get(url).text
    html_soup = BeautifulSoup(html_contents,"html.parser")
    prices = html_soup.find_all("span",{"class":"a-color- price"}) #価格の取得
    price = None
    for p in prices:
        if "¥" in p.text:#通貨記号がある情報をpriceとして取得
            price = p.text
            break
    item_name = html_soup.find("",{"id":"productTitle"}).text #商品名の取得
    item_name = item_name.replace("\n","")   #改行を察駆除する
    #新しいエクセルブックに書き出し
    df = pd.read_excel("Amazon商品リスト.xlsx")
    data = [datetime.datetime.now(),item_name,price,url]
    df2 = pd.DataFrame([data],columns= df.columns)
    df = df.append(df2)
    with pd.ExcelWriter("Amazon商品リスト.xlsx") as writer:
        df.to_excel(writer,index=False,columns=df.columns) #シートを書き出し
    messagebox.showinfo("完了", "エクセルデータの書き出しが完了しました。")
#GUIの用意
root = tk.Tk()
root.title("商品データ書き出し") #タイトルの設定
root.geometry("700x55") #サイズの設定
root.grid()
urlLabel = tk.Label(root,text="URL")
urlText = tk.Text(root,borderwidth = 3,height =3,relief="ridge")
urlText.bind("<Button-1>",pasteUrl)
getButton = tk.Button(root,text="データ取得",command=getData) #データ取得ボタン
urlLabel.grid(row=1,column=1)
urlText.grid(row=1,column=2)
getButton.grid(row=1,column=3) 
root.mainloop() #ウィンドウを表示