import random
import bisect


def find(target, array, e1, e2):
    m1 = (e1 + e2) / 2
    m2 = m1 + 1
    if target == array[m1]:
        return m1
    elif e1 == e2:
        return -1
    elif target < array[m1]:
        return find(target, array, e1, m1)
    else:
        return find(target, array, m2, e2)


def main():
    print "Binary Search"
    count = int(raw_input("Number of Items: "))
    numbers = []
    for i in xrange(count):
        numbers.append(random.getrandbits(64))
    numbers.sort()
    index = int(raw_input("Index of Item to Search: "))
    if index >= 0 and index < len(numbers):
        target = numbers[index]
    else:
        target = -999
    print "\nfind(): " + str(find(target, numbers, 0, len(numbers) - 1))
    print "bisect.bisect() - 1: " + str(bisect.bisect(numbers, target) - 1)
    raw_input()


if __name__ == "__main__":
    main()
