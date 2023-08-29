def roleInvestigationActionFunction(gameInfo, npcName):
    deadNpcNames = [npc.name for npc in gameInfo.npcList if not npc.isAlive]
    if npcName not in deadNpcNames:
        print("NPC not found.")
        return

    print("You investigated " + npcName + ".")
    resolveRoleInvestigationAction(gameInfo, npcName)

def resolveRoleInvestigationAction(gameInfo, npcName):
    npcNameList = [npc.name for npc in gameInfo.npcList]
    npcRole = gameInfo.npcList[npcNameList.index(npcName)].role.roleName
    print("By investigating, you think that " + npcName + " is a " + npcRole + ".")