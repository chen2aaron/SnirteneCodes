wx_temp_response = {
    'set_password': """{
            "touser": "{}".format(openid),
            "template_id": "Zu4weUNeJt3DMRv8dZzvScZz1QfDkIlejQWhPNCyoPI",
            "topcolor": "#FF0000",
            "data": {
                "Mobile": {
                    "value": "{}".format(mobile),
                    "color": "#173177",
                },
                "CreateTime": {
                    "value": "{}".format(time.strftime("%Y-%m-%d  %H:%M:%S")),
                    "color": "#173177",
                },
            }
        }""",
    'set_pwd': {
            "touser": "ojRiMuFScoR8NpOhgUVYu4RaDkuU",
            "template_id": "84e0AedZVnrtQyhH7vlh1z61Vc26xf0RtHbMRRu46Ys",
            "topcolor": "#FF0000",
            "data": {
                "first": {
                    "value": "恭喜您，您已成功重置账户支付密码"
                },
                "keyword1": {
                    "value": "支付密码"
                },
                "keyword2": {
                    "value": "设置成功"
                },
                "remark": {
                    "value": "如有疑问,请致电XXXXXX联系我们"
        }
    }
    }}
# a = PropDict(wx_temp_response)
# print(a.set_password)
content = wx_temp_response
path = 'set_pwd/data/keyword1'
value = 'xixi'
def fill_dict_value(content, path, value):
    keys = path.split('/')
    for key in keys:
        content = content[key]
    return content
a = fill_dict_value(content, path)
print(a)