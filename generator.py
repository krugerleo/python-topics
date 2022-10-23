from ctypes.wintypes import PINT


def infinite_five_sequence():
    result = 1
    while True:
        yield result
        result *=5

values = infinite_five_sequence()
print(next(values))
print(next(values))
print(next(values))
print(next(values))