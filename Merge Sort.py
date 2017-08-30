import random


def sort(array, e1, e2):
    m1 = (e1 + e2) / 2
    m2 = m1 + 1
    if e1 != m1:
        sort(array, e1, m1)
        sort(array, m2, e2)
    temp = []
    i1 = e1
    i2 = m2
    while i1 <= m1 and i2 <= e2:
        if array[i1] <= array[i2]:
            temp.append(array[i1])
            i1 += 1
        else:
            temp.append(array[i2])
            i2 += 1
    if i1 > m1:
        while i2 <= e2:
            temp.append(array[i2])
            i2 += 1
    else:
        while i1 <= m1:
            temp.append(array[i1])
            i1 += 1
    for i in xrange(len(temp)):
        array[e1 + i] = temp[i]


def main():
    print "Merge Sort"
    count = int(raw_input("Number of Items: "))
    numbers = []
    for i in xrange(count):
        numbers.append(random.getrandbits(64))
    print "\nBefore Sorting:"
    print "numbers == sorted(numbers): " + str(numbers == sorted(numbers))
    sort(numbers, 0, len(numbers) - 1)
    print "\nAfter Sorting:"
    print "numbers == sorted(numbers): " + str(numbers == sorted(numbers))
    raw_input()


if __name__ == "__main__":
    main()
