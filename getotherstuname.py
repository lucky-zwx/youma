import sqlite3
import requests
import json


headers = {'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NDQ5MjQwMjAwMjcsImlhdCI6MTU0NDMxOTIyMDAyNywic2Vzc2lvbklkIjoiNDAyOGE1NWMtODIxZC00ZDZlLTg0ZDgtODg4ODA3ZjVlODQ2In0=.q7Nrpg6eBtbkSPacqzvHtkOj+yTKC095ZyNJbmJgFz4=',
           'Content-Type':'application/x-www-form-urlencoded',
           'Content-Length':'100',
           'Host':'portal.328ym.com',
           'Accept-Encoding':'gzip',
           'User-Agent':'okhttp/3.12.0'}

conn = sqlite3.connect('test.db')
c = conn.cursor()

cursor = c.execute("SELECT * from Message")


for message in cursor.fetchall():

    data = {'otherMemberId': message[0], 'token': '27c23fc682284428a6c8bd9cd3f246e5'}
    r = requests.post(url='http://portal.328ym.com/member/member/memberBasic', headers=headers, data=data)
    r_json = json.loads(r.text)
    mes = "\""+str(r_json['data']['realName'])+"\""+","+"\""+str(r_json['data']['phone'])+"\""+","+"\""+str(r_json['data']['studentNo'])+"\""
    print(mes)
    c.execute("INSERT INTO new (name,phone,number ) "+"VALUES ( "+mes+" );")

conn.commit()
c.close()
conn.close()
