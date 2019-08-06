import sqlite3

conn = sqlite3.connect("mydatabase.db", check_same_thread = False)
cursor = conn.cursor()
#cursor.execute("CREATE TABLE LINK ('user_id' int, 'links' text)")




def appendlinks(message_id, link):
    data = [(message_id, str(link))]
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO LINK VALUES (?, ?)", data)
    conn.commit()


def execute(user_id):
    links = []
    cursor = conn.cursor()
    sql = "SELECT * FROM LINK where user_id=?"
    cursor.execute(sql, [(user_id)])
    for i, value in cursor.fetchall():
        links.append(value)
    return links



sql = "select * FROM LINK where user_id=?"
cursor.execute(sql, [(148927934)])
#conn.commit()
print cursor.fetchall()
