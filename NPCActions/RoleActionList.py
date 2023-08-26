from NPC import NPC


# class RoleEffectList:

def seerActionFunction(gameInfo, targetNpcName: str, selfNPC: NPC):
    if targetNpcName not in gameInfo.npcList:
        raise Exception(targetNpcName + " not found.")

    # selfNPC.journal.append((targetNpcName, gameInfo.npcList[targetNpcName].role.roleName))
    selfNPC.journal.append(targetNpcName + " is a " + gameInfo.npcList[targetNpcName].role.roleName)


def werewolfActionFunction(gameInfo, targetNpcName: str, selfNPC: NPC):
    if targetNpcName not in gameInfo.npcList:
        raise Exception(targetNpcName + " not found.")

    #if not full moon, werewolf does nothing
    if gameInfo.currentNightType == "Full Moon":
        gameInfo.npcList[targetNpcName].isBeingKilled = True


# The doctor can save a villager even if the villager is targeted by multiple hostiles
def doctorActionFunction(gameInfo, targetNpcName: str, selfNPC: NPC):
    if targetNpcName not in gameInfo.npcList:
        raise Exception(targetNpcName + " not found.")

    if gameInfo.npcList[targetNpcName].isBeingKilled == True:
        selfNPC.journal.append(
            "visited " + targetNpcName + " on night" + str(gameInfo.currentTurn) + " and saved his life.")
    else:
        selfNPC.journal.append("visited " + targetNpcName + " on night" + str(gameInfo.currentTurn))

roleActionMap = {
    "Seer": seerActionFunction,
    "Werewolf": werewolfActionFunction,
    "Doctor": doctorActionFunction
}
