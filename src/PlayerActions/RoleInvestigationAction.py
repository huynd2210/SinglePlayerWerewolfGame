def _possibleTargetNames(gameInfo):
    return [npc.name for npc in gameInfo.npcList if not npc.isAlive]

def roleInvestigationActionWrapper(gameInfo):
    possibleTargetsNames = _possibleTargetNames(gameInfo)

    if len(possibleTargetsNames) == 0:
        print("No possible targets ")
        return False
    print("Who do you want to investigate?")
    _printTargetNames(possibleTargetsNames)
    targetNameToInvestigate = input()

    while targetNameToInvestigate not in possibleTargetsNames:
        print("Invalid input, try again")
        print("Who do you want to investigate?")
        _printTargetNames(possibleTargetsNames)
        targetNameToInvestigate = input()

    _roleInvestigationActionFunction(gameInfo, targetNameToInvestigate)
    return True

def _printTargetNames(possibleTargetsNames):
    for targetNames in possibleTargetsNames:
        print(targetNames)


def _roleInvestigationActionFunction(gameInfo, npcName):
    possibleNpcTargetNames = _possibleTargetNames(gameInfo)

    if npcName not in possibleNpcTargetNames:
        print("Npc not found.")
        return

    print("You investigated " + npcName + ".")
    _resolveRoleInvestigationAction(gameInfo, npcName)


def _resolveRoleInvestigationAction(gameInfo, npcName):
    npcNameList = [npc.name for npc in gameInfo.npcList]
    npc = gameInfo.npcList[npcNameList.index(npcName)]
    npcRole = npc.role.roleName

    if npc.isCleaned:
        print("The scene has been wiped clean, you cannot find any traces of their occupation")
    else:
        print("By investigating, you think that " + npcName + " is a " + npcRole + ".")
