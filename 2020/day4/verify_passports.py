import re

def convert_passport(text):
    return dict([element.split(':') for element in text.strip().split()])

def verify_passport1(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if field not in passport.keys():
            return False
    return True

def item_in_range(item, low, high):
    return int(item) in range(low, high+1)

def verify_passport2(passport):

    if not item_in_range(passport['byr'],1920,2002) or not item_in_range(passport['iyr'],2010,2020) or not item_in_range(passport['eyr'], 2020, 2030):
        return False

    if passport['hgt'] not in [str(num)+"cm" for num in range(150, 194)] + [str(num)+"in" for num in range(59, 77)]:
        return False

    if not re.match(r'^#[0-9a-z]{6,6}$', passport['hcl']):
        return False

    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if len(passport['pid']) != 9 or not passport['pid'].isdecimal():
        return False

    return True
    
def read_passports():
    passports = []
    tmp_passport = ""
    for line in open('full_input.txt', 'r'):
        if line == '\n':
            passports.append(tmp_passport)
            tmp_passport = ""
        else:
            tmp_passport += line + " "
    passports.append(tmp_passport)
    return passports
    
def main():
    passports = read_passports()
    passports = [convert_passport(passport) for passport in passports]

    count = 0
    for passport in passports:
        if verify_passport1(passport) and verify_passport2(passport):
            count += 1
            
    print(f"There are {count} valid passports out of {len(passports)}")


if __name__ == '__main__':
    main()
