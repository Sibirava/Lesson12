def calc_avg_mark(groups):
    s = 0
    number = 0

    for group in groups:
        for mark in group:
            s += mark

        number += len(group)

    return s / number

def main():

    groups = []
    group_number = int(input("Input number of groups: "))

    for _ in range(group_number):
        groups.append([])

    for group in groups:
        number = int(input("Input number of students: "))

        for i in range(number):
            mark = int(input(f"Input{i + 1} mark: "))
            group.append(mark)

    # print(groups)

    avg = calc_avg_mark(groups)


    msg = f"Average student's mark is {round(avg, 2)}"

    print(msg)


main()
