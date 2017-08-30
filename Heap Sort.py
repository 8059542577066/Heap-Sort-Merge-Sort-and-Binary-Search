import random


def swap(array, i1, i2):
    temp = array[i1]
    array[i1] = array[i2]
    array[i2] = temp

def heapify(array):
    for i in xrange(1, len(array)):
        c = i
        while c > 0:
            if c % 2 == 1:
                p = c / 2
            else:
                p = c / 2 - 1
            if array[p] < array[c]:
                swap(array, p, c)
                c = p
            else:
                break

def sort(array, samples):
    if samples == 0:
        return
    else:
        heapify(array)
        s = 0
        i = len(array) - 1
        swap(array, 0, i)
        s += 1
        if s == samples:
            return
        i -= 1
        while i > 0:
            p = 0
            c1 = 2 * p + 1
            c2 = c1 + 1
            while c1 <= i:
                if c2 <= i:
                    if array[c1] < array[c2]:
                        if array[p] < array[c2]:
                            swap(array, p, c2)
                            p = c2
                        else:
                            break
                    else:
                        if array[p] < array[c1]:
                            swap(array, p, c1)
                            p = c1
                        else:
                            break
                else:
                    if array[p] < array[c1]:
                        swap(array, p, c1)
                        p = c1
                    else:
                        break
                c1 = 2 * p + 1
                c2 = c1 + 1
            swap(array, 0, i)
            s += 1
            if s == samples:
                return
            i -= 1


def main():
    print "Heap Sort"
    count = int(raw_input("Number of Items: "))
    samples = int(raw_input("Number of Samples: "))
    if count > samples:
        first = count - samples
    else:
        first = 0
    numbers = []
    for i in xrange(count):
        numbers.append(random.getrandbits(64))
    print "\nBefore Sorting:"
    check = numbers[first:] == sorted(numbers)[first:]
    print "numbers == sorted(numbers): " + str(check)
    sort(numbers, samples)
    print "\nAfter Sorting:"
    check = numbers[first:] == sorted(numbers)[first:]
    print "Result Items: " + str(len(numbers[first:]))
    print "numbers == sorted(numbers): " + str(check)
    raw_input()


if __name__ == "__main__":
    main()
