import random
from src.NPC import NPC
from src.Npc import Faction

def deceiverActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = deceiverPossibleTarget(gameInfo, selfNPC)
    chosenTarget = random.choice(list(filter(lambda npc: npc != selfNPC, possibleTargets)))
    if selfNPC.isBeingSuppressed:
        return

    deceiverActionFunction(gameInfo, chosenTarget)

def deceiverPossibleTarget(gameInfo, selfNPC: NPC):
    return [npc for npc in gameInfo.npcList if npc.isAlive and npc != selfNPC and npc.role.faction == Faction.criminal]
def deceiverActionFunction(gameInfo, targetNpc: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    gameInfo.npcList[gameInfo.npcList.index(targetNpc)].isBeingCoveredByDeceiver = True
