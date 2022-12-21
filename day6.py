def findIndex(message, amount_needed):
    currentList = []
    index = 0
    for i in message:
        index += 1
        if len(currentList) < amount_needed:
            currentList.append(i)
        else:
            currentList.pop(0)
            currentList.append(i)
            if len(set(currentList)) == amount_needed:
                break
    print(index)

with open("input6.txt", "r") as wf:
    Values = wf.read().replace("\n","")
    findIndex(Values, 4)
    findIndex(Values, 14)