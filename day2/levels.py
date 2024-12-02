from enum import Enum

SAFE_INTERVAL = 3

UP = 2
DOWN = 1
NONE = 0

with open("test.txt", "r") as f:
    input = f.readlines()


def parsing (input):
    reports = []
    for line in input:
        reports.append(list(map(int, line.split())))
    print (reports)
    return reports


def safe_reports(reports):
    safe_reports = 0
    for report in reports:
        if part_two_safe_levels(report):
            safe_reports += 1
    print(safe_reports)
    return safe_reports



def safe_levels(report: list, direction= NONE ):
    already_unsafe = False
    if report[0] - report[1] > 0 or direction == UP:
        for i, level in enumerate(report):
            if i == len(report) - 1:
                print("TRUE: ", report)
                return True

            difference = level - report[i + 1]

            if 1 <= difference <= SAFE_INTERVAL:
                continue
            else:
                return False

    elif report[0] - report[1] < 0 or direction == DOWN:
        for i, level in enumerate(report):
            if i == len(report) - 1:
                print("TRUE: ", report)
                return True
            difference = level - report[i + 1]

            if -1 >= difference >= -SAFE_INTERVAL:
                continue
            else:
                return False

    print("False: ", report)
    return False



def part_two_safe_levels(report: list):
    already_unsafe = False

    if report[0] - report[1] == 0:
        return safe_levels(report[1::])

    if report[0] - report[1] > 0:
        direction = UP # means up
        for i, level in enumerate(report):
            if i == len(report) - 1:
                print("TRUE: ", report)
                return True

            difference = level - report[i + 1]

            if 1 <= difference <= SAFE_INTERVAL:
                continue
            else:
                if i == len(report) - 2:
                    print("TRUE: ", report)
                    return True
                return safe_levels(report[i + 1::],direction )

    elif report[0] - report[1] < 0:
        direction = DOWN
        for i, level in enumerate(report):
            if i == len(report) - 1:
                print("TRUE: ", report)
                return True
            difference = level - report[i + 1]

            if -1 >= difference >= -SAFE_INTERVAL:
                continue
            else:
                if i == len(report) - 2:
                    print("TRUE: ", report)
                    return True
                return safe_levels(report[i + 1::], direction)

    print("False: ", report)
    return False


with open("output.txt", "w") as f:
    f.write(str(safe_reports(parsing(input))))


# safe_reports(parsing(input))
