import sqlite3
import psycopg2


conn = psycopg2.connect(dbname='d2mo1re4fcqlhr', host='ec2-107-20-151-189.compute-1.amazonaws.com', 
    user='ipbifgmvvhliav', password='4f013680ded4541e46c951b71eb51b07aa53d5a04deab331814a370005cffd3e')
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


cur.execute("create table seating ("
            "id serial primary key,"
            "name text not null,"
            "table_no integer"
            ");")



print("insertion successful")
conn.commit()

cur.execute("select * from users")

rows = cur.fetchall();
for row in rows:
    print(row)

cur.close()
conn.close()