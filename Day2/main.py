from enum import Enum



with open('/Users/htelfer/Development/adventofcode2022/Day2/input.txt') as f:
    lines = f.readlines()
    scoreKey1 = [[4,1,7],[8,5,2],[3,9,6]]
    scoreKey2 = [[3,1,2],[4,5,6],[8,9,7]]
    scoreCoords = {
        "A":0,
        "X":0,
        "B":1,
        "Y":1,
        "C":2,
        "Z":2
    }


    totalScore1 = 0
    totalScore2 = 0
    for i,v in enumerate(lines):
        moves = v.split()
        x = moves[0]
        y = moves[1]
        # realized I did the key backwards, so as they say: a negative times a negative is worth a comment or something like that
        totalScore1 = totalScore1 + scoreKey1[scoreCoords[y]][scoreCoords[x]]
        totalScore2 = totalScore2 + scoreKey2[scoreCoords[y]][scoreCoords[x]]

    print("Final Score part 1: ", totalScore1)
    print("Final Score part 2: ", totalScore2)
    