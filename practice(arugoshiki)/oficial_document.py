A = ["Hello", "Algo"]
B = ["SUN", "MON", "TUE", "WED", "TSU", "FRI", "SAT"]
C = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

A.append("Method") # ["Hello", "Algo", "Method"]　加える
print(A) # ["Hello", "Algo", "Method"]
print(len(B)) # 7len()はリストの要素数を返す
C.sort() # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]　並び替える
print(C) 
