import pandas as pd

# 데이터 프레임 #
df1 = pd.DataFrame([[3,2,5], [10,0,2], [6,5,3]],
                   columns=["사과", "자두", "포도"],
                   index=["이성계", "김유신", "이순신"])
# print(df1,"\n") # 데이터 프레임

# 시리즈 #
s1 = df1["사과"] 
# print(s1,"\n") # 시리즈


# pandas 는 넘파이 기반으로 만들어져 있어서 넘파이 함수 적용가능.
# print(df1.sum(),"\n")
# print(df1.mean())

# np array 로 출력
# print(df1.values) 
# print(df1.index)
# print(df1.columns)

# 넘파이의 특성 array 를 bool형태로 바꾸기 용이함
# print(df1.values > 3)
# print(df1 > 3)
# print(s1 > 3)

data = pd.read_excel("C:\study\python\pandas\E00EXAMPLE.xlsx").set_index("이름")

print(data)