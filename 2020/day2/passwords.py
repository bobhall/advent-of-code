import re

def main():
    fd = open('passwords.txt', 'r')
    passwords = fd.readlines()

    passwords = [password.strip() for password in passwords]

    count = 0
    for password in passwords:

        minimum, maximum, letter, phrase = parse_password(password)
        if legal_password2(minimum, maximum, letter, phrase):
            count += 1

    print(f"Out of {len(passwords)} passwords, {count} are legal")

def parse_password(password):
    mm = re.match(r'(?P<min>\w+)-(?P<max>\w+) (?P<letter>\w+): (?P<phrase>\w+)', password)
    return int(mm.group('min')), int(mm.group('max')), mm.group('letter'), mm.group('phrase')

def legal_password2(index1, index2, letter, phrase):
    index1_match = phrase[index1-1] == letter
    index2_match = phrase[index2-1] == letter
    return bool(index1_match) ^ bool(index2_match)

def legal_password(minimum, maximum, letter, phrase):
    table = {}
    for char in phrase:
        if table.get(char):
            table[char] += 1
        else:
            table[char] = 1
    return table.get(letter, 0) >= minimum and table.get(letter, 0) <= maximum


if __name__ == '__main__':
    main()