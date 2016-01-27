import sqlite3
from Utils import torndb, sql

def db_client():
    db = torndb.Connection(
        host='127.0.0.1:3306',
        database='wd',
        user='root',
        password='',
        time_zone='+8:00',
        charset='utf8mb4',
    )
    return db
def main(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    rows = c.execute('select * from wd limit 3851, 2')
    for r in rows:
        # print(r)
        args = r[1]
        print(args)
        print(type(args))
        # db_client().execute(*sql.insert('wd', args))
        # print(c.fetchone())

if __name__ == '__main__':
    main('/Users/chan/Downloads/wd')