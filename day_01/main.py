
def main():
    left_numbers = []
    right_numbers = []
    with open("input") as file:
        for line in file:
            n = line.strip().split()
            left_numbers.append(n[0])
            right_numbers.append(n[1])
    x = solution_1(sorted(left_numbers), sorted(right_numbers))
    y = solution_2(left_numbers, right_numbers)
    print("solution_1:", x, "solution_2", y)

def solution_1(l, r):
    if len(l) == len(r):
        leng = len(l)
    else:
        print("Weird, different lengths")
    ans = 0
    for i in range(leng):
        ans += abs(int(l[i]) - int(r[i]))
    return ans

def solution_2(l, r):
    # this is slow
    ans = 0
    for num_l in l:
        multiplier = 0
        for num_r in r:
            if num_l == num_r:
                multiplier += 1
        ans += int(num_l) * int(multiplier)
        print(num_l, multiplier, ans)
    return ans


if __name__ == "__main__":
    main()
