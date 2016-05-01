# 8.7. Calling a Method on a Parent Class

# class A(object):
#     def spam(self):
#         print('A.spam')
#
#
# class B(A):
#     def spam(self):
#         print('B.spam')
#         super().spam()  # Call parent spam()

#
# class A:
#     def __init__(self):
#         self.x = 0
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.y = 1
#
# print(vars(A))
# class Base:
#     def __init__(self):
#         print('Base.__init__')
#
# class A(Base):
#     def __init__(self):
#         super().__init__()
#         print('A.__init__')
#
# class B(Base):
#     def __init__(self):
#         super().__init__()
#         print('B.__init__')
#
# class C(A,B):
#     def __init__(self):
#         super().__init__()  # Only one call to super() here
#         print('C.__init__')

class A:
    def spam(self):
        print('A.spam')
        super().spam()

class B:
    def spam(self):
        print('B.spam')


class C(A, B):
    pass
