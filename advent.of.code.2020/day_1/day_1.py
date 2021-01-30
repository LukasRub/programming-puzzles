import numpy as np
from functools import reduce
from operator import mul

SUMS_TO = 2020

def find_tuple(arr, sums_to=SUMS_TO):
    return tuple(set(arr) & set(sums_to - arr))

def find_triple(arr, sums_to=SUMS_TO):
    for num in arr:
        _tuple = find_tuple(arr, sums_to - num)
        if len(_tuple) > 0:
            return (num, *_tuple)

def main():
    arr = np.loadtxt('advent.of.code.2020/day_1/input.txt', dtype=np.int_)
    part1_res = find_tuple(arr)
    part2_res = find_triple(arr)
    print('Tuple {0}; product {1}'.format(part1_res, reduce(mul, part1_res)))
    print('Triple {0}; product {1}'.format(part2_res, reduce(mul, part2_res)))

if __name__ == '__main__':
    main()