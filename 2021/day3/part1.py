#fd = open('small-input.txt')
fd = open('input.txt')
lines = [line[::-1].strip() for line in fd.readlines()]

numeral_length = len(lines[0])

gamma_rate = 0
epsilon_rate = 0

for ix in range(numeral_length):
    digits = [int(line[ix]) for line in lines]

    ones_win = False
    if sum(digits) > (len(lines)/2):
        ones_win = True

    if ones_win:
        gamma_rate += 1 * pow(2, ix)
    else:
        epsilon_rate += 1 * pow(2, ix)

    print(f"sample digis: {digits[0:10]} ==> {ones_win}: {sum(digits)}/{len(lines)}")

print(f"gamma rate: {gamma_rate}")
print(f"epsilon rate: {epsilon_rate}")
print(f"product: {gamma_rate*epsilon_rate}")