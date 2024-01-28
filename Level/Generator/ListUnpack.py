Level = [
    [True, True, True, True, True],
    [True, False, False, False, True],
    [True, False, False, False, True],
    [True, False, False, False, True],
    [True, True, True, True, True],
]

lists = []
notLists = []


def unpackList(name, debugMode=False):

    noListsLeft = False
    __list__ = 0
    __notaList__ = 0

    def checkIfList(toCheck):
        return type(toCheck) == list


    for item in name:
        if checkIfList(item):
            lists.append(item)
            __list__ += 1
        else:
            notLists.append(item)
            __notaList__ += 1

        if __list__ == 0:
            noListsLeft = True

    for thing in lists:
        for junk in thing:
            if checkIfList(junk):
                lists.append(junk)
                __list__ += 1
            else:
                notLists.append(junk)
                __notaList__ += 1

            if __list__ == 0:
                noListsLeft = True

    return notLists


out = unpackList(Level)

print(out)
print(out[5])
