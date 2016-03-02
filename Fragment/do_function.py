def setup_1():
    print('1')

def setup_2():
    print('2')

def setup_3():
    print('3')

if __name__ == '__main__':
    for func in (val for key,val in vars().items()
         if key.startswith('setup_')):
        func()