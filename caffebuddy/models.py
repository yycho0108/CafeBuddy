# import sqlite3 as sql
import psycopg2


def insertUser(username, password):
    con = psycopg2.connect(dbname='d2mo1re4fcqlhr', user='ipbifgmvvhliav', host='ec2-107-20-151'
                                                                                '-189.compute-1.amazonaws.com',
                           password='4f013680ded4541e46c951b71eb51b07aa53d5a04deab331814a370005cffd3e')
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username, password))
    con.commit()
    con.close()

def retrieveUsers():
    con = psycopg2.connect(dbname='d2mo1re4fcqlhr', user='ipbifgmvvhliav' ,host='ec2-107-20-151'
        '-189.compute-1.amazonaws.com' ,password='4f013680ded4541e46c951b71eb51b07aa53d5a04deab331814a370005cffd3e')
    cur = con.cursor()
    cur.execute("SELECT username, password FROM users")
    users = cur.fetchall()
    con.close()
    return users

