def _possibleTargetNames(gameInfo):
    return [npc.name for npc in gameInfo.npcList if npc.isAlive]

def executeNPCActionWrapper(gameInfo):
    print("Who do you want to execute")
    possibleTargetNames = _possibleTargetNames(gameInfo)

    _printTargetNames(possibleTargetNames)
    targetNameToExecute = input()

    if targetNameToExecute == "None":
        return

    if targetNameToExecute not in possibleTargetNames:
        print("Invalid input, try again")
        print("Who do you want to execute?")
        _printTargetNames(possibleTargetNames)
        targetNameToExecute = input()
        if targetNameToExecute == "None":
            return


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