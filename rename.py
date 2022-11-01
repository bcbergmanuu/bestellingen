import os
from datetime import datetime

files = [file for file in os.listdir(os.getcwd()) if file.endswith('.txt')]

for item in files:    
    dateobj = datetime.strptime(item, '%d-%m-%Y.txt')        
    os.rename(item, dateobj.strftime("%Y-%m-%d.txt"))
