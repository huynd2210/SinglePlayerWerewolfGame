from typing import List

from src.NPC import NPC
from src.Player import Player


class GameInfo:
    def __init__(self, player: Player, npcList: List[NPC]):
        self.player = player
        self.npcList = npcList
        #Each turn consists of a day and a night
        self.currentTurn = 0
        #There are currently 2 types of nights: Normal and Full Moon
        self.currentNightType = "Normal"

    #refactor: remove this, replace with a class that has a list of util related functions
    def findNpcByPredicate(self, predicate, **kwargs):
        for npc in self.npcList:
            if predicate(npc, kwargs):
                return npc
        return None

    def findNpcByName(self, targetNpcName):
        npc = [npc for npc in self.npcList if npc.name == targetNpcName]

        if len(npc) > 1:
            raise Exception("There is more than one NPC with the name " + targetNpcName)

        return npc[0] if len(npc) > 0 else []

    def __repr__(self):
        return str(self.player) + "\n" + str(self.npcList)

    def __str__(self):
        return str(self.player) + "\n" + str(self.npcList)