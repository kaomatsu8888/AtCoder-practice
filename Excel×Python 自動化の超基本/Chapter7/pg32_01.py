#指定したフォルダのエクセルデータを圧縮し解凍する
import os
import glob
import zipfile
import datetime
path = os.getcwd()#現在の作業フォルダ位置を取得
zipFile = os.path.join(path,"圧縮データ","圧縮データ"+str(datetime.date.today())+".zip")
reciveFileFolder = os.path.join(path,"受信データ")
unPackFileFolder = os.path.join(path,"解凍データ") #受信データフォルダのファイルを圧縮
os.chdir(reciveFileFolder) #受信データフォルダに移動 
with zipfile.ZipFile(zipFile,"w") as zf:
    for packFile in glob.glob("*.xlsx"):
        zf.write(packFile) #ファイルを圧縮
#圧縮ファイルを解凍
os.chdir(unPackFileFolder) #解凍データフォルダに移動
with zipfile.ZipFile(zipFile) as zf:
    zf.extractall() #すべてのファイルを解凍