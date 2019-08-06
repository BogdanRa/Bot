import sqlite3

conn = sqlite3.connect("mydatabase.db", check_same_thread = False)
cursor = conn.cursor()
#cursor.execute("CREATE TABLE data ('user_id' int, 'links' text, 'category' text)")
#conn.commit()



def appendlinks(message_id, link, domain):
    data = [(message_id, str(link), domain)]

    cursor = conn.cursor()
    cursor.executemany("INSERT INTO data VALUES (?, ?, ?)", data)
    conn.commit()


def execute(user_id, category):
    links = []
    cursor = conn.cursor()
    sql = "SELECT * FROM data where user_id=? and category LIKE ?"
    cursor.execute(sql, [(user_id), ('%'+category+'%')])
    for value in cursor.fetchall():
        links.append(value[1])
    return links




#sql = "select * FROM data where user_id=? and category like ?"
#cursor.execute(sql, [(148927934), ('%'+'habr'+'%')])
#for value in cursor.fetchall():
#    print value[1]
#conn.commit()
#print cursor.fetchall()
