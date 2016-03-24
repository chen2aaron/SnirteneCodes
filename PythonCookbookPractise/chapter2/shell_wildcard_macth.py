# 2.3. Matching Strings Using Shell Wildcard Patterns
from fnmatch import fnmatch, fnmatchcase


names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
# 底层操作系统的大小写敏感规则
print([name for name in names if fnmatch(name, 'Dat*.csv')])
# 自定义的大小写敏感规则
print([name for name in names if fnmatchcase(name, 'Dat*.csv')])
