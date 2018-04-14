import sqlite3
import psycopg2


conn = psycopg2.connect(dbname='d2mo1re4fcqlhr', host='ec2-107-20-151-189.compute-1.amazonaws.com', 
    user='ipbifgmvvhliav', password='4f013680ded4541e46c951b71eb51b07aa53d5a04deab331814a370005cffd3e')
print("db created successfully")

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS people_attr (name TEXT, relationship TEXT, class_year TEXT, major TEXT, misc TEXT);")
cur.execute("INSERT INTO people_attr (name, relationship, class_year, major, misc) VALUES"
                "('Murtaza Haji', 'Friend', 'Class of 2019', 'Computer and Informational Sciences Major', 'Helps me in math class'),"
                "('Vadim Castro', 'Acquaintance', 'Class of 2019', 'Computer Science and Applied Math Major', ''),"
                "('Jamie Cho', 'Friend', 'Class of 2019', 'Robotics Major', 'Eats lots of bagels'),"
                "('Serena Chen', 'Stranger', 'Class of 2019', 'Computing Major', ''),"
                "('Gwendal Plumier','Stranger', 'Class of 2018', 'Biochemistry Major', 'Exchange student from Belgium'),"
                "('Kim Winter', 'Friend', 'Class of 2019', 'Electrical and Computer Engineering Major', '')")


# cur.execute("create table seating ("
#             "id serial primary key,"
#             "name text not null,"
#             "table_no integer"
#             ");")



print("insertion successful")
conn.commit()

cur.execute("select * from users")

rows = cur.fetchall();
for row in rows:
    print(row)

cur.close()
conn.close()