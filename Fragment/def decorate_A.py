def decorate_A(function):
    def wrap_function(*args, **kwargs):
        kwargs['str'] = 'Hello!'
        return function(*args, **kwargs)
    return wrap_function


@decorate_A
def print_message_A(*args, **kwargs):
    print(kwargs['str'])

print_message_A()
