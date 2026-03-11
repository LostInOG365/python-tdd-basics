def addition(a, b):
    return a + b

def division(a, b):
    if b == 0:
        raise ValueError("Division durch Null nicht erlaubt")
    return a / b