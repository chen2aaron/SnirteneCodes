from db import *


def select_table(table, column, condition, value):
    sql = "select" + column + "from" + table + \
        " where " + condition + "='" + value + "'"
    cur.excute(sql)
    lines = cur.fetchall()
    return lines
