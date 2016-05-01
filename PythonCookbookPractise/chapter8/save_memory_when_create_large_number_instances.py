# 8.4. Saving Memory When Creating a Large Number of Instances

# __slots__ 更多的是用来作为一个内存优化工具。
# 假设你不使用slots直接存储一个Date实例，
# 在64位的Python上面要占用428字节，
# 而如果使用了slots，内存占用下降到156字节。
class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
