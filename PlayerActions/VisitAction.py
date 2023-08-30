
def visitActionWrapper(gameInfo):
    print("Who do you want to visit")
    possibleTargetNames = _possibleTargetNames(gameInfo)

    _printTargetNames(possibleTargetNames)
    targetNameToVisit = input()

    if targetNameToVisit not in possibleTargetNames:
        print("Invalid input, try again")
        print("Who do you want to visit?")
        _printTargetNames(possibleTargetNames)
        targetNameToVisit = input()
    _visitActionFunction(gameInfo, targetNameToVisit)

def _visitActionFunction(gameInfo, npcName):
    aliveNpcNames = [npc.name for npc in gameInfo.npcList if npc.isAlive]
    if npcName not in aliveNpcNames:
        print("NPC not found.")
        return

    print("You visited " + npcName + ".")
    _resolveVisitAction(gameInfo, npcName)

def _resolveVisitAction(gameInfo, npcName):
    npcEffect = {}
    # roleName = gameInfo.npcList[npcName].role.roleName
    npcEffect["villager"] = _resolveVisitingVillager

    npcEffect["seer"] = _resolveVisitingSeer

    npcEffect["werewolf"] = _resolveVisitingWerewolf

    npcEffect["doctor"] = _resolveVisitingDoctor

    npcNameList = [npc.name for npc in gameInfo.npcList]
    npcRole = gameInfo.npcList[npcNameList.index(npcName)].role.roleName
    print(npcEffect[npcRole](gameInfo, npcName))

def _resolveVisitingWerewolf(gameInfo, npcName):
    if gameInfo.currentNightType == "full moon":
        return npcName + " is not at home. There are traces of wolf fur on the floor. You conclude that he is a werewolf."
    else:
        return "You think that " + npcName + " is a villager."


def _resolveVisitingVillager(gameInfo, npcName):
    return "You think that " + npcName + " is a villager."


def _resolveVisitingSeer(gameInfo, npcName):
    # return npcName + \
    #     " revealed that he is a seer, and he has learned that " + \
    #     str(gameInfo.npcList[npcName].journal[0]) + \
    #     " is a " + gameInfo.npcList[npcName].journal[1] + "."
    npcNameList = [npc.name for npc in gameInfo.npcList]
    return npcName + " revealed that he is a seer, and he has learned that " + str(gameInfo.npcList[npcNameList.index(npcName)].journal)


def _resolveVisitingDoctor(gameInfo, npcName):
    npcNameList = [npc.name for npc in gameInfo.npcList]
    if gameInfo.npcList[npcNameList.index(npcName)].isAtHome:
        return npcName + " revealed that he is a doctor and he " + str(gameInfo.npcList[npcNameList.index(npcName)].journal)

def _printTargetNames(possibleTargetNames):
    for targetNames in possibleTargetNames:
        print(targetNames)

def _possibleTargetNames(gameInfo):
    return [npc.name for npc in gameInfo.npcList if npc.isAlive]