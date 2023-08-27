def executeNPCActionFunction(gameInfo, npcName):
    npcNameList = [npc.name for npc in gameInfo.npcList]
    if npcName not in npcNameList:
        raise Exception("NPC " + npcName + " not found.")

    gameInfo.npcList[npcNameList.index(npcName)].isAlive = False
    print(npcName + " was executed.")
