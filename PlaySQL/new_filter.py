from itertools import groupby
from pprint import pprint
import re
from PlaySQL.account_log import SHOP_TRADE_FEE
from Utils import torndb

pattern_recharge = re.compile(r'充值')
def filter_recharge(row):
    if row.type == 0:
        p = pattern_recharge.match(row.remark)
        if p:
            row['recharge'] = row.balance_diff
            return {
                'recharge': row.balance_diff,
                }

pattern_investment = re.compile(r'投资标的 (\d+)')
def filter_investment(row):
    if row.type == 1:
        p = pattern_investment.match(row.remark)
        if p:
            return {
                'borrowing_id': p.group(1),
                'investment': row.balance_diff,
                }

pattern_withdrawal = re.compile(r'\w+提现')
def filter_withdrawal(row):
    if row.type in (2, 9):
        p = pattern_withdrawal.match(row.remark)
        if p:
            return {
                'withdrawal': row.balance_diff,
                }

pattern_agency_fee = re.compile(r'^标的 (\d+) .*中介费$')
def filter_agency_fee(row):
    if row.type == 4:
        p = pattern_agency_fee.match(row.remark)
        if p:
            return {
                'borrowing_id': p.group(1),
                'agency_fee': row.balance_diff,
                }

pattern_valuation_fee = re.compile(r'^标的 (\d+) .*评估费$')
def filter_valuation_fee(row):
    if row.type == 4:
        p = pattern_valuation_fee.match(row.remark)
        if p:
            return {
                'borrowing_id': p.group(1),
                'valuation_fee': row.balance_diff,
                }

pattern_park_fee = re.compile(r'^标的 (\d+) .*停车费$')
def filter_park_fee(row):
    if row.type == 4:
        p = pattern_park_fee.match(row.remark)
        if p:
            return {
                'borrowing_id': p.group(1),
                'park_fee': row.balance_diff,
                }

pattern_violation_deposit_1 = re.compile(r'^标的 (\d+) .*违章押金$')
pattern_violation_deposit_2 = re.compile(r'标的 (\d+) 首期 押金')
def filter_violation_deposit(row):
    if row.type == 4:
        p1 = pattern_violation_deposit_1.match(row.remark)
        p2 = pattern_violation_deposit_2.match(row.remark)
        p = p1 or p2
        if p:
            return {
                'borrowing_id': p.group(1),
                'violation_deposit': row.balance_diff,
                }

pattern_gps_use_fee = re.compile(r'^标的 (\d+) .*GPS使用费$')
def filter_gps_use_fee(row):
    if row.type == 4:
        p = pattern_gps_use_fee.match(row.remark)
        if p:
            return {
                'borrowing_id': p.group(1),
                'gps_use_fee': row.balance_diff,
                }

pattern_account_management_fee = re.compile((r'\w+\s+(\d+)[\s\w]+管理费'))
def filter_account_management_fee(row):
    if row.type in (4, 7):
        p = pattern_account_management_fee.match(row.remark)
        if p:
            return {
                'borrowing_id': p.group(1),
                'account_management_fee': row.balance_diff,
                }

pattern_risk_deposit = re.compile(r'^标的 (\d+) .*风险押金$')
def filter_risk_deposit(row):
    if row.type == 4:
        p = pattern_risk_deposit.match(row.remark)
        if p:
            return {
                'borrowing_id': p.group(1),
                'risk_deposit': row.balance_diff,
                }

pattern_gps_deposit = re.compile(r'^标的 (\d+) .*GPS押金$')
def filter_gps_deposit(row):
    if row.type == 4:
        p = pattern_gps_deposit.match(row.remark)
        if p:
            return {
                'borrowing_id': p.group(1),
                'gps_deposit': row.balance_diff,
                }

pattern_refund_deposit = re.compile(r'^退还标的 (\d+) .*押金')
def filter_refund_deposit(row):
    if row.type == 4:
        p = pattern_refund_deposit.match(row.remark)
        if p:
            return {
                'borrowing_id': p.group(1),
                'refund_deposit': row.balance_diff,
                }

pattern_refund_interest = re.compile(r'^退还标的 (\d+) .*收益')
def filter_refund_interest(row):
    if row.type in (4, 6):
        p = pattern_refund_interest.match(row.remark)
        if p:
            return {
                'borrowing_id': p.group(1),
                'refund_interest': row.balance_diff,
                }

pattern_advance_payment = re.compile(r'垫付标的 (\d+)')
def filter_advance_payment(row):
    if row.type in (5, 9):
        p = pattern_advance_payment.match(row.remark)
        if p:
            return {
                'borrowing_id': p.group(1),
                'advance_payment': row.balance_diff,
                }

pattern_advance_interest = re.compile(r'^预收标的 (\d+).*收益$')
def filter_advance_interest(row):
    if row.type == 6:
        p = pattern_advance_interest.match(row.remark)
        if p:
            return {
                'borrowing_id': p.group(1),
                'advance_interest': row.balance_diff,
                }


pattern_saving_pot_bonus=re.compile(r'存钱罐(\d+).*收益')
def filter_saving_pot_bonus(row):
    if row.type == 6:
        p = pattern_saving_pot_bonus.match(row.remark)
        if p:
            return {
                'saving_pot_bonus': row.balance_diff,
                }


pattern_rate_diff_income_1 = re.compile(r'^预收标的 (\d+).*资金成本差值$')
pattern_rate_diff_income_2 = re.compile(r'[\w\s]+利息差额')
def filter_rate_diff_income(row):
    if row.type == 7:
        p1 = pattern_rate_diff_income_1.match(row.remark)
        p2 = pattern_rate_diff_income_2.match(row.remark)
        if p1:
            return {
                'borrowing_id': p1.group(1),
                'rate_diff_income': row.balance_diff,
                }
        elif p2:
            return {
                'rate_diff_income': row.balance_diff,
            }


pattern_activity_bonus_1 = re.compile(r'[\w\s]+奖励')
pattern_activity_bonus_2 = re.compile(r'标的 (\d+) 用户 (\d+) 推荐返点')
pattern_activity_bonus_3 = re.compile(r'补充标的 (\d+) 借款本金')
def filter_activity_bonus(row):
    if row.type == 8:
        p1 = pattern_activity_bonus_1.match(row.remark)
        if p1:
            return {'activity_bonus': row.balance_diff}
    elif row.type == 9:
        p2 = pattern_activity_bonus_2.match(row.remark)
        p3 = pattern_activity_bonus_3.match(row.remark)
        if p2:
            return {
                'borrowing_id': p2.group(1),
                'activity_bonus': row.balance_diff,
                }
        elif p3:
            return {
                'borrowing_id': p3.group(1),
                'activity_bonus': row.balance_diff,
            }


pattern_loan_1 = re.compile(r'标的(\d+) 续借本金')
pattern_loan_2 = re.compile(r'标的 (\d+) 到账')
def filter_loan(row):
    if row.type in (3, 9):
        p1 = pattern_loan_1.match(row.remark)
        p2 = pattern_loan_2.match(row.remark)
        p = p1 or p2
        if p:
            return {
                'borrowing_id': p.group(1),
                'loan': row.balance_diff,
            }


def filter_other_fee(row):
    return {
        'other_fee': row.balance_diff,
        }


def filter_withdrawal_transfer(row):
    pattern = re.compile(r'')
    if row.type == 1 and pattern.match(row.remark):
        result = [None,] * 10
        result[20] = 1
        result[21] = 1
        return result


def merge_items(data):
    sorted_items = sorted(data, key=lambda k: k.get('borrowing_id', 'default'))
    result_items = []
    for borrowing_id, sub_items in groupby(sorted_items, key=lambda k: k.get('borrowing_id', 'default')):
        data_item = {}
        data_item['borrowing_id'] = borrowing_id
        sub_items = list(sub_items)
        for fee_type in SHOP_TRADE_FEE:
            data_item[fee_type] = sum(item[fee_type] for item in sub_items if fee_type in item)

        # 过滤掉value为0的key
        result_items.append({k: data_item[k] for k in data_item.keys() if data_item[k] != 0})
    return result_items


def main():
    print('-------- start --------')
    db = torndb.Connection(
        host='127.0.0.1',
        database='',
        user='',
        password='',
        time_zone='+8:00',
        charset='utf8mb4',
        read_timeout=10,
        write_timeout=15,
    )
    al_data = db.query('select s.name, s.id, al.type, al.balance_diff, al.remark, al.created_at '
                       'from account_logs al, users u, shops s '
                       'where s.account_user_id=u.id and u.id=al.account_id '
                       'and s.id>=0 and al.balance_diff !=0 and al.created_at>"2015-04-01" order by type')
    filters = [
        filter_recharge,
        filter_investment,
        filter_withdrawal,
        filter_agency_fee,
        filter_valuation_fee,
        filter_park_fee,
        filter_violation_deposit,
        filter_gps_use_fee,
        filter_account_management_fee,
        filter_risk_deposit,
        filter_gps_deposit,
        filter_refund_deposit,
        filter_refund_interest,
        filter_advance_payment,
        filter_advance_interest,
        filter_saving_pot_bonus,
        filter_rate_diff_income,
        filter_activity_bonus,
        filter_loan,
        filter_other_fee,
    ]
    filtered_data = []
    for data_item in al_data:
        for f in filters:
            filtered_item = f(data_item)
            if filtered_item is not None:
                filtered_data.append(filtered_item)
                break
                # print(filtered_item)
    # pprint(filtered_data)
    result = merge_items(filtered_data)
    pprint(result)

if __name__ == '__main__':
    main()
