#Your optional code here
#You can import some modules or create additional functions


def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.
    array = []
    cont = 0
    for i in data:
        aux = data[:]
        aux.pop(cont)
        if i in aux:
            array.append(i)
        cont += 1
    #replace this for solution
    return array

#Some hints
#You can use list.count(element) method fort counting.
#Create new list with non-unique elements
#or remove elements from original list (but it's bad practice for many real cases)
#Loop over original list

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list)
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
    assert checkio([1, 2, 3, 4, 5]) == []
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
