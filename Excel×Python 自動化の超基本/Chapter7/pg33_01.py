#Google ドライブからファイルを取得する
from urllib.parse import urlparse
import urllib.request
import requests
#Googleドライブのファイル共有URL すべてのコード完成後共有フォルダを再アサイン
url = "https://drive.google.com/file/d/1gRzF7gFFJ-jBfrVEGF7QG6CpLhpqZWLl/view?usp=sharing"
workUrl = "https://drive.google.com/uc?id=<file_id>"
path = urlparse(url).path
path = path.lstrip("/file/d/")
path = path.rstrip("/view")
url = workUrl.replace("<file_id>",path)
response = requests.get(url)
file_name = "店別売上表.xlsx"
with open(file_name, 'wb') as sf:
    sf.write(response.content)