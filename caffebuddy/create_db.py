import sqlite3

conn = sqlite3.connect("/Users/vadimcastro/Desktop/katePerkins/CafeBuddy/caffebuddy/cafebuddy.db")
print("db created successfully")

cur = conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS people (first_name TEXT, last_name TEXT, table_no INTEGER);")
# cur.execute("INSERT INTO people (first_name,last_name, table_no) VALUES"
#                 "('Murtaza','Haji',1),"
#                 "('Vadim','Castro', 2),"
#                 "('Jamie','Cho', 3),"
#                 "('Serena','Chen', 4),"
#                 "('Gwendal','Plumier',5),"
#                 "('Kimberly', 'Winter', 6)")


# cur.execute("create table users ("
#             "id integer primary key autoincrement,"
#             "username text not null,"
#             "password text not null"
#             ");")



print("insertion successful")
conn.commit()

cur.execute("select * from users")

rows = cur.fetchall();
for row in rows:
    print(row)

cur.close()
conn.close()