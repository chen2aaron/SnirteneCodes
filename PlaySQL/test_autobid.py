import json
from decimal import Decimal
from pprint import pprint
from Utils import torndb


def db():
    print('-------- start --------')
    return torndb.Connection(
        host='127.0.0.1:3366',
        database='',
        user='',
        password='',
        time_zone='+8:00',
        charset='utf8mb4',
        read_timeout=10,
        write_timeout=15,
    )
borrowing = db().get('select * from borrowings where id=%s', 236)
money_min = Decimal('100.00')
money_max = Decimal('1000.00')
invest_amount = max(money_min, money_max)
coupon = db().query('select c.id, c.type, c.value_a, c.value_b, c.limits from coupons c '
                  ' where c.user_id=%s and c.status=0 and c.expire_at > NOW() '
                  ' order by c.expire_at', 83028)
valid_coupon = []
coupon_id = ''
duration = 'xd' if borrowing.duration_type == 0 else '%sm' % borrowing.duration
for c in coupon:

    coupon_limits = json.loads(c.limits) if c.limits else dict()

    if coupon_limits and duration not in coupon_limits.get('duration', ''):
        continue

    if c.type == 0 and c.value_a > invest_amount:
        continue

    coupon_interest = Decimal(0)       # 该券能获得的收益
    extend_invest_amount = Decimal(0)  # 该券可以使得投资金额扩大的部分

    if c.type == 0:
        coupon_interest = extend_invest_amount = c.value_b
    if c.type == 1:
        if borrowing.duration_type == 0:
            coupon_interest = round(invest_amount * c.value_a / 365 * borrowing.duration, 2)
        else:
            bonus_interest_limit = borrowing.duration
            if coupon_limits:
                bonus_interest_limit = min(coupon_limits.get('bonus_interest_limit', bonus_interest_limit),
                                           bonus_interest_limit)
            coupon_interest = round(invest_amount * c.value_a / 12 * bonus_interest_limit, 2)

    valid_coupon.append((c.id, coupon_interest, extend_invest_amount))
if valid_coupon:
    # 选择收益最大的优惠券
    selected_coupon = max(valid_coupon, key=lambda c: c[1])
    coupon_id, _, extend_invest_amount = selected_coupon
    invest_amount = invest_amount + extend_invest_amount
    print(selected_coupon)

pprint(valid_coupon)
print(max(money_min, money_max))
