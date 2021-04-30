import re

INPUT_FILE = './src/input.txt'

class Passport():
    
    # If any new or different fields are needed, they only need to be changed here
    REQUIRED_FIELDS = {'byr': (lambda x: 1920 <= int(re.match('^\d{4}$', x).string) <= 2002),
                       'iyr': (lambda x: 2010 <= int(re.match('^\d{4}$', x).string) <= 2020),
                       'eyr': (lambda x: 2020 <= int(re.match('^\d{4}$', x).string) <= 2030),
                       'hgt': (lambda x: Passport.__validate_hgt(x)),
                       'hcl': (lambda x: re.match('^#(\d|[a-f]){6}$', x) != None),
                       'ecl': (lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
                       'pid': (lambda x: re.match('^\d{9}$', x) != None)}
                       
    OPTIONAL_FIELDS = {'cid': (lambda x: True)}
    
   
    def __init__(self, **kwargs): 
        self._req_fields = dict.fromkeys(self.REQUIRED_FIELDS, None)
        self._optional_fields = dict.fromkeys(self.OPTIONAL_FIELDS, None)
        for name, value in kwargs.items():
            if name in (self.REQUIRED_FIELDS | self.OPTIONAL_FIELDS):
                setattr(self, name, value)
            else:
                raise TypeError("__init__() got an unexpected keyword argument '{0}'".format(name))
            
            
    def __setattr__(self, key, value):
        if key in self.REQUIRED_FIELDS:
            self.__dict__['_req_fields'][key] = value
        elif key in self.OPTIONAL_FIELDS:
            self.__dict__['_optional_fields'][key] = value
        else:
            # Normal class instance behaviour is to allow new attribute assignment
            self.__dict__[key] = value
    
    
    def __getattr__(self, key):
        if key in self.REQUIRED_FIELDS.keys():
            return self._req_fields[key]
        elif key in self.OPTIONAL_FIELDS.keys():
            return self._optional_fields[key]
        else:
            return self.__dict__[key]

            
    def is_valid(self):
        # Checks if all values in the required fields are present
        return all(map(bool, self._req_fields.values()))
    
    
    def is_valid_advanced(self):
        # Validates each field according to individual rules
        try:
            return all(map(lambda kv: self.REQUIRED_FIELDS[kv[0]](kv[1]), self._req_fields.items()))
        except TypeError:
            return False
    
    
    @staticmethod
    def __validate_hgt(field):
        valid_ranges = {
            'cm': range(150, 193+1),
            'in': range(59, 76+1)
        }
        units, value = field[-2:], field[:-2]           
        if units in valid_ranges.keys():
            return int(value) in valid_ranges[units]
        else:
            return False
        
        
    @classmethod
    def from_string(cls, string):
        present_fields = {kv[0]:kv[1] for kv in map(lambda x: x.split(':'), string.split(' '))}
        return cls(**present_fields)


def read_file(file=INPUT_FILE):
    passports = []
    with open(INPUT_FILE, 'r') as fp:
        passport_data_str = ''
        for line in fp:
            if line != '\n':
                passport_data_str += line.replace('\n', ' ')
            else:
                passports.append(Passport.from_string(passport_data_str.strip()))
                passport_data_str = ''
        passports.append(Passport.from_string(passport_data_str.strip()))
    return passports


def part_one(passports):
    print(sum(map(lambda x: x.is_valid(), passports)))


def part_two(passports):
    print(sum(map(lambda x: x.is_valid_advanced(), passports)))


def main():
    passports = read_file()
    part_one(passports)
    part_two(passports)


if __name__ == '__main__':
    main()