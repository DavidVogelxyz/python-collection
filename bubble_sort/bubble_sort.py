list = [420, 69, 710, 11, 19, 26, 42, 12, 91, 88, 24, 33, 10, 4, 7, 9]


def bubble(list_a):
    index_len = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index_len):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a


print(bubble(list))
