import pandas as pd
from collections import Counter

def ensemble_majority_vote(csv_file):

    # 讀取 CSV 檔案，每一行代表同一筆資料的各模型預測
    df = pd.read_csv(csv_file)
    
    # 定義一個函數對單一行資料做多數表決
    def majority_vote(row):
        # 利用 Counter 統計每個預測出現次數
        vote_count = Counter(row)
        # 取得出現次數最多的預測值
        most_common, _ = vote_count.most_common(1)[0]
        return most_common
    
    # 對每一行做 majority vote
    ensemble_preds = df.apply(majority_vote, axis=1)
    return ensemble_preds