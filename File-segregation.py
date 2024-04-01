import os
import shutil as stl
from_dir="C:/Users/mail2/Documents/Python Projects/C-102 Project/From"
to_dir="C:/Users/mail2/Documents/Python Projects/C-102 Project/To"
lst_of_fls=os.listdir(from_dir)
'''print(lst_of_fls)'''
iext=[".png",".gif",".jfif",".jpg",".doc",".docx"]
for file  in lst_of_fls:
    name,ext=os.path.splitext(file)
    if ext in iext:
        p1=from_dir+"/"+file
        p2=to_dir+"/"+file
        stl.move(p1,p2)