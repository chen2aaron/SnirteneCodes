import sys
import json
from Utils import torndb
import sqlite3


keys = ('addIp','autoNum','bcrAcceptTime','bcrStatus','bcrUserName','bid','bidStatus','bidSubStatus','borroePeriod','borrowAmount','borrowAnnualYield','borrowEndTime','capital','cid','conllenctionMoney','creator','cumulativePer','currCid','currentExpectAmount','currentTenderAmount','debtFee','debtTenderSum','endDay','errMsg','flag','gmtCreated','gmtModified','id','incoming','instid','ipone','isAuto','isDeducted','isDeleted','isOver','loginName','mobile','modifier','order','page','pageNum','pageSize','paging','periodTimeUnit','pid','productTypeId','reVerifyTime','recoverStatus','repayTime','repaymentStyle','reportDate','retCode','rowNo','rows','securityNo','sort','source','start','stationName','stationNo','status','successTime','tenderAmount','tenderPer','tenderPerCount','tenderSum','tenderTime','title','totalAmount','transferId','tuid','uid','userName','verifyTime')

sql = 'insert wd_investments(%s) values(%s)' % (','.join('`%s`' % k for k in keys), ','.join(['%s']*len(keys)))
batch_size = 1000


def main(sl_filename):
    sl_conn = sqlite3.connect(sl_filename)
    sl_cursor = sl_conn.cursor()

    ms_conn = torndb.Connection(
            host='127.0.0.1:3366',
            database='',
            user='',
            password='',
            time_zone='+8:00',
            charset='utf8mb4',
            read_timeout=10,
            write_timeout=15,
    )

    sl_cursor.execute('select id,content from wd')

    batch = sl_cursor.fetchmany(batch_size)
    row_count = len(batch)

    while batch:
        param_list = []
        for row in batch:
            jc = json.loads(row[1], encoding='utf-8')
            for investment in jc['rows']:
                param_list.append(list(investment[k] for k in keys))

        ms_conn.executemany(sql, param_list)
        print(row_count)

        batch = sl_cursor.fetchmany(batch_size)
        row_count += len(batch)


if __name__ == '__main__':
    main(sys.argv[1])
