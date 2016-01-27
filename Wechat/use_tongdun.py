tongdun = Tongdun()
data = {
    'ip_address': '180.116.49.54',
    'user_agent_cust': '',
    'refer_cust': '',
    'token_id': '',
    'black_box': '',
    'account_login': '',
    'account_name': '阿里狼',
    'id_number': '310108198810200019',
    'account_email': '',
    'account_phone': '',
    'account_mobile': '13333332222',
    'qq_number': '',
    'organization': '',
    'account_address': '',
    'loan_purpose': '',
    'pay_amount': '20000',
    'pay_currency': '人民币',
    'card_number': '6222801216881010620',
    'cc_bin': '',
    'card_name': '',
    'card_city': '上海',
    'contacts_phone': '',
    'contacts_id_number': '',
    'contacts_address': '',
    'state': '0',
    }
resp = tongdun(**data)
if tongdun.is_ok(resp):
    print('xixihahahuhuheihei')
