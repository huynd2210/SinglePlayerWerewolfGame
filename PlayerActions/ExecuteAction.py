class ExecuteAction:
    def executeNPCActionFunction(self, gameInfo, npcName):
        if npcName not in gameInfo.npcList:
            raise Exception("NPC " + npcName + " not found.")

        gameInfo.npcList[npcName].isAlive = False
        print(npcName + " was executed.")