# read trees.dat and put each valid element into a list
# Contains height in even feet of a large sample of CA coastal redwood trees
# use only built-in functions (min, max, sum, len) and normal math equations to produce a report showing:
#   1. Number of trees
#   2. Average height of the trees to one decimal place
#   3. height of the tallest tree
#   4. height of the shortest tee


def main():
    """
    TODO: Actual docstring
    """

    with open("/home/kek/PycharmProjects/ACCD-Python/Python II/classData/trees.dat", "r") as f:
        data = f.read().split("\n")

    trees = len(data)
    maxTree = max(data)
    minTree = min(data)
    sumTree = 0

    for i in data:
        sumTree += int(i)

    avgTree = sumTree/trees

    print(
        f"Total trees = {trees}\n"
        f"Average height = {round(avgTree, 1):}\n"
        f"Shortest tree = {minTree}\n"
        f"Tallest tree = {maxTree}\n"
    )


if __name__ == '__main__':
    main()
