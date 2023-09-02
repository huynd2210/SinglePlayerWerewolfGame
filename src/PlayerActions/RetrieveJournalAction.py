def _possibleTargetNames(gameInfo):
    return [npc.name for npc in gameInfo.npcList if not npc.isAlive]

def retrieveJournalActionWrapper(gameInfo):
    print("Whose journal do you want to retrieve?")
    possibleTargetsNames = _possibleTargetNames(gameInfo)
    _printTargetNames(possibleTargetsNames)
    targetNameToRetrieve = input()

    if targetNameToRetrieve not in possibleTargetsNames:
        print("Invalid input, try again")
        print("Whose journal do you want to retrieve?")
        _printTargetNames(possibleTargetsNames)
        targetNameToRetrieve = input()
    _retrieveJournalActionFunction(gameInfo, targetNameToRetrieve)

def _printTargetNames(possibleTargetsNames):
    for targetNames in possibleTargetsNames:
        print(targetNames)

def _retrieveJournalActionFunction(gameInfo, npcName):
    possibleNpcTargetNames = _possibleTargetNames(gameInfo)

    if npcName not in possibleNpcTargetNames:
        print("Npc not found.")
        return

    print("You retrieved " + npcName + " journal.")
    _resolveRetrieveJournalAction(gameInfo, npcName)


def _resolveRetrieveJournalAction(gameInfo, npcName):
    npcNameList = [npc.name for npc in gameInfo.npcList]
    npcJournal = gameInfo.npcList[npcNameList.index(npcName)].journal

    itemName = npcName + "'s journal"
    gameInfo.player.inventory[itemName] = npcJournal
    print(npcName, "'s journal", npcJournal)
