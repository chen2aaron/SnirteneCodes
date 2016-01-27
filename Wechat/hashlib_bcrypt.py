import hashlib
import bcrypt
pwd = '$2a$12$fpmjsPGJOL6S8X97GlMXcOw/4hhDBxz2MWxhfdPx7ZhgyRWuMTGpO'
pay_pwd = 'eve17068'
print(hashlib.md5(pay_pwd.encode('utf-8')).hexdigest())
if len(pwd) == 32:
    has = hashlib.md5(pay_pwd)
    print(has)
    if pwd.lower() == hashlib.md5(pay_pwd.encode('utf-8')).hexdigest():
        new_pay_pwd = bcrypt.hashpw(pay_pwd.encode('utf-8'), bcrypt.gensalt())
        print('ok')
    else:
        print('pwd failed')
else:
    print('pwd != 32')
    hashed = bcrypt.hashpw(
        pay_pwd.encode('utf-8'), pwd.encode('utf-8')).decode('utf-8')
    print(hashed)
    if pwd != hashed:
        print('pwd failed 12222')
