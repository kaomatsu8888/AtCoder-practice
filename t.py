from module import *  # モジュールの全ての関数をインポート
def greet(name):
    print(f"Hello, {name}!")

result = greet("Alice")
print(result)  # None
#集合は{}で表し、ミュータブルのため要素の追加や削除ができる。また、同じ値を重複して格納し、取り出すことができる。

#集合の作成
#空集合の作成
empty_set = set()
print(empty_set)  # set()

#要素を持つ集合の作成. 重複する要素は無視される
fruits = {"apple", "banana", "apple", "orange"}
print(fruits)  # {'banana', 'apple', 'orange'}


number = {'one': 1, 'two': 2}
for k, v in number.items():
    print(k, v)
