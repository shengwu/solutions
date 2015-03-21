from fractions import Fraction

digits = range(1, 10)

def are_equal(anum, adenom, bnum, bdenom):
    if adenom == 0 or bdenom == 0:
        return False
    return Fraction(anum, adenom) == Fraction(bnum, bdenom)

# Only looking for fractions < 1
result_num = 1
result_denom = 1
for denom in digits:
    for num in xrange(1, denom):
        for digit in digits:
            # For each digit, try having the cancellable digits in the four
            # possible combinations of locations
            front_num = int(str(digit) + str(num))
            front_denom = int(str(digit) + str(denom))
            back_num = int(str(num) + str(digit))
            back_denom = int(str(denom) + str(digit))

            if are_equal(num, denom, front_num, front_denom):
                result_num *= front_num
                result_denom *= front_denom
                print num, denom, front_num, front_denom
            if are_equal(num, denom, front_num, back_denom):
                result_num *= front_num
                result_denom *= back_denom
                print num, denom, front_num, back_denom
            if are_equal(num, denom, back_num, front_denom):
                result_num *= back_num
                result_denom *= front_denom
                print num, denom, back_num, front_denom
            if are_equal(num, denom, back_num, back_denom):
                result_num *= back_num
                result_denom *= back_denom
                print num, denom, back_num, back_denom

print Fraction(result_num, result_denom).denominator
