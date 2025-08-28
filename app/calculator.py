def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("b must not be 0")
    return a / b
