import pandas as pd
from collections import Counter


# 讀取CSV檔案並將它們合併成一個DataFrame
df1 = pd.read_csv('0.8303.csv', header=None)
df2 = pd.read_csv('0.83711.csv', header=None)
df3 = pd.read_csv('0.83768.csv', header=None)
df4 = pd.read_csv('0.83825.csv', header=None)
df5 = pd.read_csv('0.83257.csv', header=None)
df6 = pd.read_csv('0.83825-2.csv', header=None)
df7 = pd.read_csv('0.83427.csv', header=None)
df8 = pd.read_csv('0.83087.csv', header=None)
# df9 = pd.read_csv('0.83484.csv', header=None)






# df3 = pd.read_csv('lstmtest_hidden_dim_384_0.80813.csv', header=None)
# df4 = pd.read_csv('prediction_lstmtest_hidden_dim_360.csv', header=None)
# df_merged = pd.concat([df1.iloc[:,1]], axis=0)  #df3.iloc[:,1], df4.iloc[:,1]

df_merged = pd.concat([df1.iloc[:,1], df2.iloc[:,1], df3.iloc[:,1], df4.iloc[:,1], df5.iloc[:,1],df6.iloc[:,1],df7.iloc[:,1],df8.iloc[:,1]],  axis=1)  
df_merged.columns = ['ID', 'Answer', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8'] 

# print(df_merged)
# 創建一個新的column，其中每一行的值都是前四個column中的值的列表
df_merged['combined'] = df_merged.apply(lambda x: [x['ID'], x['Answer'], x['col3'], x['col4'], x['col5'], x['col6'], x['col7'], x['col8']], axis=1) #  #前兩行直接命名成output的形式


# 假設原始資料的DataFrame名稱是df，目標column名稱是my_list_column
# 先使用Counter計算每個list中出現次數最多的元素
counters = [Counter(lst) for lst in df_merged['combined'].tolist()]

most_common_values = [c.most_common(1)[0][0] if len(c) > 0 else None for c in counters]

# 將計算結果添加到新的column中
df_merged['category'] = most_common_values


# 刪除“combined”列，因為它現在沒有用了
# df_merged.drop('combined', axis=1, inplace=True)

#把第一列變成繳交要求
df_merged.iloc[:, 0] = df1.iloc[:,0]

# #把output放到第二個col
df_merged.iloc[:,1] = df_merged.iloc[:, 9]

df_merged = df_merged.drop(0, axis=0)


# #剩下的刪掉
df_merged = df_merged.iloc[:, :2]



print(df_merged)
# print(df_merged)

# 將數據保存到一個新的CSV文件中
df_merged.to_csv('ensemble_output.csv', index=False)