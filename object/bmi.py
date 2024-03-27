"""
class (成人の)BMI:
    関連しそうな属性:
        - 身長
        - 体重
        - BMIという値そのもの
    ルール:
        - BMIは10以上40以下 <- 常識的な範囲
        - 表示するときは小数点第2位まで
            - ex: 23.689 => 23.69
            - ex: 23.681 => 23.68
    できること:
        - BMIの計算
"""
# Pythonのクラス名はUpperCamelCaseが普通
# 例外として一般的に大文字で意味が通じる場合はOK 正式名称のBodyMassIndexだと一般的ではない(伝わらない)
class BMI:
    def __init__(self, height, weight):
        self.height = height  # インスタンス変数
        self.weight = weight  # インスタンス変数

    # インスタンスメソッドの作成
    def calculate_bmi(self):
        # BMIの計算式を返す 体重÷身長2乗
        return self.weight / (self.height ** 2)


# BMIクラスのインスタンス化
tanaka_bmi = BMI(height=1.80, weight=67.0)
sasami_bmi = BMI(height=1.58, weight=80.0)

print(tanaka_bmi.height, sasami_bmi.height)
