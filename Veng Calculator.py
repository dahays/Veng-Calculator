#  This program calculates the total number of points a player
#  will score in the Vengeance is Mine SMS and SLB events

#  Initialize global constants for scoring

G6_UNCOMMON = 10
G6_RARE = 20
G7_UNCOMMON = 55
G7_RARE = 65
HONORS = 161
SECTION_31 = 424
ARCHIVES = 43
OBSERVATORY = 274
SPIRITS = 566
ATHENA_PARTS = 140
ATHENA_DATA = 415
SPHERE_PARTS = 95
EXCELSIOR_PARTS = 89
EXCELSIOR_RESEARCH = 89
DAUNTLESS_PARTS = 68
DAUNTLESS_DATA = 142

def main():
    print(f"Welcome to the Vengeance is Mine SMS and SLB calculator.\nEnter values for the following:")
    g7_uncommon_gas = int(input("G7 Uncommon Gas: "))
    g7_rare_gas = int(input("G7 Rare Gas: "))
    g7_uncommon_ore = int(input("G7 Uncommon Ore: "))
    g7_rare_ore = int(input("G7 Rare Ore: "))
    g7_uncommon_crystal = int(input("G7 Uncommon Crystal: "))
    g7_rare_crystal = int(input("G7 Rare Crystal: "))
    
    g7_uncommon_total = g7_uncommon_gas + g7_uncommon_ore + g7_uncommon_crystal
    g7_rare_total = g7_rare_gas + g7_rare_ore + g7_rare_crystal
    
    g6_uncommon_gas = int(input("G6 Uncommon Gas: "))
    g6_rare_gas = int(input("G6 Rare Gas: "))
    g6_uncommon_ore = int(input("G6 Uncommon Ore: "))
    g6_rare_ore = int(input("G6 Rare Ore: "))
    g6_uncommon_crystal = int(input("G6 Uncommon Crystal: "))
    g6_rare_crystal = int(input("G6 Rare Crystal: "))
    
    g6_uncommon_total = g6_uncommon_gas + g6_uncommon_ore + g6_uncommon_crystal
    g6_rare_total = g6_rare_gas + g6_rare_ore + g6_rare_crystal
    
    honors = int(input("Class Honors: "))
    section_31 = int(input("Enhanced Section 31 Transmitters: "))
    archives = int(input("Enhanced Independent Archives Schematics: "))
    observatory = int(input("Signal Observatory Schematics: "))
    spirits = int(input("Exotic Spirits Shipment: "))
    
    athena_parts = int(input("Athena Parts: "))
    athena_data = int(input("Athena Data Modules: "))
    sphere_parts = int(input("Borg Sphere Parts: "))
    excelsior_parts = int(input("U.S.S. Excelsior Parts: "))
    excelsior_research = int(input("U.S.S. Excelsior Research: "))
    dauntless_parts = int(input("U.S.S. Dauntless Parts: "))
    dauntless_data = int(input("U.S.S. Dauntless Prototype Data: "))
    
    total_G7_points = g7(g7_uncommon_total, g7_rare_total)
    total_G6_points = g6(g6_uncommon_total, g7_rare_total)
    total_building_points = buildings(honors, section_31, archives, observatory, spirits)
    total_ship_points = ships(athena_parts, athena_data, sphere_parts, excelsior_parts, excelsior_research, dauntless_parts, dauntless_data)
    
    total = total_G7_points + total_G6_points + total_building_points + total_ship_points
    
    # output results
    print("\n\nHere are your results: ")
    print(f"Total points from spending G7: {total_G7_points}")
    print(f"Total points from spending G6: {total_G6_points}")
    print(f"Total points from special buildings components: {total_building_points}")
    print(f"Total points from special ship parts: {total_ship_points}")
    
    print(f"\n\nTotal points earned: {total}")
    
def g7(unc, rar):
    uncommon = unc * G7_UNCOMMON
    rare = rar * G7_RARE
    return uncommon + rare

def g6(unc, rar):
    uncommon = unc * G6_UNCOMMON
    rare = rar * G6_RARE
    return uncommon + rare

def buildings(honors, sec31, archives, observatory, spirits):
    honors_points = honors * HONORS
    sec31_points = sec31 * SECTION_31
    archive_points = archives * ARCHIVES
    observatory_points = observatory * OBSERVATORY
    spirits_points = spirits * SPIRITS
    return honors_points + sec31_points + archive_points + observatory_points + spirits_points

def ships(athenaParts, athenaResearch, sphereParts, excelsiorParts, excelsiorResearch, dauntlessParts, dauntlessResearch):
    athena_points = (athenaParts * ATHENA_PARTS) + (athenaResearch * ATHENA_DATA)
    sphere_points = sphereParts * SPHERE_PARTS
    excelsior_points = (excelsiorParts * EXCELSIOR_PARTS) + (excelsiorResearch * EXCELSIOR_RESEARCH)
    dauntless_points = (dauntlessParts * DAUNTLESS_PARTS) + (dauntlessResearch * DAUNTLESS_DATA)
    return athena_points + sphere_points + excelsior_points + dauntless_points

main()