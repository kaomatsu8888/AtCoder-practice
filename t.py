import argparse  # argparseの機能は、コマンドライン引数を解析することです。

parser = argparse.ArgumentParser()  # ArgumentParser オブジェクトを作成
parser.add_argument("--command")  # 引数を追加
parser.add_argument("target", nagrgs="+")  # 引数を追加
args = parser.parse_args()  # 引数を解析
print(args)
