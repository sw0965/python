import pandas as pd

a1 = [[1,2,3], [4,5,6,], [7,8,9]]
df1 = pd.DataFrame(a1, columns=list("ABC"), index=list("가나다"))
df2 = df1.reindex(columns=list("BCA"), index=list("나다가")).copy()
sr1 = df1.loc["가"]
df3 = df1.iloc[:2,:2]

# 데이터 프레임간 연산자
#print(df1 * df1)
#print(df1 + df3)

#print(df1.add(df3, fill_value=0))




