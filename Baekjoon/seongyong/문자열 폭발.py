import sys
from collections import *


def read_line():
    return sys.stdin.readline().rstrip()


def split_n_map(split_target, seperator, to_map):
    return map(to_map, split_target.split(seperator))


def read_n_map(to_map, seperator):
    return split_n_map(read_line(), seperator, to_map)


def read_line_as(return_type, element_type, seperator):
    return return_type(read_n_map(element_type, seperator))


def read_lines(line_number, trim_each_line=None):
    if trim_each_line:
        return [trim_each_line(read_line()) for _ in range(line_number)]
    else:
        return [read_line() for _ in range(line_number)]


def read_lines_as(row_type, col_type, seperator, line_number):
    return [read_line_as(row_type, col_type, seperator)
            for _ in range(line_number)]


def add_iter(iter0, iter2, return_type):
    return return_type(sum(e) for e in zip(iter0, iter2))


def find_root(target, root_of: list):
    if root_of[target] == target:
        return target

    root_of[target] = find_root(root_of[target], root_of)
    return root_of[target]


def union(x, y, root_of: list):
    x, y = find_root(x, root_of), find_root(y, root_of)
    if x != y:
        # bigger, smaller = min(x, y), max(x, y)
        root_of[x] = y


dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def adjacencies_of(target: tuple):
    return (add_iter(d, target, tuple) for d in dirs)


def pos_in_field(pos: tuple, field: list):
    return 0 <= pos[0] < len(field) and 0 <= pos[1] < len(field[pos[0]])


# main logic
given = list(read_line())
bomb = list(read_line())
result = list()
for i in given:
    result.append(i)
    if result[-1] == bomb[-1] and len(result) >= len(bomb):
        need_to_bomb = True
        for j in range(-1, -len(bomb) - 1, -1):
            if result[j] != bomb[j]:
                need_to_bomb = False
                break
        if need_to_bomb:
            for j in range(len(bomb)):
                result.pop()

if not result:
    result = list('FRULA')

print(''.join(result))
