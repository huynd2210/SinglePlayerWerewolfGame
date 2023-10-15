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

    def findNpcByPredicate(self, predicate, **kwargs):
        for npc in self.npcList:
            if predicate(npc, kwargs):
                return npc

    def __repr__(self):
        return str(self.player) + "\n" + str(self.npcList)

    def __str__(self):
        return str(self.player) + "\n" + str(self.npcList)