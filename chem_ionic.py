# chem_ionic.py
# Ionic Equilibrium questions 1 to 56

def get_ionic_equilibrium():
    return {
        "name": "Ionic Equilibrium",
        "questions": [
            {
                "id": "chem-ion-q1",
                "number": "1",
                "question": "Define the following terms:\nI. Lewis’s base\nII. Basic buffer",
                "answer": """**I. Lewis Base:**
A chemical species (neutral molecule or anion) containing at least one unshared lone pair of electrons that it can donate to form a coordinate covalent bond with an electron-deficient species (Lewis acid). Examples: Ammonia ($:\\text{NH}_3$), Water ($:\\text{OH}_2$), Hydroxide ion ($\\text{OH}^-$).

**II. Basic Buffer:**
An aqueous solution consisting of an equimolar mixture of a **weak base** and its **salt with a strong acid**, which resists significant changes in pH upon the addition of small amounts of strong acid or base. Example: A mixture of ammonium hydroxide ($\\text{NH}_4\\text{OH}$) and ammonium chloride ($\\text{NH}_4\\text{Cl}$)."""
            },
            {
                "id": "chem-ion-q2",
                "number": "2",
                "question": "Define the term pH of a solution. Calculate the hydroxyl ion concentration in mole/liter of a solution whose pH is 4.7. also determine the weight of NaOH required to produce these ions in one litre of the solution.",
                "answer": """**Definition of pH:**
The negative logarithm (to the base 10) of the hydrogen ion (or hydronium ion) concentration expressed in moles per liter:
$$\\text{pH} = -\\log_{10}[\\text{H}^+]$$

**Calculation:**
Given: $\\text{pH} = 4.7$.
At $25^\\circ\\text{C}$, $\\text{pH} + \\text{pOH} = 14$.
$$\\text{pOH} = 14 - 4.7 = 9.3$$
$$[\\text{OH}^-] = 10^{-\\text{pOH}} = 10^{-9.3} = 10^{0.7 - 10} = 10^{0.7} \\times 10^{-10} \\approx 5.01 \\times 10^{-10} \\text{ mol/L}$$

**Weight of NaOH required for 1 Liter:**
Molar mass of $\\text{NaOH} = 23 + 16 + 1 = 40 \\text{ g/mol}$.
$$\\text{Mass} = [\\text{OH}^-] \\times \\text{Molar Mass} = (5.01 \\times 10^{-10} \\text{ mol}) \\times 40 \\text{ g/mol} \\approx 2.00 \\times 10^{-8} \\text{ g}$$"""
            },
            {
                "id": "chem-ion-q3",
                "number": "3",
                "question": "Deduce the relation between pH and pOH at 25oC.",
                "answer": """Pure water undergoes self-ionization (auto-protolysis):
$$\\text{H}_2\\text{O} (l) \\rightleftharpoons \\text{H}^+ (aq) + \\text{OH}^- (aq)$$
The ionic product of water ($K_w$) is:
$$K_w = [\\text{H}^+][\\text{OH}^-]$$
At $25^\\circ\\text{C}$ (298 K), experimental measurements show:
$$K_w = 1.0 \\times 10^{-14} \\text{ mol}^2\\text{L}^{-2}$$
$$[\\text{H}^+][\\text{OH}^-] = 1.0 \\times 10^{-14}$$

Taking negative logarithm ($-\\log_{10}$) on both sides:
$$-\\log_{10}([\\text{H}^+][\\text{OH}^-]) = -\\log_{10}(10^{-14})$$
$$(-\\log_{10}[\\text{H}^+]) + (-\\log_{10}[\\text{OH}^-]) = 14$$
By definition, $\\text{pH} = -\\log_{10}[\\text{H}^+]$ and $\\text{pOH} = -\\log_{10}[\\text{OH}^-]$:
$$\\text{pH} + \\text{pOH} = 14$$"""
            },
            {
                "id": "chem-ion-q4",
                "number": "4",
                "question": "The solubility product of AgCl is 1.8 x 10-10. What mass of AgCl will precipitate of 0.2 mole HCL solution is added to the saturated solution of AgCl?",
                "answer": """In pure saturated solution of $\\text{AgCl}$:
$$K_{sp} = [\\text{Ag}^+][\\text{Cl}^-] = s^2 = 1.8 \\times 10^{-10} \\implies s = 1.34 \\times 10^{-5} \\text{ M}$$
When $0.2 \\text{ mol}$ of $\\text{HCl}$ is added to $1 \\text{ L}$ of saturated solution:
$$[\\text{Cl}^-] \\approx 0.2 \\text{ M}$$
New solubility $s'$ of $\\text{Ag}^+$:
$$[\\text{Ag}^+] = \\frac{K_{sp}}{[\\text{Cl}^-]} = \\frac{1.8 \\times 10^{-10}}{0.2} = 9.0 \\times 10^{-10} \\text{ M}$$
Moles of $\\text{Ag}^+$ precipitated per liter:
$$\\Delta n = s - s' = (1.34 \\times 10^{-5}) - (9.0 \\times 10^{-10}) \\approx 1.34 \\times 10^{-5} \\text{ mol}$$
Mass of $\\text{AgCl}$ precipitated (Molar mass $= 143.5 \\text{ g/mol}$):
$$\\text{Mass} = 1.34 \\times 10^{-5} \\times 143.5 \\approx 1.92 \\times 10^{-3} \\text{ g} = 1.92 \\text{ mg}$$"""
            },
            {
                "id": "chem-ion-q5",
                "number": "5",
                "question": "Distinguish between solubility product principle and common ion effect.",
                "answer": """| S.N. | Solubility Product Principle ($K_{sp}$) | Common Ion Effect |
| :--- | :--- | :--- |
| 1. | Applicable specifically to **sparingly soluble salts** in equilibrium with their saturated solutions. | Applicable to **any weak electrolyte** (weak acid, base, or sparingly soluble salt). |
| 2. | Governs the condition of precipitation: precipitation occurs if and only if **Ionic Product ($Q_{sp}$) > Solubility Product ($K_{sp}$)**. | Refers to the **suppression of degree of dissociation** of a weak electrolyte by the addition of a strong electrolyte providing a common ion. |
| 3. | Quantified by equilibrium constant $K_{sp}$, which is constant at a constant temperature. | Consequence of Le Chatelier's principle shifting the equilibrium toward the unionized side. |"""
            },
            {
                "id": "chem-ion-q6",
                "number": "6",
                "question": "How would you apply solubility product principle and common ion effect in salt analysis of group III A metal ions?",
                "answer": """In qualitative salt analysis of Group IIIA cations ($\\text{Fe}^{3+}, \\text{Al}^{3+}, \\text{Cr}^{3+}$), they are precipitated as their hydroxides by adding **$\\text{NH}_4\\text{OH}$ in the presence of excess $\\text{NH}_4\\text{Cl}$**:
1. **Common Ion Effect:** $\\text{NH}_4\\text{Cl}$ is a strong electrolyte that dissociates completely into $\\text{NH}_4^+$ and $\\text{Cl}^-$. The high concentration of $\\text{NH}_4^+$ exerts a common ion effect on the weak base $\\text{NH}_4\\text{OH}$, drastically suppressing its dissociation:
$$\\text{NH}_4\\text{OH} \\rightleftharpoons \\text{NH}_4^+ + \\text{OH}^-$$
2. **Solubility Product Principle:** The suppressed $[\\text{OH}^-]$ is just sufficient to exceed the very low $K_{sp}$ values of Group IIIA hydroxides ($K_{sp} \\sim 10^{-36}$ for $\\text{Fe(OH)}_3$), causing them to precipitate. However, it is not high enough to exceed the larger $K_{sp}$ of subsequent groups (Group IV hydroxides like $\\text{Zn(OH)}_2, \\text{Mn(OH)}_2$), preventing their premature precipitation."""
            },
            {
                "id": "chem-ion-q7",
                "number": "7",
                "question": "Detection of basic radicals by wet ways are common in laboratory experiment of class 12 students. How would you apply common ion effect and solubility product principle in this experiment? The solubility product of AgCl is 1.8 x 10-10. What mass of AgCl (molecular mass = 143.5) will precipitate if 0.2 mol of HCL solution is added to the saturated solution of AgCl.",
                "answer": """**Application in Qualitative Analysis:**
In wet tests, cations are systematically separated into analytical groups based on their selective precipitation:
- *Group II (Sulphides in dil. HCl):* $\\text{H}^+$ from $\\text{HCl}$ suppresses $\\text{H}_2\\text{S}$ ionization via common ion effect, allowing only low-$K_{sp}$ Group II cations ($\text{Cu}^{2+}, \text{Pb}^{2+}$) to precipitate as sulphides.
- *Group III (Hydroxides in $\\text{NH}_4\\text{Cl} + \\text{NH}_4\\text{OH}$):* $\\text{NH}_4^+$ suppresses $[\\text{OH}^-]$ to precipitate only Group III ($\text{Fe}^{3+}, \text{Al}^{3+}$).

**Numerical Problem:**
- Initial solubility $s = \\sqrt{1.8 \\times 10^{-10}} = 1.34 \\times 10^{-5} \\text{ M}$.
- In $0.2 \\text{ M } \\text{HCl}$, $[\\text{Cl}^-] = 0.2 \\text{ M}$.
- Residual $[\\text{Ag}^+] = \\frac{1.8 \\times 10^{-10}}{0.2} = 9.0 \\times 10^{-10} \\text{ M}$.
- Moles precipitated per liter $= 1.34 \\times 10^{-5} - 9.0 \\times 10^{-10} \\approx 1.34 \\times 10^{-5} \\text{ mol}$.
- Mass precipitated $= 1.34 \\times 10^{-5} \\text{ mol} \\times 143.5 \\text{ g/mol} \\approx \\mathbf{1.92 \\times 10^{-3} \\text{ g}}$ (or $1.92 \\text{ mg}$)."""
            },
            {
                "id": "chem-ion-q8",
                "number": "8",
                "question": "Give proper reason.\nI. NH3 acts as Bronsted base but not Arrhenius base.\nII. NaCl can't undergo hydrolysis.\nIII. Group II metal ions get precipitated as their sulphides when H2S s is passed through their acidified salts.\nIV. Ostwald’s dilution law is not applicable for strong electrolyte.",
                "answer": """**I. $\\text{NH}_3$ as Bronsted Base:**
According to Arrhenius, a base must contain and liberate hydroxyl ions ($\\text{OH}^-$) in water; ammonia lacks $-\\text{OH}$ in its formula. According to Bronsted-Lowry, a base is a proton acceptor. $\\text{NH}_3$ readily accepts a proton ($\text{H}^+$) via its lone pair to form $\\text{NH}_4^+$, making it a Bronsted base.

**II. NaCl cannot undergo hydrolysis:**
$\text{NaCl}$ is the salt of a strong acid ($\text{HCl}$) and a strong base ($\text{NaOH}$). Its dissociated ions ($\\text{Na}^+$ and $\\text{Cl}^-$) are weak conjugate acids and bases that do not interact with water molecules to alter $[\\text{H}^+]$ or $[\\text{OH}^-]$.

**III. Group II Cations Precipitation:**
In acidic medium, $\\text{HCl}$ provides common $\\text{H}^+$ ions that suppress the ionization of weak diprotic acid $\\text{H}_2\\text{S}$, keeping $[\\text{S}^{2-}]$ extremely low. This low concentration is sufficient to exceed the very small $K_{sp}$ of Group II sulphides, but insufficient to precipitate Group IV sulphides.

**IV. Ostwald's Dilution Law and Strong Electrolytes:**
Ostwald's dilution law assumes an equilibrium between unionized molecules and ions ($\\alpha = \\sqrt{K/C}$). Strong electrolytes are completely ionized at all reasonable concentrations ($\alpha \\approx 1$). Furthermore, interionic electrostatic attractions deviate strong electrolytes from ideal equilibrium behavior."""
            },
            {
                "id": "chem-ion-q9",
                "number": "9",
                "question": "How many moles of Ca(OH)2 must be dissolved to produce 250 ml of aqueous solution of pH 10.65?",
                "answer": """Given:
$$\\text{pH} = 10.65$$
$$\\text{pOH} = 14 - 10.65 = 3.35$$
$$[\\text{OH}^-] = 10^{-3.35} = 4.47 \\times 10^{-4} \\text{ M}$$

$\\text{Ca(OH)}_2$ dissociates as:
$$\\text{Ca(OH)}_2 \\rightarrow \\text{Ca}^{2+} + 2\\text{OH}^-$$
$$[\\text{Ca(OH)}_2] = \\frac{[\\text{OH}^-]}{2} = \\frac{4.47 \\times 10^{-4}}{2} = 2.235 \\times 10^{-4} \\text{ mol/L}$$

For volume $V = 250 \\text{ mL} = 0.250 \\text{ L}$:
$$\\text{Moles} = M \\times V = (2.235 \\times 10^{-4} \\text{ mol/L}) \\times 0.250 \\text{ L} \\approx \\mathbf{5.59 \\times 10^{-5} \\text{ moles}}$$"""
            },
            {
                "id": "chem-ion-q10",
                "number": "10",
                "question": "If equal volume of two solutions having (pH=1) and (pH= 12) are mixed what will be the pH of the solution?",
                "answer": """Let equal volume be $V$ liters:
1. **Solution 1 (Acidic):** $\\text{pH} = 1 \\implies [\\text{H}^+] = 10^{-1} = 0.1 \\text{ M}$
   $$\\text{Moles of } \\text{H}^+ = 0.1 V$$
2. **Solution 2 (Basic):** $\\text{pH} = 12 \\implies \\text{pOH} = 14 - 12 = 2 \\implies [\\text{OH}^-] = 10^{-2} = 0.01 \\text{ M}$
   $$\\text{Moles of } \\text{OH}^- = 0.01 V$$

Neutralization:
$$\\text{Excess moles of } \\text{H}^+ = 0.1 V - 0.01 V = 0.09 V$$
$$\\text{Total volume} = V + V = 2V$$
$$[\\text{H}^+]_{\\text{mix}} = \\frac{0.09 V}{2 V} = 0.045 \\text{ M}$$
$$\\text{pH} = -\\log_{10}(0.045) = -(-1.347) \\approx \\mathbf{1.35}$$"""
            },
            {
                "id": "chem-ion-q11",
                "number": "11",
                "question": "Ionic product of water at 25oC is 1 x 10-14 and water is regarded as very weak electrolyte\nI. Define ionic product of water\nII. Deduce the relation Kw=[H+] [OH-]\nIII. Calculate the concentration of 0.1 M HCl at 25oC.\nIV. What is the effect of temperature on ionic product of water?\nV. State Ostwald dilution law. Derive an expression for Ostwald dilution law and mention its limitation.",
                "answer": """**I. Definition of $K_w$:**
The product of molar concentrations of hydrogen ions ($\\text{H}^+$) and hydroxyl ions ($\\text{OH}^-$) in pure water or in any aqueous solution at a given temperature.

**II. Deduction of $K_w = [\\text{H}^+][\\text{OH}^-]$:**
$$\\text{H}_2\\text{O} \\rightleftharpoons \\text{H}^+ + \\text{OH}^-$$
$$K_c = \\frac{[\\text{H}^+][\\text{OH}^-]}{[\\text{H}_2\\text{O}]}$$
Since water is ionized to an extremely small extent, $[\\text{H}_2\\text{O}]$ is practically constant:
$$K_c [\\text{H}_2\\text{O}] = K_w = [\\text{H}^+][\\text{OH}^-]$$

**III. Concentration in 0.1 M HCl at $25^\\circ\\text{C}$:**
$\\text{HCl}$ is a strong acid: $[\\text{H}^+] = 0.1 \\text{ M}$.
$$[\\text{OH}^-] = \\frac{K_w}{[\\text{H}^+]} = \\frac{1.0 \\times 10^{-14}}{0.1} = 1.0 \\times 10^{-13} \\text{ M}$$

**IV. Effect of Temperature:**
The self-ionization of water is an **endothermic process** ($\\Delta H > 0$). According to Le Chatelier's principle, increasing the temperature shifts the equilibrium forward, causing **$K_w$ to increase with temperature** (at $100^\\circ\\text{C}$, $K_w \\approx 5.1 \\times 10^{-13}$).

**V. Ostwald's Dilution Law:**
- *Statement:* The degree of dissociation ($\\alpha$) of a weak binary electrolyte is directly proportional to the square root of its dilution ($V$) or inversely proportional to the square root of its molar concentration ($C$).
- *Derivation:* For weak acid $\\text{HA} \\rightleftharpoons \\text{H}^+ + \\text{A}^-$:
  Initial: $C, 0, 0$; Equilibrium: $C(1-\\alpha), C\\alpha, C\\alpha$.
  $$K_a = \\frac{(C\\alpha)(C\\alpha)}{C(1 - \\alpha)} = \\frac{C\\alpha^2}{1 - \\alpha}$$
  For weak electrolytes, $\\alpha \\ll 1$, so $1 - \\alpha \\approx 1$:
  $$K_a = C\\alpha^2 \\implies \\alpha = \\sqrt{\\frac{K_a}{C}} = \\sqrt{K_a \\cdot V}$$
- *Limitations:* Fails completely for strong electrolytes."""
            },
            {
                "id": "chem-ion-q12",
                "number": "12",
                "question": "What is pH of 10-9 M HCl?",
                "answer": """In extremely dilute acid ($10^{-9} \\text{ M } \\text{HCl}$), the auto-ionization of water cannot be ignored:
$$[\\text{H}^+]_{\\text{total}} = [\\text{H}^+]_{\\text{acid}} + [\\text{H}^+]_{\\text{water}} = 10^{-9} + x$$
$$[\\text{OH}^-] = x$$
$$K_w = (10^{-9} + x)(x) = 10^{-14}$$
$$x^2 + 10^{-9}x - 10^{-14} = 0$$
Solving the quadratic equation:
$$x = \\frac{-10^{-9} + \\sqrt{10^{-18} + 4 \\times 10^{-14}}}{2} \\approx \\frac{-10^{-9} + 2.00 \\times 10^{-7}}{2} \\approx 9.95 \\times 10^{-8} \\text{ M}$$
$$[\\text{H}^+]_{\\text{total}} = 10^{-9} + 9.95 \\times 10^{-8} = 1.005 \\times 10^{-7} \\text{ M}$$
$$\\text{pH} = -\\log_{10}(1.005 \\times 10^{-7}) \\approx \\mathbf{6.998} \\; (\\approx 7.00)$$
*(It is slightly acidic, just under 7).*"""
            },
            {
                "id": "chem-ion-q13",
                "number": "13",
                "question": "Calculate pH of 1 x 10-3 M KOH?",
                "answer": """$\\text{KOH}$ is a strong monobasic base:
$$[\\text{OH}^-] = 1.0 \\times 10^{-3} \\text{ M}$$
$$\\text{pOH} = -\\log_{10}[\\text{OH}^-] = -\\log_{10}(10^{-3}) = 3$$
$$\\text{pH} = 14 - \\text{pOH} = 14 - 3 = \\mathbf{11}$$"""
            },
            {
                "id": "chem-ion-q14",
                "number": "14",
                "question": "Find the pH of 1 x 10-6N of H2SO4?",
                "answer": """Normality $N = 1 \\times 10^{-6} \\text{ N}$.
Since Normality directly gives the equivalent concentration of $\\text{H}^+$:
$$[\\text{H}^+] = 1.0 \\times 10^{-6} \\text{ g-eq/L} = 1.0 \\times 10^{-6} \\text{ M}$$
$$\\text{pH} = -\\log_{10}[\\text{H}^+] = -\\log_{10}(10^{-6}) = \\mathbf{6}$$"""
            },
            {
                "id": "chem-ion-q15",
                "number": "15",
                "question": "Is the solution acidic, basic, or neutral in which concentration of hydroxyl ion is 3.33x 10-10 mol/litre?",
                "answer": """Given: $[\\text{OH}^-] = 3.33 \\times 10^{-10} \\text{ mol/L}$ at $25^\\circ\\text{C}$.
$$[\\text{H}^+] = \\frac{K_w}{[\\text{OH}^-]} = \\frac{1.0 \\times 10^{-14}}{3.33 \\times 10^{-10}} = 3.00 \\times 10^{-5} \\text{ mol/L}$$
Since $[\\text{H}^+] = 3.00 \\times 10^{-5} > 1.0 \\times 10^{-7} \\text{ M}$ (and $[\\text{H}^+] > [\\text{OH}^-]$), the solution is **ACIDIC** ($\text{pH} = 4.52$)."""
            },
            {
                "id": "chem-ion-q16",
                "number": "16",
                "question": "Write to conjugate acid and base of ammonia.",
                "answer": """- **Conjugate Acid of Ammonia ($\text{NH}_3$):**  
  Add a proton ($\text{H}^+$):  
  $$\\text{NH}_3 + \\text{H}^+ \\rightarrow \\mathbf{NH_4^+} \\quad (\\text{Ammonium ion})$$

- **Conjugate Base of Ammonia ($\text{NH}_3$):**  
  Remove a proton ($\text{H}^+$):  
  $$\\text{NH}_3 - \\text{H}^+ \\rightarrow \\mathbf{NH_2^-} \\quad (\\text{Amide ion})$$"""
            },
            {
                "id": "chem-ion-q17",
                "number": "17",
                "question": "Calculate the pH of the solution sun by dissolving one gram of sodium hydroxide in one litre of its solution.",
                "answer": """Given: Mass of $\\text{NaOH} = 1.0 \\text{ g}$, Volume $V = 1.0 \\text{ L}$.
Molar mass of $\\text{NaOH} = 40.0 \\text{ g/mol}$.
$$[\\text{NaOH}] = \\frac{1.0 \\text{ g}}{40.0 \\text{ g/mol} \\times 1.0 \\text{ L}} = 0.025 \\text{ M}$$
Since $\\text{NaOH}$ is a strong base, $[\\text{OH}^-] = 0.025 \\text{ M}$.
$$\\text{pOH} = -\\log_{10}(0.025) = 1.602$$
$$\\text{pH} = 14 - \\text{pOH} = 14 - 1.602 = \\mathbf{12.40}$$"""
            },
            {
                "id": "chem-ion-q18",
                "number": "18",
                "question": "Define ionic product of water and PH of solution. Write the relation between PH&POH.",
                "answer": """- **Ionic Product of Water ($K_w$):** The product of the molar concentrations of hydronium/hydrogen ions and hydroxide ions in water or an aqueous solution at a given temperature ($K_w = [\\text{H}^+][\\text{OH}^-] = 1.0 \\times 10^{-14}$ at $25^\\circ\\text{C}$).
- **pH:** The negative logarithm (to the base 10) of the hydrogen ion concentration in moles per liter ($\\text{pH} = -\\log_{10}[\\text{H}^+]$).
- **Relation:** At $25^\\circ\\text{C}$, $\\mathbf{pH + pOH = 14}$."""
            },
            {
                "id": "chem-ion-q19",
                "number": "19",
                "question": "Define Bronsted concept of acid and base with an example of each.",
                "answer": """- **Bronsted-Lowry Acid:** A substance (molecule or ion) capable of donating a proton ($\text{H}^+$) to another substance (a proton donor). Example: $\\text{HCl} + \\text{H}_2\\text{O} \\rightarrow \\text{H}_3\\text{O}^+ + \\text{Cl}^-$, where $\\text{HCl}$ acts as an acid.
- **Bronsted-Lowry Base:** A substance capable of accepting a proton from another substance (a proton acceptor). Example: $\\text{NH}_3 + \\text{H}_2\\text{O} \\rightleftharpoons \\text{NH}_4^+ + \\text{OH}^-$, where $\\text{NH}_3$ acts as a base."""
            },
            {
                "id": "chem-ion-q20",
                "number": "20",
                "question": "What happens when HCl gas is passed through a saturated solution of sodium chloride and why?",
                "answer": """**Observation:**
Pure **sodium chloride ($\text{NaCl}$) precipitates out** as white crystals.

**Reason (Common Ion Effect):**
In a saturated $\\text{NaCl}$ solution:
$$\\text{NaCl} (s) \\rightleftharpoons \\text{Na}^+ (aq) + \\text{Cl}^- (aq)$$
When $\\text{HCl}$ gas is bubbled through, it dissociates completely, drastically increasing the concentration of chloride ions ($\\text{Cl}^-$). The ionic product $[\\text{Na}^+][\\text{Cl}^-]$ exceeds the solubility product ($K_{sp}$) of $\\text{NaCl}$. According to Le Chatelier's principle, equilibrium shifts left, precipitating pure $\\text{NaCl}$ while more soluble impurities remain in solution."""
            },
            {
                "id": "chem-ion-q21",
                "number": "21",
                "question": "Define Lewis acid and Lewis’s base giving one example of each.",
                "answer": """- **Lewis Acid:** An electron-pair acceptor. Example: Boron trifluoride ($\\text{BF}_3$), Aluminium chloride ($\\text{AlCl}_3$).
- **Lewis Base:** An electron-pair donor. Example: Ammonia ($:\\text{NH}_3$), Water ($:\\text{OH}_2$)."""
            },
            {
                "id": "chem-ion-q22",
                "number": "22",
                "question": "Define common ion effect.",
                "answer": """The common ion effect is the phenomenon of suppression of the degree of dissociation of a weak electrolyte by the addition of a strong electrolyte that provides an ion common to the weak electrolyte."""
            },
            {
                "id": "chem-ion-q23",
                "number": "23",
                "question": "Whether the aqueous solution of calcium chloride is acidic basic or neutral? Give reason.",
                "answer": """The aqueous solution of calcium chloride ($\\text{CaCl}_2$) is **NEUTRAL (or practically neutral, pH $\\approx$ 7)**.
**Reason:** $\\text{CaCl}_2$ is a salt derived from a strong base [$\\text{Ca(OH)}_2$] and a strong acid [$\\text{HCl}$]. Neither $\\text{Ca}^{2+}$ nor $\\text{Cl}^-$ ions undergo significant hydrolysis in water; hence, $[\\text{H}^+] = [\\text{OH}^-]$."""
            },
            {
                "id": "chem-ion-q24",
                "number": "24",
                "question": "49 grams of sulfuric acid is present in one litre of its solution. What is the pH of solution?",
                "answer": """Molar mass of $\\text{H}_2\\text{SO}_4 = 2(1) + 32 + 4(16) = 98 \\text{ g/mol}$.
$$\\text{Molarity} = \\frac{49 \\text{ g}}{98 \\text{ g/mol} \\times 1 \\text{ L}} = 0.5 \\text{ M}$$
Since $\\text{H}_2\\text{SO}_4$ is a diprotic strong acid:
$$[\\text{H}^+] = 2 \\times 0.5 = 1.0 \\text{ M}$$
$$\\text{pH} = -\\log_{10}[\\text{H}^+] = -\\log_{10}(1.0) = \\mathbf{0}$$"""
            },
            {
                "id": "chem-ion-q25",
                "number": "25",
                "question": "Predict weather the aqueous solution of copper sulphate acidic basic or neutral.",
                "answer": """The aqueous solution of copper sulphate ($\\text{CuSO}_4$) is **ACIDIC** (pH < 7).
**Reason:** $\\text{CuSO}_4$ is the salt of a weak base [$\\text{Cu(OH)}_2$] and a strong acid [$\\text{H}_2\\text{SO}_4$]. The cupric cation undergoes cationic hydrolysis:
$$\\text{Cu}^{2+} + 2\\text{H}_2\\text{O} \\rightleftharpoons \\text{Cu(OH)}_2 + 2\\text{H}^+$$
The generation of excess hydronium ions makes the solution acidic, turning blue litmus red."""
            },
            {
                "id": "chem-ion-q26",
                "number": "26",
                "question": "Explain the fact that the aqueous solution of sodium carbonate is basic while aqueous solution of sodium chloride is neutral.",
                "answer": """- **Sodium Carbonate ($\text{Na}_2\text{CO}_3$):** Salt of a strong base ($\text{NaOH}$) and a weak acid ($\text{H}_2\text{CO}_3$). The carbonate ion ($\text{CO}_3^{2-}$) undergoes anionic hydrolysis:
$$\\text{CO}_3^{2-} + \\text{H}_2\\text{O} \\rightleftharpoons \\text{HCO}_3^- + \\text{OH}^-$$
Liberation of excess hydroxyl ions makes the solution **basic (pH > 7)**.
- **Sodium Chloride ($\text{NaCl}$):** Salt of a strong base ($\text{NaOH}$) and strong acid ($\text{HCl}$). Neither $\\text{Na}^+$ nor $\\text{Cl}^-$ hydrolyzes; thus $[\\text{H}^+] = [\\text{OH}^-]$ and the solution is **neutral (pH = 7)**."""
            },
            {
                "id": "chem-ion-q27",
                "number": "27",
                "question": "Calculate the pH of an aqueous solution containing 10-7 moles of sodium hydroxide per litre.",
                "answer": """In $10^{-7} \\text{ M } \\text{NaOH}$, $[\\text{OH}^-]$ from water must be included:
$$[\\text{OH}^-]_{\\text{total}} = 10^{-7} + x, \\quad [\\text{H}^+] = x$$
$$K_w = x(10^{-7} + x) = 1.0 \\times 10^{-14}$$
$$x^2 + 10^{-7}x - 10^{-14} = 0$$
$$x = \\frac{-10^{-7} + \\sqrt{10^{-14} + 4 \\times 10^{-14}}}{2} = \\frac{-10^{-7} + \\sqrt{5} \\times 10^{-7}}{2} = 0.618 \\times 10^{-7} \\text{ M}$$
$$[\\text{OH}^-]_{\\text{total}} = 10^{-7} + 0.618 \\times 10^{-7} = 1.618 \\times 10^{-7} \\text{ M}$$
$$\\text{pOH} = -\\log_{10}(1.618 \\times 10^{-7}) = 6.79$$
$$\\text{pH} = 14 - 6.79 = \\mathbf{7.21}$$"""
            },
            {
                "id": "chem-ion-q28",
                "number": "28",
                "question": "What are the limitations of Lewis concept of acid and base? The solubility product of barium sulphate is 2x 10-10. Will precipitate occur or not if equal volume of 2x 10-8 M Barium chloride and 2x 10-4 M Sodium sulphate are mixed.",
                "answer": """**Limitations of Lewis Concept:**
1. Does not explain the relative strengths of acids and bases.
2. Many classical acid-base reactions are instantaneous, whereas coordination complex formation is often slow.
3. Protonic acids ($\\text{HCl, } \\text{H}_2\\text{SO}_4$) do not form coordinate bonds directly, yet are the strongest acids.

**Precipitation Calculation:**
When equal volumes are mixed, concentrations are halved:
$$[\\text{Ba}^{2+}] = \\frac{2 \\times 10^{-8}}{2} = 1.0 \\times 10^{-8} \\text{ M}$$
$$[\\text{SO}_4^{2-}] = \\frac{2 \\times 10^{-4}}{2} = 1.0 \\times 10^{-4} \\text{ M}$$
Ionic product $Q_{sp}$:
$$Q_{sp} = [\\text{Ba}^{2+}][\\text{SO}_4^{2-}] = (1.0 \\times 10^{-8}) \\times (1.0 \\times 10^{-4}) = 1.0 \\times 10^{-12}$$
Given $K_{sp} = 2 \\times 10^{-10}$.
Since **$Q_{sp} < K_{sp}$**, the solution remains unsaturated; **NO PRECIPITATE WILL OCCUR**."""
            },
            {
                "id": "chem-ion-q29",
                "number": "29",
                "question": "The solubility product of barium sulphate is 1x 10-10. Will precipitate occur or not if equal volume of 2x10-3 M barium chloride solution and 2X10-4 M Sodium sulphate solution are mixed.",
                "answer": """On mixing equal volumes, concentrations halve:
$$[\\text{Ba}^{2+}] = \\frac{2 \\times 10^{-3}}{2} = 1.0 \\times 10^{-3} \\text{ M}$$
$$[\\text{SO}_4^{2-}] = \\frac{2 \\times 10^{-4}}{2} = 1.0 \\times 10^{-4} \\text{ M}$$
Ionic Product $Q_{sp}$:
$$Q_{sp} = [\\text{Ba}^{2+}][\\text{SO}_4^{2-}] = (1.0 \\times 10^{-3}) \\times (1.0 \\times 10^{-4}) = 1.0 \\times 10^{-7}$$
Given $K_{sp} = 1.0 \\times 10^{-10}$.
Since **$Q_{sp} > K_{sp}$** ($10^{-7} > 10^{-10}$), the solution is supersaturated; **PRECIPITATE OF $\\text{BaSO}_4$ WILL OCCUR**."""
            },
            {
                "id": "chem-ion-q30",
                "number": "30",
                "question": "All Bronsted base are also Lewis bases, but all Bronsted acids are not Lewis’s acids. Explain. If 80 ml of 0.01M silver nitrate are mixed with 20 ml of 0.001 M sodium chloride solution. Will any silver chloride precipitate or not? [Ksp of AgCl =1.5 x10-10]",
                "answer": """**Explanation:**
- A Bronsted base accepts a proton ($\text{H}^+$), which requires having an unshared lone pair of electrons. Because it possesses a lone pair capable of being donated to a proton or any other electron-deficient center, **every Bronsted base is also a Lewis base**.
- However, Bronsted acids donate a proton (e.g., $\text{HCl, } \text{HNO}_3$), while Lewis acids must be capable of accepting an electron pair. Molecules like $\text{HCl}$ do not accept electron pairs; only the detached proton $\text{H}^+$ acts as a Lewis acid. Hence, **all Bronsted acids are not Lewis acids**.

**Precipitation Calculation:**
$$\\text{Total volume} = 80 + 20 = 100 \\text{ mL}$$
$$[\\text{Ag}^+] = \\frac{80 \\times 0.01}{100} = 8.0 \\times 10^{-3} \\text{ M}$$
$$[\\text{Cl}^-] = \\frac{20 \\times 0.001}{100} = 2.0 \\times 10^{-4} \\text{ M}$$
Ionic product $Q_{sp}$:
$$Q_{sp} = [\\text{Ag}^+][\\text{Cl}^-] = (8.0 \\times 10^{-3}) \\times (2.0 \\times 10^{-4}) = 1.6 \\times 10^{-6}$$
Since $K_{sp} = 1.5 \\times 10^{-10}$ and **$Q_{sp} > K_{sp}$**, **PRECIPITATION OF AgCl WILL OCCUR**."""
            },
            {
                "id": "chem-ion-q31",
                "number": "31",
                "question": "Calculate the pH of saturated solution of magnesium hydroxide, Ksp for magnesium hydroxide is 8.9 x10-12.",
                "answer": """$$\\text{Mg(OH)}_2 (s) \\rightleftharpoons \\text{Mg}^{2+} + 2\\text{OH}^-$$
$$K_{sp} = [\\text{Mg}^{2+}][\\text{OH}^-]^2 = s(2s)^2 = 4s^3$$
$$4s^3 = 8.9 \\times 10^{-12} \\implies s^3 = 2.225 \\times 10^{-12}$$
$$s = (2.225 \\times 10^{-12})^{1/3} \\approx 1.305 \\times 10^{-4} \\text{ M}$$
$$[\\text{OH}^-] = 2s = 2 \\times 1.305 \\times 10^{-4} = 2.61 \\times 10^{-4} \\text{ M}$$
$$\\text{pOH} = -\\log_{10}(2.61 \\times 10^{-4}) = 3.58$$
$$\\text{pH} = 14 - 3.58 = \\mathbf{10.42}$$"""
            },
            {
                "id": "chem-ion-q32",
                "number": "32",
                "question": "200 ml of aqueous solution of hydrochloric acid (PH= 2) is mixed with 300 ml of aqueous solution of sodium hydroxide (PH=12). What will be the P chop resulting mixture solution.",
                "answer": """1. $\\text{HCl}$ solution: $\\text{pH} = 2 \\implies [\\text{H}^+] = 10^{-2} = 0.01 \\text{ M}$, Volume $= 200 \\text{ mL}$
$$\\text{Millimoles of } \\text{H}^+ = 200 \\times 0.01 = 2.0 \\text{ mmol}$$
2. $\\text{NaOH}$ solution: $\\text{pH} = 12 \\implies \\text{pOH} = 2 \\implies [\\text{OH}^-] = 10^{-2} = 0.01 \\text{ M}$, Volume $= 300 \\text{ mL}$
$$\\text{Millimoles of } \\text{OH}^- = 300 \\times 0.01 = 3.0 \\text{ mmol}$$

Neutralization leaves excess $\\text{OH}^-$:
$$\\text{Excess } \\text{OH}^- = 3.0 - 2.0 = 1.0 \\text{ mmol}$$
$$\\text{Total volume} = 200 + 300 = 500 \\text{ mL}$$
$$[\\text{OH}^-]_{\\text{mix}} = \\frac{1.0 \\text{ mmol}}{500 \\text{ mL}} = 2.0 \\times 10^{-3} \\text{ M}$$
$$\\text{pOH} = -\\log_{10}(2.0 \\times 10^{-3}) = 2.70$$
$$\\text{pH} = 14 - 2.70 = \\mathbf{11.30}$$"""
            },
            {
                "id": "chem-ion-q33",
                "number": "33",
                "question": "0.41 gram of sodium hydroxide is placed in 100 ML of 0.1N sulfuric acid. Find the PH of resulting solution.",
                "answer": """1. $\\text{NaOH}$ added: Molar mass $= 40 \\text{ g/mol}$
$$\\text{Moles of } \\text{NaOH} = \\frac{0.41 \\text{ g}}{40 \\text{ g/mol}} = 0.01025 \\text{ mol} = 10.25 \\text{ mmol of } \\text{OH}^-$$
2. $\\text{H}_2\\text{SO}_4$ present:
$$\\text{Milliequivalents of } \\text{H}^+ = 100 \\text{ mL} \\times 0.1 \\text{ N} = 10.0 \\text{ meq} = 10.0 \\text{ mmol of } \\text{H}^+$$

Excess $\\text{OH}^-$:
$$\\text{Excess } \\text{OH}^- = 10.25 - 10.0 = 0.25 \\text{ mmol}$$
Assuming volume remains $100 \\text{ mL}$:
$$[\\text{OH}^-] = \\frac{0.25 \\text{ mmol}}{100 \\text{ mL}} = 2.5 \\times 10^{-3} \\text{ M}$$
$$\\text{pOH} = -\\log_{10}(2.5 \\times 10^{-3}) = 2.60$$
$$\\text{pH} = 14 - 2.60 = \\mathbf{11.40}$$"""
            },
            {
                "id": "chem-ion-q34",
                "number": "34",
                "question": "Calculate the pH of 1 M solution of acetic acid. To what volume one litre of this solution b diluted so that the pH of the solution that is formed will be twice of original value. [Ka= 1.8 x10-5]",
                "answer": """**1. Initial pH:**
$$[\\text{H}^+] = \\sqrt{K_a \\cdot C} = \\sqrt{1.8 \\times 10^{-5} \\times 1.0} = 4.24 \\times 10^{-3} \\text{ M}$$
$$\\text{pH}_1 = -\\log_{10}(4.24 \\times 10^{-3}) = 2.37$$

**2. Target pH:**
$$\\text{pH}_2 = 2 \\times 2.37 = 4.74$$
$$[\\text{H}^+]_2 = 10^{-4.74} = 1.82 \\times 10^{-5} \\text{ M}$$

Using $[\\text{H}^+]_2 = \\sqrt{K_a \\cdot C_2}$:
$$C_2 = \\frac{([\\text{H}^+]_2)^2}{K_a} = \\frac{(1.82 \\times 10^{-5})^2}{1.8 \\times 10^{-5}} = 1.84 \\times 10^{-5} \\text{ M}$$
Dilution formula $M_1 V_1 = M_2 V_2$:
$$(1.0 \\text{ M})(1.0 \\text{ L}) = (1.84 \\times 10^{-5} \\text{ M}) \\times V_2$$
$$V_2 = \\frac{1.0}{1.84 \\times 10^{-5}} \\approx \\mathbf{5.43 \\times 10^4 \\text{ Liters}}$$"""
            },
            {
                "id": "chem-ion-q35",
                "number": "35",
                "question": "Define solubility product principle. 0.00143 gram of silver chloride dissolved in one litre of water at 25oC to form or saturated solution. What is the solubility product of the salt.",
                "answer": """**Principle:** In a saturated solution of a sparingly soluble salt, the product of the molar concentrations of its constituent ions, raised to powers equal to their stoichiometric coefficients, is constant at a constant temperature.

**Calculation:**
Molar mass of $\\text{AgCl} = 143.5 \\text{ g/mol}$.
$$s = \\frac{0.00143 \\text{ g/L}}{143.5 \\text{ g/mol}} = 1.0 \\times 10^{-5} \\text{ mol/L}$$
$$K_{sp} = [\\text{Ag}^+][\\text{Cl}^-] = s^2 = (1.0 \\times 10^{-5})^2 = \\mathbf{1.0 \\times 10^{-10}}$$"""
            },
            {
                "id": "chem-ion-q36",
                "number": "36",
                "question": "PH of 0.1 M hydrogen cyanide solution is 5.2. what is the value of ionization constant for the acid.",
                "answer": """Given: $C = 0.1 \\text{ M}, \\text{pH} = 5.2$.
$$[\\text{H}^+] = 10^{-5.2} = 6.31 \\times 10^{-6} \\text{ M}$$
For a weak acid:
$$[\\text{H}^+] = \\sqrt{K_a \\cdot C} \\implies K_a = \\frac{[\\text{H}^+]^2}{C}$$
$$K_a = \\frac{(6.31 \\times 10^{-6})^2}{0.1} = \\frac{3.98 \\times 10^{-11}}{0.1} = \\mathbf{3.98 \\times 10^{-10}}$$"""
            },
            {
                "id": "chem-ion-q37",
                "number": "37",
                "question": "The solubility of AgCl in water is 1.43 x10-3 g/l, calculate the solubility in 0.5 M KCl.",
                "answer": """Molar mass of $\\text{AgCl} = 143.5 \\text{ g/mol}$.
$$s = \\frac{1.43 \\times 10^{-3} \\text{ g/L}}{143.5 \\text{ g/mol}} = 1.0 \\times 10^{-5} \\text{ mol/L}$$
$$K_{sp} = s^2 = (1.0 \\times 10^{-5})^2 = 1.0 \\times 10^{-10}$$

In $0.5 \\text{ M } \\text{KCl}$, $[\\text{Cl}^-] = 0.5 \\text{ M}$:
$$s' = [\\text{Ag}^+] = \\frac{K_{sp}}{[\\text{Cl}^-]} = \\frac{1.0 \\times 10^{-10}}{0.5} = 2.0 \\times 10^{-10} \\text{ mol/L}$$
$$\\text{Solubility in g/L} = (2.0 \\times 10^{-10} \\text{ mol/L}) \\times 143.5 \\text{ g/mol} = \\mathbf{2.87 \\times 10^{-8} \\text{ g/L}}$$"""
            },
            {
                "id": "chem-ion-q38",
                "number": "38",
                "question": "Why does Kw of water increase with temperature? 10 ml of N/2 HCl, N/10 HNO3 and 60 ml of N/5 H2SO4 are mixed together. Find the PH oh the mixture.",
                "answer": """**Why $K_w$ increases with temperature:**
The dissociation of water is an endothermic process:
$$\\text{H}_2\\text{O} \\rightleftharpoons \\text{H}^+ + \\text{OH}^-, \\quad \\Delta H > 0$$
According to Le Chatelier's principle, supplying heat shifts the equilibrium forward, producing more $\\text{H}^+$ and $\\text{OH}^-$ ions and increasing $K_w$.

**Mixture pH Calculation:**
- $10 \\text{ mL}$ of $N/2 \\text{ HCl} \\implies 10 \\times 0.5 = 5.0 \\text{ meq}$
- Let volume of $N/10 \\text{ HNO}_3$ be $30 \\text{ mL}$ (or if omitted in text, assume standard $10 \\text{ mL}$: $10 \\times 0.1 = 1.0 \\text{ meq}$)
- $60 \\text{ mL}$ of $N/5 \\text{ H}_2\\text{SO}_4 \\implies 60 \\times 0.2 = 12.0 \\text{ meq}$
$$\\text{Total meq of } \\text{H}^+ = 5.0 + 1.0 + 12.0 = 18.0 \\text{ meq}$$
$$\\text{Total volume} = 10 + 10 + 60 = 80 \\text{ mL}$$
$$N_{\\text{mix}} = [\\text{H}^+] = \\frac{18.0}{80} = 0.225 \\text{ N (or M)}$$
$$\\text{pH} = -\\log_{10}(0.225) = \\mathbf{0.65}$$"""
            },
            {
                "id": "chem-ion-q39",
                "number": "39",
                "question": "What do you understand by equilibrium state in our reversible reaction? Why is aqueous solution of ferric chloride acidic?",
                "answer": """**Equilibrium State:**
The state of a reversible chemical reaction in which the rate of the forward reaction equals the rate of the reverse reaction, and the macroscopic observable properties (concentrations, pressure, temperature, color) remain constant over time.

**Why aqueous $\\text{FeCl}_3$ is acidic:**
$\\text{FeCl}_3$ is the salt of a weak base [$\\text{Fe(OH)}_3$] and a strong acid [$\\text{HCl}$]. The small, highly charged $\\text{Fe}^{3+}$ ion undergoes strong cationic hydrolysis:
$$\\text{Fe}^{3+} + 3\\text{H}_2\\text{O} \\rightleftharpoons \\text{Fe(OH)}_3 + 3\\text{H}^+$$
The release of free $\\text{H}^+$ ions makes the solution acidic."""
            },
            {
                "id": "chem-ion-q40",
                "number": "40",
                "question": "Differentiate between strong and weak electrolyte.",
                "answer": """| S.N. | Strong Electrolyte | Weak Electrolyte |
| :--- | :--- | :--- |
| 1. | Ionizes almost completely ($100\\%, \\alpha \\approx 1$) in aqueous solution. | Ionizes only partially (usually $\\alpha < 5\\%$) in aqueous solution. |
| 2. | Exhibits high electrical conductivity. | Exhibits low electrical conductivity. |
| 3. | Ostwald's dilution law is not applicable. | Obeys Ostwald's dilution law. |
| 4. | Examples: $\\text{HCl, NaOH, NaCl, KNO}_3$. | Examples: $\\text{CH}_3\\text{COOH, NH}_4\\text{OH, HCN}$. |"""
            },
            {
                "id": "chem-ion-q41",
                "number": "41",
                "question": "If the volume of 25 ml of 0.05 M Ba(NO3)2 are mixed with 0.02 M NaF. Will BaF2 precipitate? [Ksp of BaF2= 1.7x10-6 at 298K]",
                "answer": """Assuming equal volume ($25 \\text{ mL}$) of $0.02 \\text{ M } \\text{NaF}$:
$$\\text{Total volume} = 50 \\text{ mL}$$
$$[\\text{Ba}^{2+}] = \\frac{25 \\times 0.05}{50} = 0.025 \\text{ M}$$
$$[\\text{F}^-] = \\frac{25 \\times 0.02}{50} = 0.010 \\text{ M}$$

Ionic Product $Q_{sp}$:
$$Q_{sp} = [\\text{Ba}^{2+}][\\text{F}^-]^2 = (0.025) \\times (0.010)^2 = 2.5 \\times 10^{-6}$$
Given $K_{sp} = 1.7 \\times 10^{-6}$.
Since **$Q_{sp} > K_{sp}$** ($2.5 \\times 10^{-6} > 1.7 \\times 10^{-6}$), **PRECIPITATION OF $\\text{BaF}_2$ WILL OCCUR**."""
            },
            {
                "id": "chem-ion-q42",
                "number": "42",
                "question": "A solubility of calcium hydroxide at 25o C is 4.42 X 10-5. A 500 ml of saturated solution of calcium hydroxide is mixed with an equal volume of 0.4 M NaOH. What mass of calcium hydroxide is precipitated out?",
                "answer": """Let $K_{sp} = [\\text{Ca}^{2+}][\\text{OH}^-]^2 = 4s^3 = 4(4.42 \\times 10^{-5})^3 \\approx 3.46 \\times 10^{-13}$.
Initial moles of $\\text{Ca}^{2+}$ in $500 \\text{ mL}$:
$$n_i = (4.42 \\times 10^{-5} \\text{ mol/L}) \\times 0.500 \\text{ L} = 2.21 \\times 10^{-5} \\text{ mol}$$

After mixing with $500 \\text{ mL}$ of $0.4 \\text{ M } \\text{NaOH}$, total volume $= 1.0 \\text{ L}$:
$$[\\text{OH}^-] \\approx \\frac{500 \\times 0.4}{1000} = 0.20 \\text{ M}$$
Residual $[\\text{Ca}^{2+}]$ in solution:
$$[\\text{Ca}^{2+}] = \\frac{K_{sp}}{[\\text{OH}^-]^2} = \\frac{3.46 \\times 10^{-13}}{(0.20)^2} = 8.65 \\times 10^{-12} \\text{ M}$$
Moles of $\\text{Ca(OH)}_2$ precipitated:
$$\\Delta n = 2.21 \\times 10^{-5} - 8.65 \\times 10^{-12} \\approx 2.21 \\times 10^{-5} \\text{ mol}$$
Mass precipitated (Molar mass of $\\text{Ca(OH)}_2 = 74 \\text{ g/mol}$):
$$\\text{Mass} = (2.21 \\times 10^{-5} \\text{ mol}) \\times 74 \\text{ g/mol} \\approx \\mathbf{1.64 \\times 10^{-3} \\text{ g}} = 1.64 \\text{ mg}$$"""
            },
            {
                "id": "chem-ion-q43",
                "number": "43",
                "question": "State solubility product constant. What is the proper condition of precipitation of salt from the solution. What is the minimum volume of water is required to dissolve 1g of calcium sulphate at 298K? [Ksp for CaSO4= 9.1 x 10-6]",
                "answer": """**1. Solubility Product Constant ($K_{sp}$):**
The product of the molar concentrations of ions in a saturated solution of a sparingly soluble salt at a given temperature, each concentration raised to the power of its stoichiometric coefficient.

**2. Condition for Precipitation:**
A salt precipitates if its **Ionic Product exceeds its Solubility Product ($Q_{sp} > K_{sp}$)**.

**3. Minimum Volume of Water:**
$$s = \\sqrt{K_{sp}} = \\sqrt{9.1 \\times 10^{-6}} = 3.017 \\times 10^{-3} \\text{ mol/L}$$
Molar mass of $\\text{CaSO}_4 = 40 + 32 + 64 = 136 \\text{ g/mol}$.
$$\\text{Solubility in g/L} = (3.017 \\times 10^{-3} \\text{ mol/L}) \\times 136 \\text{ g/mol} = 0.4103 \\text{ g/L}$$
$$\\text{Volume required for 1 g} = \\frac{1.0 \\text{ g}}{0.4103 \\text{ g/L}} \\approx \\mathbf{2.44 \\text{ Liters}}$$"""
            },
            {
                "id": "chem-ion-q44",
                "number": "44",
                "question": "What mass of KOH should be dissolved in one litre of solution having PH is 12 at 298K?",
                "answer": """$$\\text{pH} = 12 \\implies \\text{pOH} = 14 - 12 = 2$$
$$[\\text{OH}^-] = 10^{-2} = 0.01 \\text{ M}$$
Molar mass of $\\text{KOH} = 39 + 16 + 1 = 56 \\text{ g/mol}$.
$$\\text{Mass required} = 0.01 \\text{ mol} \\times 56 \\text{ g/mol} = \\mathbf{0.56 \\text{ g}}$$"""
            },
            {
                "id": "chem-ion-q45",
                "number": "45",
                "question": "A sample of AgCl is treated with 5 ml of 2M Na2CO3 solution to produce AgCO3. The remaining solution contains 0.003 g of Cl- per litre. Calculate solubility product of AgCl. [Ksp of Ag2CO3= 8.2x10-12]",
                "answer": """In presence of $2 \\text{ M } \\text{Na}_2\\text{CO}_3$, $[\\text{CO}_3^{2-}] \\approx 2.0 \\text{ M}$.
$$K_{sp}(\\text{Ag}_2\\text{CO}_3) = [\\text{Ag}^+]^2 [\\text{CO}_3^{2-}] = 8.2 \\times 10^{-12}$$
$$[\\text{Ag}^+]^2 (2.0) = 8.2 \\times 10^{-12} \\implies [\\text{Ag}^+] = \\sqrt{4.1 \\times 10^{-12}} = 2.025 \\times 10^{-6} \\text{ M}$$

Given $[\text{Cl}^-] = 0.003 \\text{ g/L}$:
$$[\\text{Cl}^-] = \\frac{0.003 \\text{ g/L}}{35.5 \\text{ g/mol}} = 8.45 \\times 10^{-5} \\text{ M}$$

$$K_{sp}(\\text{AgCl}) = [\\text{Ag}^+][\\text{Cl}^-] = (2.025 \\times 10^{-6}) \\times (8.45 \\times 10^{-5}) \\approx \\mathbf{1.71 \\times 10^{-10}}$$"""
            },
            {
                "id": "chem-ion-q46",
                "number": "46",
                "question": "What is the PH of a solution of NaOH whose concentration of 0.4g/l?",
                "answer": """Molar mass of $\\text{NaOH} = 40 \\text{ g/mol}$.
$$[\\text{NaOH}] = \\frac{0.4 \\text{ g/L}}{40 \\text{ g/mol}} = 0.01 \\text{ M} = 10^{-2} \\text{ M}$$
$$\\text{pOH} = -\\log_{10}(10^{-2}) = 2$$
$$\\text{pH} = 14 - 2 = \\mathbf{12}$$"""
            },
            {
                "id": "chem-ion-q47",
                "number": "47",
                "question": "Calculate the concentration of hydroxide ion of a solution having PH 10.5.",
                "answer": """$$\\text{pOH} = 14 - 10.5 = 3.5$$
$$[\\text{OH}^-] = 10^{-3.5} = 10^{0.5 - 4} = 10^{0.5} \\times 10^{-4} \\approx \\mathbf{3.16 \\times 10^{-4} \\text{ mol/L}}$$"""
            },
            {
                "id": "chem-ion-q48",
                "number": "48",
                "question": "The solubility product constant of BaSO4 in water at 25o C is 1x 10-10. Calculate the solubility of BaSO4 in g/l.",
                "answer": """$$K_{sp} = s^2 = 1.0 \\times 10^{-10} \\implies s = 1.0 \\times 10^{-5} \\text{ mol/L}$$
Molar mass of $\\text{BaSO}_4 = 137.3 + 32 + 64 = 233.3 \\text{ g/mol}$.
$$\\text{Solubility in g/L} = (1.0 \\times 10^{-5} \\text{ mol/L}) \\times 233.3 \\text{ g/mol} = \\mathbf{2.33 \\times 10^{-3} \\text{ g/L}}$$"""
            },
            {
                "id": "chem-ion-q49",
                "number": "49",
                "question": "Calculate the degree of ionization of HCN having concentration 0.01 M (Ka of HCN = 4.8 X 10-10). Also calculate H+ ion concentration and PH.",
                "answer": """1. **Degree of ionization ($\\alpha$):**
$$\\alpha = \\sqrt{\\frac{K_a}{C}} = \\sqrt{\\frac{4.8 \\times 10^{-10}}{0.01}} = \\sqrt{4.8 \\times 10^{-8}} \\approx \\mathbf{2.19 \\times 10^{-4}} \\; (0.0219\\%)$$

2. **$\\text{H}^+$ concentration:**
$$[\\text{H}^+] = C\\alpha = 0.01 \\times 2.19 \\times 10^{-4} = \\mathbf{2.19 \\times 10^{-6} \\text{ M}}$$

3. **pH:**
$$\\text{pH} = -\\log_{10}(2.19 \\times 10^{-6}) = 6 - \\log_{10}(2.19) \\approx \\mathbf{5.66}$$"""
            },
            {
                "id": "chem-ion-q50",
                "number": "50",
                "question": "Two litres of 1M HCl is mixed with one litre of 1M NaOH. Calculate the strength of salt formed and the PH of the resulting solution.",
                "answer": """1. $\\text{HCl}$: Moles $= 2.0 \\text{ L} \\times 1.0 \\text{ M} = 2.0 \\text{ mol}$
2. $\\text{NaOH}$: Moles $= 1.0 \\text{ L} \\times 1.0 \\text{ M} = 1.0 \\text{ mol}$
Total volume $= 2.0 + 1.0 = 3.0 \\text{ L}$.

Reaction: $\\text{HCl} + \\text{NaOH} \\rightarrow \\text{NaCl} + \\text{H}_2\\text{O}$
- Moles of $\\text{NaCl}$ formed $= 1.0 \\text{ mol}$
- Strength of $\\text{NaCl} = \\frac{1.0 \\text{ mol}}{3.0 \\text{ L}} = \\mathbf{0.333 \\text{ M}}$ ($19.5 \\text{ g/L}$).
- Excess moles of $\\text{HCl} = 2.0 - 1.0 = 1.0 \\text{ mol}$
$$[\\text{H}^+] = \\frac{1.0 \\text{ mol}}{3.0 \\text{ L}} = 0.333 \\text{ M}$$
$$\\text{pH} = -\\log_{10}(0.333) = \\mathbf{0.48}$$"""
            },
            {
                "id": "chem-ion-q51",
                "number": "51",
                "question": "The solubility product of chalk is 9.3 x 10-8. Calculate its solubility in gram per litre.",
                "answer": """Chalk is $\\text{CaCO}_3$ (Molar mass $= 40 + 12 + 48 = 100 \\text{ g/mol}$).
$$K_{sp} = s^2 = 9.3 \\times 10^{-8}$$
$$s = \\sqrt{9.3 \\times 10^{-8}} \\approx 3.05 \\times 10^{-4} \\text{ mol/L}$$
$$\\text{Solubility in g/L} = (3.05 \\times 10^{-4} \\text{ mol/L}) \\times 100 \\text{ g/mol} = \\mathbf{0.0305 \\text{ g/L}}$$"""
            },
            {
                "id": "chem-ion-q52",
                "number": "52",
                "question": "What is meant by buffer solution? Write down the mechanism of acidic buffer and basic buffer solution.",
                "answer": """**Definition:**
A buffer solution is an aqueous solution that resists drastic changes in its pH upon the addition of small amounts of strong acid, strong base, or upon dilution.

### Mechanism of Acidic Buffer ($\text{CH}_3\text{COOH} + \text{CH}_3\text{COONa}$):
1. **Addition of Acid ($\text{H}^+$):** The added $\\text{H}^+$ ions react with reserve acetate anions to form undissociated acetic acid molecules:
$$\\text{CH}_3\\text{COO}^- + \\text{H}^+ \\rightarrow \\text{CH}_3\\text{COOH}$$
2. **Addition of Base ($\text{OH}^-$):** The added $\\text{OH}^-$ ions are neutralized by undissociated acetic acid molecules:
$$\\text{CH}_3\\text{COOH} + \\text{OH}^- \\rightarrow \\text{CH}_3\\text{COO}^- + \\text{H}_2\\text{O}$$

### Mechanism of Basic Buffer ($\text{NH}_4\text{OH} + \text{NH}_4\text{Cl}$):
1. **Addition of Acid ($\text{H}^+$):** Neutralized by weak base molecules:
$$\\text{NH}_4\\text{OH} + \\text{H}^+ \\rightarrow \\text{NH}_4^+ + \\text{H}_2\\text{O}$$
2. **Addition of Base ($\text{OH}^-$):** Neutralized by ammonium cations:
$$\\text{NH}_4^+ + \\text{OH}^- \\rightarrow \\text{NH}_4\\text{OH}$$"""
            },
            {
                "id": "chem-ion-q53",
                "number": "53",
                "question": "What amount of Zn(OH)2 will be precipitated out at 25o C? if 100 ml of 0.22g NaOH is added to 1 litre of a saturated solution of Zn(OH)2? Precipitate is obtained in this reaction, why? [solubility product of Zn(OH)2 at 25o C is 1.8 x 10-14]",
                "answer": """In pure saturated solution:
$$K_{sp} = 4s^3 = 1.8 \\times 10^{-14} \\implies s = 1.65 \\times 10^{-5} \\text{ M}$$
Initial moles of $\\text{Zn}^{2+} = 1.65 \\times 10^{-5} \\text{ mol}$.

Moles of $\\text{NaOH}$ added:
$$\\text{Moles} = \\frac{0.22 \\text{ g}}{40 \\text{ g/mol}} = 5.5 \\times 10^{-3} \\text{ mol}$$
Total volume $= 1.0 + 0.1 = 1.1 \\text{ L}$.
$$[\\text{OH}^-] = \\frac{5.5 \\times 10^{-3}}{1.1} = 5.0 \\times 10^{-3} \\text{ M}$$

Residual $[\\text{Zn}^{2+}]$:
$$[\\text{Zn}^{2+}] = \\frac{K_{sp}}{[\\text{OH}^-]^2} = \\frac{1.8 \\times 10^{-14}}{(5.0 \\times 10^{-3})^2} = 7.2 \\times 10^{-10} \\text{ M}$$
Moles of $\\text{Zn(OH)}_2$ precipitated $\\approx 1.65 \\times 10^{-5} \\text{ mol}$.
Mass precipitated (Molar mass of $\\text{Zn(OH)}_2 = 99.4 \\text{ g/mol}$):
$$\\text{Mass} = (1.65 \\times 10^{-5} \\text{ mol}) \\times 99.4 \\text{ g/mol} \\approx \\mathbf{1.64 \\times 10^{-3} \\text{ g}} = 1.64 \\text{ mg}$$
**Reason for Precipitation:** Common ion effect of $\\text{OH}^-$ causes the ionic product $Q_{sp} > K_{sp}$."""
            },
            {
                "id": "chem-ion-q54",
                "number": "54",
                "question": "Potassium hydroxide having PH 8 diluted 1000 times. Calculate the PH of the diluted bases.",
                "answer": """Initial: $\\text{pH} = 8 \\implies \\text{pOH} = 6 \\implies [\\text{OH}^-]_{\\text{base}} = 10^{-6} \\text{ M}$.
Diluted 1000 times:
$$[\\text{OH}^-]_{\\text{base}} = \\frac{10^{-6}}{1000} = 10^{-9} \\text{ M}$$
Since the base is extremely dilute, auto-ionization of water dominates:
$$[\\text{OH}^-]_{\\text{total}} = 10^{-9} + x, \\quad [\\text{H}^+] = x$$
$$x(10^{-9} + x) = 1.0 \\times 10^{-14} \\implies x \\approx 9.95 \\times 10^{-8} \\text{ M}$$
$$[\\text{OH}^-]_{\\text{total}} \\approx 1.005 \\times 10^{-7} \\text{ M}$$
$$\\text{pOH} = 6.998 \\implies \\text{pH} = 14 - 6.998 = \\mathbf{7.002} \\; (\\approx 7.00)$$"""
            },
            {
                "id": "chem-ion-q55",
                "number": "55",
                "question": "0.1 M ethanoic acid is 1.34% ionized. Find its dissociation constant.",
                "answer": """Given:
$$C = 0.1 \\text{ M}$$
$$\\alpha = 1.34\\% = \\frac{1.34}{100} = 0.0134$$

Dissociation constant $K_a$:
$$K_a = \\frac{C\\alpha^2}{1 - \\alpha} \\approx C\\alpha^2$$
$$K_a = 0.1 \\times (0.0134)^2 = 0.1 \\times 1.7956 \\times 10^{-4} = \\mathbf{1.80 \\times 10^{-5}}$$"""
            },
            {
                "id": "chem-ion-q56",
                "number": "56",
                "question": "a. Write the applications of solubility product principle and common ion effect in qualitative salt analysis.[4]\nb. Differentiate between Bronsted-Lowry and Lewis concept of bases. [2]\nc. Calculate the degree of ionization of HCN having concentration 0.01M (Ka of HCN = 4.8x10-10). Also calculate H+ concentration and pH of the solution.[2]",
                "answer": """### a. Applications in Qualitative Salt Analysis:
1. **Precipitation of Group I Radicals:** Group I cations ($\\text{Ag}^+, \\text{Pb}^{2+}, \\text{Hg}_2^{2+}$) are precipitated as insoluble chlorides using dilute $\\text{HCl}$. The high $[\\text{Cl}^-]$ easily exceeds their $K_{sp}$.
2. **Selective Precipitation of Group II vs Group IV Sulphides:** $\\text{H}_2\\text{S}$ is passed in acidic medium ($\\text{HCl}$) for Group II. Common $\\text{H}^+$ ions suppress $\\text{S}^{2-}$ concentration so that only Group II sulphides with very low $K_{sp}$ precipitate. In Group IV, $\\text{H}_2\\text{S}$ is passed in alkaline medium ($\\text{NH}_4\\text{OH}$), where $\\text{OH}^-$ removes $\\text{H}^+$, raising $[\\text{S}^{2-}]$ to precipitate Group IV sulphides with higher $K_{sp}$.
3. **Precipitation of Group III Hydroxides:** $\\text{NH}_4\\text{Cl}$ suppresses ionization of $\\text{NH}_4\\text{OH}$, preventing precipitation of Group IV cations.
4. **Purification of Common Salt:** Bubbling $\\text{HCl}$ gas into saturated brine precipitates pure $\\text{NaCl}$ due to the common ion effect of $\\text{Cl}^-$.

---

### b. Difference between Bronsted-Lowry and Lewis Bases:
- **Bronsted-Lowry Base:** Defined as a **proton ($\text{H}^+$) acceptor**. Focuses exclusively on proton transfer.
- **Lewis Base:** Defined as an **electron-pair donor**. Broader concept covering coordination with metal cations and electron-deficient molecules without involving protons.

---

### c. Calculation for 0.01 M HCN:
- **Degree of ionization ($\\alpha$):**
$$\\alpha = \\sqrt{\\frac{K_a}{C}} = \\sqrt{\\frac{4.8 \\times 10^{-10}}{0.01}} = \\sqrt{4.8 \\times 10^{-8}} = \\mathbf{2.19 \\times 10^{-4}} \\; (0.0219\\%)$$
- **$\\text{H}^+$ concentration:**
$$[\\text{H}^+] = C\\alpha = 0.01 \\times 2.19 \\times 10^{-4} = \\mathbf{2.19 \\times 10^{-6} \\text{ M}}$$
- **pH:**
$$\\text{pH} = -\\log_{10}(2.19 \\times 10^{-6}) = \\mathbf{5.66}$$"""
            }
        ]
    }
