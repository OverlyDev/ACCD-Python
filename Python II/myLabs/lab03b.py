# use range function to create a list containing the numbers: [2, 5, 8, 11, 14, 17]
# create and print a new list with only the even numbers from the original list (filter)
# create and print a new list containing the square of the original numbers (map)
# create a result showing the sum of all the original numbers (reduce)
# use normal loops to accomplish each of these tasks


def main():
    """
    TODO: Actual docstring
    :return:
    """
    startList = [2, 5, 8, 11, 14, 17]
    filterList = []
    mapList = []
    reduced = 0

    for i in startList:
        if i % 2 == 0:
            filterList.append(i)

    for i in startList:
        mapList.append(i**2)

    for i in startList:
        reduced += i

    print(
        f"Original List: {startList}\n"
        f"Filter: {filterList}\n"
        f"Map: {mapList}\n"
        f"Reduce: {reduced}"
    )


if __name__ == '__main__':
    main()
