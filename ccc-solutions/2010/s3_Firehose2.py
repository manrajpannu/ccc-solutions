def _find_hoses_needed (circle_length, hose_span, houses):
    # We assume that houses is sorted.
    answers = [] # We can always get away with one hydrant per house.
    for start in range(len(houses)):
        needed = 1
        last_begin = start
        current_house = start + 1 if start + 1 < len(houses) else 0
        while current_house != start:
            pos_begin = houses[last_begin]
            pos_end = houses[current_house]
            length = pos_end - pos_begin if pos_begin <= pos_end else circle_length + pos_begin - pos_end
            if hose_span < length:
                # We need a new hose.
                needed = needed + 1
                last_begin = current_house
            current_house = current_house + 1
            if len(houses) <= current_house:
                # We looped around the circle.
                current_house = 0
        answers.append(needed)
    return min(answers)

def find_min_hose_coverage (circle_length, hydrant_count, houses):
    houses = sorted(houses)

    # First we find all of the possible answers.
    is_length = set()
    for i in range(len(houses)):
        for j in range(i, len(houses)):
            is_length.add(houses[j] - houses[i])
            is_length.add(houses[i] - houses[j] + circle_length)
    possible_answers = sorted(is_length)

    # Now we do a binary search.
    lower = 0
    upper = len(possible_answers) - 1
    while lower < upper:
        mid = (lower + upper) / 2 # Note, we lose the fraction here.
        if hydrant_count < _find_hoses_needed(circle_length, possible_answers[mid], houses):
            # We need a strictly longer coverage to make it.
            lower = mid + 1
        else:
            # Longer is not needed
            upper = mid
    return possible_answers[lower]

print(find_min_hose_coverage(1000000, 2, [0, 67000, 68000, 77000])/2)