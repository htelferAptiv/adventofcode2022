with open('/Users/htelfer/Development/adventofcode2022/one/input.txt') as f:
    lines = f.readlines()
    sumList = []
    currentElfStashSize = 0
    for i,v in enumerate(lines):
        
        if v == "\n":
            sumList.append(currentElfStashSize)
            currentElfStashSize = 0
        else:
            currentElfStashSize = currentElfStashSize + int(v)
    
    sumList.sort()
    print("BEEG elf: " + str(sumList[len(sumList)-1]))
    beegSquad = []
    beegSquad.append(sumList[len(sumList)-1])
    beegSquad.append(sumList[len(sumList)-2])
    beegSquad.append(sumList[len(sumList)-3])

    print("BEEG SQUAD: " + str(beegSquad))
    print("squad power level: " + str(sum(beegSquad)))

        
