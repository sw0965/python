import pandas as pd
import numpy as np

a = np.random.randint(0, 10, 24).reshape(4,6)
df = pd.DataFrame(a, index=list("가나다라"), columns=list("ABCDEF"))

# 인덱싱
# df["열이름"] : 열만 가능 여러개 부를때는 
# df[["A", "B", "C"]]

# loc 인덱싱
# df.loc["가", "A"]
# df.loc["가":"다", "A":"E"] 가 ~ 다 A ~ E 까지
# df.loc["가":"다", ["A", "E"]]
# E 열을 두번 부르고 싶으면
# df.loc["가":"다", ["A", "E", "E"]]
# df.loc["가":"다"] 이렇게 하면 default 로 행만 지정이 된다 열은 안된다.

# iloc = 숫자 인덱싱
# df.iloc[0]
# df.iloc[0,0]
# df.iloc[0:3,0:5]
# B와 D만 부르고 싶을때 리스트 형식으로
# df.iloc[0:3, [1, 3]]

# drop "D"열 드롭하기 | axis=1 열 axis=0 행
#df.drop("D", axis=1)  

# 문제 B, D, E, F 열과 가나다행의 자료를 추출하기

# loc
#print(df.loc["가":"다", ["B", "D", "E", "F"]])

# iloc
# print(df.iloc[0:3, [1,3,4,5]])

# 섞어 사용
# print(df.iloc[:3, 1:].drop("C", axis=1))

