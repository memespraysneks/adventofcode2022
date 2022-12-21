with open("input2.txt", "r") as wf:
    Values = wf.readlines()
    total_score = 0
    win = {"A": 8, "B": 9, "C": 7}
    tie = {"A": 4,"B": 5,"C": 6}
    lose = {"A": 3, "B": 1, "C": 2}
    for line in Values:
        outcome = line.split()
        if outcome[1] == "X":
            total_score += lose[outcome[0]]
        elif outcome[1] == "Y":
            total_score += tie[outcome[0]]
        elif outcome[1] == "Z":
            total_score += win[outcome[0]]
    print(total_score)