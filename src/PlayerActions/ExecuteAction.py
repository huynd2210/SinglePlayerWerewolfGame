def _possibleTargetNames(gameInfo):
    return [npc.name for npc in gameInfo.npcList if npc.isAlive]

#Returning True to indicte action was sucessfully performed
def executeNPCActionWrapper(gameInfo):
    print("Who do you want to execute")
    possibleTargetNames = _possibleTargetNames(gameInfo)

    _printTargetNames(possibleTargetNames)
    targetNameToExecute = input()

    if targetNameToExecute == "None":
        return True

    if targetNameToExecute not in possibleTargetNames:
        print("Invalid input, try again")
        print("Who do you want to execute?")
        _printTargetNames(possibleTargetNames)
        targetNameToExecute = input()
        if targetNameToExecute == "None":
            return True

    return True

    _executeNPCActionFunction(gameInfo, targetNameToExecute)
def _executeNPCActionFunction(gameInfo, npcName):
    npcNameList = [npc.name for npc in gameInfo.npcList]
    if npcName not in npcNameList:
        raise Exception("Npc " + npcName + " not found.")

    gameInfo.npcList[npcNameList.index(npcName)].isAlive = False
    print(npcName + " was executed.")


def _printTargetNames(possibleTargetNames):
    for targetNames in possibleTargetNames:
        print(targetNames)