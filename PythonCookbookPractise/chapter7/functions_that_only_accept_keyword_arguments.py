# 7.2. Writing Functions That Only Accept Keyword Arguments

def recv(maxsize, *, block):
    'Receives a message'
    pass


recv(1024, True)  # TypeError
recv(1024, block=True)  # Ok
