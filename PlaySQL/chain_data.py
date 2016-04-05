from decimal import Decimal
from pprint import pprint

def find(lst, key, value):
    for index, d in enumerate(lst):
        if d[key] == value:
            return index
    return -1

def chain_data(raw_data, **kwargs):
    if not kwargs or not kwargs['borrowing_id']:
        return raw_data

    index = find(raw_data, 'borrowing_id', kwargs['borrowing_id'])
    if index >= 0:
        kwargs.pop('borrowing_id')
        raw_data[index].update(kwargs)
    else:
        raw_data.append(kwargs)
    return raw_data


if __name__ == '__main__':
    l = [{'agency_fee': Decimal('12.00'),
          'borrowing_id': '486',
          'gps_use_fee': Decimal('20.00'),
          'other_fee': Decimal('20.00'),
          'valuation_fee': Decimal('10.00')},
         {'agency_fee': Decimal('12.00'),
          'borrowing_id': '488',
          'gps_use_fee': Decimal('20.00'),
          'other_fee': Decimal('30.00'),
          'valuation_fee': Decimal('10.00')},
         {'borrowing_id': '490',
          'gps_use_fee': Decimal('10.00'),
          'other_fee': Decimal('20.00'),
          'valuation_fee': Decimal('20.00')},
         {'agency_fee': Decimal('12.00'),
          'borrowing_id': '491',
          'gps_use_fee': Decimal('10.00'),
          'other_fee': Decimal('6.00'),
          'refund_deposit': Decimal('-6.00'),
          'valuation_fee': Decimal('20.00')}, ]
    c = {'borrowing_id': '491',
         'hahahah': 'asdasdasdas'}
    chain_data(l, borrowing_id='491', jasd=123)
    chain_data(l, borrowing_id='491', jaz=123123)
    pprint(l)
