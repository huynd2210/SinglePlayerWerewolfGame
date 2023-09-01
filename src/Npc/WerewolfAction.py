import random
from src.NPC import NPC
from src.Npc import Faction


def werewolfActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = werewolfPossibleTarget(gameInfo, selfNPC)
    chosenTarget = random.choice(list(filter(lambda npc: npc != selfNPC, possibleTargets)))
    werewolfActionFunction(gameInfo, chosenTarget)

def werewolfPossibleTarget(gameInfo, selfNPC: NPC):
    return [npc for npc in gameInfo.npcList if npc.isAlive and npc != selfNPC and npc.role.faction != Faction.beast]

def werewolfActionFunction(gameInfo, targetNpc: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    #if not full moon, werewolf does nothing
    if gameInfo.currentNightType == "full moon":
        gameInfo.npcList[gameInfo.npcList.index(targetNpc)].isBeingKilled = True