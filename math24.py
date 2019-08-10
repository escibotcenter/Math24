#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

value_2_math_execute = [['+', '-'], ['-', '+'], ['+', '*'], ['*', '+'], ['+', '/'], ['/', '+'], ['-', '-'], ['-', '-'], ['-', '*'], ['*', '-'], ['-', '/'], ['/', '-'], ['*', '-'], ['-', '*'], ['*', '*'], ['*', '*'], ['*', '/'], ['/', '*'], ['/', '-'], ['-', '/'], ['/', '*'], ['*', '/'], ['/', '/'], ['/', '/']]
value_3_math_execute = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '-'], ['-', '+', '+'], ['+', '+', '*'], ['*', '+', '+'], ['+', '+', '/'], ['/', '+', '+'], ['+', '-', '+'], ['+', '-', '+'], ['+', '-', '-'], ['-', '-', '+'], ['+', '-', '*'], ['*', '-', '+'], ['+', '-', '/'], ['/', '-', '+'], ['+', '*', '+'], ['+', '*', '+'], ['+', '*', '-'], ['-', '*', '+'], ['+', '*', '*'], ['*', '*', '+'], ['+', '*', '/'], ['/', '*', '+'], ['+', '/', '+'], ['+', '/', '+'], ['+', '/', '-'], ['-', '/', '+'], ['+', '/', '*'], ['*', '/', '+'], ['+', '/', '/'], ['/', '/', '+'], ['-', '+', '-'], ['-', '+', '-'], ['-', '+', '-'], ['-', '+', '-'], ['-', '+', '*'], ['*', '+', '-'], ['-', '+', '/'], ['/', '+', '-'], ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '*'], ['*', '-', '-'], ['-', '-', '/'], ['/', '-', '-'], ['-', '*', '-'], ['-', '*', '-'], ['-', '*', '-'], ['-', '*', '-'], ['-', '*', '*'], ['*', '*', '-'], ['-', '*', '/'], ['/', '*', '-'], ['-', '/', '-'], ['-', '/', '-'], ['-', '/', '-'], ['-', '/', '-'], ['-', '/', '*'], ['*', '/', '-'], ['-', '/', '/'], ['/', '/', '-'], ['*', '+', '*'], ['*', '+', '*'], ['*', '+', '-'], ['-', '+', '*'], ['*', '+', '*'], ['*', '+', '*'], ['*', '+', '/'], ['/', '+', '*'], ['*', '-', '*'], ['*', '-', '*'], ['*', '-', '-'], ['-', '-', '*'], ['*', '-', '*'], ['*', '-', '*'], ['*', '-', '/'], ['/', '-', '*'], ['*', '*', '*'], ['*', '*', '*'], ['*', '*', '-'], ['-', '*', '*'], ['*', '*', '*'], ['*', '*', '*'], ['*', '*', '/'], ['/', '*', '*'], ['*', '/', '*'], ['*', '/', '*'], ['*', '/', '-'], ['-', '/', '*'], ['*', '/', '*'], ['*', '/', '*'], ['*', '/', '/'], ['/', '/', '*'], ['/', '+', '/'], ['/', '+', '/'], ['/', '+', '-'], ['-', '+', '/'], ['/', '+', '*'], ['*', '+', '/'], ['/', '+', '/'], ['/', '+', '/'], ['/', '-', '/'], ['/', '-', '/'], ['/', '-', '-'], ['-', '-', '/'], ['/', '-', '*'], ['*', '-', '/'], ['/', '-', '/'], ['/', '-', '/'], ['/', '*', '/'], ['/', '*', '/'], ['/', '*', '-'], ['-', '*', '/'], ['/', '*', '*'], ['*', '*', '/'], ['/', '*', '/'], ['/', '*', '/'], ['/', '/', '/'], ['/', '/', '/'], ['/', '/', '-'], ['-', '/', '/'], ['/', '/', '*'], ['*', '/', '/'], ['/', '/', '/'], ['/', '/', '/']]

value_2_math_algorithm = [
    "(%s %s %s) %s (%s %s %s)",
    "%s %s (%s %s %s) %s %s"
]
value_3_math_algorithm = [
    "(%s %s (%s %s %s)) %s %s",
    "((%s %s %s) %s %s) %s %s",
    "%s %s (%s %s %s %s %s)"
]

class Math24(object):
    def __init__(self, _input, timeout=5, debug=False, *option, **options):
        assert False if not isinstance(_input, list) else len(_input) == 4, 'Invaild argument, simple %s([4, 5, 6, 7])' % (self.__class__.__name__)
    
        def value_3(_value):
            math_algorithm = random.choice(value_3_math_execute)
            value = list(_value)
            try:
                execute = random.choice(value_3_math_algorithm) % (value.pop(value.index(random.choice(value))), math_algorithm[0], value.pop(value.index(random.choice(value))), math_algorithm[1], value.pop(value.index(random.choice(value))), math_algorithm[2], value.pop(value.index(random.choice(value))))
                result = eval(execute)
                if debug == True:
                    print(execute, result)
                if result == 24:
                    return execute
            except ZeroDivisionError:
                pass

        def value_2(_value):
            math_algorithm = random.choice(value_2_math_execute)
            for _cen in random.choice(value_2_math_execute):
                value = list(_value)
                try:
                    execute = random.choice(value_2_math_algorithm) % (value.pop(value.index(random.choice(value))), math_algorithm[0], value.pop(value.index(random.choice(value))), _cen, value.pop(value.index(random.choice(value))), math_algorithm[1], value.pop(value.index(random.choice(value))))
                    result = eval(execute)
                    if debug == True:
                        print(execute, result)
                    if result == 24:
                        return execute
                except ZeroDivisionError:
                    pass

        timeout = time.time() + timeout
        while getattr(self, 'result', None) == None:
            if time.time() > timeout:
                self.result = "Timeout"
            if getattr(self, 'result', None) == None:
                self.result = value_2(list(_input))
            if getattr(self, 'result', None) == None:
                self.result = value_3(list(_input))
    
    def __repr__(self):
        return str(self.result)

if __name__ == "__main__":
    while True:
        #print(Math24([int(i) for i in input("Input: ").split(" ")]))
        _input = [int(i) for i in input("Input: ").split(" ")]
        result = []
        timeout = time.time() + 1
        while True: 
            if time.time() > timeout:
                break
            res = Math24(_input).result
            if res != "Timeout":
                if res not in result:
                    result.append(res)
        print("\n".join(result), "\n%s" % (len(result)))
