import os
import shutil

# 指定目錄路徑和新文件名的前綴
dir_path = 'C:\\Users\william\Desktop\hw6sub'

# 遍歷目錄中的所有JPG文件
for i, filename in enumerate(os.listdir(dir_path)):
    if filename.endswith('.jpg'):
        # 構建新文件名
        new_filename = f'{i+1}.jpg'
        
        # 獲取文件的完整路徑
        old_path = os.path.join(dir_path, filename)
        new_path = os.path.join(dir_path, new_filename)
        
        # 使用shutil模組進行文件重命名
        shutil.move(old_path, new_path)
        shutil.move(new_path, os.path.join(dir_path, new_filename))
