from src.Role import Role

villager = Role("villager", "commoner", "good")
seer = Role("seer", "commoner", "good")
werewolf = Role("werewolf", "werebeast", "evil")
doctor = Role("doctor", "commoner", "good")

roleMap = {
    "villager": villager,
    "seer": seer,
    "werewolf": werewolf,
    "doctor": doctor,
}