import random

from src.Common import Utility
from src.NPC import NPC
from src.Npc import Faction

def isThisNpcAllowedToAct(gameInfo, selfNPC: NPC, possibleTargets):
    if len(possibleTargets) == 0:
        Utility.logDebug("Werewolf: No possible targets")
        return False

    if selfNPC.isBeingSuppressed:
        Utility.logDebug("Werewolf: NPC is being suppressed")
        return False

    #if not full moon, werewolf does nothing
    if gameInfo.currentNightType != "full moon":
        Utility.logDebug("Werewolf: Night is not full moon")
        return False

    return True

def werewolfActionWrapper(gameInfo, selfNPC: NPC):

    possibleTargets = werewolfPossibleTarget(gameInfo, selfNPC)

    if not isThisNpcAllowedToAct(gameInfo, selfNPC, possibleTargets):
        return

    chosenTarget = random.choice(list(filter(lambda npc: npc != selfNPC, possibleTargets)))
    werewolfActionFunction(gameInfo, chosenTarget)

def werewolfPossibleTarget(gameInfo, selfNPC: NPC):
    return [npc for npc in gameInfo.npcList if npc.isAlive and npc != selfNPC and npc.role.faction != Faction.beast]

def werewolfActionFunction(gameInfo, targetNpc: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    Utility.logDebug("Werewolf: Visiting " + targetNpc.name + " the " + targetNpc.role.roleName)

    gameInfo.npcList[gameInfo.npcList.index(targetNpc)].isBeingKilled = True