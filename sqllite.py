import sqlite3

#conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()


#cursor.execute("""CREATE TABLE saved_links
#                 (user_id, links, category_id)
#               """)


def appendlinks(message_id, link, category):
    data = [(message_id, link, category)]

    cursor.executemany("INSERT INTO saved_links VALUES (?,?,?)", data)
    conn.commit()

    sql = "SELECT * FROM saved_links"
    cursor.execute(sql)
    print (cursor.fetchall())

#appendlinks(2, 'http://prnhub.com', 'xss')

for row in cursor.execute("SELECT * FROM saved_links"):
   print(row)