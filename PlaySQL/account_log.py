from collections import namedtuple
from decimal import Decimal
from itertools import groupby
from operator import itemgetter
from pprint import pprint
import re
from Utils import torndb
from Utils.utils import PropDict

HEAD_SHOP_FEE = {
    'account_management_fee':   '管理费收入',
    'advance_interest':         '预收投资人收益',
    'refund_interest':          '退还投资人收益',
    'rate_diff_income':         '利率差异收入',
}

SHOP_TRADE_FEE = {
    'rate_diff_income':         '利率差异收入',
    'account_management_fee':   '综合服务费',

    'other_fee':                '其他费用',

    'refund_deposit':           '退还押金',

    'advance_interest':         '预收利息',
    'refund_interest':          '退还预收利息 ',

    'advance_payment':          '垫付还款',
    'renewal_principal':        '续借本金',
    'activity_bonus':           '活动奖励',

    'agency_fee':               '中介费',
    'valuation_fee':            '评估费',
    'park_fee':                 '停车费',
    'violation_deposit':        '违章押金',
    'gps_use_fee':              'GPS使用费',
    'trailer_fee':              '拖车费用',
    'risk_deposit':             '风险押金',
    'gps_deposit':              'GPS押金',

    'recharge':                 '充值',
    'investment':               '投资',
    'loan':                     '放款',
    'withdrawal':               '提现',
    'saving_pot_bonus':         '存钱罐收益',
    'transfer':                 '转账',
}
SHOP_TRADE_INFO = {
    'finished_at':              '日期',
    'user_name':                '客户',
    'borrowing_type':           '类型',
    'money':                    '借款金额',
    'duration_type':            '期限',
    'borrow_rate':              '利率',
    'salesman_name':            '业务员',
    'borrowing_id':             '标的',
    }



ShopTradeRow = namedtuple(
    'ShopTradeRow',
    ['finished_at', 'user_name', 'borrowing_type', 'money', 'duration_type', 'borrow_rate',
     'salesman_name', 'borrowing_id', 'service_fee', 'gps_use_fee', 'saving_pot_bonus',
     'other_fee', 'valuation_fee', 'park_fee', 'agency_fee', 'violation_deposit', 'trailer_fee',
     'account_management_fee', 'risk_deposit', 'gps_deposit', 'refund_deposit', 'advance_interest',
     'refund_advance_interest', 'advance_payment', 'renewal_principal', 'activity_bonus',
     'loan', 'transfer', 'recharge', 'withdrawal', 'investment'])
# s = ShopTradeRow(**SHOP_TRADE_TYPE)

def find(lst, key, value):
    for index, d in enumerate(lst):
        if d[key] == value:
            return index
    return -1

def filter_null_value(**kwargs):
    if 'borrowing_id' in kwargs:
        kwargs.pop('borrowing_id')
    return {k: kwargs[k] for k in kwargs.keys() if kwargs[k] != 0}


def chain_data(raw_data, **kwargs):
    if not kwargs:
        return raw_data

    if 'borrowing_id' not in kwargs:
        filter_kwargs = filter_null_value(**kwargs)
        return raw_data[0].update(filter_kwargs)

    index = find(raw_data, 'borrowing_id', kwargs['borrowing_id'])
    borrowing_id = kwargs.pop('borrowing_id')
    filter_kwargs = filter_null_value(**kwargs)

    if filter_kwargs:
        if index >= 0:
            raw_data[index].update(filter_kwargs)
        else:
            filter_kwargs.update(borrowing_id=borrowing_id)
            raw_data.append(filter_kwargs)

    return raw_data


def recharge_filter(iterable):
    pattern_recharge = re.compile(r'充值')
    data = []
    for i in iterable:
        if pattern_recharge.match(i.remark):
            i['recharge'] = i.balance_diff
        else:
            i['other_fee'] = i.balance_diff
        data.append(i)
    return data

def investment_filter(iterable):
    pattern_investment = re.compile(r'投资标的 (\d+)')
    data = []
    for i in iterable:
        if pattern_investment.match(i.remark):
            i['borrowing_id'] = pattern_investment.match(i.remark).group(1)
            i['investment'] = i.balance_diff
        else:
            i['other_fee'] = i.balance_diff
        data.append(i)
    return data

def withdrawal_filter(iterable):
    pattern_withdrawal = re.compile(r'申请提现')
    data = []
    for i in iterable:
        if pattern_withdrawal.match(i.remark):
            i['withdrawal'] = i.balance_diff
        else:
            i['other_fee'] = i.balance_diff
        data.append(i)
    return data

# 4
def fee_filter(iterable):
    pattern_agency_fee = re.compile(r'^标的 (\d+) .*中介费$')
    pattern_valuation_fee = re.compile(r'^标的 (\d+) .*评估费$')
    pattern_park_fee = re.compile(r'^标的 (\d+) .*停车费$')
    pattern_violation_deposit = re.compile(r'^标的 (\d+) .*违章押金$')
    pattern_gps_use_fee = re.compile(r'^标的 (\d+) .*GPS使用费$')
    pattern_account_management_fee = re.compile(r'\w+\s+(\d+)\s+\w+\s+(\d+)\s+\w+管理费')
    pattern_risk_deposit = re.compile(r'^标的 (\d+) .*风险押金$')
    pattern_gps_deposit = re.compile(r'^标的 (\d+) .*GPS押金$')
    pattern_refund_deposit = re.compile(r'^退还标的 (\d+) .*押金')
    pattern_refund_interest = re.compile(r'^退还标的 (\d+) .*收益')
    data = []
    for i in iterable:
        if pattern_agency_fee.match(i.remark):
            i['borrowing_id'] = pattern_agency_fee.match(i.remark).group(1)
            i['agency_fee'] = i.balance_diff
        elif pattern_valuation_fee.match(i.remark):
            i['borrowing_id'] = pattern_valuation_fee.match(i.remark).group(1)
            i['valuation_fee'] = i.balance_diff
        elif pattern_park_fee.match(i.remark):
            i['borrowing_id'] = pattern_park_fee.match(i.remark).group(1)
            i['park_fee'] = i.balance_diff
        elif pattern_violation_deposit.match(i.remark):
            i['borrowing_id'] = pattern_violation_deposit.match(i.remark).group(1)
            i['violation_deposit'] = i.balance_diff
        elif pattern_gps_use_fee.match(i.remark):
            i['borrowing_id'] = pattern_gps_use_fee.match(i.remark).group(1)
            i['gps_use_fee'] = i.balance_diff
        elif pattern_account_management_fee.match(i.remark):
            i['borrowing_id'] = pattern_account_management_fee.match(i.remark).group(1)
            i['account_management_fee'] = i.balance_diff
        elif pattern_risk_deposit.match(i.remark):
            i['borrowing_id'] = pattern_risk_deposit.match(i.remark).group(1)
            i['risk_deposit'] = i.balance_diff
        elif pattern_gps_deposit.match(i.remark):
            i['borrowing_id'] = pattern_gps_deposit.match(i.remark).group(1)
            i['gps_deposit'] = i.balance_diff
        elif pattern_refund_deposit.match(i.remark):
            i['borrowing_id'] = pattern_refund_deposit.match(i.remark).group(1)
            i['refund_deposit'] = i.balance_diff
        elif pattern_refund_interest.match(i.remark):
            i['borrowing_id'] = pattern_refund_interest.match(i.remark).group(1)
            i['refund_interest'] = i.balance_diff
        else:
            i['other_fee'] = i.balance_diff
        data.append(i)
    return data


# 5
def loan_filter(iterable):
    pattern_advance_payment = re.compile(r'垫付标的 (\d+)')
    data = []
    for i in iterable:
        if pattern_advance_payment.match(i.remark):
            i['borrowing_id'] = pattern_advance_payment.match(i.remark).group(1)
            i['advance_payment'] = i.balance_diff
        else:
            i['other_fee'] = i.balance_diff
        data.append(i)
    return data

# 6
def income_filter(iterable):
    pattern_advance_interest = re.compile(r'^预收标的 (\d+).*收益$')
    pattern_refund_advance_interest = re.compile(r'^退还标的 (\d+).*收益$')
    pattern_saving_pot_bonus=re.compile(r'存钱罐(\d+).*收益')
    data = []
    for i in iterable:
        if pattern_advance_interest.match(i.remark):
            i['borrowing_id'] = pattern_advance_interest.match(i.remark).group(1)
            i['advance_interest'] = i.balance_diff
        elif pattern_refund_advance_interest.match(i.remark):
            i['borrowing_id'] = pattern_refund_advance_interest.match(i.remark).group(1)
            i['refund_advance_interest'] = i.balance_diff
        elif pattern_saving_pot_bonus.match(i.remark):
            i['saving_pot_bonus'] = i.balance_diff
        else:
            i['other_fee'] = i.balance_diff
        data.append(i)
    return data

# 7
def commission_filter(iterable):
    pattern_service_fee = re.compile(r'^预收标的 (\d+).*管理费$')
    pattern_rate_diff_income = re.compile(r'^预收标的 (\d+).*资金成本差值$')
    data = []
    for i in iterable:
        if pattern_service_fee.match(i.remark):
            i['borrowing_id'] = pattern_service_fee.match(i.remark).group(1)
            i['service_fee'] = i.balance_diff
        elif pattern_rate_diff_income.match(i.remark):
            i['borrowing_id'] = pattern_rate_diff_income.match(i.remark).group(1)
            i['rate_diff_income'] = i.balance_diff
        else:
            i['other_fee'] = i.balance_diff
        data.append(i)
    return data

# 8
def bonus_filter(iterable):
    pattern_activity_bonus = re.compile(r'\w+|\s+|\d+奖励$')
    data = []
    for i in iterable:
        if pattern_activity_bonus.match(i.remark):
            i['activity_bonus'] = i.balance_diff
        else:
            i['other_fee'] = i.balance_diff
        data.append(i)
    return data

# 9
def transfer_filter(iterable):
    pattern_advance_payment = re.compile(r'垫付标的 (\d+)')
    pattern_activity_bonus = re.compile(r'标的 (\d+) 用户 (\d+) 推荐返点')
    pattern_activity_bonus_2 = re.compile(r'补充标的 (\d+) 借款本金')
    pattern_loan = re.compile(r'标的(\d+) 续借本金')
    pattern_withdrawal = re.compile(r'押金提现')
    data = []
    for i in iterable:
        if pattern_advance_payment.match(i.remark):
            i['borrowing_id'] = pattern_advance_payment.match(i.remark).group(1)
            i['advance_payment'] = i.balance_diff
        elif pattern_activity_bonus.match(i.remark):
            i['borrowing_id'] = pattern_activity_bonus.match(i.remark).group(1)
            i['activity_bonus'] = i.balance_diff
        elif pattern_activity_bonus_2.match(i.remark):
            i['borrowing_id'] = pattern_activity_bonus_2.match(i.remark).group(1)
            i['activity_bonus'] = i.balance_diff
        elif pattern_loan.match(i.remark):
            i['borrowing_id'] = pattern_loan.match(i.remark).group(1)
            i['loan'] = i.balance_diff
        elif pattern_withdrawal.match(i.remark):
            i['withdrawal'] = i.balance_diff
        else:
            i['other_fee'] = i.balance_diff
        data.append(i)
    return data


def merge_items(data):
    sorted_items = sorted(data, key=lambda k: k.get('borrowing_id', 'default'))
    result_items = []
    for borrowing_id, sub_items in groupby(sorted_items, key=lambda k: k.get('borrowing_id', 'default')):
        dl = {}
        dl['borrowing_id'] = borrowing_id
        sub_items = list(sub_items)
        for fee_type in SHOP_TRADE_FEE:
            dl[fee_type] = sum(item[fee_type] for item in sub_items if fee_type in item)
        result_items.append(dict(dl))
    return result_items

def remark_filter(**kwargs):
    kwargs = PropDict(kwargs)
    if 'remark' not in kwargs:
        return kwargs

    pattern_recharge = re.compile(r'充值')

    pattern_investment = re.compile(r'投资标的 (\d+)')

    pattern_withdrawal = re.compile(r'申请提现')

    pattern_agency_fee = re.compile(r'^标的 (\d+) .*中介费$')
    pattern_valuation_fee = re.compile(r'^标的 (\d+) .*评估费$')
    pattern_park_fee = re.compile(r'^标的 (\d+) .*停车费$')
    pattern_violation_deposit = re.compile(r'^标的 (\d+) .*违章押金$')
    pattern_gps_use_fee = re.compile(r'^标的 (\d+) .*GPS使用费$')
    pattern_account_management_fee = re.compile(r'\w+\s+(\d+)\s+\w+\s+(\d+)\s+\w+管理费')
    pattern_risk_deposit = re.compile(r'^标的 (\d+) .*风险押金$')
    pattern_gps_deposit = re.compile(r'^标的 (\d+) .*GPS押金$')
    pattern_refund_deposit = re.compile(r'^退还标的 (\d+) .*押金')
    pattern_refund_interest = re.compile(r'^退还标的 (\d+) .*收益')

    pattern_advance_payment = re.compile(r'垫付标的 (\d+)')

    pattern_advance_interest = re.compile(r'^预收标的 (\d+).*收益$')
    pattern_refund_advance_interest = re.compile(r'^退还标的 (\d+).*收益$')
    pattern_saving_pot_bonus=re.compile(r'存钱罐(\d+).*收益')

    pattern_service_fee = re.compile(r'^预收标的 (\d+).*管理费$')
    pattern_rate_diff_income = re.compile(r'^预收标的 (\d+).*资金成本差值$')

    pattern_activity_bonus = re.compile(r'\w+|\s+|\d+奖励$')

    pattern_advance_payment = re.compile(r'垫付标的 (\d+)')
    pattern_activity_bonus = re.compile(r'标的 (\d+) 用户 (\d+) 推荐返点')
    pattern_activity_bonus_2 = re.compile(r'补充标的 (\d+) 借款本金')
    pattern_loan = re.compile(r'标的(\d+) 续借本金')
    pattern_withdrawal = re.compile(r'押金提现')

    if pattern_recharge.match(kwargs.remark):
        kwargs['recharge'] = kwargs.balance_diff

    if pattern_investment.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_investment.match(kwargs.remark).group(1)
        kwargs['investment'] = kwargs.balance_diff

    if pattern_withdrawal.match(kwargs.remark):
        kwargs['withdrawal'] = kwargs.balance_diff

    if pattern_agency_fee.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_agency_fee.match(kwargs.remark).group(1)
        kwargs['agency_fee'] = kwargs.balance_diff
    elif pattern_valuation_fee.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_valuation_fee.match(kwargs.remark).group(1)
        kwargs['valuation_fee'] = kwargs.balance_diff
    elif pattern_park_fee.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_park_fee.match(kwargs.remark).group(1)
        kwargs['park_fee'] = kwargs.balance_diff
    elif pattern_violation_deposit.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_violation_deposit.match(kwargs.remark).group(1)
        kwargs['violation_deposit'] = kwargs.balance_diff
    elif pattern_gps_use_fee.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_gps_use_fee.match(kwargs.remark).group(1)
        kwargs['gps_use_fee'] = kwargs.balance_diff
    elif pattern_account_management_fee.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_account_management_fee.match(kwargs.remark).group(1)
        kwargs['account_management_fee'] = kwargs.balance_diff
    elif pattern_risk_deposit.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_risk_deposit.match(kwargs.remark).group(1)
        kwargs['risk_deposit'] = kwargs.balance_diff
    elif pattern_gps_deposit.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_gps_deposit.match(kwargs.remark).group(1)
        kwargs['gps_deposit'] = kwargs.balance_diff
    elif pattern_refund_deposit.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_refund_deposit.match(kwargs.remark).group(1)
        kwargs['refund_deposit'] = kwargs.balance_diff
    elif pattern_refund_interest.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_refund_interest.match(kwargs.remark).group(1)
        kwargs['refund_interest'] = kwargs.balance_diff

    if pattern_advance_payment.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_advance_payment.match(kwargs.remark).group(1)
        kwargs['advance_payment'] = kwargs.balance_diff

    if pattern_advance_interest.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_advance_interest.match(kwargs.remark).group(1)
        kwargs['advance_interest'] = kwargs.balance_diff
    elif pattern_refund_advance_interest.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_refund_advance_interest.match(kwargs.remark).group(1)
        kwargs['refund_advance_interest'] = kwargs.balance_diff
    elif pattern_saving_pot_bonus.match(kwargs.remark):
        kwargs['saving_pot_bonus'] = kwargs.balance_diff

    if pattern_service_fee.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_service_fee.match(kwargs.remark).group(1)
        kwargs['advance_interest'] = kwargs.balance_diff
    elif pattern_rate_diff_income.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_rate_diff_income.match(kwargs.remark).group(1)
        kwargs['rate_diff_income'] = kwargs.balance_diff

    if pattern_activity_bonus.match(kwargs.remark):
        kwargs['activity_bonus'] = kwargs.balance_diff

    if pattern_advance_payment.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_advance_payment.match(kwargs.remark).group(1)
        kwargs['advance_payment'] = kwargs.balance_diff
    elif pattern_activity_bonus.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_activity_bonus.match(kwargs.remark).group(1)
        kwargs['activity_bonus'] = kwargs.balance_diff
    elif pattern_activity_bonus_2.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_activity_bonus_2.match(kwargs.remark).group(1)
        kwargs['activity_bonus'] = kwargs.balance_diff
    elif pattern_loan.match(kwargs.remark):
        kwargs['borrowing_id'] = pattern_loan.match(kwargs.remark).group(1)
        kwargs['loan'] = kwargs.balance_diff
    elif pattern_withdrawal.match(kwargs.remark):
        kwargs['withdrawal'] = kwargs.balance_diff
    else:
        kwargs['other_fee'] = kwargs.balance_diff
    return kwargs

def sql_pra():
    print('-------- start --------')
    db = torndb.Connection(
        host='',
        database='',
        user='',
        password='',
        time_zone='+8:00',
        charset='utf8mb4',
        read_timeout=10,
        write_timeout=15,
    )
    al_data = db.query('select s.name, s.id, al.type, al.balance_diff, al.remark from account_logs al, users u, shops s where s.account_user_id=u.id and u.id=al.account_id and s.id>=0 and al.balance_diff !=0 order by type')
    data = []
    for type, items in groupby(al_data, key=itemgetter('type')):
        # 充值
        if type == 0:
            filtered_items = recharge_filter(items)
            data.extend(filtered_items)

        # 投资
        elif type == 1:
            filtered_items = investment_filter(items)
            data.extend(filtered_items)

        # 提现
        elif type == 2:
            filtered_items = withdrawal_filter(items)
            data.extend(filtered_items)

        # 放款
        elif type == 3:
            pass

        # 收费
        elif type == 4:
            filtered_items = fee_filter(items)
            data.extend(filtered_items)

        # 还款
        elif type == 5:
            filtered_items = loan_filter(items)
            data.extend(filtered_items)

        # 收益
        elif type == 6:
            filtered_items = income_filter(items)
            data.extend(filtered_items)

        # 佣金
        elif type == 7:
            filtered_items = commission_filter(items)
            data.extend(filtered_items)

        # 奖励
        elif type == 8:
            filtered_items = bonus_filter(items)
            data.extend(filtered_items)

        # 转账
        elif type == 9:
            filtered_items = transfer_filter(items)
            data.extend(filtered_items)

    # pprint(data)
    pprint(merge_items(data))




if __name__ == '__main__':
    # sql_pra()

    # k = {'borrowing_id': '32055', 'service_fee': Decimal('0'), 'advance_payment': Decimal('-402.00'), 'other_fee': Decimal('0'),}
    # print(filter_null_value(**k))

    # lst = [
    #     {'loan': Decimal('411.00'), 'borrowing_id': '538'},
    #     {'borrowing_id': '538', 'activity_bonus': Decimal('-250.00')},
    #     {'borrowing_id': '538', 'activity_bonus': Decimal('-0.50')}
    # ]
    # dl = defaultdict(list)
    # for fee_type in SHOP_TRADE_FEE:
    #     dl[fee_type] = sum(item[fee_type] for item in lst if fee_type in item)
    # pprint(dict(dl))
    d = {'type': 1, 'remark': '充值', 'name': '总店', 'id': 0, 'balance_diff': Decimal('1.25')}


