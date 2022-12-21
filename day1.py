with open("input1.txt", "r") as wf:
    Input = wf.readlines()
    elfs = []
    count = 0
    for line in Input:
        if line == "\n":
            elfs.append(count)
            count = 0
        else:
            count += int(line)
    elf1 = max(elfs)
    elfs.remove(max(elfs))
    elf2 = max(elfs)
    elfs.remove(max(elfs))
    elf3 = max(elfs)
    print(elf1+elf2+elf3)   