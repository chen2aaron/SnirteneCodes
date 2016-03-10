import json
from PlaySQL.test_autobid import db

coupon = db().get('select c.* from coupons c '
                  ' where c.status = 0 and c.expire_at > NOW() and c.id=%s and user_id=%s ', 386, 83028)
coupon.limits = json.loads(coupon.limits)
if coupon.limits:
    print(coupon.limits)
    # coupon.limits = json.loads(coupon.limits)
    print(type(coupon.limits))
