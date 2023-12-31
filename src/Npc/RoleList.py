from src.Npc import Alignment, Faction
from src.Npc.Role import Role

#Reminder: To add a new role, add init the role here and add to roleMap, then create a new file and implement the necessaru function in NpcActions, add act Frequncy to GameConfig
# add resolve visiting, modify initmap, then finally add the function to the roleActionMap

villager = Role("villager", Faction.commoner, Alignment.good)
seer = Role("seer", Faction.commoner, Alignment.good)
werewolf = Role("werewolf", Faction.beast, Alignment.evil, canKill=True)
doctor = Role("doctor", Faction.commoner, Alignment.good)
guard = Role("guard", Faction.commoner, Alignment.good, canKill=True)
trapper = Role("trapper", Faction.criminal, Alignment.evil)
deceiver = Role("deceiver", Faction.criminal, Alignment.evil)
cleaner = Role("cleaner", Faction.criminal, Alignment.evil)
serialKiller = Role("serial killer", Faction.criminal, Alignment.evil, canKill=True)

ambusher = Role("ambusher", Faction.criminal, Alignment.evil, actionPriority=1, canKill=True)
terrorist = Role("terrorist", Faction.criminal, Alignment.evil, canKill=True)

roleMap = {
    "villager": villager,
    "seer": seer,
    "werewolf": werewolf,
    "doctor": doctor,
    "trapper": trapper,
    "deceiver": deceiver,
    "cleaner": cleaner,
    "serial killer": serialKiller,
    "guard": guard,
    "ambusher": ambusher,
    "terrorist": terrorist
}