from src.passport_processing import Passport
import pytest


@pytest.fixture(scope='module', params=['init_directly', 'init_from_string'])
def passport_valid(request):
    if request.param == 'init_directly':
        return Passport(ecl='gry', pid='860033327', eyr='2020', hcl='#fffffd', 
                        byr='1937', iyr='2017', cid='147', hgt='183cm')
    elif request.param == 'init_from_string':
        return Passport.from_string('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm')


@pytest.mark.parametrize('field', ('ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'))
def test_passport_field_not_in_instance_dict(passport_valid, field):
    assert field not in passport_valid.__dict__.keys()


@pytest.mark.parametrize('field', ('ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'))
def test_passport_field_not_in_instance_dir(passport_valid, field):
    assert field not in dir(passport_valid)


@pytest.mark.parametrize('field', ('ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'))
def test_passport_field_in_defined_inner_dict(passport_valid, field):
    assert field in (passport_valid._req_fields.keys() | passport_valid._optional_fields.keys())


@pytest.mark.parametrize("string, expected", [
    ('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm', True),
    ('iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929', False),
    ('hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm', True),
    ('hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in', False)
])
def test_passport_validation(string, expected):
    passport = Passport.from_string(string)
    assert passport.is_valid() == expected