import sys
import os
sys.path.append(os.path.abspath('project.euler/problem_18'))

from problem_18 import read_triangle, rolling_max

def main():
    triangle = read_triangle('project.euler/problem_67/p067_triangle.txt')
    for i in range(len(triangle)-1):
        triangle[i+1] += rolling_max(triangle[i])
    print(triangle[-1][0])

if __name__ == '__main__':
    main()