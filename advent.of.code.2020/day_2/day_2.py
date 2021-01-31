from collections import Counter
from abc import ABC, abstractclassmethod, abstractmethod
from operator import xor


PATH_TO_INPUT = 'advent.of.code.2020/day_2/input.txt'


class Policy(ABC):
    @abstractmethod
    def __init__(self, symb, restriction):
        self.symb = symb
        self.restriction = restriction

    @abstractclassmethod
    def from_string(cls, string):
        pass

    @abstractmethod
    def is_valid_psw(string):
        pass


class RangePolicy(Policy):

    def __init__(self, symb, range):
        self.symb = symb
        self.range = range

    @classmethod
    def from_string(cls, string, inclusive=True):
        restr_str, symb = string.split(' ')
        boundaries = [int(x) for x in restr_str.split('-')]
        if inclusive:
            boundaries[1] += 1
        return cls(symb, range(*boundaries))

    def is_valid_psw(self, password):
        return Counter(password)[self.symb] in self.range

    @classmethod
    def __repr__(cls):
        return 'RangePolicy(symb=str, range=range(int, int))'


class PositionPolicy(Policy):

    def __init__(self, symb, positions):
        self.symb = symb
        self.positions = positions
    
    @classmethod
    def from_string(cls, string, inclusive=True):
        restr_str, symb = string.split(' ')
        positions = [int(x) for x in restr_str.split('-')]
        return cls(symb, positions)

    def is_valid_psw(self, password):
        return xor(*(password[i-1] == self.symb for i in self.positions if i <= len(password)))

    @classmethod
    def __repr__(cls):
        return 'PositionPolicy(symb=str, positions=[int, int])'


def read_file(file=PATH_TO_INPUT):
    policies = []
    passwords = []
    with open(file, 'r') as fp:
        for line in fp.readlines():
            policy_str, password = line.rstrip().split(': ')
            policies.append(policy_str)
            passwords.append(password)
    return policies, passwords


def apply_policy(policies, passwords, policy_cls):
    valid_pswds = 0
    for pol_str, psw in zip(policies, passwords):
        if policy_cls.from_string(pol_str).is_valid_psw(psw):
            valid_pswds += 1
    print('Policy: {0}'.format(policy_cls.__repr__()))
    print('Total passwords: {0}, of them valid: {1}'.format(len(passwords), valid_pswds))


def main():
    policies_str, passwords = read_file()
    for policy_cls in (RangePolicy, PositionPolicy):
        apply_policy(policies_str, passwords, policy_cls=policy_cls)
    

if __name__ == '__main__':
    main()