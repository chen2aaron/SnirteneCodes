import bz2
import fnmatch
import gzip
import os
import re
from pprint import pprint

# 4.13. Creating Data Processing Pipelines


def gen_find(file_pat, top):
    """
    找到所有匹配 shell通配符的文件名
    :param file_pat: shell 通配符
    :param top: file tree 的顶层目录名
    :return: generator
    """
    for path, dir_list, file_list in os.walk(top):
        for name in fnmatch.filter(file_list, file_pat):
            yield os.path.join(path, name)


def gen_opener(file_names):
    """
    在产生一个文件对象同时打开一个文件名的序列
    到下一次迭代时，文件被立即关闭
    :param file_names: 文件名列表
    :return: generator
    """
    for filename in file_names:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt', encoding='utf-8')
        yield f
        f.close()


def gen_concatenate(iterators):
    """
    把迭代器的序列连接成一个单独的序列
    :param iterators: 迭代器
    :return: generator
    """
    for i in iterators:
        yield from i


def gen_grep(pattern, lines):
    """
    寻找一行的正则匹配
    :param pattern: 匹配样式
    :param lines: lines
    :return: generator
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


if __name__ == '__main__':
    # 管道工作流
    # yield 作为生产者
    # for循环 作为消费者
    iter_names = (gen_find('*iter*', '../../PythonCookbookPractise'))
    files = gen_opener(iter_names)
    lines = gen_concatenate(files)
    py_lines = gen_grep('(\s+)yield', lines)
    byte_column = (line.rsplit(None, 1)[1] for line in py_lines)
    pprint(list(byte_column))
