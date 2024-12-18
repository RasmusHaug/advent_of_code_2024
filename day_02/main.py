
def main():
    counter_1 = solution_1()
    counter_2 = solution_2()
    print("ANSWER 1: ", counter_1)
    print("ANSWER 2: ", counter_2)

def solution_1():
    counter = 0
    with open("input") as file:
        for line in file:
            level = list(map(int, line.split()))
            print(f"Checking Line: {level}")
            if is_safe_report(level):
                counter += 1
    return counter

def solution_2():
    counter = 0
    with open("input") as file:
        for line in file:
            level = list(map(int, line.split()))
            print(f"Checking line: {level}")
            if is_safe_with_dampners(level):
                counter += 1
            print()
        return counter

def is_safe_report(levels):
    # Check if the list of differences is consistently positive or consistently negative
    differences = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]
    # Check if all differences are in the range [-3, -1] (strictly decreasing) or [1, 3] (strictly increasing)
    all_increasing = all(1 <= diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff <= -1 for diff in differences)
    return all_increasing or all_decreasing

def is_safe_with_dampners(levels):
    if is_safe_report(levels):
        return True

    for i in range(len(levels)):
        # Remove 1 level at a time; going through the list of levels.
        modified_levels = levels[:i] + levels[i+1:]
        if is_safe_report(modified_levels):
            return True

    return False


if __name__ == "__main__":
    main()
