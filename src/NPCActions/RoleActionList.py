from src.NPC import NPC


# class RoleEffectList:

def seerActionFunction(gameInfo, targetNPC: NPC, selfNPC: NPC):
    if targetNPC not in gameInfo.npcList:
        raise Exception(targetNPC.name + " not found.")

    # selfNPC.journal.append((targetNpcName, gameInfo.npcList[targetNpcName].role.roleName))
    selfNPC.journal.append(targetNPC.name + " is a " + gameInfo.npcList[gameInfo.npcList.index(targetNPC)].role.roleName)

def werewolfActionFunction(gameInfo, targetNpc: NPC, selfNPC: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    #if not full moon, werewolf does nothing
    if gameInfo.currentNightType == "full moon":
        npcNameList = [npc.name for npc in gameInfo.npcList]
        # gameInfo.npcList[npcNameList.index(targetNpcName)].isBeingKilled = True
        gameInfo.npcList[gameInfo.npcList.index(targetNpc)].isBeingKilled = True

# The doctor can save a villager even if the villager is targeted by multiple hostiles
def doctorActionFunction(gameInfo, targetNpc: NPC, selfNPC: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    if gameInfo.npcList[gameInfo.npcList.index(targetNpc)].isBeingKilled == True:
        selfNPC.journal.append(
            "visited " + targetNpc.name + " on night " + str(gameInfo.currentTurn) + " and saved his life")
        gameInfo.npcList[gameInfo.npcList.index(targetNpc)].isBeingKilled = False
    else:
        selfNPC.journal.append("visited " + targetNpc.name + " on night " + str(gameInfo.currentTurn))

#Villagers do nothing
def villagerActionFunction(gameInfo, targetNpcName: str, selfNPC: NPC):
    pass

roleActionMap = {
    "seer": seerActionFunction,
    "werewolf": werewolfActionFunction,
    "doctor": doctorActionFunction,
    "villager": villagerActionFunction,
}
