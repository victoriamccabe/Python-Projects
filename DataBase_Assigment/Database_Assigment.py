import sqlite3


# Connect and create "assignment.db"
conn = sqlite3.connect('assignment.db')


with conn:
    cur = conn.cursor()
    
# Create table "tbl_files" if not exist 
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                fnum INTEGER PRIMARY KEY AUTOINCREMENT, \
                fname TEXT)")
    conn.commit()
conn.close()


# File list
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


# Connect to database "assignment.db"
conn = sqlite3.connect('assignment.db')
cur = conn.cursor()
    
# Add each item in fileList 
for item in fileList:
    cur.execute("INSERT INTO tbl_files (fname) VALUES (?)", (item,))
conn.commit()
conn.close()


# Connect to database "assignment.db"
conn = sqlite3.connect('assignment.db')
with conn:
    cur = conn.cursor()
    
    # Fetch and print .txt files
    cur.execute("SELECT fname FROM tbl_files WHERE fname LIKE '%.txt'")
    varFiles = cur.fetchall()
    print("The files that end with '.txt' are:")
    for item in varFiles:
        print(item[0])
