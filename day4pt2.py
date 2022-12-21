def createRange(min, max):
    values = []
    for i in range(min,max+1):
        values.append(i)
    return values

with open("input4.txt", "r") as wf:
    Values = wf.readlines()
    dupes = 0
    for line in Values:
        ranges = line.replace("\n","").split(",")
        ranges[0] = ranges[0].split("-")
        ranges[1] = ranges[1].split("-")
        areas = [createRange(int(ranges[0][0]),int(ranges[0][1])),createRange(int(ranges[1][0]),int(ranges[1][1]))]
        if list(set(areas[0]).intersection(areas[1])):
            dupes += 1
    print(dupes)
