class VisitAction:
    def visitActionFunction(self, gameInfo, npcName):
        if npcName not in gameInfo.npcList:
            print("NPC not found.")
            return

        print("You visited " + npcName + ".")

    def _resolveVisitAction(self, gameInfo, npcName):
        npcEffect = {}
        # roleName = gameInfo.npcList[npcName].role.roleName
        npcEffect["villager"] = self._resolveVisitingVillager(gameInfo, npcName)

        npcEffect["seer"] = self._resolveVisitingSeer(gameInfo, npcName)

        npcEffect["werewolf"] = self._resolveVisitingWerewolf(gameInfo, npcName)

        npcEffect["doctor"] = self._resolveVisitingDoctor(gameInfo, npcName)

    def _resolveVisitingWerewolf(self, gameInfo, npcName):
        if gameInfo.currentNightType == "Full Moon":
            return npcName + " is not at home. There are traces of wolf fur on the floor. You conclude that he is a werewolf."
        else:
            return "You think that " + npcName + " is a villager."

    def _resolveVisitingVillager(self, gameInfo, npcName):
        return "You think that " + npcName + " is a villager."

    def _resolveVisitingSeer(self, gameInfo, npcName):
        # return npcName + \
        #     " revealed that he is a seer, and he has learned that " + \
        #     str(gameInfo.npcList[npcName].journal[0]) + \
        #     " is a " + gameInfo.npcList[npcName].journal[1] + "."
        return npcName + "revealed that he is a seer, and he has learned that " + str(gameInfo.npcList[npcName].journal)

    def _resolveVisitingDoctor(self, gameInfo, npcName):
        if gameInfo.npcList[npcName].isAtHome:
            return npcName + " revealed that he is a doctor and he " + str(gameInfo.npcList[npcName].journal)