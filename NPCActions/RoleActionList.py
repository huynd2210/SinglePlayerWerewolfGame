from NPC import NPC


class RoleEffectList:
    def seerActionFunction(self, gameInfo, targetNpcName: str, selfNPC: NPC):
        if targetNpcName not in gameInfo.npcList:
            raise Exception(targetNpcName + " not found.")

        # selfNPC.journal.append((targetNpcName, gameInfo.npcList[targetNpcName].role.roleName))
        selfNPC.journal.append(targetNpcName + " is a " + gameInfo.npcList[targetNpcName].role.roleName)

    def werewolfActionFunction(self, gameInfo, targetNpcName: str, selfNPC: NPC):
        if targetNpcName not in gameInfo.npcList:
            raise Exception(targetNpcName + " not found.")

        if gameInfo.currentNightType != "Full Moon":
            raise Exception("Werewolf " + selfNPC.name + " can only attack during Full Moon.")

        gameInfo.npcList[targetNpcName].isBeingKilled = True

    def doctorActionFunction(self, gameInfo, targetNpcName: str, selfNPC: NPC):
        if targetNpcName not in gameInfo.npcList:
            raise Exception(targetNpcName + " not found.")

        if gameInfo.npcList[targetNpcName].isBeingKilled == True:
            selfNPC.journal.append("visited " + targetNpcName + " on night" + str(gameInfo.currentTurn) + " and saved his life.")
        else:
            selfNPC.journal.append("visited " + targetNpcName + " on night" + str(gameInfo.currentTurn))







