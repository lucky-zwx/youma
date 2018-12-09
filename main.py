import requests
import json
import sqlite3

GG = ['memberId', 'photoUrl', 'nick', 'gender', 'realName', 'majorName', 'gradeNumber', 'classNumber', 'type', 'fans', 'attention']



headers = {'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NDQ5MjQwMjAwMjcsImlhdCI6MTU0NDMxOTIyMDAyNywic2Vzc2lvbklkIjoiNDAyOGE1NWMtODIxZC00ZDZlLTg0ZDgtODg4ODA3ZjVlODQ2In0=.q7Nrpg6eBtbkSPacqzvHtkOj+yTKC095ZyNJbmJgFz4=',
           'Content-Type':'application/x-www-form-urlencoded',
           'Content-Length':'100',
           'Host':'portal.328ym.com',
           'Accept-Encoding':'gzip',
           'User-Agent':'okhttp/3.12.0'}
conn = sqlite3.connect('test.db')
c = conn.cursor()


for number in range(1,31):

    data = {'groupId': '58ea09b5ec9611e8bb3c02420a183a07', 'token':'27c23fc682284428a6c8bd9cd3f246e5', 'pageNo':str(number), 'pageSize':'100'}
    r = requests.post(url='http://portal.328ym.com/find/groupMember/memberList', headers=headers, data=data)
    r_json=json.loads(r.text)



    mess = r_json['data']['result']
    for num in range(0, 100):
        try:
            mes = r_json['data']['result'][num]
        except:
            continue
        mes2 = str(GG[0]+','+GG[1]+','+GG[2]+','+GG[3]+','+GG[4]+','+GG[5]+','+GG[6]+','+GG[7]+','+GG[8]+','+GG[9]+','+GG[10])
        mes3 = "\""+str(mes[GG[0]])+"\""+','+"\""+str(mes[GG[1]])+"\""+','+"\""+str(mes[GG[2]])+"\""+','+"\""+str(mes[GG[3]])+"\""+','+"\""+str(mes[GG[4]])+"\""+','+"\""+str(mes[GG[5]])+"\""+','+"\""+str(mes[GG[6]])+"\""+','+"\""+str(mes[GG[7]])+"\""+','+"\""+str(mes[GG[8]])+"\""+','+"\""+str(mes[GG[9]])+"\""+','+"\""+str(mes[GG[10]])+"\""
        submess = "INSERT INTO Message ("+mes2+") "+"VALUES ( "+mes3+" );"
        try:
            c.execute(submess)
        except BaseException:
            print(submess)
            continue
c.close()
conn.commit()
conn.close()
