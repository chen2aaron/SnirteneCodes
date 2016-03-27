# 2.8. Writing a Regular Expression for Multiline Patterns
import re


# comment = re.compile(r'/\*(.*?)\*/')
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline comment */
'''
print(comment.findall(text1))
print(comment.findall(text2))
