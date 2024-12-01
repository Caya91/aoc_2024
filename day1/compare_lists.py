import os

with open("input.txt", "r") as f:
    input = f.read()


left_list = []
right_list = []

for line in input.splitlines():
    left_list.append(int(line.split()[0]))
    right_list.append(int(line.split()[1]))

left_list.sort()
right_list.sort()


def list_distance(list1, list2):
    total_distance = 0
    for i, place in enumerate(list1):
        total_distance += abs(list1[i] - list2[i])
    return total_distance

output = list_distance(left_list, right_list)

with open("output1.txt", "w") as f:
    f.write(str(output))


def similarity_score(list1, list2):
    score = 0
    for i, place in enumerate(list1):
        score += list1[i] * list2.count(list1[i])
    return score

with open("output2.txt", "w") as f:
    f.write(str(similarity_score(left_list, right_list)))