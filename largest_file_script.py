#import operating system
import os

file_data = []
for root, directories, files in os.walk('.'):
    for _file in files:
        path = os.path.join(root,_file)
        path = path.replace('.\\','')
        size = os.path.getsize(path)
        file_data.append((path,size))
      # takes all files in the local directory and gets the file size

import sqlite3

connection = sqlite3.connect(':memory:')
#connects to local memory
c = connection.cursor()

c.execute("CREATE TABLE local_files (File_Name TEXT, File_Size INTEGER)")
#creates a new table with two columns, file names and size
for i in file_data:
    query = "INSERT INTO local_files (File_Name,File_Size) VALUES(?,?)"
    c.execute(query,i)
query1 = "SELECT* FROM LOCAL_FILES ORDER BY 2 DESC LIMIT(5) "
for i in c.execute(query1):
    print(i)
