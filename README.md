# Veng Calculator

A Python calculator for **Star Trek Fleet Command's "Vengeance is Mine" SMS/SLB events**.

This tool helps players determine:

* How many event points they can earn from their available resources.
* Whether they can reach the **Tier 1 milestone (1,520,000 points)**.
* Whether they can continue on to the **Tier 2 milestone (3,050,000 points)**.
* The **minimum number of resources** required to reach each milestone.
* Which resources should be spent first to maximize efficiency.
* What inventory remains after reaching each milestone.

The calculator uses a priority-based spending strategy that consumes the highest-value resources first, minimizing the total number of resources spent.

---

# Features

## Point Calculation

Calculates points from:

### G7 Resources

* Uncommon Gas
* Rare Gas
* Uncommon Ore
* Rare Ore
* Uncommon Crystal
* Rare Crystal

### G6 Resources

* Uncommon Gas
* Rare Gas
* Uncommon Ore
* Rare Ore
* Uncommon Crystal
* Rare Crystal

### Buildings

* Class Honors
* Enhanced Section 31 Transmitters
* Enhanced Independent Archives Schematics
* Signal Observatory Schematics
* Exotic Spirits Shipment

### Ships

* Athena Parts
* Athena Data Modules
* Borg Sphere Parts
* U.S.S. Excelsior Parts
* U.S.S. Excelsior Research
* U.S.S. Dauntless Parts
* U.S.S. Dauntless Prototype Data

---

# SMS Milestone Analysis

The calculator performs a sequential analysis:

## Tier 1 Analysis

Determines:

* Can Tier 1 be reached?
* Which resources should be spent?
* How many resources are required?
* How many points are earned?
* How many points are wasted (overshoot)?

## Tier 2 Continuation Analysis

After Tier 1 spending is applied:

* Remaining inventory is calculated.
* The calculator determines whether Tier 2 can be reached using only the remaining inventory.
* Provides a recommended spending plan.

This mirrors how most players actually progress through the event.

---

# Requirements

Python 3.10 or newer is recommended.

The script uses only the Python standard library.

No additional packages are required.

---

# Installing Python

If you already have Python installed, skip to the next section.

## Windows

1. Visit:

https://www.python.org/downloads/

2. Download the latest version of Python.

3. Run the installer.

4. **IMPORTANT:** Check the box:

```text
Add Python to PATH
```

before clicking Install.

5. Finish installation.

---

# Verify Python Installation

Open:

```text
Command Prompt
```

and type:

```bash
python --version
```

You should see something similar to:

```text
Python 3.13.0
```

If you receive an error, reinstall Python and ensure "Add Python to PATH" is checked.

---

# Downloading the Calculator

## Option 1: Download ZIP

1. Open the repository:

https://github.com/dahays/Veng-Calculator

2. Click:

```text
Code
```

3. Click:

```text
Download ZIP
```

4. Extract the ZIP file.

---

## Option 2: Clone with Git

If Git is installed:

```bash
git clone https://github.com/dahays/Veng-Calculator.git
```

Move into the folder:

```bash
cd Veng-Calculator
```

---

# Running the Calculator

Open Command Prompt.

Navigate to the folder containing the script.

Example:

```bash
cd Downloads\Veng-Calculator
```

Run the script:

```bash
python veng_calculator.py
```

Replace the filename with the actual script name if different.

---

# Example

```text
G7 Uncommon Gas: 1000
G7 Rare Gas: 500

G7 Uncommon Ore: 1000
G7 Rare Ore: 500

...

Exotic Spirits Shipment: 500
```

After entering all values, the calculator displays:

```text
======================================================================
POINT SUMMARY
======================================================================

G7 Points        : 215,000
G6 Points        : 48,000
Building Points  : 1,125,000
Ship Points      : 900,000

Total SMS Points Available: 2,288,000
```

---

# Example Tier Analysis

```text
======================================================================
TIER 1 (1,520,000)
======================================================================

ACHIEVABLE

Spend:

Exotic Spirits                 2,100
Section 31                       785
Athena Data                      120

Summary

Resources Used : 3,005
Points Earned  : 1,520,321
Overshoot      : 321
```

---

# Input Validation

The calculator validates all inputs.

Accepted:

```text
0
10
2500
999999
```

Rejected:

```text
abc
12.5
-100
one thousand
```

If invalid data is entered, the calculator will continue prompting until a valid number is provided.

---

# Spending Strategy

The calculator is optimized to use the minimum number of resources possible to reach T1 and/or T2.

Resources are spent in descending point value order.

Current priority:

| Resource           | Points |
| ------------------ | -----: |
| Exotic Spirits     |    566 |
| Section 31         |    424 |
| Athena Data        |    415 |
| Observatory        |    274 |
| Class Honors       |    161 |
| Dauntless Data     |    142 |
| Athena Parts       |    140 |
| Sphere Parts       |     95 |
| Excelsior Parts    |     89 |
| Excelsior Research |     89 |
| Dauntless Parts    |     68 |
| G7 Rare            |     65 |
| G7 Uncommon        |     55 |
| Archives           |     43 |
| G6 Rare            |     20 |
| G6 Uncommon        |     10 |

This approach minimizes the total number of resources consumed.

---

# Known Limitation

The calculator intentionally uses a greedy priority strategy.

It does **not** attempt to find the mathematically perfect combination that minimizes overspend.

Instead it focuses on:

* Fast execution
* Simplicity
* Resource conservation
* Practical event planning

For most STFC inventories, this produces results that closely match optimal play.


---

# Disclaimer

Star Trek Fleet Command and all associated assets are property of their respective owners.

This project is a fan-created utility and is not affiliated with or endorsed by Scopely.

This project was created with G7 being inaccessible but G7 spending SHOULD be accurate.
