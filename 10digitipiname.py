import sys


def check_ipi_digit(all_digits):
    digits = all_digits.rjust(11, '0')[:-2]
    sum = 0
    for i, digit in enumerate(digits):
        sum += int(digit) * (10 - i)
    sum = sum % 101
    if sum != 0:
        sum = (101 - sum) % 100
    if '{:02d}'.format(sum) != all_digits[-2:]:
        return False
    return True


def report_on(num):
    if len(num) > 9:
        raise Exception('Works only with up to 9 digits.')
    all_digits = num.rjust(9, '0')
    if check_ipi_digit(all_digits):
        yield '{} is a valid IPI Name #.'.format(all_digits.rjust(11, '0'))
    else:
        for d in range(1, 10):
            candidate = str(d) + all_digits
            if check_ipi_digit(candidate):
                yield '{} is a valid 10-digit IPI Name # ending in {}.'.format(
                    candidate, all_digits)
                break
        else:
            yield 'No valid 10-digit IPI Name numbers ending in {}.'.format(
                all_digits)


for arg in sys.argv[1:]:
    for line in report_on(arg):
        print(line)
