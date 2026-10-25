sanat = ["omena", "banaani", "koira", "tietokone", "auto", "appelsiini"]

maara = 0

for sana in sanat:
    if len(sana) > 5:
        maara = maara + 1

print("Yli viisi kirjainta sisältäviä sanoja:", maara)