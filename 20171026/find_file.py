#获取当前目录下最新的文件
import os

file_path = "E:\\selenium_py\\20171025\\"

lists = os.listdir(file_path)

lists.sort(key=lambda fn:os.path.getmtime(file_path+"\\"+fn))

print(("最新的文件为:")+lists[-1])

file = os.path.join(file_path,lists[-1])
print(file)