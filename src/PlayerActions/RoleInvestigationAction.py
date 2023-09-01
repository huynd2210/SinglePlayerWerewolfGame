def _possibleTargetNames(gameInfo):
    return [npc.name for npc in gameInfo.npcList if not npc.isAlive]

def roleInvestigationActionWrapper(gameInfo):
    print("Who do you want to investigate?")
    possibleTargetsNames = _possibleTargetNames(gameInfo)
    _printTargetNames(possibleTargetsNames)
    targetNameToInvestigate = input()

    if targetNameToInvestigate not in possibleTargetsNames:
        print("Invalid input, try again")
        print("Who do you want to investigate?")
        _printTargetNames(possibleTargetsNames)
        targetNameToInvestigate = input()
    _roleInvestigationActionFunction(gameInfo, targetNameToInvestigate)

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
    npcRole = gameInfo.npcList[npcNameList.index(npcName)].role.roleName

    if npcRole == "Cleaned":
        print("The scene has been wiped clean, you cannot find any traces of their occupation")
    else:
        print("By investigating, you think that " + npcName + " is a " + npcRole + ".")
