import random

from src.NPC import NPC


def trapperPossibleTarget(gameInfo):
    return [npc for npc in gameInfo.npcList if npc.isAlive]

def trapperActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = trapperPossibleTarget(gameInfo)
    chosenTarget = random.choice(list(filter(lambda npc: npc != selfNPC, possibleTargets)))
    trapperActionFunction(gameInfo, chosenTarget, selfNPC)

def trapperActionFunction(gameInfo, targetNpc: NPC, selfNPC: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    targetNpc.isBeingTrapped = True
    selfNPC.isAtHome = False
