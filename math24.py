#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import asyncio

def switch_list(_list):
    algorithm = ""
    keys_list = {}
    result = []
    for key_number in range(len(_list)):
        keys_list[key_number] = f"_{key_number}"
    for _, i in enumerate(keys_list):
        algorithm += " " * (4 * _) + f"for {keys_list[i]} in _list:\n"
    algorithm += " " * (4 * len(keys_list)) + "result.append([%s])" % (", ".join([value for key, value in keys_list.items()]))
    exec(algorithm)
    return result

def switch_positon(_list):
    result = [_list]
    source_list = {}
    for i in _list:
        if i not in source_list:
            source_list[i] = 0
        source_list[i] += 1
    for x in switch_list(_list):
        recv_list = {}
        for i in x:
            if i not in recv_list:
                recv_list[i] = 0
            recv_list[i] += 1
        if all([recv_list[y] == source_list[y] for y in recv_list]):
            if x not in result:
                result.append(x)
    return result

def make_bracket(numbers_length):
    result = ""
    for i in range(int(numbers_length / 2)):
        if i == 0:
            result += "(%d %s %d)"
        elif i > 0:
            result += " %s %d)"
    for i in range(numbers_length - len([i for i in result.split(" ") if "%d" in i])):
        result += " %s %d"
    result = result[::-1]
    for i in range(len([i for i in result.split(" ") if ")" in i]) - len([i for i in result.split(" ") if "(" in i])):
        result += "("
    return result[::-1]

def join_list(_list, _list_2):
    a = 0
    result = []
    for i in range(len(_list)):
        result.append(_list[i])
        if len(result) % 2 == 1:
            if a < len(_list_2):
                result.append(_list_2[a])
            a += 1
    return result

class Math24(object):
    attempts = 0
    time_usage = 0

    def __init__(self, values):
        assert isinstance(values, list), 'values must be list'
        if len(values) <= 1:
            self.result = None
        start_time = time.time()
        bracket = make_bracket(len(values))
        if not hasattr(self, 'result'):
            for b in switch_positon(values):
                for a in switch_list(['+', '-', '*', '/']):
                    self.attempts += 1
                    while len(a) < len(b) - 1:
                        a.append(a[len(a) - 1])
                    algorithm = bracket % (tuple(join_list(b, a[:len(b) - 1])))
                    try:
                        if eval(algorithm) == 24:
                            self.result = algorithm
                            self.time_usage = time.time() - start_time
                            break
                    except ZeroDivisionError:
                        continue

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, ", ".join("%s=%r" % (key, value) for key, value in self.__dict__.items()))

async def Math24WithAsync(values):
    assert isinstance(values, list), 'values must be list'
    if len(values) <= 1:
        return None
    bracket = make_bracket(len(values))
    for b in switch_positon(values):
        for a in switch_list(['+', '-', '*', '/']):
            while len(a) < len(b) - 1:
                a.append(a[len(a) - 1])
            algorithm = bracket % (tuple(join_list(b, a[:len(b) - 1])))
            try:
                if eval(algorithm) == 24:
                    return algorithm
                    break
            except ZeroDivisionError:
                continue
    return None

if __name__ == "__main__":
    while True:
        _input = input("Input: ")
        start_time = time.time()
        solution = asyncio.get_event_loop().run_until_complete(Math24WithAsync([int(x) for x in _input.split(" ")]))
        #solution = Math24([int(x) for x in _input.split(" ")])
        print("Solution: %s" % (solution), 'took', time.time() - start_time, end="\n\n")
