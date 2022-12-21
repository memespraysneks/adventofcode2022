def createStacks(rawInput):
    stackHeight = rawInput.split("\n")
    stackHeight.pop(-1)
    stackAmount = len(stackHeight)
    stacksHor = []
    stacksVer = [[] for _ in range(stackAmount)]
    for line in (stackHeight):
        working = [line[i:i+3] for i in range(0, len(line),4)]
        stacksHor.append(working)
    # Everything Up to Here works, the following code is broken because it doesn't parse the last set of boxes
    for i in range(stackAmount+1):
        for j in range(stackAmount+1):
            if stacksHor[j][i] != "   ":
                stacksVer[i].append(stacksHor[j][i])
        stacksVer[i].reverse()
    print(stacksVer)


with open("input5.txt", "r") as wf:
    Values = wf.read()
    stacks, movements = Values.split("\n\n")
    createStacks(stacks)