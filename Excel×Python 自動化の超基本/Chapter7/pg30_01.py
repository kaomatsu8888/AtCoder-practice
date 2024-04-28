#共有フォルダにアクセスする
import os
import glob
from smb.SMBConnection import SMBConnection 
path = os.getcwd()#現在の作業フォルダ位置を取得 
sendFileFolder = os.path.join(path,"送信データ")
reciveFileFolder = os.path.join(path,"受信データ") 
user = "" #サーバー接続ユーザー名
password = "" #サーバー接続パスワード
ipAdress = "192.168.130.100" #サーバーIPアドレス（例）
serverFolder = "test" #サーバーフォルダ（例）
connection = SMBConnection(user,password,"myClie nt","HostServer")
connection.connect(ipAdress, 139)   #サーバーにデータを送信
os.chdir(sendFileFolder) #送信データフォルダに移動
for sendFile in glob.glob("*.xlsx"):
    with open(sendFile, "rb") as file:
        connection.storeFile(serverFolder, sendFile, file)#サーバーのデータを受信
os.chdir(reciveFileFolder) #受信データフォルダに移動
for reciveFile in connection.listPath(serverFolder, '/'):
    if reciveFile.filename =="." or reciveFile.filename == "..":
        continue #不要な要素を読み飛ばす
    with open(reciveFile.filename, 'wb') as file:
        connection.retrieveFile(serverFolder, reciveFile.filename, file)
connection.close()
