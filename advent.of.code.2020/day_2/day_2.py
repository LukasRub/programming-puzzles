from collections import Counter

class Policy:

    def __init__(self, symb, range):
        self.symb = symb
        self.range = range
    
    @classmethod
    def from_string(cls, string):
        range_str, symb = string.split(' ')
        return cls(symb, range(*(int(x) for x in range_str.split('-'))))

    def is_valid_psw(self, password):
        return Counter(password)[self.symb] in self.range


def main():
    print(Policy.from_string('1-3 b').is_valid_psw('cdefg'))



if __name__ == '__main__':
    main()