import pandas as pd
import numpy as np

a1 = [60, 84, 80, 70, "문예부"]
a2 = [77, 62, 95, 85, "과학부"]
a3 = [61, 97, 72, np.nan, "농구부"]
a4 = [75, 65, 95, np.nan, "다도부"]
cols = ["국어", "영어", "수학", "과학", "소속"]
b1 = ["문예부", "과학부", "다도부"]

df = pd.DataFrame([a1, a2, a3, a4], index=list("ABCD"), columns=cols)


print(df)
#print(df["영어"] > 80)

print(df.loc[df["영어"] > 80])


#cond1 = df["영어"] > 80 # 조건이 여러개일경우 빼서 쓰자
#print(df.loc[cond1, "국어":"과학"])

cond2 = df["국어"] > 60
cond3 = df["수학"] > 75

# 둘 이상 조건 = 논리 연산자로 사용
print(df.loc[cond2 & cond3])

print(df["과학"].isnull())

# ~  =  not 논리연산자
print(df.loc[~df["과학"].isnull()])
# 단순한 삭제는 dropnan 이 좋은데 nan 값으로 여러가지 조합을 해야할 때는 isnull이 필요하다