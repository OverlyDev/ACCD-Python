# change the program you developed in the last lab to remove the newline characters from the data you read in
# put them back in the data you write
# How will you read the server data?
# How will you write the new server file?
# When finished you should be able to open the new server file with any text editor and display one server per line


def main():

    with open('/home/kek/PycharmProjects/ACCD-Python/Python II/classData/serverupdates.txt', 'r') as f:
        updates = set(f.read().split())
    with open('/home/kek/PycharmProjects/ACCD-Python/Python II/classData/servers.txt', 'r') as f:
        servers = set(f.read().split())

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
            for i in newMaster:
                f.write(i + '\n')


if __name__ == '__main__':
    main()