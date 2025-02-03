import os
import random
import shutil

# 定義源資料夾和目標資料夾的路徑
src_folder = 'C:\\Users\william\Desktop\sub6-2'
dst_folder = 'C:\\Users\william\Desktop\hw123'



# 獲取源資料夾中所有文件（圖片）的名稱列表
file_names = [f for f in os.listdir(src_folder) if f.endswith('.jpg')]

# 從所有文件名稱列表中隨機選擇1000個文件名稱
selected_files = random.sample(file_names, 1000)

# 將選中的1000個文件復制到目標資料夾中
for file_name in selected_files:
    src_path = os.path.join(src_folder, file_name)
    dst_path = os.path.join(dst_folder, file_name)
    shutil.copy(src_path, dst_path)
print('end')
