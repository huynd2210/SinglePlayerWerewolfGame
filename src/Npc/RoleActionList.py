from src.NPC import NPC
from src.Npc.NpcActions.AmbusherAction import ambusherActionWrapper

from src.Npc.NpcActions.CleanerAction import cleanerActionWrapper
from src.Npc.NpcActions.DeceiverAction import deceiverActionWrapper
from src.Npc.NpcActions.DoctorAction import doctorActionWrapper
from src.Npc.NpcActions.GuardAction import guardActionWrapper
from src.Npc.NpcActions.SeerAction import seerActionWrapper
from src.Npc.NpcActions.SerialKillerAction import serialKillerActionWrapper
from src.Npc.NpcActions.TrapperAction import trapperActionWrapper
from src.Npc.NpcActions.WerewolfAction import werewolfActionWrapper


#Villagers do nothing
def villagerActionFunction(gameInfo, selfNPC:NPC):
    pass

def cleanedRoleDebug():
    print("somehow this function gets called")

roleActionMap = {
    "seer": seerActionWrapper,
    "werewolf": werewolfActionWrapper,
    "doctor": doctorActionWrapper,
    "villager": villagerActionFunction,
    "trapper": trapperActionWrapper,
    "deceiver": deceiverActionWrapper,
    "cleaner": cleanerActionWrapper,
    "serial killer": serialKillerActionWrapper,
    "guard": guardActionWrapper,
    "ambusher": ambusherActionWrapper,
    #"terrorist": terroristActionWrapper,
}
