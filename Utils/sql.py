
def insert(table, params):
    """
    :param table: table name
    :param params:  {'column_a': value_a, '*column_b': value_b}  '*' means keep raw value, like 'NOW()'
    """

    ks = []
    vs = []

    r = []

    for k in params:
        if k.startswith('*'):
            ks.append(k.lstrip('*'))
            vs.append(str(params[k]))
        else:
            ks.append(k)
            vs.append('%s')
            r.append(params[k])

    sql = 'insert %s(%s) values (%s)' % (
        table,
        ','.join(ks),
        ','.join(vs),
    )
    r.insert(0, sql)
    return r


def update(table, params, condition=None):
    sql = []
    param = []

    for p, k in params.items():
        if p.startswith('*'):
            param.append('%s=%s' % (p.lstrip('*'), str(k)))
        else:
            param.append('%s=%%s' % p)
            sql.append(k)

    update_sql = 'update %s set %s ' % (table, ','.join(param))

    if condition:
        c_params = []
        c_key = []
        for p, k in condition.items():
            if p.startswith('*'):
                c_params.append('%s=%s' % (p.lstrip('*'), str(k)))
            else:
                c_params.append('%s=%%s' % p)
                c_key.append(k)
        update_sql += ' where %s' % ' and '.join(c_params)
        sql.extend(c_key)

    sql.insert(0, update_sql)
    return sql
