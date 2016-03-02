# -*- coding:utf8 -*-
# Author: xixijun
# Github: github.com/chen2aaron
# Date: 15/7/20
# Python 3.4
from Utils.utils import qf
a = 8273.2133
b = 21398739821.232
print(qf(b))
from datetime import datetime, timedelta
today = datetime.today()
print(today)
# start_time = datetime.strptime(today, '%Y%m%d%H%M%S')
# print(start_time)
today2 = datetime.date((datetime.now()))
print(today+timedelta(5))
print(timedelta(5))
TRADE_STATUS_CHOICES = list(zip(range(4), ('待处理', '处理中', '成功', '失败')))
print(zip(range(4), ('待处理', '处理中', '成功', '失败')))
