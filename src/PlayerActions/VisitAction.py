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
        print("Npc not found.")
        return False

    print("You visited " + npcName + ".")
    _resolveVisitAction(gameInfo, npcName)

    return True

def _resolveVisitAction(gameInfo, npcName):
    npcEffect = {}
    # roleName = gameInfo.npcList[npcName].role.roleName
    npcEffect["villager"] = _resolveVisitingVillager

    npcEffect["seer"] = _resolveVisitingSeer

    npcEffect["werewolf"] = _resolveVisitingWerewolf

    npcEffect["doctor"] = _resolveVisitingDoctor

    npcEffect["cleaner"] = _resolveVisitingCleaner

    npcEffect["trapper"] = _resolveVisitingTrapper

    npcEffect["deceiver"] = _resolveVisitingDeceiver

    npcEffect["serial killer"] = _resolveVisitingSerialKiller

    npcEffect['guard'] = _resolveVisitingGuard

    npcEffect['ambusher'] = _resolveVisitingAmbusher

    npcEffect['terrorist'] = _resolveVisitingTerrorist

    npcNameList = [npc.name for npc in gameInfo.npcList]
    npc = gameInfo.npcList[npcNameList.index(npcName)]


    #resolving traps
    if npc.isBeingTrapped:
        print("You were caught in a trap while visiting", npcName, "you spent the entire night disarming the trap")
        return

    if npc.isBeingCoveredByDeceiver:
        print(visitResultVillager(npcName))
        return

    npcRoleName = npc.role.roleName

    print(npcEffect[npcRoleName](gameInfo, npcName))


def visitResultVillager(npcName):
    return "You think that " + npcName + " is a villager."

def nobodyHomeVisitResult():
    return "You knocked on the door, but it seems that nobody is at home right now"

def visitResultCriminal(npcName):
    return npcName + " is highly suspicious, you think that he is potentially a criminal"

def visitingCriminalFaction(gameInfo, npcName):
    npcNameList = [npc.name for npc in gameInfo.npcList]
    if gameInfo.npcList[npcNameList.index(npcName)].isAtHome:
        return visitResultCriminal(npcName)
    else:
        return nobodyHomeVisitResult()

def _resolveVisitingWerewolf(gameInfo, npcName):
    if gameInfo.currentNightType == "full moon":
        return npcName + " is not at home. There are traces of wolf fur on the floor. You conclude that he is a werewolf."
    else:
        return visitResultVillager(npcName)


def _resolveVisitingVillager(gameInfo, npcName):
    return visitResultVillager(npcName)


def _resolveVisitingSeer(gameInfo, npcName):
    npcNameList = [npc.name for npc in gameInfo.npcList]
    return npcName + " revealed that he is a seer, and he has learned that " + str(gameInfo.npcList[npcNameList.index(npcName)].journal)

def _resolveVisitingDoctor(gameInfo, npcName):
    npcNameList = [npc.name for npc in gameInfo.npcList]
    if gameInfo.npcList[npcNameList.index(npcName)].isAtHome:
        return npcName + " revealed that he is a doctor and he " + str(gameInfo.npcList[npcNameList.index(npcName)].journal)
    else:
        return nobodyHomeVisitResult()

def _resolveVisitingGuard(gameInfo, npcName):
    npcNameList = [npc.name for npc in gameInfo.npcList]
    if gameInfo.npcList[npcNameList.index(npcName)].isAtHome:
        return npcName + " revealed that he is a guard and he " + str(
            gameInfo.npcList[npcNameList.index(npcName)].journal)
    else:
        return nobodyHomeVisitResult()

def _resolveVisitingCleaner(gameInfo, npcName):
    visitingCriminalFaction(gameInfo, npcName)

def _resolveVisitingTrapper(gameInfo, npcName):
    visitingCriminalFaction(gameInfo, npcName)

def _resolveVisitingDeceiver(gameInfo, npcName):
    visitingCriminalFaction(gameInfo, npcName)

def _resolveVisitingSerialKiller(gameInfo, npcName):
    visitingCriminalFaction(gameInfo, npcName)

def _resolveVisitingAmbusher(gameInfo, npcName):
    visitingCriminalFaction(gameInfo, npcName)

def _resolveVisitingTerrorist(gameInfo, npcName):
    visitingCriminalFaction(gameInfo, npcName)

def _printTargetNames(possibleTargetNames):
    for targetNames in possibleTargetNames:
        print(targetNames)

def _possibleTargetNames(gameInfo):
    return [npc.name for npc in gameInfo.npcList if npc.isAlive]