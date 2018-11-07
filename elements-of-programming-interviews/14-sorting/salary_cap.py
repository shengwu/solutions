salaries = [90, 30, 100, 40, 20]
target = 210

def apply_cap(salaries, cap):
    result = 0
    for salary in salaries:
        result += min(salary, cap)
    return result

assert apply_cap(salaries, 60) == target

# idea: what if we sorted the salaries?
# once we reach 20, 30, 40
# acc = 90
# remainder = 210 - 90 = 120
# implies that each of the two remaining salaries need to be capped at 60
# but they both must be greater than or equal to 60
# we can do this by checking the next element
# overall algorithm is O(n log n)

def find_cap(salaries, target):
    sorted_salaries = sorted(salaries)
    salary_count = len(salaries)
    sums = []
    acc = 0
    for salary in sorted_salaries:
        acc += salary
        sums.append(acc)
    for i, salary in enumerate(sorted_salaries):
        remainder = target - sums[i]
        avg_of_remaining = remainder / (salary_count - i - 1)
        if i < salary_count - 1:
            next_salary = sorted_salaries[i+1]
            if next_salary >= avg_of_remaining:
                return avg_of_remaining
        else:
            return salary


assert find_cap(salaries, target) == 60
assert find_cap([10, 10, 100, 100], 60) == 20
assert find_cap([10, 20, 30, 40], 100) == 40
assert find_cap([10, 20, 30, 40], 40) == 10

# doesn't handle the case where the cap needs to be lower than everyone's salary
