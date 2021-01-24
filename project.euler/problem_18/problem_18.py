import numpy as np


def read_triangle(filename):
    triangle = list()
    with open(filename, 'r') as fp:
        for line in fp.readlines():
            triangle.append(np.fromstring(line, dtype=np.int_, sep=' '))
    return triangle[::-1]


def rolling_max(array, window_size=2):
    rolling_max = list()
    for i in range(len(array)-1):
        rolling_max.append(max(array[i:i+window_size]))
    return np.array(rolling_max)


def main():
    triangle = read_triangle('project.euler/problem_18/p018.txt')
    for i in range(len(triangle)-1):
        triangle[i+1] += rolling_max(triangle[i])
    print(triangle[-1][0])


if __name__ == '__main__':
    main()