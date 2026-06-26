
"""
Vengeance is Mine Calculator v4
"""
import json

POINTS = {
    "Exotic Spirits":566,"Section 31":424,"Athena Data":415,"Observatory":274,
    "Class Honors":161,"Dauntless Data":142,"Athena Parts":140,"Sphere Parts":95,
    "Excelsior Parts":89,"Excelsior Research":89,"Dauntless Parts":68,
    "G7 Rare":65,"G7 Uncommon":55,"Archives":43,"G6 Rare":20,"G6 Uncommon":10
}

PRIORITY = [
    "Exotic Spirits",
    "Section 31",
    "Athena Data",
    "Observatory",
    "Class Honors",
    "Dauntless Data",
    "Athena Parts",
    "Sphere Parts",
    "Excelsior Parts",
    "Excelsior Research",
    "Dauntless Parts",
    "G7 Rare",
    "G7 Uncommon",
    "Archives",
    "G6 Rare",
    "G6 Uncommon"
]

TIER1 = 1_520_000
TIER2 = 3_050_000
TIER2_ADDITIONAL = TIER2 - TIER1

def create_inventory():
    return {
        "g7":{"Uncommon Gas":0,"Rare Gas":0,"Uncommon Ore":0,"Rare Ore":0,
              "Uncommon Crystal":0,"Rare Crystal":0},
        "g6":{"Uncommon Gas":0,"Rare Gas":0,"Uncommon Ore":0,"Rare Ore":0,
              "Uncommon Crystal":0,"Rare Crystal":0},
        "ships":{"Athena Parts":0,"Athena Data":0,"Sphere Parts":0,
                 "Excelsior Parts":0,"Excelsior Research":0,
                 "Dauntless Parts":0,"Dauntless Data":0},
        "buildings":{"Class Honors":0,"Section 31":0,"Archives":0,
                     "Observatory":0,"Exotic Spirits":0}
    }
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


def print_spending_result(title, result):

    print("\n" + "=" * 65)
    print(title)
    print("=" * 65)

    if not result["achieved"]:

        print("NOT ACHIEVABLE")
        return

    print("ACHIEVABLE\n")

    print(f'{"Resource":<28}{"Qty":>10}{"Points":>15}')
    print("-" * 55)

    for item, qty in result["plan"].items():

        earned = qty * POINTS[item]

        print(
            f"{item:<28}"
            f"{qty:>10,}"
            f"{earned:>15,}"
        )

    print("\nSummary")

    print(
        f"Resources Used : "
        f"{result['resources_used']:,}"
    )

    print(
        f"Points Earned  : "
        f"{result['points_earned']:,}"
    )

    print(
        f"Overshoot      : "
        f"{result['overshoot']:,}"
    )

def enter_category(title,d):
    print(f"\n{title}")
    for k in d:
        print(f"Current {k}: {d[k]:,}")
        d[k]+=get_int("Add amount: ")

def display(inv):
    print("\nCURRENT INVENTORY")
    for cat,data in inv.items():
        print(f"\n{cat.upper()}")
        for k,v in data.items():
            print(f"{k:<22}{v:>10,}")

def save(inv):
    with open("inventory.json","w") as f:
        json.dump(inv,f,indent=2)
    print("Saved.")

def load():
    with open("inventory.json") as f:
        return json.load(f)

def spend_for_target(target, inventory):
    """
    Spend the fewest resources possible by consuming the
    highest-value resources first.

    Parameters
    ----------
    target : int
        Target number of points.

    inventory : dict
        Dictionary containing the available SMS resources.

    Returns
    -------
    dict
        Dictionary describing the spending plan.
    """

    plan = {}

    resources_used = 0
    points_earned = 0

    for item in PRIORITY:

        qty_available = inventory.get(item, 0)

        if qty_available <= 0:
            continue

        point_value = POINTS[item]

        remaining = target - points_earned

        if remaining <= 0:
            break

        qty_needed = remaining // point_value

        if remaining % point_value:
            qty_needed += 1

        qty_to_spend = min(qty_available, qty_needed)

        if qty_to_spend == 0:
            continue

        plan[item] = qty_to_spend

        inventory[item] -= qty_to_spend

        earned = qty_to_spend * point_value

        points_earned += earned
        resources_used += qty_to_spend

    return {
        "achieved": points_earned >= target,
        "plan": plan,
        "resources_used": resources_used,
        "points_earned": points_earned,
        "overshoot": max(0, points_earned - target)
    }

def total_available_points(inventory):
    """
    Calculate the maximum possible SMS points available.
    """

    total = 0

    for item, qty in inventory.items():

        total += qty * POINTS[item]

    return total

def calculate(inv):
    """
    Calculate available points and perform sequential
    Tier 1 -> Tier 2 SMS analysis.
    """

    # -----------------------------
    # Totals
    # -----------------------------

    g7_uncommon = (
        inv["g7"]["Uncommon Gas"] +
        inv["g7"]["Uncommon Ore"] +
        inv["g7"]["Uncommon Crystal"]
    )

    g7_rare = (
        inv["g7"]["Rare Gas"] +
        inv["g7"]["Rare Ore"] +
        inv["g7"]["Rare Crystal"]
    )

    g6_uncommon = (
        inv["g6"]["Uncommon Gas"] +
        inv["g6"]["Uncommon Ore"] +
        inv["g6"]["Uncommon Crystal"]
    )

    g6_rare = (
        inv["g6"]["Rare Gas"] +
        inv["g6"]["Rare Ore"] +
        inv["g6"]["Rare Crystal"]
    )

    g7_points = (
        g7_uncommon * POINTS["G7 Uncommon"] +
        g7_rare * POINTS["G7 Rare"]
    )

    g6_points = (
        g6_uncommon * POINTS["G6 Uncommon"] +
        g6_rare * POINTS["G6 Rare"]
    )

    building_points = sum(
        qty * POINTS[item]
        for item, qty in inv["buildings"].items()
    )

    ship_points = sum(
        qty * POINTS[item]
        for item, qty in inv["ships"].items()
    )

    total_points = (
        g7_points +
        g6_points +
        building_points +
        ship_points
    )

    print("\n" + "=" * 65)
    print("POINT SUMMARY")
    print("=" * 65)

    print(f"G7 Materials         : {g7_points:,}")
    print(f"G6 Materials         : {g6_points:,}")
    print(f"Building Components  : {building_points:,}")
    print(f"Ship Components      : {ship_points:,}")
    print("-" * 65)
    print(f"TOTAL AVAILABLE      : {total_points:,}")

    # -----------------------------
    # SMS Inventory
    # -----------------------------

    sms_inventory = {
        "Exotic Spirits": inv["buildings"]["Exotic Spirits"],
        "Section 31": inv["buildings"]["Section 31"],
        "Athena Data": inv["ships"]["Athena Data"],
        "Observatory": inv["buildings"]["Observatory"],
        "Class Honors": inv["buildings"]["Class Honors"],
        "Dauntless Data": inv["ships"]["Dauntless Data"],
        "Athena Parts": inv["ships"]["Athena Parts"],
        "Sphere Parts": inv["ships"]["Sphere Parts"],
        "Excelsior Parts": inv["ships"]["Excelsior Parts"],
        "Excelsior Research": inv["ships"]["Excelsior Research"],
        "Dauntless Parts": inv["ships"]["Dauntless Parts"],
        "G7 Rare": g7_rare,
        "G7 Uncommon": g7_uncommon,
        "Archives": inv["buildings"]["Archives"],
        "G6 Rare": g6_rare,
        "G6 Uncommon": g6_uncommon
    }

    available_sms = total_available_points(sms_inventory)

    print(f"SMS Available        : {available_sms:,}")

    if available_sms < TIER1:

        print("\nTier 1 NOT Achievable")
        print(f"Short by {TIER1 - available_sms:,} points.")
        return

    tier1 = spend_for_target(TIER1, sms_inventory)

    print_spending_result(f"TIER 1 ({TIER1:,})", tier1)

    if not tier1["achieved"]:
        return

    tier2 = spend_for_target(
        TIER2_ADDITIONAL,
        sms_inventory
    )

    print_spending_result(f"TIER 2 (+{TIER2_ADDITIONAL:,})", tier2)

    print("\n" + "=" * 65)
    print("EVENT SUMMARY")
    print("=" * 65)

    print(f"Tier 1 Achieved : {tier1['achieved']}")
    print(f"Tier 2 Achieved : {tier2['achieved']}")

    print()

    print(
        f"Total Resources Used : "
        f"{tier1['resources_used'] + tier2['resources_used']:,}"
    )

    print(
        f"Total Points Earned  : "
        f"{tier1['points_earned'] + tier2['points_earned']:,}"
    )

    print(
        f"Total Overshoot      : "
        f"{tier1['overshoot'] + tier2['overshoot']:,}"
    )

    #print_remaining_inventory(sms_inventory)
    
def menu():
    print("""
1. Enter G7 Materials
2. Enter G6 Materials
3. Enter Ship Components
4. Enter Building Components
5. Display Current Resources
6. Calculate
7. Reset Resources
8. Save Inventory
9. Load Inventory
0. Exit
""")
    return input("Choice: ")

def main():
    inv=create_inventory()
    while True:
        c=menu()
        if c=="1":
            enter_category("G7",inv["g7"])
        elif c=="2":
            enter_category("G6",inv["g6"])
        elif c=="3":
            enter_category("Ships",inv["ships"])
        elif c=="4":
            enter_category("Buildings",inv["buildings"])
        elif c=="5":
            display(inv)
        elif c=="6":
            calculate(inv)
        elif c=="7":
            inv=create_inventory()
        elif c=="8":
            save(inv)
        elif c=="9":
            inv=load()
        elif c=="0":
            break
        else:
            print("Invalid choice.")
if __name__=="__main__":
    main()
