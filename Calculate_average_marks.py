# Успеваемость школы
def calc_avg_mark(group):
    s = 0
    for mark in group:
        s += mark

    return s / len(group)


def main():
    # input block
    number = int(input("Input number of students: "))

    group = []

    for i in range(number):
        mark = int(input(f"Input{i + 1} mark: "))
        group.append(mark)

    # logic block
    avg = calc_avg_mark(group)

    # output block
    msg = f"Average student's mark is {avg}"

    print(msg)


main()
