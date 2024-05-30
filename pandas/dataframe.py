import pandas as pd
df1 = pd.DataFrame([[3,2,5], [10,0,2], [6,5,3]],
                   columns=["사과", "자두", "포도"],
                   index=["이성계", "김유신", "이순신"])
s1 = df1["사과"]