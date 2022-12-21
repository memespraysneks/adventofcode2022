def stupidIdiotForgotLastCycle(current_elfs):
    first_int = set(current_elfs[0]).intersection(current_elfs[1])
    second_int = set(first_int).intersection(current_elfs[2])
    final = list(second_int)[0]
    if final.isupper():
        return ord(final) - 64 + 26
    else:
        return ord(final) - 96

with open("input3.txt", "r") as wf:
    Values = wf.readlines()
    priority = 0
    current_elfs = []
    count = 0
    for line in Values:
        if count == 3:
            priority += stupidIdiotForgotLastCycle(current_elfs)
            current_elfs = []
            count = 0
        current_elfs.append(line.replace("\n",""))
        count += 1
    priority += stupidIdiotForgotLastCycle(current_elfs)
    print(priority)