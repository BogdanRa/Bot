import sqlite3

conn = sqlite3.connect("mydatabase.db", check_same_thread = False)
cursor = conn.cursor()
#cursor.execute("CREATE TABLE LINK ('user_id' int, 'links' text)")




def appendlinks(message_id, link):
    data = [(message_id, str(link))]

    cursor.executemany("INSERT INTO LINK VALUES (?, ?)", data)
    conn.commit()

    #excute
    #sql = "SELECT * FROM saved_links"
    #cursor.execute(sql)
    #print (cursor.fetchall())

def execute(message_id):

    sql = "SELECT * FROM LINK where user_id=?"
    cursor.execute(sql, [(message_id)])
    for i, value in cursor.fetchall():
        return value

#sql = "SELECT * FROM LINK where user_id=?"
#cursor.execute(sql, [(148927934)])
#for i, valu in cursor.fetchall():
#    print valu