def framework(logic, callback):
    s = logic()
    print("[FX] logic: ", s)
    print("[FX] do something...")
    callback("async:" + s)

def logic():
    s = 'mylogic'
    return s

def callback(s):
    print(s)

framework(logic, callback)
