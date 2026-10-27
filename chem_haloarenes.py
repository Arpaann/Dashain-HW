# chem_haloarenes.py
# Haloarenes questions 1 to 23

def get_haloarenes():
    return {
        "name": "Haloarenes",
        "questions": [
            {
                "id": "chem-hr-q1",
                "number": "1",
                "question": "Write a chemical equation for each of the following: Wurtz-Fitting reaction and Sandmeyer reaction.",
                "answer": """**Wurtz-Fittig Reaction:**
Reaction of an aryl halide with an alkyl halide in the presence of sodium metal and dry ether to produce an alkylarene (e.g., Toluene):
$$\\text{C}_6\\text{H}_5\\text{Cl} + 2\\text{Na} + \\text{CH}_3\\text{Cl} \\xrightarrow{\\text{dry ether}} \\text{C}_6\\text{H}_5\\text{-CH}_3 + 2\\text{NaCl} \\quad (\\text{Toluene})$$

**Sandmeyer Reaction:**
Treatment of freshly prepared benzene diazonium chloride with cuprous chloride ($\\text{Cu}_2\\text{Cl}_2$) dissolved in $\\text{HCl}$ to form chlorobenzene:
$$\\text{C}_6\\text{H}_5\\text{N}_2^+\\text{Cl}^- \\xrightarrow{\\text{Cu}_2\\text{Cl}_2 / \\text{HCl}} \\text{C}_6\\text{H}_5\\text{Cl} + \\text{N}_2 \\uparrow$$"""
            },
            {
                "id": "chem-hr-q2",
                "number": "2",
                "question": "An aromatic compound (A) undergoes Sandmeyer's reaction to give (B). The compound (B) is reduced with Ni-Al in presence of alkali to give compound (C). The compound (C) further reacts with CH3Cl in the presence of Anhydrous AlCl3. The compound (B) when heated with chloral in acidic medium gives a common insecticide. Identify (A), (B), (C) and (D) giving complete reaction.",
                "answer": """**Identification:**
- **Compound (A):** **Benzene diazonium chloride** [$\\text{C}_6\\text{H}_5\\text{N}_2^+\\text{Cl}^-$]
- **Compound (B):** **Chlorobenzene** [$\\text{C}_6\\text{H}_5\\text{Cl}$]
- **Compound (C):** **Benzene** [$\\text{C}_6\\text{H}_6$]
- **Compound (D):** **Toluene** [$\\text{C}_6\\text{H}_5\\text{CH}_3$]
- *Insecticide:* **DDT**

Reactions:
1. *Sandmeyer Reaction:*
$$\\text{C}_6\\text{H}_5\\text{N}_2^+\\text{Cl}^- \\xrightarrow{\\text{Cu}_2\\text{Cl}_2 / \\text{HCl}} \\text{C}_6\\text{H}_5\\text{Cl} \\; (B) + \\text{N}_2 \\uparrow$$
2. *Reduction of (B) with Ni-Al / NaOH:*
$$\\text{C}_6\\text{H}_5\\text{Cl} + 2[\\text{H}] \\xrightarrow{\\text{Ni-Al / NaOH}} \\text{C}_6\\text{H}_6 \\; (C) + \\text{HCl}$$
3. *Friedel-Crafts Alkylation:*
$$\\text{C}_6\\text{H}_6 + \\text{CH}_3\\text{Cl} \\xrightarrow{\\text{anhyd. AlCl}_3} \\text{C}_6\\text{H}_5\\text{CH}_3 \\; (D) + \\text{HCl}$$
4. *Condensation of (B) with chloral:*
$$\\text{CCl}_3\\text{CHO} + 2\\text{C}_6\\text{H}_5\\text{Cl} \\xrightarrow{\\text{conc. }\\text{H}_2\\text{SO}_4} (p\\text{-Cl-C}_6\\text{H}_4)_2\\text{CH-CCl}_3 + \\text{H}_2\\text{O} \\quad (\\text{DDT})$$"""
            },
            {
                "id": "chem-hr-q3",
                "number": "3",
                "question": "The vapour of organic compound (A) if inhaled causes the loss of consciousness and if heated with conc. HNO3 forms a component of tear gas.\na. How would you prepare compound (A) by using one of the isomers of C3H6O?\nb. What happens when compound (A) is: (a) exposed in air (b) heated with Ag powder (c) condensed with acetone, and (d) heated with aniline in the presence of alc. KOH?",
                "answer": """**Identification:**
Compound (A) is **Chloroform (Trichloromethane, $\\text{CHCl}_3$)**.

**a. Preparation from an isomer of $\\text{C}_3\\text{H}_6\\text{O}$:**
The isomer is **Propan-2-one (Acetone, $\\text{CH}_3\\text{COCH}_3$)**.
$$\\text{CH}_3\\text{COCH}_3 + 3\\text{Cl}_2 \\rightarrow \\text{CCl}_3\\text{COCH}_3 + 3\\text{HCl}$$
$$2\\text{CCl}_3\\text{COCH}_3 + \\text{Ca(OH)}_2 \\rightarrow 2\\text{CHCl}_3 + (\\text{CH}_3\\text{COO})_2\\text{Ca}$$

**b. Reactions of Compound (A):**
- *(a) Exposed to air:* Forms poisonous phosgene:
$$2\\text{CHCl}_3 + \\text{O}_2 \\xrightarrow{h\\nu} 2\\text{COCl}_2 + 2\\text{HCl}$$
- *(b) Heated with Ag powder:* Forms ethyne:
$$2\\text{CHCl}_3 + 6\\text{Ag} \\xrightarrow{\\Delta} \\text{CH}\\equiv\\text{CH} + 6\\text{AgCl}$$
- *(c) Condensed with acetone:* Forms chloretone:
$$\\text{CHCl}_3 + \\text{CH}_3\\text{COCH}_3 \\xrightarrow{\\text{KOH}} (\\text{CH}_3)_2\\text{C(OH)CCl}_3$$
- *(d) Carbylamine reaction with aniline:* Forms phenyl isocyanide (offensive carbylamine smell):
$$\\text{C}_6\\text{H}_5\\text{NH}_2 + \\text{CHCl}_3 + 3\\text{alc. KOH} \\xrightarrow{\\Delta} \\text{C}_6\\text{H}_5\\text{-NC} + 3\\text{KCl} + 3\\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-hr-q4",
                "number": "4",
                "question": "Give reasons:\na. Ether is stored in a bottle containing iron wire.\nb. Though ethanol is an organic compound, it is soluble in water.",
                "answer": """**a. Reason for storing ether with iron wire:**
When diethyl ether is exposed to atmospheric oxygen and light, it forms explosive organic peroxides (hydroperoxides). The iron wire reacts with oxygen and reduces any peroxides back to ether, acting as a preservative and preventing explosive hazards.

**b. Reason for ethanol solubility in water:**
Ethanol contains a polar hydroxyl group ($-\\text{OH}$). The hydrogen atom of the $-\\text{OH}$ group forms strong **intermolecular hydrogen bonds** with water molecules, overcoming hydrophobic interactions of the short ethyl chain and resulting in high miscibility."""
            },
            {
                "id": "chem-hr-q5",
                "number": "5",
                "question": "Give correct chemical reaction for the preparation chlorobenzene from benzene and benzene diazonium chloride.",
                "answer": """**1. From Benzene (Electrophilic Chlorination):**
$$\\text{C}_6\\text{H}_6 + \\text{Cl}_2 \\xrightarrow{\\text{anhyd. FeCl}_3 / \\text{dark}} \\text{C}_6\\text{H}_5\\text{Cl} + \\text{HCl}$$

**2. From Benzene Diazonium Chloride (Sandmeyer Reaction):**
$$\\text{C}_6\\text{H}_5\\text{N}_2^+\\text{Cl}^- \\xrightarrow{\\text{Cu}_2\\text{Cl}_2 / \\text{HCl}} \\text{C}_6\\text{H}_5\\text{Cl} + \\text{N}_2 \\uparrow$$
*(Or Gattermann Reaction using $\\text{Cu}$ powder / $\\text{HCl}$).*"""
            },
            {
                "id": "chem-hr-q6",
                "number": "6",
                "question": "Why is haloarene less reactive than haloalkane towards nucleophilic substitution reactions? iii. A reaction sequence is given below.\na. Write down the reagents and conditions for (P) and (Q)\nb. Draw structural formula of (R) and (S).",
                "answer": """### Why Haloarenes are Less Reactive:
1. **Resonance Effect:** The lone pair of electrons on the chlorine atom is delocalized with the $\\pi$-electron cloud of the benzene ring. This gives the $\\text{C-Cl}$ bond a **partial double-bond character**, making it shorter ($1.69\\text{ \\AA}$ vs $1.78\\text{ \\AA}$) and much stronger than a purely single $\\text{C-Cl}$ bond in haloalkanes.
2. **Hybridization of Carbon:** In haloarenes, chlorine is bonded to an $sp^2$-hybridized carbon atom (more electronegative, holds bonding electrons more tightly) compared to an $sp^3$-hybridized carbon in haloalkanes.
3. **Instability of Phenyl Cation:** Self-ionization to produce a phenyl cation ($S_N1$) is energetically unfavorable because the phenyl cation is unstable.
4. **Electrostatic Repulsion:** The electron-rich aromatic $\\pi$-electron cloud repels approaching nucleophiles.

---

### Reaction Sequence Analysis:
**a. Reagents and conditions:**
- **(P):** $\\text{Cl}_2$ in the presence of $\\text{anhydrous FeCl}_3$ in the dark (for electrophilic chlorination of benzene to chlorobenzene).
- **(Q):** Chloral ($\\text{CCl}_3\\text{CHO}$) in the presence of concentrated $\\text{H}_2\\text{SO}_4$, heated.

**b. Structural Formulae:**
- **(R): Chlorobenzene:** $\\text{C}_6\\text{H}_5\\text{Cl}$
- **(S): DDT [1,1,1-trichloro-2,2-bis(4-chlorophenyl)ethane]:**
$$(p\\text{-Cl-C}_6\\text{H}_4)_2\\text{CH-CCl}_3$$"""
            },
            {
                "id": "chem-hr-q7",
                "number": "7",
                "question": "Give two chemical reactions for the preparation of chlorobenzene. Why does it give ortho and para products during electrophilic substitution reaction? Give its action on chloral.",
                "answer": """**Two Preparation Reactions:**
1. *Chlorination of Benzene:*
$$\\text{C}_6\\text{H}_6 + \\text{Cl}_2 \\xrightarrow{\\text{FeCl}_3, \\text{dark}} \\text{C}_6\\text{H}_5\\text{Cl} + \\text{HCl}$$
2. *Sandmeyer Reaction:*
$$\\text{C}_6\\text{H}_5\\text{N}_2^+\\text{Cl}^- \\xrightarrow{\\text{Cu}_2\\text{Cl}_2 / \\text{HCl}} \\text{C}_6\\text{H}_5\\text{Cl} + \\text{N}_2 \\uparrow$$

**Why it is Ortho- and Para-Directing:**
In chlorobenzene, the unshared lone pairs on the chlorine atom participate in resonance with the benzene ring ($+M$ effect). Resonance structures demonstrate that electron density increases specifically at the **ortho** and **para** positions:
$$\\text{Resonance Hybrid shows } \\delta^- \\text{ at positions 2, 4, and 6}.$$
Consequently, an incoming electrophile ($E^+$) preferentially attacks these electron-rich ortho and para centers. Due to steric hindrance at the ortho position, the **para-isomer is the major product**.

**Action on Chloral:**
Forms DDT:
$$\\text{CCl}_3\\text{CHO} + 2\\text{C}_6\\text{H}_5\\text{Cl} \\xrightarrow{\\text{conc. }\\text{H}_2\\text{SO}_4} (p\\text{-Cl-C}_6\\text{H}_4)_2\\text{CH-CCl}_3 + \\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-hr-q8",
                "number": "8",
                "question": "Write an example of each of the following reactions. Sandmeyer's reaction and Fittig reaction.",
                "answer": """**1. Sandmeyer's Reaction:**
$$\\text{C}_6\\text{H}_5\\text{N}_2^+\\text{Cl}^- \\xrightarrow{\\text{Cu}_2\\text{Cl}_2 / \\text{HCl}} \\text{C}_6\\text{H}_5\\text{Cl} + \\text{N}_2 \\uparrow \\quad (\\text{Chlorobenzene})$$

**2. Fittig Reaction:**
Heating an aryl halide with sodium in dry ether to form a diaryl (diphenyl):
$$2\\text{C}_6\\text{H}_5\\text{Cl} + 2\\text{Na} \\xrightarrow{\\text{dry ether}} \\text{C}_6\\text{H}_5\\text{-C}_6\\text{H}_5 + 2\\text{NaCl} \\quad (\\text{Diphenyl / Biphenyl})$$"""
            },
            {
                "id": "chem-hr-q9",
                "number": "9",
                "question": "Give reason, why are haloalkanes more reactive than haloarenes towards nucleophilic substitution reaction.",
                "answer": """1. **Partial Double Bond Character:** Delocalization of lone-pair electrons on the halogen into the aromatic ring creates resonance structures giving the $\\text{C-X}$ bond partial double bond character in haloarenes.
2. **Difference in Carbon Hybridization:** Haloalkanes have $sp^3$-hybridized carbon (longer $\\text{C-X}$ bond, lower bond dissociation energy), while haloarenes have $sp^2$-hybridized carbon with 33.3% s-character (shorter, stronger $\\text{C-X}$ bond).
3. **Steric and Electrostatic Shielding:** Approaching nucleophiles face electronic repulsion from the aromatic $\\pi$-electron cloud."""
            },
            {
                "id": "chem-hr-q10",
                "number": "10",
                "question": "Why is haloarene less reactive than benzene in electrophilic substitution reaction?",
                "answer": """The halogen atom exhibits two opposing electronic effects:
1. **Strong $-I$ (Inductive) Effect:** Halogens are strongly electronegative and withdraw electron density inductively through the $\\sigma$-bond from the benzene ring.
2. **Weak $+M$ (Resonance) Effect:** Halogen donates its lone pair into the ring through resonance.

The strong electron-withdrawing inductive ($-I$) effect outweighs the resonance ($+M$) effect in terms of overall electron density. Hence, the halogen **deactivates the benzene ring** toward electrophilic attack compared to unsubstituted benzene, making haloarenes less reactive than benzene."""
            },
            {
                "id": "chem-hr-q11",
                "number": "11",
                "question": "What products would you expect when\na. Benzene diazonium chloride is heated with copper powder in presence of HCI.\nb. Chlorobenzene is heated with 2,2,2-trichloroethanal.",
                "answer": """**a. Benzene diazonium chloride with Cu powder and HCl (Gattermann Reaction):**
Yields **Chlorobenzene**:
$$\\text{C}_6\\text{H}_5\\text{N}_2^+\\text{Cl}^- + \\text{Cu} / \\text{HCl} \\rightarrow \\text{C}_6\\text{H}_5\\text{Cl} + \\text{N}_2 \\uparrow + \\text{CuCl}$$

**b. Chlorobenzene with 2,2,2-trichloroethanal (Chloral) in presence of conc. H2SO4:**
Yields **DDT [2,2-bis(4-chlorophenyl)-1,1,1-trichloroethane]**:
$$\\text{CCl}_3\\text{CHO} + 2\\text{C}_6\\text{H}_5\\text{Cl} \\xrightarrow{\\text{conc. }\\text{H}_2\\text{SO}_4} (p\\text{-Cl-C}_6\\text{H}_4)_2\\text{CH-CCl}_3 + \\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-hr-q12",
                "number": "12",
                "question": "Why is nucleophilic substitution difficult in haloarenes?",
                "answer": """Nucleophilic substitution is extremely difficult in haloarenes because:
1. **Resonance stabilization:** Imparts partial double bond character to the $\\text{C-halogen}$ bond.
2. **$sp^2$ Hybridization:** Stronger orbital overlap and shorter bond distance than $sp^3$ in haloalkanes.
3. **Instability of Phenyl Cation:** Carbocation cannot be stabilized by resonance.
4. **Electronic Repulsion:** High $\\pi$-electron density of the ring repels incoming negative nucleophiles."""
            },
            {
                "id": "chem-hr-q13",
                "number": "13",
                "question": "What happens when chlorobenzene is heated with Ni-Al in alkaline medium.",
                "answer": """Chlorobenzene undergoes reduction (dehalogenation) in the presence of $\\text{Ni-Al}$ alloy and aqueous $\\text{NaOH}$ to produce **Benzene**:
$$\\text{C}_6\\text{H}_5\\text{Cl} + 2[\\text{H}] \\xrightarrow{\\text{Ni-Al / aq. NaOH}} \\text{C}_6\\text{H}_6 + \\text{HCl} \\quad (\\textbf{Benzene})$$"""
            },
            {
                "id": "chem-hr-q14",
                "number": "14",
                "question": "How would you convert chlorobenzene into:\na. DDT\nb. Toluene",
                "answer": """**a. Chlorobenzene to DDT:**
Condensation with chloral in the presence of conc. $\\text{H}_2\\text{SO}_4$:
$$2\\text{C}_6\\text{H}_5\\text{Cl} + \\text{CCl}_3\\text{CHO} \\xrightarrow{\\text{conc. }\\text{H}_2\\text{SO}_4} (p\\text{-Cl-C}_6\\text{H}_4)_2\\text{CH-CCl}_3 + \\text{H}_2\\text{O} \\quad (\\text{DDT})$$

**b. Chlorobenzene to Toluene (Wurtz-Fittig Reaction):**
Reaction with chloromethane and sodium in dry ether:
$$\\text{C}_6\\text{H}_5\\text{Cl} + 2\\text{Na} + \\text{CH}_3\\text{Cl} \\xrightarrow{\\text{dry ether}} \\text{C}_6\\text{H}_5\\text{CH}_3 + 2\\text{NaCl} \\quad (\\text{Toluene})$$"""
            },
            {
                "id": "chem-hr-q15",
                "number": "15",
                "question": "Write the action of Monohydroxy benzene with trichloromethane in presence of aqueous NaOH.",
                "answer": """Monohydroxy benzene (Phenol) reacts with trichloromethane (chloroform) in the presence of aqueous $\\text{NaOH}$ at $60–70^\\circ\\text{C}$ (**Reimer-Tiemann Reaction**) to introduce a formyl group ($-\\text{CHO}$) at the ortho position, producing **Salicylaldehyde (2-hydroxybenzaldehyde)**:
$$\\text{C}_6\\text{H}_5\\text{OH} + \\text{CHCl}_3 + 3\\text{NaOH} \\xrightarrow{60-70^\\circ\\text{C}} o\\text{-}\\text{HOC}_6\\text{H}_4\\text{CHO} + 3\\text{NaCl} + 2\\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-hr-q16",
                "number": "16",
                "question": "Write any two methods of preparation of chlorobenzene. Why does it give ortho and para products during electrophilic substitution reaction?",
                "answer": """**Two Methods of Preparation:**
1. *Direct Halogenation of Benzene:*
$$\\text{C}_6\\text{H}_6 + \\text{Cl}_2 \\xrightarrow{\\text{FeCl}_3, \\text{dark}} \\text{C}_6\\text{H}_5\\text{Cl} + \\text{HCl}$$
2. *Sandmeyer Reaction from Benzene Diazonium Chloride:*
$$\\text{C}_6\\text{H}_5\\text{N}_2^+\\text{Cl}^- \\xrightarrow{\\text{Cu}_2\\text{Cl}_2 / \\text{HCl}} \\text{C}_6\\text{H}_5\\text{Cl} + \\text{N}_2 \\uparrow$$

**Why Ortho- and Para-Orienting:**
Due to $+M$ resonance, lone pair electrons on chlorine delocalize into the ring, selectively increasing electron density at the 2-, 4-, and 6-positions (ortho and para). Thus, electrophilic attack occurs at these activated positions, with the para isomer dominating due to minimal steric hindrance."""
            },
            {
                "id": "chem-hr-q17",
                "number": "17",
                "question": "Complete the following reaction:\nC6H5Cl + 2Na + C6H5Cl --(dry ether)--> ?\nC6H5Cl + CH3Cl + 2Na --(dry ether)--> ?",
                "answer": """1. **Fittig Reaction:**
$$\\text{C}_6\\text{H}_5\\text{Cl} + 2\\text{Na} + \\text{Cl-C}_6\\text{H}_5 \\xrightarrow{\\text{dry ether}} \\text{C}_6\\text{H}_5\\text{-C}_6\\text{H}_5 + 2\\text{NaCl} \\quad (\\textbf{Biphenyl / Diphenyl})$$

2. **Wurtz-Fittig Reaction:**
$$\\text{C}_6\\text{H}_5\\text{Cl} + 2\\text{Na} + \\text{Cl-CH}_3 \\xrightarrow{\\text{dry ether}} \\text{C}_6\\text{H}_5\\text{-CH}_3 + 2\\text{NaCl} \\quad (\\textbf{Toluene})$$"""
            },
            {
                "id": "chem-hr-q18",
                "number": "18",
                "question": "An aromatic hydrocarbon (A) on Cl2 and FeCl3 (dark) treatment gives a halogenated aromatic compound (B) which on reacting with chloral in presence of conc. H₂SO₄ gives (C) a famous insecticide DDT. Identify (A), (B) and (C) with structure, IUPAC name and necessary reactions.",
                "answer": """**Identification:**
- **Compound (A):** **Benzene** ($\\text{C}_6\\text{H}_6$)
- **Compound (B):** **Chlorobenzene** ($\\text{C}_6\\text{H}_5\\text{Cl}$)
- **Compound (C):** **DDT** [$\\text{C}_{14}\\text{H}_9\\text{Cl}_5$]  
  *IUPAC Name:* **1,1,1-trichloro-2,2-bis(4-chlorophenyl)ethane**

**Reactions:**
1. Chlorination:
$$\\text{C}_6\\text{H}_6 + \\text{Cl}_2 \\xrightarrow{\\text{FeCl}_3, \\text{dark}} \\text{C}_6\\text{H}_5\\text{Cl} \\; (B) + \\text{HCl}$$
2. Synthesis of DDT:
$$2\\text{C}_6\\text{H}_5\\text{Cl} + \\text{CCl}_3\\text{CHO} \\xrightarrow{\\text{conc. }\\text{H}_2\\text{SO}_4} (p\\text{-Cl-C}_6\\text{H}_4)_2\\text{CH-CCl}_3 \\; (C) + \\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-hr-q19",
                "number": "19",
                "question": "Why is DDT not stored in iron containers?",
                "answer": """DDT is not stored in iron containers because **iron ($\text{Fe}$) acts as a Lewis acid catalyst** that promotes the dehydrochlorination (decomposition) of DDT into **DDE [2,2-bis(p-chlorophenyl)-1,1-dichloroethene]**, causing DDT to lose its insecticidal potency:
$$(p\\text{-Cl-C}_6\\text{H}_4)_2\\text{CH-CCl}_3 \\xrightarrow{\\text{Fe catalyst}} (p\\text{-Cl-C}_6\\text{H}_4)_2\\text{C=CCl}_2 + \\text{HCl}$$"""
            },
            {
                "id": "chem-hr-q20",
                "number": "20",
                "question": "Draw the resonance structure of chlorobenzene and show that C-Cl bond in chlorobenzene is shorter and stronger than that in chloroethane.",
                "answer": """### Resonance Structures of Chlorobenzene:
Chlorine donates its unshared $p$-electron pair into the conjugated $\\pi$-system:
```
   :Cl:              +:Cl:             +:Cl:             +:Cl:             :Cl:
    ||                 ||                ||                ||               |
   /  \\              /  \\              /  \\              /  \\             /  \\
  |    |  <----->   |    |- <----->   |  - |  <----->  -|    | <----->   |    |
   \\  /              \\  /              \\  /              \\  /             \\  /
  (I)                (II)              (III)             (IV)             (V)
```
- Structures II, III, and IV exhibit a **double bond between carbon and chlorine ($\text{C}=\text{Cl}^+$)**.

### Comparison with Chloroethane:
- In **Chlorobenzene**, the partial double-bond character makes the $\\text{C-Cl}$ bond length **$1.69 \\text{ \\AA}$**, and the carbon is $sp^2$-hybridized.
- In **Chloroethane**, the $\\text{C-Cl}$ bond is a pure single bond of length **$1.78 \\text{ \\AA}$**, attached to an $sp^3$-hybridized carbon.

Because bond strength is inversely proportional to bond length, the $\\text{C-Cl}$ bond in chlorobenzene is significantly shorter and stronger."""
            },
            {
                "id": "chem-hr-q21",
                "number": "21",
                "question": "In 1939, after discovery of DDT, war against insects was dramatically changed and saved millions of people from malaria, yellow fever, etc.\na. Write the full form of DDT.\nb. Draw its structure with IUPAC name.\nc. Write the name of the other two chlorinated insecticides.\nd. Which form of DDT hinders egg formation of bird?",
                "answer": """**a. Full Form of DDT:**
**Dichlorodiphenyltrichloroethane**

**b. IUPAC Name and Structure:**
- *IUPAC Name:* **1,1,1-trichloro-2,2-bis(4-chlorophenyl)ethane**
- *Structure:*
$$(p\\text{-Cl-C}_6\\text{H}_4)_2\\text{CH-CCl}_3$$

**c. Two other Chlorinated Insecticides:**
1. **BHC** (Benzene Hexachloride / Gammexane / Lindane)
2. **Aldrin** (or Chlordane / Dieldrin)

**d. Form that hinders egg formation:**
The persistent metabolite of DDT, **DDE [2,2-bis(p-chlorophenyl)-1,1-dichloroethene]**, along with $p,p'\\text{-DDT}$, causes eggshell thinning in birds by inhibiting the enzyme calcium ATPase in the oviduct gland."""
            },
            {
                "id": "chem-hr-q22",
                "number": "22",
                "question": "An aromatic compound (P) with one chlorine atom in benzene ring when heated with 2.2.2-trichloroethanal in presence of conc.H₂SO₄ gives an insecticide (Q). The compound (A) when reacted with conc.H₂SO₄ gives (R). (P) also gives compound (S) when heated with chloroethane and sodium in dry ether.\na. Identify (P), (Q), (R) and (S).\nb. The reaction of (P) with aq. NaOH is difficult than with chloroethane. Justify with suitable explanation.\nc. How would you obtain compound (P) from benzene diazonium chloride?\nd. Convert (P) into an aniline.",
                "answer": """**a. Identification:**
- **(P):** **Chlorobenzene** ($\\text{C}_6\\text{H}_5\\text{Cl}$)
- **(Q):** **DDT** [$(p\\text{-Cl-C}_6\\text{H}_4)_2\\text{CH-CCl}_3$]
- **(R):** **p-chlorobenzenesulphonic acid**
- **(S):** **Ethylbenzene** ($\\text{C}_6\\text{H}_5\\text{CH}_2\\text{CH}_3$)

**b. Justification:**
Chlorobenzene contains a partial double bond ($\text{C-Cl}$) due to resonance with the benzene ring and an $sp^2$ carbon, whereas chloroethane has a single bond with an $sp^3$ carbon. Hence, displacement by $\\text{OH}^-$ requires extreme conditions ($300^\\circ\\text{C}, 200\\text{ atm}$, Dow's process).

**c. Preparation from Benzene Diazonium Chloride:**
Sandmeyer reaction:
$$\\text{C}_6\\text{H}_5\\text{N}_2^+\\text{Cl}^- \\xrightarrow{\\text{Cu}_2\\text{Cl}_2 / \\text{HCl}} \\text{C}_6\\text{H}_5\\text{Cl} + \\text{N}_2 \\uparrow$$

**d. Convert (P) into Aniline:**
Heat chlorobenzene with aqueous ammonia in the presence of cuprous oxide at $200^\\circ\\text{C}$ under high pressure:
$$2\\text{C}_6\\text{H}_5\\text{Cl} + 2\\text{NH}_3 + \\text{Cu}_2\\text{O} \\xrightarrow{200^\\circ\\text{C}, \\text{press.}} 2\\text{C}_6\\text{H}_5\\text{NH}_2 + \\text{Cu}_2\\text{Cl}_2 + \\text{H}_2\\text{O} \\quad (\\textbf{Aniline})$$"""
            },
            {
                "id": "chem-hr-q23",
                "number": "23",
                "question": "Chloroquine, a medicine used to treat malaria, has following structure.\na. Which haloarene moiety is present in chloroquine?\nb. Does chlorobenzene occur naturally in the environment?\nc. Name any two herbicides which is made from chlorobenzene.\nd. What might be the environmental impact of the use of halogenated compounds?",
                "answer": """**a. Haloarene Moiety:**
The **7-chloroquinoline** aromatic bicyclic core moiety.

**b. Natural Occurrence:**
No. Chlorobenzene is entirely anthropogenic (man-made synthetic chemical) and does not occur naturally in the environment.

**c. Two Herbicides derived from Chlorobenzene:**
1. **2,4-D** (2,4-dichlorophenoxyacetic acid)
2. **2,4,5-T** (2,4,5-trichlorophenoxyacetic acid)

**d. Environmental Impacts:**
1. **Bioaccumulation & Biomagnification:** Fat-soluble chlorinated hydrocarbons accumulate up trophic levels, causing toxic effects in apex predators.
2. **Eggshell Thinning:** Leads to reproductive failure in raptor bird populations.
3. **Ozone Layer Depletion & Persistence:** Resist microbial breakdown, persisting as environmental pollutants."""
            }
        ]
    }
