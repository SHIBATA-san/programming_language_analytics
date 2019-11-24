import pandas as pd


month = 'mon'
data = [['python', 'jupyter-notebook'],
    ['python', 'deep-learning', 'google-colaboratory'],
    ['python'],
    ['python', 'optimization', 'neural-network', 'deep-learning', 'pytorch'],
    ['python', 'indexing', 'merge', 'pyspark'],
    ['python', 'django', 'python-3.x', 'msbuild', 'misaka'],
    ['python', 'git-bash'],
    ['python', 'python-3.x', 'sockets', 'python-unittest']]


# リスト型のタグをpandas DataFrame型にしてカウントする
df = pd.DataFrame()
for tag in data:
    #print([tag])
    tmp_df = pd.DataFrame([tag], columns=tag)
    #df = pd.merge(df, tmp_df, how='outer', on='python') # 初回に結合できる軸がないためエラー
    df = df.append(tmp_df, ignore_index=True, sort=False)
#print(df.count())

# カウントしたものをpandas.df型にして転置
df2 = pd.DataFrame(df.count()).T
print(df2)
