# Vengeance is Mine SMS and SLB Calculator
# Sequential Tier Analysis
# Goal: Use the minimum number of resources possible to reach
# Tier 1 (1.52M) and then continue to Tier 2 (3.05M)

# ============================================================
# Named constants for points
# ============================================================

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

TIER1 = 1_520_000
TIER2 = 3_050_000
TIER2_ADDITIONAL = TIER2 - TIER1

# ============================================================
# Input Validation
# ============================================================

def get_int(prompt):
    """Get a validated non-negative integer."""

    while True:

        try:

            value = int(input(prompt))

            if value < 0:
                print("Please enter a value greater than or equal to 0.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")

        except KeyboardInterrupt:
            print("\nProgram cancelled.")
            raise SystemExit

# ============================================================
# Point Calulations
# ============================================================

def g7(uncommon, rare):
    return (uncommon * G7_UNCOMMON) + (rare * G7_RARE)


def g6(uncommon, rare):
    return (uncommon * G6_UNCOMMON) + (rare * G6_RARE)


def buildings(honors, sec31, archives, observatory, spirits):

    return (
        honors * HONORS
        + sec31 * SECTION_31
        + archives * ARCHIVES
        + observatory * OBSERVATORY
        + spirits * SPIRITS
    )


def ships(
    athena_parts,
    athena_data,
    sphere_parts,
    excelsior_parts,
    excelsior_research,
    dauntless_parts,
    dauntless_data
):

    return (
        athena_parts * ATHENA_PARTS
        + athena_data * ATHENA_DATA
        + sphere_parts * SPHERE_PARTS
        + excelsior_parts * EXCELSIOR_PARTS
        + excelsior_research * EXCELSIOR_RESEARCH
        + dauntless_parts * DAUNTLESS_PARTS
        + dauntless_data * DAUNTLESS_DATA
    )

# ============================================================
# SMS priority order
# Highest point value first
# ============================================================

PRIORITY = [
    ("Exotic Spirits", SPIRITS),
    ("Section 31", SECTION_31),
    ("Athena Data", ATHENA_DATA),
    ("Observatory", OBSERVATORY),
    ("Class Honors", HONORS),
    ("Dauntless Data", DAUNTLESS_DATA),
    ("Athena Parts", ATHENA_PARTS),
    ("Sphere Parts", SPHERE_PARTS),
    ("Excelsior Parts", EXCELSIOR_PARTS),
    ("Excelsior Research", EXCELSIOR_RESEARCH),
    ("Dauntless Parts", DAUNTLESS_PARTS),
    ("G7 Rare", G7_RARE),
    ("G7 Uncommon", G7_UNCOMMON),
    ("Archives", ARCHIVES),
    ("G6 Rare", G6_RARE),
    ("G6 Uncommon", G6_UNCOMMON)
]

# ============================================================
# SMS Spending Engine
# ============================================================

def spend_for_target(target, inventory):
    """
    Spend the minimum number of resources possible
    by consuming highest point-value resources first.
    """

    plan = {}

    resources_used = 0
    points_earned = 0

    for item_name, point_value in PRIORITY:

        qty_available = inventory[item_name]

        if qty_available <= 0:
            continue

        remaining_needed = target - points_earned

        if remaining_needed <= 0:
            break

        qty_needed = remaining_needed // point_value

        if remaining_needed % point_value:
            qty_needed += 1

        qty_to_spend = min(qty_available, qty_needed)

        if qty_to_spend > 0:

            plan[item_name] = qty_to_spend

            inventory[item_name] -= qty_to_spend

            earned = qty_to_spend * point_value

            points_earned += earned
            resources_used += qty_to_spend

    achieved = points_earned >= target

    return {
        "achieved": achieved,
        "plan": plan,
        "resources_used": resources_used,
        "points_earned": points_earned,
        "overshoot": max(0, points_earned - target)
    }

# ============================================================
# Display functions
# ============================================================

def print_spending_result(title, target, result):

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    if not result["achieved"]:

        print("NOT ACHIEVABLE")
        return

    print("ACHIEVABLE")

    print("\nSpend:")

    for item, qty in result["plan"].items():

        print(f"  {item:<25} {qty:>12,}")

    print("\nSummary")
    print(f"  Resources Used : {result['resources_used']:,}")
    print(f"  Points Earned  : {result['points_earned']:,}")
    print(f"  Overshoot      : {result['overshoot']:,}")


def print_remaining_inventory(inventory):

    print("\n" + "=" * 70)
    print("REMAINING INVENTORY")
    print("=" * 70)

    for item, qty in inventory.items():

        if qty > 0:

            print(f"{item:<25} {qty:>12,}")


def total_available_points(inventory):

    points_lookup = dict(PRIORITY)

    total = 0

    for item, qty in inventory.items():

        total += qty * points_lookup[item]

    return total

# ============================================================
# MAIN
# ============================================================

def main():

    try:

        print(
            "Vengeance is Mine SMS / SLB Calculator\n"
            "Enter your available inventory amounts.\n"
        )

        # -------------------------
        # G7
        # -------------------------

        g7_uncommon_gas = get_int("G7 Uncommon Gas: ")
        g7_rare_gas = get_int("G7 Rare Gas: ")

        g7_uncommon_ore = get_int("G7 Uncommon Ore: ")
        g7_rare_ore = get_int("G7 Rare Ore: ")

        g7_uncommon_crystal = get_int("G7 Uncommon Crystal: ")
        g7_rare_crystal = get_int("G7 Rare Crystal: ")

        g7_uncommon_total = (
            g7_uncommon_gas +
            g7_uncommon_ore +
            g7_uncommon_crystal
        )

        g7_rare_total = (
            g7_rare_gas +
            g7_rare_ore +
            g7_rare_crystal
        )

        # -------------------------
        # G6
        # -------------------------

        g6_uncommon_gas = get_int("G6 Uncommon Gas: ")
        g6_rare_gas = get_int("G6 Rare Gas: ")

        g6_uncommon_ore = get_int("G6 Uncommon Ore: ")
        g6_rare_ore = get_int("G6 Rare Ore: ")

        g6_uncommon_crystal = get_int("G6 Uncommon Crystal: ")
        g6_rare_crystal = get_int("G6 Rare Crystal: ")

        g6_uncommon_total = (
            g6_uncommon_gas +
            g6_uncommon_ore +
            g6_uncommon_crystal
        )

        g6_rare_total = (
            g6_rare_gas +
            g6_rare_ore +
            g6_rare_crystal
        )

        # -------------------------
        # Buildings
        # -------------------------

        honors = get_int("Class Honors: ")
        section_31 = get_int("Enhanced Section 31 Transmitters: ")
        archives = get_int("Enhanced Independent Archives Schematics: ")
        observatory = get_int("Signal Observatory Schematics: ")
        spirits = get_int("Exotic Spirits Shipment: ")

        # -------------------------
        # Ships
        # -------------------------

        athena_parts = get_int("Athena Parts: ")
        athena_data = get_int("Athena Data Modules: ")

        sphere_parts = get_int("Borg Sphere Parts: ")

        excelsior_parts = get_int("U.S.S. Excelsior Parts: ")
        excelsior_research = get_int("U.S.S. Excelsior Research: ")

        dauntless_parts = get_int("U.S.S. Dauntless Parts: ")
        dauntless_data = get_int("U.S.S. Dauntless Prototype Data: ")

        # ====================================================
        # Summary
        # ====================================================

        total_g7_points = g7(
            g7_uncommon_total,
            g7_rare_total
        )

        total_g6_points = g6(
            g6_uncommon_total,
            g6_rare_total
        )

        total_building_points = buildings(
            honors,
            section_31,
            archives,
            observatory,
            spirits
        )

        total_ship_points = ships(
            athena_parts,
            athena_data,
            sphere_parts,
            excelsior_parts,
            excelsior_research,
            dauntless_parts,
            dauntless_data
        )

        total_points = (
            total_g7_points +
            total_g6_points +
            total_building_points +
            total_ship_points
        )

        # ====================================================
        # Inventory
        # ====================================================

        inventory = {
            "Exotic Spirits": spirits,
            "Section 31": section_31,
            "Athena Data": athena_data,
            "Observatory": observatory,
            "Class Honors": honors,
            "Dauntless Data": dauntless_data,
            "Athena Parts": athena_parts,
            "Sphere Parts": sphere_parts,
            "Excelsior Parts": excelsior_parts,
            "Excelsior Research": excelsior_research,
            "Dauntless Parts": dauntless_parts,
            "G7 Rare": g7_rare_total,
            "G7 Uncommon": g7_uncommon_total,
            "Archives": archives,
            "G6 Rare": g6_rare_total,
            "G6 Uncommon": g6_uncommon_total
        }

        available_sms_points = total_available_points(inventory)

        # ====================================================
        # Summary
        # ====================================================

        print("\n" + "=" * 70)
        print("POINT SUMMARY")
        print("=" * 70)

        print(f"G7 Points        : {total_g7_points:,}")
        print(f"G6 Points        : {total_g6_points:,}")
        print(f"Building Points  : {total_building_points:,}")
        print(f"Ship Points      : {total_ship_points:,}")

        print(f"\nTotal SMS Points Available: {available_sms_points:,}")
        print(f"Total Points Available    : {total_points:,}")

        # ====================================================
        # T1 - 1.52M points
        # ====================================================

        tier1_result = spend_for_target(
            TIER1,
            inventory
        )

        print_spending_result(
            f"TIER 1 ({TIER1:,})",
            TIER1,
            tier1_result
        )

        if not tier1_result["achieved"]:

            print_remaining_inventory(inventory)
            return

        # ====================================================
        # T2 - 3.05M points
        # ====================================================

        tier2_result = spend_for_target(
            TIER2_ADDITIONAL,
            inventory
        )

        print_spending_result(
            f"TIER 2 CONTINUATION (+{TIER2_ADDITIONAL:,})",
            TIER2_ADDITIONAL,
            tier2_result
        )

        # ====================================================
        # Event Summary
        # ====================================================

        print("\n" + "=" * 70)
        print("EVENT SUMMARY")
        print("=" * 70)

        total_resources = (
            tier1_result["resources_used"] +
            tier2_result["resources_used"]
        )

        total_event_points = (
            tier1_result["points_earned"] +
            tier2_result["points_earned"]
        )

        total_overshoot = (
            tier1_result["overshoot"] +
            tier2_result["overshoot"]
        )

        print(f"Tier 1 Achieved : {tier1_result['achieved']}")
        print(f"Tier 2 Achieved : {tier2_result['achieved']}")

        print(f"\nTotal Resources Used : {total_resources:,}")
        print(f"Total Points Earned  : {total_event_points:,}")
        print(f"Total Overshoot      : {total_overshoot:,}")

        print_remaining_inventory(inventory)

    except Exception as error:

        print(f"\nUnexpected error: {error}")

#  main guard
if __name__ == "__main__":
    main()