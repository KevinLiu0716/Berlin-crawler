# 若未安裝requests，執行以下指令
# pip install requests --user
import os
import requests
from concurrent.futures import ThreadPoolExecutor

# 設定要載的範圍 (Tile-x-y)
start_x = 102  # 開始x值
end_x = 115    # 結束x值(含)
start_y = 69   # 開始y值
end_y = 78     # 結束y值(含)
thread_num = 3 # 一次載幾個

# 塞入檔名進陣列
file_names = []
for x in range(start_x, end_x + 1):
    for y in range(start_y, end_y + 1):
        file_name = "Tile-" + str(x) + "-" + str(y) +"-1-1.zip"
        file_names.append(file_name)

# 下載函數
def Download(file_name):
    # 確認該檔案是否已存在
    if (os.path.exists(file_name)):
        print(file_name + " already exists!")
        return
    # 製作Placeholder
    open(file_name + ".tmp", "w")
    # 開始下載
    print("Downloading " + file_name + "...")
    url = "https://www.businesslocationcenter.de/berlin3d-downloadportal/datasource-data/berlin_mesh_2021/" + file_name
    r = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(r.content)
    # 刪除Placeholder
    if (os.path.exists(file_name + ".tmp")):
        os.remove(file_name + ".tmp")    

# 一次載n個
with ThreadPoolExecutor(max_workers=thread_num) as pool:
    pool.map(Download, file_names)
print("All Finished!!")