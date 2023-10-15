from src.Npc import Alignment, Faction
from src.Npc.Role import Role

villager = Role("villager", Faction.commoner, Alignment.good)
seer = Role("seer", Faction.commoner, Alignment.good)
werewolf = Role("werewolf", Faction.beast, Alignment.evil, canKill=True)
doctor = Role("doctor", Faction.commoner, Alignment.good)
trapper = Role("trapper", Faction.criminal, Alignment.evil)
deceiver = Role("deceiver", Faction.criminal, Alignment.evil)
cleaner = Role("cleaner", Faction.criminal, Alignment.evil)
serialKiller = Role("serial killer", Faction.criminal, Alignment.evil, canKill=True)

roleMap = {
    "villager": villager,
    "seer": seer,
    "werewolf": werewolf,
    "doctor": doctor,
    "trapper": trapper,
    "deceiver": deceiver,
    "cleaner": cleaner,
    "serial killer": serialKiller,
}