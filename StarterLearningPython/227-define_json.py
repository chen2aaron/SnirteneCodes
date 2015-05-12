#!/usr/bin/env python
# -*- coding:utf-8 -*-


import json


class Person(object):

    """docstring for Person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Person Object name: %s, age: %d" % (self.name, self.age)


def object2dict(obj):
    '''pass'''
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d


def dict2object(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items())
        inst = class_(**args)
    else:
        inst = d
    return inst

if __name__ == '__main__':
    p = Person('Snitene', 24)
    print p
    d = object2dict(p)
    print d
    o = dict2object(d)
    print "-"*50
    print type(o), o
    print "-"*50
    dump = json.dumps(p, default=object2dict)
    print dump
    load = json.loads(dump, object_hook=dict2object)
    print load
