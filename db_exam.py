import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1234",
        db = "sensorDB"
)

cur = db.cursor()
cur.execute("insert into sensorTable values (now(), 1, 2)")
db.commit()
cur.execute("select * from sensorTable")

rows = cur.fetchall()
for row in rows:
    print(row)

db.close()
