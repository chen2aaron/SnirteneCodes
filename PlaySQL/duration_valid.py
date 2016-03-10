
def coupon_duration_valid(duration, limits):
    return not limits.get('duration') or duration in limits.get('duration', '')


def coupon_duration_invalid(duration, limits):
    return limits.get('duration') and duration not in limits.get('duration', '')


def main(duration, limits):
    print(coupon_duration_valid(duration, limits))
    print(coupon_duration_invalid(duration, limits))


if __name__ == '__main__':
    duration = '1m'
    limits1 = {"bonus_interest_limit": 1, "duration": ["1m", "2m", "3m", "6m"]}
    limits2 = {"bonus_interest_limit": 1, "duration": []}
    limits3 = {}
    limits4 = None
    limits5 = {"duration": ["1m"]}
    limits6 = {"duration": ["xd"]}
    limits7 = {"bonus_interest_limit": 1}

    main(duration, limits7)
