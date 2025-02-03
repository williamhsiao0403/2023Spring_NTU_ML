import pandas as pd
from collections import Counter


# 讀取CSV檔案並將它們合併成一個DataFrame
df1 = pd.read_csv('lstm_tr08.csv', header=None)
df2 = pd.read_csv('lstmtest_81126.csv', header=None)
df3 = pd.read_csv('lstmtest_hidden_dim_384_0.80813.csv', header=None)
df4 = pd.read_csv('lstmtest_hidden_dim_360.csv', header=None)
df5 = pd.read_csv('lstmtest_hidden_dim_384_change.csv', header=None)
# df3 = pd.read_csv('resnet152.csv', header=None)
# df4 = pd.read_csv('0.95825_output.csv', header=None)
df_merged = pd.concat([df1.iloc[:,1], df2.iloc[:,1], df3.iloc[:,1], df4.iloc[:,1], df5.iloc[:,1]],  axis=1) #df4.iloc[:,1]
df_merged.columns = ['Id', 'Class', 'col3', 'col4', 'col5'] #, 'col4'
# print(df_merged)
# 創建一個新的column，其中每一行的值都是前四個column中的值的列表
df_merged['combined'] = df_merged.apply(lambda x: [x['Id'], x['Class'], x['col3'], x['col4'], x['col5']], axis=1) #, x['col4']  #前兩行直接命名成output的形式


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
df_merged.iloc[:,1] = df_merged.iloc[:, 6]

df_merged = df_merged.drop(0, axis=0)


# #剩下的刪掉
df_merged = df_merged.iloc[:, :2]



print(df_merged)
# print(df_merged)

# 將數據保存到一個新的CSV文件中
df_merged.to_csv('ensemble_output.csv', index=False)




