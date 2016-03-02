from datetime import datetime
import json
from Utils.utils import PropDict

a = {'created_at': datetime.now(),
     'msg': 3123,
     'status': 3,
     'trade_no': 8489204}

def notify(args):
    print(type(args))
    print(type(args.msg))
    print(args.msg)

notify(PropDict(PropDict(a)))