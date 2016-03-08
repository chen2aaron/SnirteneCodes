import json
from decimal import Decimal
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
borrowing = db().get('select * from borrowings where id=%s', 544)
coupon = db().query('select c.id, c.type, c.value_a, c.value_b, c.limits from coupons c '
                  ' where c.user_id=%s and c.status=0 and c.expire_at > NOW() '
                  ' order by c.expire_at', 83028)
valid_coupon = []
coupon_interest = 0
money_min = Decimal('100.00')
money_max = Decimal('1100.00')

duration = 'xd' if borrowing.duration_type == 0 else '%sm' % borrowing.duration
for c in coupon:
    if c.limits and duration not in json.loads(c.limits).get('duration', ''):
        continue
    if c.type == 0 and c.value_a <= max(money_min, money_max):
        coupon_interest = c.value_b
    if c.type == 1:
        coupon_interest = max(money_min, money_max) * c.value_a
    valid_coupon.append((c.id, coupon_interest))
print(valid_coupon)
coupon_select = max(valid_coupon, key=lambda c: c[1])
print(coupon_select)
print(borrowing)
