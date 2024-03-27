"""
次のコードを実行した結果として、正しいものはどれか。

a = 'Apple'
print(a[5])

選択 1

e

選択 2

エラーになる。

選択 3

何も表示されない。

選択 4

a
このコードを理解するには、Pythonにおける文字列のインデックスについて知る必要があります。Pythonでは、文字列の最初の文字のインデックスは0です。したがって、'Apple' という文字列でインデックス5を参照しようとすると、実際には文字列の範囲を超えてしまいます。なぜなら、'Apple' の長さは5であり、最後の文字 e のインデックスは4だからです。

したがって、print(a[5]) は文字列 'Apple' の範囲外を参照しようとするため、Pythonはエラーを返します。この場合、IndexError が発生します。

正しい選択は選択 2「エラーになる。」です。

Keyword arguments:
argument -- description
Return: return_description
"""

"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
