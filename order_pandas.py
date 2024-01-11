import pandas as pd
from glob import glob

filepaths = glob('source/*.xlsx')
filepath = filepaths[0]

# a,b,c,dには列番号を入力してください 表示したい順番に列が並びます
def arrange(filepath, a, b, c, d):
  df_original = pd.read_excel(filepath)
  df_changed = df_original.iloc[0: , [a+1, b+1, c+1, d+1]]
  df_changed['テスト名'] = df_original['テスト名'].str.cat(df_original['回数'].astype(str), sep='-') # 「テスト名」と「回数」を-で結合します
  df_changed['日付'] = df_original['日付'].dt.strftime('%Y/%m/%d') #「日付」形式を丸ごと変更
  df = df_changed.drop('回数', axis=1)
  return df


df = pd.DataFrame()
for filepath in filepaths:
  _df = arrange(filepath)
  df = pd.concat([df, _df])

df.to_excel('arranged_data.xlsx', index=False)