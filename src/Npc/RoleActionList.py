from src.NPC import NPC
import random

from src.Npc import Faction, Alignment
from src.Npc.CleanerAction import cleanerActionWrapper
from src.Npc.DoctorAction import doctorActionWrapper
from src.Npc.SeerAction import seerActionWrapper
from src.Npc.WerewolfAction import werewolfActionWrapper


#Villagers do nothing
def villagerActionFunction(gameInfo, selfNPC:NPC):
    pass

def trapperActionFunction(gameInfo, targetNPC: NPC, selfNPC: NPC):
    pass

def deceiverActionFunction(gameInfo, targetNPC: NPC, selfNPC: NPC):
    pass



roleActionMap = {
    "seer": seerActionWrapper,
    "werewolf": werewolfActionWrapper,
    "doctor": doctorActionWrapper,
    "villager": villagerActionFunction,
    "trapper": trapperActionFunction,
    "deceiver": deceiverActionFunction,
    "cleaner": cleanerActionWrapper,
}
