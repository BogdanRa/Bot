import sqlite3

conn = sqlite3.connect("mydatabase.db", check_same_thread = False)
cursor = conn.cursor()




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

def other_excute(user_id):
    links = []
    cursor = conn.cursor()

    sql = "SELECT * FROM data where user_id=? and category not LIKE ? and category not like ?  and category not like ?"
    cursor.execute(sql, [(user_id), ('%'+'habr'+'%'), ('%'+'xakep'+'%'), ('%'+'tproger'+'%')])
    for value in cursor.fetchall():
        links.append(value[1])
    return links

