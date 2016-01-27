# -*- coding: utf-8 -*-
import json
from pprint import pprint
import string
from Utils import torndb


def sql_pra():
    print('-------- start --------')
    db = torndb.Connection(
        host='127.0.0.1:3366',
        database='',
        user='',
        password='',
        time_zone='+8:00',
        charset='utf8mb4',
        read_timeout=10,
        write_timeout=15,
    )

    # r.status=2 成功充值
    # u.borrowd=0 没借过款

    recharges = db.get('select count(1) total_count, sum(amount) total_amount, '
                       'count(case when r.type=0 then 1 else NULL end) online_count, '
                       'sum(case when r.type=0 then r.amount else 0 end) online_amount, '
                       'count(case when r.type in (1,2) then 1 else NULL end) binding_count, '
                       'sum(case when r.type in (1,2) then r.amount else 0 end) binding_amount '
                       'from recharges r, users u where r.user_id=u.id and r.status=2 and u.borrowed=0  '
                       'and r.user_id not in (select account_user_id from shops where status=0)')

    withdrawals = db.get('select count(1) total_count, sum(w.amount) total_amount '
                         'from withdrawals w, users u where w.user_id=u.id and w.status=2 and u.borrowed=0 '
                         'and w.user_id not in (select account_user_id from shops where status=0)')

    balance = db.get('select sum(a.balance) balance from accounts a, users u '
                     'where a.user_id=u.id and u.borrowed=0 '
                     'and a.user_id not in (select account_user_id from shops where status=0) '
                     )

    receivables = db.get('select sum(r.capital) capital, sum(r.interest) interest '
                         'from receivables r, users u, investments i '
                         'where r.investment_id=i.id and i.user_id=u.id and u.borrowed=0 and r.status = 0 '
                         'and i.user_id not in (select account_user_id from shops where status=0)')

    # 总标数 最大标的金额 标的平均金额 各门店标数 100000以上标数 续借/新标数 手动标/自动标数
    borrowings = db.get('select count(id) all_count, round(avg(b.money),2) avg_money, '
                        ' sum(b.money) total_money, '
                        ' count(case when b.auto_bid = 1 then b.id else NULL end) auto_bid_count, '
                        ' sum(case when b.renew_from is null then 1 else 0 END) new_borrowings, '
                        ' count(id)-sum(case when b.renew_from is null then 1 else 0 END) renew_borrowings'
                        ' from borrowings b where b.status in (4, 5)')

    payables = db.get('select sum(capital) capital, sum(interest) interest from payables where status = 0')

    shops_b = db.query('select s.name shop_name, count(b.id) count from borrowings b, shops s '
                       ' where b.shop_id=s.id and b.status in (4,5) group by b.shop_id')

    members = db.get('select count(id) all_members, count(case when u.name!="" then 1 else NULL end) has_name,'
                     ' sum(u.borrowed) borrowed_count, '
                     ' count(case when TIMESTAMPDIFF(day, u.created_at, now()) <=7 '
                     ' then 1 else NULL end) last_seven_signup, '
                     ' count(case when TIMESTAMPDIFF(day, u.last_active, now()) <=7 then 1 else NULL end) '
                     ' last_active, '
                     ' count(case when ui.auto_bid is null or ui.auto_bid="" then 1 else NULL END)'
                     ' auto_bid_off, count(case when ui.ref_from !="" then 1 else NULL end) inv '
                     ' from users u, user_info ui where ui.user_id=u.id and u.status=0 ')
    receivable = db.get('select coalesce(sum(r.capital), 0.00) capital, '
                             'coalesce(sum(r.interest), 0.00) interest '
                             'from receivables r, investments i '
                             'where r.investment_id=i.id and i.user_id=%s and r.status=0', 83028)
    # print(recharges)
    # print(withdrawals)
    # print(balance)
    # print(receivables)
    # print(borrowings)
    # print(payables)
    # print(shops_b)
    # print(members)
    # print(receivable)
    # first_invest = db.get('select * from investments where status=2 and user_id=%s '
    #                       'and (select invest_count from users where id=%s)=1', 83025,83025)
    # print(first_invest)
    # if first_invest:
    #     first_invest.amount=21000
    #     print('OK')
    #     if 5000 <= first_invest.amount < 10000:
    #         print(20)
    #     elif 10000 <= first_invest.amount < 20000:
    #         print(30)
    #     elif first_invest.amount >= 20000:
    #         print(40)
    # else:
    #     print('false')


    rows = db.query('select brand_code, name, en_name, pinyin from car_brands order by pinyin')
    items = []
    brands = []
    args = {}
    for s in string.ascii_uppercase:
        for row in rows:
            if not row.pinyin.upper().startswith(s):
                continue
            else:
                brands.append(row.brand_code)
            args = {
                'key': s,
                'brands': brands
            }
        if args:
            items.append(args)
    pprint(items)
    db.close()


if __name__ == '__main__':
    sql_pra()
