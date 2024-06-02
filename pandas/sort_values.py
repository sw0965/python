import pandas as pd

a1 = [60, 84, 80, 70, 19]
a2 = [77, 62, 95, 85, 17]
a3 = [61, 97, 72, 67, 15]
a4 = [75, 65, 95, 51, 18]

cols = ["국어", "영어", "수학", "과학", "나이"]
df = pd.DataFrame([a1, a2, a3, a4], index=list("ABCD"), columns=cols)

# 올림차순
#print(df.sort_values("국어"))

# 내림차순 ascending = False
#print(df.sort_values("영어", ascending=False))

# 내림차순 리스트 
#print(df.sort_values(["수학", "영어"], ascending=False))

# 수학은 오름차순인데 나이는 내림차순으로 정렬
#print(df.sort_values(["수학", "나이"], ascending=[0, 1])) # 0 은 false 1 은 true