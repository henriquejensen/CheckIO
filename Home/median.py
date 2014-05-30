def checkio(data):

    data.sort()

    if len(data) % 2 != 0:
        return data[int(len(data) / 2)]

    else:
        median = data[int(len(data) / 2)] + data[int(len(data) / 2) - 1]
        median = median / 2.0
        return median



# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3
    assert checkio([3, 1, 2, 5, 3]) == 3
    assert checkio([1, 300, 2, 200, 1]) == 2
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5
    print("The local tests are done.")
