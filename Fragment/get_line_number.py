from inspect import currentframe, getframeinfo



def get_line_num():
    frameinfo = getframeinfo(currentframe())
    print(frameinfo.filename, frameinfo.lineno)
    print(get_line_num.__name__)




if __name__ == '__main__':
    get_line_num()
