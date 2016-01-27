# -*- coding: utf-8 -*-
import json
import torndb
from Utils.utils import json_hook, json_dumps


def update_auto_bid_duration():
    """
        将user_info表中的auto_bid的
        7d,10d,15d,20d都改成xd
    """
    print('-------- start update auto_bid duration --------')
    db = torndb.Connection(
        host='127.0.0.1:3366',
        database='yourdatebasename',
        user='yourname',
        password='yourpassword',
        time_zone='+8:00',
        charset='utf8mb4',
        read_timeout=10,
        write_timeout=15,
    )

    bid_rows = db.query('select user_id, auto_bid from user_info '
                        'where auto_bid is not null and auto_bid != %s', '')
    for bid_row in bid_rows:
        print('------ user_id: %s ------' % bid_row.user_id)
        bid_json = json.loads(bid_row.auto_bid, object_hook=json_hook)
        print('old duration: %s ' % bid_json.duration)
        day_list = ['7d', '10d', '15d', '20d']
        d_duration = []  # 所有的天标
        m_duration = []  # 所有的月标
        for i in bid_json.duration:
            if i in day_list:
                d_duration.append(i)
            else:
                m_duration.append(i)
        if d_duration:
            d_duration = ['xd']
        new_duration = d_duration + m_duration
        print('new duration: %s' % str(new_duration))
        bid_json.update(duration=new_duration)
        db.execute('update user_info set auto_bid=%s '
                   'where user_id=%s', json_dumps(bid_json), bid_row.user_id)
    db.close()


if __name__ == '__main__':
    update_auto_bid_duration()
