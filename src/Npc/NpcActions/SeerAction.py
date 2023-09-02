import random
from src.NPC import NPC


def seerActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = seerPossibleTarget(gameInfo, selfNPC)
    chosenTarget = random.choice(list(filter(lambda npc: npc != selfNPC, possibleTargets)))
    seerActionFunction(gameInfo, chosenTarget, selfNPC)
def seerPossibleTarget(gameInfo, selfNPC: NPC):
    # return [gameInfo.npcList[npc].name for npc in range(len(gameInfo.npcList)) if gameInfo.npcList[npc].isAlive]
    return [npc for npc in gameInfo.npcList if npc.isAlive and npc != selfNPC]

def seerActionFunction(gameInfo, targetNPC: NPC, selfNPC: NPC):
    if targetNPC not in gameInfo.npcList:
        raise Exception(targetNPC.name + " not found.")

    # selfNPC.journal.append((targetNpcName, gameInfo.npcList[targetNpcName].role.roleName))
    selfNPC.journal.append(targetNPC.name + " is a " + gameInfo.npcList[gameInfo.npcList.index(targetNPC)].role.roleName)
