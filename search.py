import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

while(True):
    sname = input("请输入人名：")
    mess = c.execute("SELECT * from new where name like "+"\'"+sname+"\'")
    for i in mess:
        print(i)
c.close()
conn.close()
