import random
encounters = {
    1: "Collapsed Building (DIA, p. 55)",
    2: "Cry for Help (DIA, p. 55)",
    3: "Ghastly Meal (DIA, p. 55)",
    4: "Ghoul Pack (DIA, p. 55)",
    5: "Hateful Patrol (DIA, p. 55)",
    6: "Imp Sales Pitch (DIA, p. 55)",
    7: "Narzugon Cavalier (DIA, p. 56)",
    8: "Spouts of Hellfire (DIA, p. 56)",
    9: "Vrock Philosophy (DIA, p. 56)",
    10: "Zombie Horde (DIA, p. 56)",
    11: "A River Ran Through It (EIA, p. 16)",
    12: "Abandoned Trunk (EIA, p. 17)",
    13: "Alchemist Shop (EIA, p. 17)",
    14: "Fiendish Trap (EIA, p. 17)",
    15: "Forbidden Delights (EIA, p. 17)",
    16: "Hellrider Uprising (EIA, p. 18)",
    17: "Injured Knight (EIA, p. 18)",
    18: "Keeper of the Keys (EIA, p. 18)",
    19: "Kid Warlock (EIA, p. 19)",
    20: "Mad Cultists (EIA, p. 19)",
    21: "Nasty Weather (EIA, p. 19)",
    22: "Nycaloth Thugs (EIA, p. 20)",
    23: "Obsesssed Avenger (EIA, p. 20)",
    24: "Priestess of Lathander (EIA, p. 20)",
    25: "Rakshasa Hustler (EIA, p. 20)",
    26: "Skeleton Bonfire (EIA, p. 20)",
    27: "Necromantic Mist",
    28: "Encounter with a Faction",
    29: "Encounter with a Faction",
    30: "Roll Again Twice & Combine"
}
businesses = {
    "No Businesses": range(1, 21),
    "Baker": range(21, 26),
    "Tavern/Inn": range(26, 31),
    "Butcher": range(31, 36),
    "Market": range(36, 40),
    "Blacksmith": range(40, 44),
    "Cartwright": range(44, 48),
    "Public Bath": range(48, 50),
    "Weaver": range(50, 53),
    "Cobbler": range(53, 56),
    "Dyer": range(56, 59),
    "Fishmonger": range(59, 62),
    "Potter": range(62, 65),
    "Rope/Net-Maker": range(65, 68),
    "Stable": range(68, 71),
    "Stonecutter": range(71, 73),
    "Miller": range(73, 75),
    "Chiurgeon": range(75, 77),
    "Bowyer/Fletcher": range(77, 79),
    "Tannery": range(79, 81),
    "Scribe/Notary": range(81, 83),
    "Carpenter": range(83, 85),
    "Glassblower": range(85, 87),
    "Tinker": range(87, 89),
    "Scholarium": range(89, 90),
    "Alchemist": range(90, 91),
    "Theater": range(91, 92),
    "Painter/Sculptor": range(92, 93),
    "Goldsmith/Silversmith": range(93, 94),
    "Jeweler": range(94, 95),
    "Spice Merchant": range(95, 96),
    "Cartographer": range(96, 97),
    "Perfumer": range(97, 98),
    "Religious Chapel": range(98, 99),
    "Distiller": range(99, 100),
    "Moneylender": range(100, 101)
}
extent_of_damage = {
    "Specific Business": range(1, 4),
    "A residence on the street": range(4, 6),
    "The entire street": range(6, 7)
}
nodes = int(input("Choose how many nodes/streets:"))
nodes_string = ""
for node in range(1,nodes+1):
    nodes_string += str(node) + ".-----------------------------------"
    encounter_int = random.randint(1,2)
    if encounter_int == 2:
        encounter = random.randint(1,30)
        if encounter == 30:
            encounter = random.randint(1,30)
            encounter_name = encounters[encounter] + "* 2"
        encounter_name = encounters[encounter]
        nodes_string += f"\nEncounter = {encounter_name}\n"
    else:
        nodes_string += f"\nEncounter = No encounter\n"

    businesses_int = random.randint(1, 100)
    for business, ranges in businesses.items():
        if businesses_int in ranges:
            # Add the business encounter to a string
            business_string = "\nBusiness Encounter: " + business + "\n"
            break
    nodes_string += business_string
    damage_int = random.randint(1,8)
    damage_string = ""
    if damage_int != 1:
        extent_int = random.randint(1,6)
        if extent_int == 1:
            damage_string += "\nExtent of Damage: Specific Business\n"
        elif extent_int <= 3:
            damage_string += "\nExtent of Damage: A residence on the street\n"
        else:
            damage_string += "\nExtent of Damage: The entire street\n"
        if damage_int == 5 or damage_int == 6:
            damage_string += "\nBuilding Damage: Fire\n"
        elif damage_int == 7:
            damage_string += "\nBuilding Damage: Looted\n"
        elif damage_int == 8:
            damage_string += "\nBuilding Damage: Boarded Up / Fortified\n"
        else: 
            damage_string += "\nNo damage\n"

    nodes_string += damage_string
print(nodes_string)