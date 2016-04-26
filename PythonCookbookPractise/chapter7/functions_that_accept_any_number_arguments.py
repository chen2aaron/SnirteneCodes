# 7.1. Writing Functions That Accept Any Number of Arguments

import html


def make_element(name, value, **attrs):
    key_vals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(key_vals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))

    return element


if __name__ == '__main__':
    print(make_element('item', 'lababa', size='large', quantity=6))
    print(make_element('p', '好帅啊', data_name='ss', style='margin'))
