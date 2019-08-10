import random
import time

value_2_math_algorithm = [['+', '-'], ['-', '+'], ['+', '*'], ['*', '+'], ['+', '/'], ['/', '+'], ['-', '-'], ['-', '-'], ['-', '*'], ['*', '-'], ['-', '/'], ['/', '-'], ['*', '-'], ['-', '*'], ['*', '*'], ['*', '*'], ['*', '/'], ['/', '*'], ['/', '-'], ['-', '/'], ['/', '*'], ['*', '/'], ['/', '/'], ['/', '/']]
value_3_math_algorithm = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '-'], ['-', '+', '+'], ['+', '+', '*'], ['*', '+', '+'], ['+', '+', '/'], ['/', '+', '+'], ['+', '-', '+'], ['+', '-', '+'], ['+', '-', '-'], ['-', '-', '+'], ['+', '-', '*'], ['*', '-', '+'], ['+', '-', '/'], ['/', '-', '+'], ['+', '*', '+'], ['+', '*', '+'], ['+', '*', '-'], ['-', '*', '+'], ['+', '*', '*'], ['*', '*', '+'], ['+', '*', '/'], ['/', '*', '+'], ['+', '/', '+'], ['+', '/', '+'], ['+', '/', '-'], ['-', '/', '+'], ['+', '/', '*'], ['*', '/', '+'], ['+', '/', '/'], ['/', '/', '+'], ['-', '+', '-'], ['-', '+', '-'], ['-', '+', '-'], ['-', '+', '-'], ['-', '+', '*'], ['*', '+', '-'], ['-', '+', '/'], ['/', '+', '-'], ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '*'], ['*', '-', '-'], ['-', '-', '/'], ['/', '-', '-'], ['-', '*', '-'], ['-', '*', '-'], ['-', '*', '-'], ['-', '*', '-'], ['-', '*', '*'], ['*', '*', '-'], ['-', '*', '/'], ['/', '*', '-'], ['-', '/', '-'], ['-', '/', '-'], ['-', '/', '-'], ['-', '/', '-'], ['-', '/', '*'], ['*', '/', '-'], ['-', '/', '/'], ['/', '/', '-'], ['*', '+', '*'], ['*', '+', '*'], ['*', '+', '-'], ['-', '+', '*'], ['*', '+', '*'], ['*', '+', '*'], ['*', '+', '/'], ['/', '+', '*'], ['*', '-', '*'], ['*', '-', '*'], ['*', '-', '-'], ['-', '-', '*'], ['*', '-', '*'], ['*', '-', '*'], ['*', '-', '/'], ['/', '-', '*'], ['*', '*', '*'], ['*', '*', '*'], ['*', '*', '-'], ['-', '*', '*'], ['*', '*', '*'], ['*', '*', '*'], ['*', '*', '/'], ['/', '*', '*'], ['*', '/', '*'], ['*', '/', '*'], ['*', '/', '-'], ['-', '/', '*'], ['*', '/', '*'], ['*', '/', '*'], ['*', '/', '/'], ['/', '/', '*'], ['/', '+', '/'], ['/', '+', '/'], ['/', '+', '-'], ['-', '+', '/'], ['/', '+', '*'], ['*', '+', '/'], ['/', '+', '/'], ['/', '+', '/'], ['/', '-', '/'], ['/', '-', '/'], ['/', '-', '-'], ['-', '-', '/'], ['/', '-', '*'], ['*', '-', '/'], ['/', '-', '/'], ['/', '-', '/'], ['/', '*', '/'], ['/', '*', '/'], ['/', '*', '-'], ['-', '*', '/'], ['/', '*', '*'], ['*', '*', '/'], ['/', '*', '/'], ['/', '*', '/'], ['/', '/', '/'], ['/', '/', '/'], ['/', '/', '-'], ['-', '/', '/'], ['/', '/', '*'], ['*', '/', '/'], ['/', '/', '/'], ['/', '/', '/']]

class Math24(object):
    def __init__(self, _input, timeout=5, debug=False, *option, **options):
        assert len(_input) == 4 if isinstance(_input, list) else False, 'Invaild argument, simple %s([4, 5, 6, 7])' % (self.__class__.__name__)
    
        def value_3(_value):
            math_algorithm = random.choice(value_3_math_algorithm)
            value = list(_value)
            try:
                execute = "((%s %s %s) %s %s) %s %s" % (value.pop(value.index(random.choice(value))), math_algorithm[0], value.pop(value.index(random.choice(value))), math_algorithm[1], value.pop(value.index(random.choice(value))), math_algorithm[2], value.pop(value.index(random.choice(value))))
                result = eval(execute)
                if debug == True:
                    print(result, execute)
                if result == 24:
                    return execute
            except ZeroDivisionError:
                pass

        def value_2(_value):
            math_algorithm = random.choice(value_2_math_algorithm)
            for _cen in random.choice(math_algorithm):
                value = list(_value)
                try:
                    execute = "(%s %s %s) %s (%s %s %s)" % (value.pop(value.index(random.choice(value))), math_algorithm[0], value.pop(value.index(random.choice(value))), _cen, value.pop(value.index(random.choice(value))), math_algorithm[1], value.pop(value.index(random.choice(value))))
                    result = eval(execute)
                    if debug == True:
                        print(result, execute)
                    if result == 24:
                        return execute
                except ZeroDivisionError:
                    pass

        timeout = time.time() + timeout
        while getattr(self, 'result', None) == None:
            if time.time() > timeout:
                self.result = "Timeout"
            if getattr(self, 'result', None) == None:
                self.result = value_3(list(_input))
            if getattr(self, 'result', None) == None:
                self.result = value_2(list(_input))
    
    def __repr__(self):
        return str(self.result)

if __name__ == "__main__":
    while True:
        print(Math24([int(i) for i in input("Input: ").split(" ")]))