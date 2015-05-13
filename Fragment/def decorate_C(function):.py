def decorate_C(function):
    def wrap_function(*args, **kwargs):
        str = 'Hello!'
        #args.insert(1, str)
        args = args + (str,)
        return function(*args, **kwargs)
    return wrap_function


class Printer:

    @decorate_C
    def print_message(self, str, *args, **kwargs):
        print(str)

p = Printer()
p.print_message()
