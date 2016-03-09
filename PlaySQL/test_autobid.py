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
borrowing = db().get('select * from borrowings where id=%s', 555)
coupon = db().query('select c.id, c.type, c.value_a, c.value_b, c.limits from coupons c '
                  ' where c.user_id=%s and c.status=0 and c.expire_at > NOW() '
                  ' order by c.expire_at', 83028)
valid_coupon = []
money_min = Decimal('100.00')
money_max = Decimal('1000.00')
duration = 'xd' if borrowing.duration_type == 0 else '%sm' % borrowing.duration
for c in coupon:
    coupon_interest = Decimal('0.00')
    if c.limits and duration not in json.loads(c.limits).get('duration', ''):
        continue
    if c.type == 0 and c.value_a <= max(money_min, money_max):
        coupon_interest = c.value_b
    if c.type == 1:
        if borrowing.duration_type == 0:
            coupon_interest = round(max(money_min, money_max) * c.value_a / 365 * borrowing.duration, 2)
        else:
            bonus_interest_limit = json.loads(c.limits).get('bonus_interest_limit', '')
            if bonus_interest_limit:
                coupon_interest = round(max(money_min, money_max) * c.value_a / 12 * min(bonus_interest_limit, borrowing.duration), 2)
            else:
                coupon_interest = round(max(money_min, money_max) * c.value_a / 12 * borrowing.duration, 2)
    valid_coupon.append((c.id, coupon_interest, c.value_b or Decimal('0.00')))
if valid_coupon:
    # 选择收益最大的优惠券
    selected_coupon = max(valid_coupon, key=lambda c: c[1])
    coupon_id = selected_coupon[0]
    money_max = max(money_min, money_max) + selected_coupon[2]
    print(selected_coupon)

pprint(valid_coupon)
print(max(money_min, money_max))
