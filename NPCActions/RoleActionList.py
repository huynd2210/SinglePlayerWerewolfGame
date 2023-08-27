from NPC import NPC


# class RoleEffectList:

def seerActionFunction(gameInfo, targetNPC: NPC, selfNPC: NPC):
    if targetNPC not in gameInfo.npcList:
        raise Exception(targetNPC.name + " not found.")

    # selfNPC.journal.append((targetNpcName, gameInfo.npcList[targetNpcName].role.roleName))
    selfNPC.journal.append(targetNPC.name + " is a " + gameInfo.npcList[gameInfo.npcList.index(targetNPC)].role.roleName)

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

#Villagers do nothing
def villagerActionFunction(gameInfo, targetNpcName: str, selfNPC: NPC):
    pass

roleActionMap = {
    "seer": seerActionFunction,
    "werewolf": werewolfActionFunction,
    "doctor": doctorActionFunction,
    "villager": villagerActionFunction,
}
