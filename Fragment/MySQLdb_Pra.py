import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="123456",db="cc",port=3306,charset="utf8")
cur = conn.cursor()
# cur.execute("insert into users (username,password,email) values (%s,%s,%s)",("python","123456","python@gmail.com"))
# conn.commit()

# cur.executemany("insert into users (username,password,email) values (%s,%s,%s)",(("google","111222","g@gmail.com"),("facebook","222333","f@face.book"),("github","333444","git@hub.com"),("docker","444555","doc@ker.com")))
# conn.commit()
cur.execute("select * from users")
lines = cur.fetchall()
for line in lines:
    print line
cur.execute("select * from users where id=7")
line_first = cur.fetchone()
print line_first
print lines
print cur.fetchall()
cur.execute("select * from users")
print cur.fetchone()
print cur.fetchone()
print cur.fetchone()
print "--------------"
cur.scroll(1)
print cur.fetchone()
cur.scroll(-2)
print cur.fetchone()
cur.scroll(1,"absolute")
print cur.fetchone()
print cur.fetchone()
print cur.fetchone()
cur.close()
conn.close()
