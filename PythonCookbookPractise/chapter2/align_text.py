# 2.13. Aligning Text Strings


text = 'Hello World'
text.ljust(20, '=')
text.rjust(20, '*')
text.center(20, '-')

# format() 函数的一个好处是它不仅适用于字符串。它可以用来格式化任何值
format(text, '=>20s')
format(text, '*^20s')

'{:>10s} {:>10s}'.format('Hello', 'World')