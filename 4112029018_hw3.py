import os
import time
folder_path='CS/homework'
os.makedirs(folder_path)

with open('CS\homework\homework.txt', 'w') as file:
    file.write('4112029018_黃婷宓\n')

with open('CS\homework\homework.txt', 'r') as file:
    content=file.read()
    print(content)
    
file_size=os.path.getsize('CS\homework\homework.txt')
print(f'文件大小:{file_size}字節')
modification_time=os.path.getmtime('CS\homework\homework.txt')
print(f'最後修改時間:{modification_time}')
formatted_time=time.ctime(modification_time)
print(f'最後修改時間(人類可讀格式):{formatted_time}')

if os.path.exists('CS\homework\homework.txt'):
    os.remove('CS\homework\homework.txt')
    
import shutil
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
   
   






