# 円周率の小数点以下の数値の中に、"1" がいくつ含まれるかを数えるプログラムを作成してください。
# 円周率を表す文字列 (小数第千桁まで)

PI = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"

# "1" の個数をカウントするための変数
cnt = 0

for number in PI[2:]: # 小数点以下を順に調べる
    if number == "1": # その数が "1" ならカウントする
        cnt += 1

# 答えを出力する
print(cnt)


# カオル氏が書いたやつ
# ここにコードを書いてください

pai = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"
cnt = 0
for i in pai:
    if i == "1":
        cnt += 1
        
print(f"{cnt}")

# コードレビュー
"""
長所:

    このスニペットも直接的で "1" の出現回数を効果的に数える。
    出力に f-文字列を使用しており、これはより現代的なPythonの機能です（ただし、この単純な使用例では大きな追加価値はありません）。

短所:

    最初のスニペットと違って、円周率の整数部分と小数点をスキップせずにカウントを始めます。この特定のインスタンスでは整数部分や小数点に "1" がないため結果に影響はありませんが、課題として記述されたタスクに対してはより正確なアプローチではありません。

比較と最適化の提案

    どちらのスニペットも円周率の文字列表現内の "1" の数を数える目標を効果的に達成しています。
"""
