# Find a duplicate, Space Edition™.
# We have a list of integers, where:

# The integers are in the range 1..n1..n
# The list has a length of n+1n+1
# It follows that our list has at least one integer which appears at least twice.
# But it may have several duplicates, and each duplicate may appear more than twice.

# Write a function which finds an integer that appears more than once in our list.
# (If there are multiple duplicates, you only need to find one of them.)

# We're going to run this function on our new, super-hip Macbook Pro With Retina Display™.
# Thing is, the damn thing came with the RAM soldered right to the motherboard, so we can't
# upgrade our RAM. So we need to optimize for space!

#My own brute force solution
def find_duplicate(numbers):
    numbers = numbers.sort()
    for idx, num in enumerate(numbers):
        if num == numbers[idx+1]:
            return num

#Interview Cake solutions for study purposes
#Classic solution - O(n) time and ... O(n)O(n) space
def find_repeat(numbers):
    numbers_seen = set()
    for number in numbers:
        if number in numbers_seen:
            return number
        else:
            numbers_seen.add(number)

    # whoops--no duplicate
    raise Exception('no duplicate!')

#A O(1) space and O(n^2) time solution
def find_repeat_brute_force(numbers):
    for needle in range(1, len(numbers)):
        has_been_seen = False
        for number in numbers:
            if number == needle:
                if has_been_seen:
                    return number
                else:
                    has_been_seen = True

    # whoops--no duplicate
    raise Exception('no duplicate!')

#Binary search solution, O(1) space and O(n log n) time
def find_repeat(the_list):
    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:

        # divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # lower range is floor..midpoint
        # upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) / 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

        # count number of items in lower range
        items_in_lower_range = 0
        for item in the_list:
            # is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = \
            lower_range_ceiling - lower_range_floor + 1

        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # there must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # there must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling


    # floor and ceiling have converged
    # we found a number that repeats!
    return floor
