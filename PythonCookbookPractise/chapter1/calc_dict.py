# 1.8. Calculating with Dictionaries


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 字典反转为元组， 注意：zip() 函数创建的是一个只能访问一次的迭代器
prices_and_names = zip(prices.values(), prices.keys())
min_price = min(prices_and_names) # ok
# max_price = max(prices_and_names) # wrong


min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)