#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

math_algorithm = [
    "(%s %s %s) %s (%s %s %s)",
    "((%s %s %s) %s %s) %s %s"
]

math_execute = ["+", "-", "*", "/"]

class ThinkValue(object):
    result = None

    def __init__(self, values, max_values=4, max_value=50, timeout=1):
        if max_values in [0, 1]:
            self.result = values
        elif len(str(values)) == max_values and all(i.isdigit() for i in list(str(values))):
            self.result = list(str(values))
        timeout = time.time() + 1
        while time.time() < timeout and self.result == None:
            v = list(str(values))
            if all(i.isdigit() for i in v):
                for i in range(len(v) - max_values):
                    v[random.randint(0, len(v) - 1)] = v[random.randint(0, len(v) - 1)] + v.pop(random.randint(0, len(v) - 1))
                if len(v) == max_values:
                    self.result = v
            else:
                break

class Math24(object):
    result = None

    def __init__(self, values, timeout=1, debug=False):
        if (len([str(i) for i in values if i != " "]) != 4 if isinstance(values, list) else True):
            print("Warning : values should be List, simple %s([4, 4, 4, 4])" % (self.__class__.__name__))
            dim_values = ThinkValue("".join([str(i) for i in values if i != " "]) if isinstance(values, list) else values, 4, 4)
            print("%s : returned %s" % (dim_values.__class__.__name__, dim_values.result))
            values = dim_values.result
        timeout = time.time() + timeout
        while time.time() < timeout and self.result == None:
            try:
                value = list(values)
                execute = random.choice(math_algorithm) % (value.pop(value.index(random.choice(value))), random.choice(math_execute), value.pop(value.index(random.choice(value))), random.choice(math_execute), value.pop(value.index(random.choice(value))), random.choice(math_execute), value.pop(value.index(random.choice(value))))
                if eval(execute) == 24:
                    self.result = execute
            except (ZeroDivisionError, TypeError, SyntaxError, NameError, IndexError):
                pass

    def __repr__(self):
        return str(self.result)

if __name__ == "__main__":
    while True:
        _input = input("Input: ")
        print("Solution: %s\n" % (Math24(list(_input) if " " in _input else None if not _input.isdigit() else int(_input)).result))
