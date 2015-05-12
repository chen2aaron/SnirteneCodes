#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-10
# Blog: morningchen.com


class Account(object):

    def __init__(self, name_number):
        '''ID'''
        self.name_number = name_number
        self.balance = 0

    def deposit(self, amount):
        '''存款'''
        assert amount > 0
        self.balance += amount

    def withdraw(self, amount):
        '''取款'''
        assert amount > 0
        if amount <= self.balance:
            self.balance -= amount
        else:
            print "balance is not enough."


if __name__ == '__main__':
    balance = 0
    a = Account("cc")
    a.deposit(500)
    print a.__dict__
    print a.balance
    a.withdraw(400)
    print a.balance
