from collections import OrderedDict, namedtuple

d = OrderedDict()
ShopTradeTable = namedtuple(
    'ShopTradeTable',
    ['finished_at', 'user_name', 'borrowing_type', 'money', 'duration_type', 'borrow_rate',
     'salesman_name', 'borrowing_id', 'service_fee', 'gps_use_fee',
     'other_fee', 'valuation_fee', 'park_fee', 'agency_fee', 'violation_deposit', 'trailer_fee',
     'account_management_fee', 'risk_deposit', 'gps_deposit', 'refund_deposit', 'advance_interest',
     'refund_advance_interest', 'advance_payment', 'renewal_principal', 'activity_bonus'])
SHOP_TRADE_TYPE = {
    'finished_at':              '日期',
    'user_name':                '客户',
    'borrowing_type':           '类型',
    'money':                    '借款金额',
    'duration_type':            '期限',
    'borrow_rate':              '利率',
    'salesman_name':            '业务员',
    'borrowing_id':             '标的',
    'service_fee':              '综合服务费',
    'other_fee':                '其他费用',
    'refund_deposit':           '退还押金',
    'advance_interest':         '预收利息',
    'refund_advance_interest':  '退还预收利息 ',
    'advance_payment':          '垫付还款',
    'renewal_principal':        '续借本金',
    'activity_bonus':           '活动奖励',
    'agency_fee':               '中介费',
    'valuation_fee':            '评估费',
    'park_fee':                 '停车费',
    'violation_deposit':        '违章押金',
    'gps_use_fee':              'GPS使用费',
    'trailer_fee':              '拖车费用',
    'account_management_fee':   '账户管理费',
    'risk_deposit':             '风险押金',
    'gps_deposit':              'GPS押金',
}
s = ShopTradeTable(**SHOP_TRADE_TYPE)
print(s)
