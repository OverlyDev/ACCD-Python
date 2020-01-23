# use servercheck.py. It reads two files (servers and updates) and converts the contents into two sets
# the updates are not always correct
# Using just these operations/methods:
#   1. Determine whether the list of updates exists in the master server list. Print a message indicating this
#   2. If it is not true, create a new set containing the update items that are NOT in the master server set
#       Print the number and names of the unmatched servers
#   3. Create a new master server set that excludes the valid updates
#   4. Print the number of items in the original master server set, the new master server, and number of valid updates
#   5. Write the contents of the new master server set to a printable external file using the writelines file method


def main():
    updates = set(open('/home/kek/PycharmProjects/ACCD-Python/Python II/classData/serverupdates.txt', 'r'))
    servers = set(open('/home/kek/PycharmProjects/ACCD-Python/Python II/classData/servers.txt', 'r'))

    unmatchedUpdates = updates.difference(servers)

    if len(unmatchedUpdates) > 0:
        print("Unmatched updates:")
        count = 0
        for i in unmatchedUpdates:
            count += 1
            updates.remove(i)
            print(f"\t{count}\t", end="")
            print(i.strip('\n'))

        newMaster = servers.difference(updates)

        print(f"Original servers: {len(servers)}")
        print(f"Valid updates: {len(updates)}")
        print(f"New servers: {len(newMaster)}")

        with open("/home/kek/PycharmProjects/ACCD-Python/Python II/newmaster.txt", "w") as f:
            f.writelines(newMaster)


if __name__ == '__main__':
    main()
