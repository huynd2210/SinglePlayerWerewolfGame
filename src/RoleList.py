from src.Role import Role

villager = Role("villager", "commoner", "good")
seer = Role("seer", "commoner", "good")
werewolf = Role("werewolf", "werebeast", "evil")
doctor = Role("doctor", "commoner", "good")
trapper = Role("trapper", "criminal", "evil")
deceiver = Role("deceiver", "criminal", "evil")
cleaner = Role("cleaner", "criminal", "evil")

roleMap = {
    "villager": villager,
    "seer": seer,
    "werewolf": werewolf,
    "doctor": doctor,
    "trapper": trapper,
    "deceiver": deceiver,
    "cleaner": cleaner,
}