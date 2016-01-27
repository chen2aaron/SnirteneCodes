# -*- coding: utf-8 -*-
import requests
from datetime import datetime


url = 'http://webapi.acfun.tv/record/actions/signin'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0',
    'Host': 'webapi.acfun.tv',
    'Origin': 'http://www.acfun.tv',
    'Referer': 'http://www.acfun.tv',
}

cookies = {'JSESSIONID': '139f105f99d3477ebb7baab3a15acb10',
           '_sid_': '139f105f99d3477ebb7baab3a15acb10',
           'Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7': '1451817552',
           'auth_key': '585801',
           'ac_username': '%E8%A5%BF%E8%A5%BF%E8%8F%8C',
           'auth_key_ac_sha1': '-1838459013',
           'auth_key_ac_sha1_': '7Gnn6E%20X8ifFc2DQeSARP4mq8y8%3D',
           'ac_userimg': 'http://cdn.aixifan.com/dotnet/artemis/u/cms/www/201512/20182726f6ipbdim.jpg',
           'bfd_g': '9facecf4bbcd46b400006a4000008579568baddd',
           'tma': '123279387.96033053.1452404754455.1452404754455.1452607661944.2',
           'tmd': '10.123279387.96033053.1452404754455.',
           'viewBeta': '1',
           '_gat': '1',
           '_gat_UA-68793632-3': '1',
           'online_status': '0',
           '_ga': 'GA1.2.1879604137.1449289043',
           'analytics': 'GA1.2.905244756.1452053189',
           'Hm_lvt_bc75b9260fe72ee13356c664daa5568c': '1450931223,1451811761,1451817545,1452404682',
           'Hm_lpvt_bc75b9260fe72ee13356c664daa5568c': '1452777057'
           }

params = {
    'channel': 0,
    'date': int(datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()*1000),
}

r = requests.post(url=url, data=params, headers=headers, cookies=cookies)

if r.json()['code']==200 and 'data' not in r.json():
    print('签到成功')

else:
    print('签到失败')
