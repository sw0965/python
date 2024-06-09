import pandas as pd
df1 = pd.DataFrame([["파이전자", 20, 30, 30, 40, "반도체"], 
                   ["썬닉스", 100, 90, 80, 100, "반도체"], 
                   ["판다센", 300, 320, 340, 0, "게임"], 
                   ["스마블", 0, 450, 300, 300, "게임"]], 
                  columns=["종목", "A팀", "B팀", "C팀", "D팀", "분류"])

s1 = pd.Series([35000, 10000, 2000, 5000], index=list(df1["종목"]))

df2 = df1.set_index("종목").iloc[:,:4].mul(s1, axis=0)

df2 = df2.reindex(["D팀", "C팀", "B팀", "A팀", "분류"], axis=1).reset_index()

df2["분류"] = df1["분류"]

# index 설정
'''
index 설정 set_index
index 리셋 reset_index
index 순서 바꾸기 reindex
index의 이름을 바꾸거나 직접입력 혹은 rename
index를 정렬 sort_index
'''


###