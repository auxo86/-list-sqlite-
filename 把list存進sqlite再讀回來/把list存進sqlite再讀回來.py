import sqlite3
import uuid
from copy import deepcopy

conn = sqlite3.connect('job_arrange.db')
listJobObjsInOneDay = [('test' + str(i)) for i in range(0, 10, 1)]
listDaysArray = [deepcopy(listJobObjsInOneDay) for i in range(0, 20,1)]
conn.execute('CREATE TABLE if not exists JobHistory (ID STRING PRIMARY KEY, strTest BLOB);')
conn.execute('delete from JobHistory')
for x in listDaysArray:
    conn.execute('insert into JobHistory values (?,?)', (str(uuid.uuid4()),str(x)))
conn.commit()
c = conn.cursor()
c.execute('select strTest from JobHistory')
xArray = c.fetchall()
xArrayNew = []
for item in xArray:
    item = eval(item[0])
    xArrayNew.append(item)
if listDaysArray == xArrayNew:
    print('true')
else:
    print('false')
conn.close()