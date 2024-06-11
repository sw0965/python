import pandas as pd
a1 = ['송중기', '이유빈', '권보아', '차유람', '박보검', '김범수',  '이효리', '유승호', '김유정']
a2 = list("남여여여남남여남여")
a3 = list("AAABBBCCC")
a4 = [97, 88, 78, 64, 84, 89, 87, 92, 99]
a5 = [i + "등" for i in list("123321321")]
a6 = [i + "시" for i in list("수정정수수수정정수")]
a7 = ['이름', '성별', '반', '점수', '반등수', '비고']

df = pd.DataFrame([a1, a2, a3, a4, a5, a6], index=a7, columns=list(range(1, 10))).T
df["점수"] = df["점수"].astype(int)