with open("input2.txt", "r") as wf:
    Values = wf.readlines()
    total_score = 0
    winning = {"A": "Y", "B":"Z", "C":"X"}
    tie = {"A":"X","B":"Y","C":"Z"}
    points = {"X": 1, "Y": 2, "Z": 3}
    for line in Values:
        outcome = line.split()
        if winning[outcome[0]] == outcome[1]:
            total_score += 6
        elif tie[outcome[0]] == outcome[1]:
            total_score += 3
        total_score += points[outcome[1]]
    print(total_score)