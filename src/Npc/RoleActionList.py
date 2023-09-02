from src.NPC import NPC

from src.Npc.NpcActions.CleanerAction import cleanerActionWrapper
from src.Npc.NpcActions.DoctorAction import doctorActionWrapper
from src.Npc.NpcActions.SeerAction import seerActionWrapper
from src.Npc.NpcActions.TrapperAction import trapperActionWrapper
from src.Npc.NpcActions.WerewolfAction import werewolfActionWrapper


#Villagers do nothing
def villagerActionFunction(gameInfo, selfNPC:NPC):
    pass

roleActionMap = {
    "seer": seerActionWrapper,
    "werewolf": werewolfActionWrapper,
    "doctor": doctorActionWrapper,
    "villager": villagerActionFunction,
    "trapper": trapperActionWrapper,
    # "deceiver": deceiverActionFunction,
    "cleaner": cleanerActionWrapper,
    # "serialKiller": serialKillerActionWrapper,
}
