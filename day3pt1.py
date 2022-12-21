with open("input3.txt", "r") as wf:
    Values = wf.readlines()
    priority = 0
    for line in Values:
        comp1 = line[0:len(line)//2]
        comp2 = line[len(line)//2:]
        common = set(comp1).intersection(comp2)
        item = list(common)[0]
        if item.isupper():
            priority += ord(list(common)[0]) - 64 + 26
        else:
            priority += ord(list(common)[0]) - 96
    print(priority)