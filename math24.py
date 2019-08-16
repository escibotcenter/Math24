#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

math_algorithm = [
    "(%s %s %s) %s (%s %s %s)",
    "((%s %s %s) %s %s) %s %s"
]

math_execute = ["+", "-", "*", "/"]

class Math24(object):
    result = None
    attempts = 0
    def __init__(self, values, timeout=1, debug=False):
        timeout = time.time() + timeout
        values = [i for i in values if i != " "]
        while time.time() < timeout and self.result == None:
            self.attempts += 1
            try:
                value = list(values)
                execute = random.choice(math_algorithm) % (value.pop(value.index(random.choice(value))), random.choice(math_execute), value.pop(value.index(random.choice(value))), random.choice(math_execute), value.pop(value.index(random.choice(value))), random.choice(math_execute), value.pop(value.index(random.choice(value))))
                if eval(execute) == 24:
                    self.result = execute
            except (ZeroDivisionError, TypeError, SyntaxError, NameError, IndexError):
                pass

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, ", ".join("%s=%r" % (key, value) for key, value in self.__dict__.items()))

if __name__ == "__main__":
    while True:
        _input = input("Input: ")
        print("Solution: %s\n" % (Math24(list(_input) if " " in _input else None if not _input.isdigit() else int(_input))))
