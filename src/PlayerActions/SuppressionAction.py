def _possibleTargetNames(gameInfo):
    return [npc.name for npc in gameInfo.npcList if npc.isAlive]

#Returning True to indicte action was sucessfully performed
def suppressionActionWrapper(gameInfo):
    message = "Who do you want to suppress"
    print(message)
    possibleTargetNames = _possibleTargetNames(gameInfo)

    _printTargetNames(possibleTargetNames)
    targetNameToSuppress = input()

    if targetNameToSuppress == "None":
        return True

    if targetNameToSuppress not in possibleTargetNames:
        print("Invalid input, try again")
        print(message)
        _printTargetNames(possibleTargetNames)
        targetNameToSuppress = input()
        if targetNameToSuppress == "None":
            return True

    _suppressionActionFunction(gameInfo, targetNameToSuppress)
    return True

def _suppressionActionFunction(gameInfo, npcName):
    npcNameList = [npc.name for npc in gameInfo.npcList]
    if npcName not in npcNameList:
        raise Exception("Npc " + npcName + " not found.")

    gameInfo.npcList[npcNameList.index(npcName)].isBeingSuppressed = True
    print(npcName + " was suppressed.")


def _printTargetNames(possibleTargetNames):
    for targetNames in possibleTargetNames:
        print(targetNames)