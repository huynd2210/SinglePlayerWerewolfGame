import random

from src.Common import Utility
from src.NPC import NPC

def isThisNpcAllowedToAct(gameInfo, selfNPC: NPC, possibleTargets):
    if len(possibleTargets) == 0:
        Utility.logDebug("Seer: No possible targets")
        return False

    if selfNPC.isBeingSuppressed:
        Utility.logDebug("Seer: NPC is being suppressed")
        return False

    return True
def seerActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = seerPossibleTarget(gameInfo, selfNPC)
    chosenTarget = random.choice(list(filter(lambda npc: npc != selfNPC, possibleTargets)))

    if not isThisNpcAllowedToAct(gameInfo, selfNPC, possibleTargets):
        return

    seerActionFunction(gameInfo, chosenTarget, selfNPC)
def seerPossibleTarget(gameInfo, selfNPC: NPC):
    # return [gameInfo.npcList[npc].name for npc in range(len(gameInfo.npcList)) if gameInfo.npcList[npc].isAlive]
    return [npc for npc in gameInfo.npcList if npc.isAlive and npc != selfNPC]

def seerActionFunction(gameInfo, targetNPC: NPC, selfNPC: NPC):
    if targetNPC not in gameInfo.npcList:
        raise Exception(targetNPC.name + " not found.")

    Utility.logDebug("Seer: Visiting " + targetNPC.name + " the " + targetNPC.role.roleName)

    # selfNPC.journal.append((targetNpcName, gameInfo.npcList[targetNpcName].role.roleName))
    selfNPC.journal.append(targetNPC.name + " is a " + gameInfo.npcList[gameInfo.npcList.index(targetNPC)].role.roleName)
