# chem_haloalkanes.py
# Haloalkanes questions 1 to 44

def get_haloalkanes():
    return {
        "name": "Haloalkanes",
        "questions": [
            {
                "id": "chem-ha-q1",
                "number": "1",
                "question": "The chlorinated compound 'A' reacts with acetone to give sleep-inducing drug.\na. How would you prepare compound 'A' by using one of the isomers of C2H6O?\nb. What happens when compound 'A' is:\ni. Exposed in air?\nii. Heated with phenol in the presence of aq. NaOH? [2]",
                "answer": """**Identification:**
Compound 'A' is **Chloroform (Trichloromethane, $\\text{CHCl}_3$)**. It condenses with acetone in the presence of $\\text{KOH}$ to give **Chloretone** (a hypnotic, sleep-inducing drug).

**a. Preparation of Compound 'A' from an isomer of $\\text{C}_2\\text{H}_6\\text{O}$:**
The isomer of $\\text{C}_2\\text{H}_6\\text{O}$ having a methyl ketone or methyl carbinol group is **Ethanol ($\text{CH}_3\\text{CH}_2\\text{OH}$)**.
Chloroform is prepared by heating ethanol with bleaching powder paste (haloform reaction):
1. *Oxidation:* $\\text{CaOCl}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{Ca(OH)}_2 + \\text{Cl}_2$  
   $\\text{CH}_3\\text{CH}_2\\text{OH} + \\text{Cl}_2 \\rightarrow \\text{CH}_3\\text{CHO} + 2\\text{HCl}$
2. *Chlorination:* $\\text{CH}_3\\text{CHO} + 3\\text{Cl}_2 \\rightarrow \\text{CCl}_3\\text{CHO} + 3\\text{HCl}$ (Chloral)
3. *Hydrolysis:* $2\\text{CCl}_3\\text{CHO} + \\text{Ca(OH)}_2 \\rightarrow 2\\text{CHCl}_3 + (\\text{HCOO})_2\\text{Ca}$ (Calcium formate)

**b. Reactions of Compound 'A' ($\\text{CHCl}_3$):**
i. **Exposed to air and sunlight:**  
Chloroform undergoes slow auto-oxidation to form highly poisonous **carbonyl chloride (phosgene gas)**:
$$2\\text{CHCl}_3 + \\text{O}_2 \\xrightarrow{\\text{sunlight}} 2\\text{COCl}_2 + 2\\text{HCl}$$

ii. **Heated with phenol and aq. NaOH (Reimer-Tiemann Reaction):**  
An aldehyde group ($-\\text{CHO}$) is introduced at the ortho position of phenol, yielding **Salicylaldehyde (2-hydroxybenzaldehyde)**:
$$\\text{C}_6\\text{H}_5\\text{OH} + \\text{CHCl}_3 + 3\\text{NaOH} \\xrightarrow{60-70^\\circ\\text{C}} o\\text{-C}_6\\text{H}_4(\\text{OH})\\text{CHO} + 3\\text{NaCl} + 2\\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-ha-q2",
                "number": "2",
                "question": "a. Identify the compounds (A) and (B).\nb. Starting from compound (A), how would you obtain 2,3-dimethylbutane?\nc. Convert compound (B) into propene.\nd. Predict the product, when compound (A) is heated with sodium methoxide. [2+1+1+1]",
                "answer": """**a. Identification:**
- Compound (A) is **2-chloropropane (isopropyl chloride, $\\text{CH}_3\\text{-CH(Cl)-CH}_3$)**.
- Compound (B) is **1-chloropropane (n-propyl chloride, $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Cl}$)**.

**b. Preparation of 2,3-dimethylbutane from (A):**
By Wurtz reaction: heating 2-chloropropane with sodium in dry ether:
$$2\\text{CH}_3\\text{-CH(Cl)-CH}_3 + 2\\text{Na} \\xrightarrow{\\text{dry ether}} (\\text{CH}_3)_2\\text{CH-CH}(\\text{CH}_3)_2 + 2\\text{NaCl}$$
The product is **2,3-dimethylbutane**.

**c. Conversion of (B) into propene:**
By dehydrohalogenation: heating 1-chloropropane with alcoholic $\\text{KOH}$:
$$\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Cl} + \\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_3\\text{-CH=CH}_2 + \\text{KCl} + \\text{H}_2\\text{O}$$

**d. Action of sodium methoxide on (A) (Williamson Ether Synthesis vs Elimination):**
When secondary haloalkane 2-chloropropane reacts with sodium methoxide ($\\text{CH}_3\\text{ONa}$), the major product formed via elimination is **Propene ($\text{CH}_3\\text{CH=CH}_2$)**, along with a minor substitution product **2-methoxypropane ($\text{CH}_3\\text{-CH(OCH}_3\\text{)-CH}_3$)**:
$$\\text{CH}_3\\text{CH(Cl)CH}_3 + \\text{CH}_3\\text{ONa} \\xrightarrow{\\Delta} \\text{CH}_3\\text{-CH=CH}_2 + \\text{CH}_3\\text{OH} + \\text{NaCl}$$"""
            },
            {
                "id": "chem-ha-q3",
                "number": "3",
                "question": "Give an example of each of the following reactions.\na. Reimer-Tiemann's reaction\nb. Wurtz’s reaction\nc. Dehydrohalogenation reaction\nd. Carbylamine reaction\ne. Markovnikov’s rule and peroxide effect\nf. Elimination reaction",
                "answer": """**a. Reimer-Tiemann Reaction:**
$$\\text{C}_6\\text{H}_5\\text{OH} + \\text{CHCl}_3 + 3\\text{NaOH} \\xrightarrow{65^\\circ\\text{C}} o\\text{-}\\text{HOC}_6\\text{H}_4\\text{CHO} + 3\\text{NaCl} + 2\\text{H}_2\\text{O} \\; (\\text{Salicylaldehyde})$$

**b. Wurtz Reaction:**
$$2\\text{CH}_3\\text{CH}_2\\text{Br} + 2\\text{Na} \\xrightarrow{\\text{dry ether}} \\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_3 + 2\\text{NaBr} \\; (n\\text{-Butane})$$

**c. Dehydrohalogenation Reaction:**
$$\\text{CH}_3\\text{CH}_2\\text{Cl} + \\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_2\\text{=CH}_2 + \\text{KCl} + \\text{H}_2\\text{O} \\; (\\text{Ethene})$$

**d. Carbylamine Reaction (Isocyanide test):**
$$\\text{CH}_3\\text{CH}_2\\text{NH}_2 + \\text{CHCl}_3 + 3\\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_3\\text{CH}_2\\text{-N}\\equiv\\text{C} + 3\\text{KCl} + 3\\text{H}_2\\text{O} \\; (\\text{Ethyl isocyanide, extremely foul smell})$$

**e. Markovnikov's Rule and Peroxide Effect:**
- *Markovnikov addition:* $\\text{CH}_3\\text{-CH=CH}_2 + \\text{HBr} \\rightarrow \\text{CH}_3\\text{-CH(Br)-CH}_3$ (2-bromopropane, major)
- *Peroxide Effect (Kharasch effect):* $\\text{CH}_3\\text{-CH=CH}_2 + \\text{HBr} \\xrightarrow{\\text{Peroxide}} \\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Br}$ (1-bromopropane, major)

**f. Elimination Reaction (Saytzeff's elimination):**
$$\\text{CH}_3\\text{-CH}_2\\text{-CH(Br)-CH}_3 + \\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_3\\text{-CH=CH-CH}_3 \\; (\\text{But-2-ene, 81\\%}) + \\text{CH}_3\\text{CH}_2\\text{CH=CH}_2 \\; (\\text{But-1-ene, 19\\%})$$"""
            },
            {
                "id": "chem-ha-q4",
                "number": "4",
                "question": "A Sweet-smelling organic compound (A) slowly oxidized by air in the presence of sunlight to give highly poisonous gas carbonyl chloride.\na. Why is the above compound (A) stored in dark and brown bottle?\nb. Give principle reaction involved in the preparation of compound (A) from ethanol.\nc. How would you convert compound (A) into (a) Chloretone (b) Chloropicrin (c) ethyne\nd. Why cannot the compound (A) give white ppt with AgNO3 solution?",
                "answer": """Compound (A) is **Chloroform (Trichloromethane, $\\text{CHCl}_3$)**.

**a. Storage in dark brown bottles:**
When exposed to air and sunlight, chloroform undergoes photo-oxidation to produce deadly carbonyl chloride (phosgene gas, $\\text{COCl}_2$). Dark brown bottles block UV/visible light, and filling them to the brim excludes air. Additionally, 1% ethanol is added to act as a negative catalyst and convert any trace phosgene formed into harmless diethyl carbonate:
$$\\text{COCl}_2 + 2\\text{C}_2\\text{H}_5\\text{OH} \\rightarrow (\\text{C}_2\\text{H}_5\\text{O})_2\\text{CO} + 2\\text{HCl}$$

**b. Preparation from Ethanol:**
$$\\text{CH}_3\\text{CH}_2\\text{OH} \\xrightarrow{\\text{CaOCl}_2/\\text{H}_2\\text{O}} \\text{CH}_3\\text{CHO} \\xrightarrow{3\\text{Cl}_2} \\text{CCl}_3\\text{CHO} \\xrightarrow{\\text{Ca(OH)}_2} 2\\text{CHCl}_3 + (\\text{HCOO})_2\\text{Ca}$$

**c. Conversions:**
- *(a) Chloretone:* $\\text{CHCl}_3 + \\text{CH}_3\\text{COCH}_3 \\xrightarrow{\\text{KOH}} (\\text{CH}_3)_2\\text{C(OH)CCl}_3$
- *(b) Chloropicrin:* $\\text{CHCl}_3 + \\text{HNO}_3 \\text{ (conc.)} \\xrightarrow{\\Delta} \\text{CCl}_3\\text{NO}_2 + \\text{H}_2\\text{O}$
- *(c) Ethyne:* $2\\text{CHCl}_3 + 6\\text{Ag} \\xrightarrow{\\Delta} \\text{CH}\\equiv\\text{CH} + 6\\text{AgCl}$

**d. Reason for no white ppt with $\\text{AgNO}_3$:**
Chloroform is a purely covalent compound. The $\\text{C-Cl}$ bond is covalent and does not ionize in water to generate free chloride ions ($\\text{Cl}^-$). Since precipitation of $\\text{AgCl}$ requires free $\\text{Cl}^-$ ions, pure chloroform gives no precipitate with $\\text{AgNO}_3$."""
            },
            {
                "id": "chem-ha-q5",
                "number": "5",
                "question": "You are given an organic compound having molecular formula C3H7X.\na. Write down a primary and a secondary haloalkane giving their IUPAC name.\nb. Give proper reaction sequence to convert the primary haloalkane into the secondary haloalkane.\nc. What product is obtained, when the secondary haloalkane is subjected to Wurtz reaction?",
                "answer": """**a. Primary and Secondary Haloalkanes:**
- Primary ($1^\\circ$): $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{X}$ $\\rightarrow$ **1-halopropane**
- Secondary ($2^\\circ$): $\\text{CH}_3\\text{-CH(X)-CH}_3$ $\\rightarrow$ **2-halopropane**

**b. Conversion of 1-halopropane into 2-halopropane:**
1. *Dehydrohalogenation:* Boil 1-halopropane with alcoholic $\\text{KOH}$ to obtain propene:
$$\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{X} + \\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_3\\text{-CH=CH}_2 + \\text{KX} + \\text{H}_2\\text{O}$$
2. *Markovnikov Addition:* Add hydrogen halide ($\text{HX}$) to propene:
$$\\text{CH}_3\\text{-CH=CH}_2 + \\text{HX} \\rightarrow \\text{CH}_3\\text{-CH(X)-CH}_3 \\; (\\text{2-halopropane})$$

**c. Wurtz Reaction of Secondary Haloalkane:**
Heating 2-halopropane with sodium in dry ether gives **2,3-dimethylbutane**:
$$2\\text{CH}_3\\text{CH(X)CH}_3 + 2\\text{Na} \\xrightarrow{\\text{dry ether}} (\\text{CH}_3)_2\\text{CH-CH}(\\text{CH}_3)_2 + 2\\text{NaX}$$"""
            },
            {
                "id": "chem-ha-q6",
                "number": "6",
                "question": "An organic compound (A) when heated with Ag powder gives C2H2 and form carbonyl chloride when it is exposed to air.\na. Identify the compound (A)\nb. Write reaction for the laboratory method of preparation of (A)\nc. What happens when the compound (A) is treated with conc.nitric acid.\nd. Convert (A) into methanoic acid",
                "answer": """**a. Identification:**
Compound (A) is **Chloroform (Trichloromethane, $\\text{CHCl}_3$)**.

**b. Laboratory preparation:**
Heating paste of bleaching powder with acetone:
$$\\text{CaOCl}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{Ca(OH)}_2 + \\text{Cl}_2$$
$$\\text{CH}_3\\text{COCH}_3 + 3\\text{Cl}_2 \\rightarrow \\text{CCl}_3\\text{COCH}_3 + 3\\text{HCl} \\; (\\text{Trichloroacetone})$$
$$2\\text{CCl}_3\\text{COCH}_3 + \\text{Ca(OH)}_2 \\rightarrow 2\\text{CHCl}_3 + (\\text{CH}_3\\text{COO})_2\\text{Ca} \\; (\\text{Calcium acetate})$$

**c. Reaction with conc. $\\text{HNO}_3$:**
$$\\text{CHCl}_3 + \\text{HNO}_3 \\text{ (conc.)} \\xrightarrow{\\Delta} \\text{CCl}_3\\text{NO}_2 + \\text{H}_2\\text{O}$$
Yields **Chloropicrin (nitrochloroform/tear gas)**.

**d. Conversion of (A) into methanoic acid:**
Hydrolyze chloroform with aqueous $\\text{KOH}$ followed by acidification:
$$\\text{CHCl}_3 + 4\\text{KOH (aq)} \\xrightarrow{\\Delta} \\text{HCOOK} + 3\\text{KCl} + 2\\text{H}_2\\text{O}$$
$$\\text{HCOOK} + \\text{HCl} \\rightarrow \\text{HCOOH} + \\text{KCl} \\; (\\text{Methanoic acid})$$"""
            },
            {
                "id": "chem-ha-q7",
                "number": "7",
                "question": "An unsaturated hydrocarbon (C3H6) undergoes Markovnikov's rule to give (A). Compound (A) is hydrolyzed with aqueous alkali to yield (B). When (B) is treated with PBr3, compound (C) is produced. (C) reacts with AgCN (alc.) to give another compound (D). The compound (D) if reduced with LiAlH4, produce (E).\na. Define Markovnikov's rule.\nb. Identify (A), (B), (C), (D) and (E) with chemical reaction.\nc. How does E react with nitrous acid?\nd. How would you convert (B) into C3Н8?",
                "answer": """**a. Markovnikov's Rule:**
When an unsymmetrical reagent (such as $\\text{H-X}$) adds to an unsymmetrical alkene, the negative part of the addendum attaches preferentially to the doubly bonded carbon atom carrying the smaller number of hydrogen atoms.

**b. Identification:**
- $\\text{C}_3\\text{H}_6$: Propene ($\\text{CH}_3\\text{-CH=CH}_2$)
- (A): **2-bromopropane** [$\\text{CH}_3\\text{CH(Br)CH}_3$]
- (B): **Propan-2-ol** [$\\text{CH}_3\\text{CH(OH)CH}_3$]
- (C): **2-bromopropane** [$\\text{CH}_3\\text{CH(Br)CH}_3$]
- (D): **Isopropyl isocyanide** [$(\\text{CH}_3)_2\\text{CH-N}\\equiv\\text{C}$]
- (E): **N-methylpropan-2-amine** (a secondary amine) [$(\\text{CH}_3)_2\\text{CH-NH-CH}_3$]

Reactions:
1. $\\text{CH}_3\\text{CH=CH}_2 + \\text{HBr} \\rightarrow \\text{CH}_3\\text{CH(Br)CH}_3 \\; (A)$
2. $\\text{CH}_3\\text{CH(Br)CH}_3 + \\text{aq. KOH} \\rightarrow \\text{CH}_3\\text{CH(OH)CH}_3 \\; (B) + \\text{KBr}$
3. $3\\text{CH}_3\\text{CH(OH)CH}_3 + \\text{PBr}_3 \\rightarrow 3\\text{CH}_3\\text{CH(Br)CH}_3 \\; (C) + \\text{H}_3\\text{PO}_3$
4. $\\text{CH}_3\\text{CH(Br)CH}_3 + \\text{AgCN} \\rightarrow (\\text{CH}_3)_2\\text{CH-NC} \\; (D) + \\text{AgBr}$
5. $(\\text{CH}_3)_2\\text{CH-NC} \\xrightarrow{\\text{LiAlH}_4} (\\text{CH}_3)_2\\text{CH-NH-CH}_3 \\; (E)$

**c. Reaction of E with nitrous acid:**
Secondary amine reacts with $\\text{HNO}_2$ to give a yellow oily N-nitrosamine:
$$(\\text{CH}_3)_2\\text{CH-NH-CH}_3 + \\text{HONO} \\rightarrow (\\text{CH}_3)_2\\text{CH-N(NO)-CH}_3 + \\text{H}_2\\text{O}$$

**d. Conversion of (B) into propane ($\\text{C}_3\\text{H}_8$):**
Dehydrate (B) with conc. $\\text{H}_2\\text{SO}_4$ at $170^\\circ\\text{C}$ to propene, followed by catalytic hydrogenation:
$$\\text{CH}_3\\text{CH(OH)CH}_3 \\xrightarrow{\\text{conc. }\\text{H}_2\\text{SO}_4, 170^\\circ\\text{C}} \\text{CH}_3\\text{-CH=CH}_2 \\xrightarrow{\\text{H}_2 / \\text{Ni}} \\text{CH}_3\\text{CH}_2\\text{CH}_3 \\; (\\text{Propane})$$"""
            },
            {
                "id": "chem-ha-q8",
                "number": "8",
                "question": "What happens when:\na. Iodoform is heated with silver powder.\nb. Chlorobenzene is treated with chloral in acidic medium.",
                "answer": """**a. Iodoform with silver powder:**
Heating iodoform with finely divided silver powder gives **ethyne (acetylene)**:
$$2\\text{CHI}_3 + 6\\text{Ag} \\xrightarrow{\\Delta} \\text{CH}\\equiv\\text{CH} + 6\\text{AgI}$$

**b. Chlorobenzene with chloral in acidic medium:**
Condensation of two molecules of chlorobenzene with chloral in the presence of conc. $\\text{H}_2\\text{SO}_4$ produces **DDT [2,2-bis(p-chlorophenyl)-1,1,1-trichloroethane]**:
$$\\text{CCl}_3\\text{CHO} + 2\\text{C}_6\\text{H}_5\\text{Cl} \\xrightarrow{\\text{conc. }\\text{H}_2\\text{SO}_4} (p\\text{-Cl-C}_6\\text{H}_4)_2\\text{CH-CCl}_3 + \\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-ha-q9",
                "number": "9",
                "question": "How does chloroform react with (i) acetone (ii) silver powder [1+1]",
                "answer": """**(i) Reaction with acetone:**
Condenses in the presence of solid $\\text{KOH}$ to form **chloretone**:
$$\\text{CH}_3\\text{COCH}_3 + \\text{CHCl}_3 \\xrightarrow{\\text{KOH}} (\\text{CH}_3)_2\\text{C(OH)CCl}_3$$

**(ii) Reaction with silver powder:**
Yields **ethyne (acetylene)**:
$$2\\text{CHCl}_3 + 6\\text{Ag} \\xrightarrow{\\Delta} \\text{HC}\\equiv\\text{CH} + 6\\text{AgCl}$$"""
            },
            {
                "id": "chem-ha-q10",
                "number": "10",
                "question": "Identify the compounds (x) and write its IUPAC name.",
                "answer": """The reaction represents:
$$\\text{CH}_3\\text{-CH=CH}_2 + \\text{HBr} \\xrightarrow{\\text{Peroxide}} \\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Br} \\; (X)$$
- Compound (X) is **1-bromopropane** (formed according to anti-Markovnikov's peroxide rule).
- IUPAC Name: **1-bromopropane**."""
            },
            {
                "id": "chem-ha-q11",
                "number": "11",
                "question": "What happens when\na. chlorobenzene is treated with chloral\nb. trichroromethane is heated with conc. Nitric acid",
                "answer": """**a. Chlorobenzene with chloral:**
In the presence of conc. $\\text{H}_2\\text{SO}_4$, chlorobenzene condenses with chloral to form **DDT**:
$$\\text{CCl}_3\\text{CHO} + 2\\text{C}_6\\text{H}_5\\text{Cl} \\xrightarrow{\\text{conc. }\\text{H}_2\\text{SO}_4} (p\\text{-Cl-C}_6\\text{H}_4)_2\\text{CH-CCl}_3 + \\text{H}_2\\text{O}$$

**b. Trichloromethane with conc. nitric acid:**
Trichloromethane (chloroform) is nitrated to yield **Chloropicrin (nitrochloroform)**:
$$\\text{CHCl}_3 + \\text{HNO}_3 \\text{ (conc.)} \\xrightarrow{\\Delta} \\text{CCl}_3\\text{NO}_2 + \\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-ha-q12",
                "number": "12",
                "question": "An alkene A undergoes addition with HBr to give B. When B is heated with sodium in the presence of dry ether give 2,3-dimethylbutane. Identify A and B.",
                "answer": """Heating B with sodium gives 2,3-dimethylbutane:
$$2\\text{B} + 2\\text{Na} \\xrightarrow{\\text{dry ether}} (\\text{CH}_3)_2\\text{CH-CH}(\\text{CH}_3)_2 + 2\\text{NaBr}$$
Therefore, B must be **2-bromopropane [$\\text{CH}_3\\text{-CH(Br)-CH}_3$]**.

Since alkene A adds $\\text{HBr}$ according to Markovnikov's rule to give 2-bromopropane:
$$\\text{A} = \\text{Propene [}\\text{CH}_3\\text{-CH=CH}_2\\text{]}$$
$$\\text{CH}_3\\text{-CH=CH}_2 + \\text{HBr} \\rightarrow \\text{CH}_3\\text{-CH(Br)-CH}_3 \\; (B)$$

- Compound A: **Propene**
- Compound B: **2-bromopropane**"""
            },
            {
                "id": "chem-ha-q13",
                "number": "13",
                "question": "Identify A and B give their IUPAC names in the following sequence of reaction.\nCH3CH2Br + alc. KCN -> A --(H3O+)--> B",
                "answer": """Reaction sequence:
1. $\\text{CH}_3\\text{CH}_2\\text{Br} + \\text{alc. KCN} \\xrightarrow{\\Delta} \\text{CH}_3\\text{CH}_2\\text{CN} + \\text{KBr}$
2. $\\text{CH}_3\\text{CH}_2\\text{CN} + 2\\text{H}_2\\text{O} + \\text{H}^+ \\rightarrow \\text{CH}_3\\text{CH}_2\\text{COOH} + \\text{NH}_4^+$

- **Compound A:** $\\text{CH}_3\\text{CH}_2\\text{CN}$ $\\rightarrow$ IUPAC: **Propanenitrile** (Ethyl cyanide)
- **Compound B:** $\\text{CH}_3\\text{CH}_2\\text{COOH}$ $\\rightarrow$ IUPAC: **Propanoic acid**"""
            },
            {
                "id": "chem-ha-q14",
                "number": "14",
                "question": "Identify A and B in the following sequence of the reaction and give their IUPAC name.\nCH3CH2CH2Cl + alc. KOH -> A --(HBr/Peroxide)--> B",
                "answer": """Reaction sequence:
1. $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Cl} + \\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_3\\text{-CH=CH}_2 + \\text{KCl} + \\text{H}_2\\text{O}$
2. $\\text{CH}_3\\text{-CH=CH}_2 + \\text{HBr} \\xrightarrow{\\text{Peroxide}} \\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Br}$

- **Compound A:** $\\text{CH}_3\\text{-CH=CH}_2$ $\\rightarrow$ IUPAC: **Propene**
- **Compound B:** $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Br}$ $\\rightarrow$ IUPAC: **1-bromopropane**"""
            },
            {
                "id": "chem-ha-q15",
                "number": "15",
                "question": "Write down the structure and IUPAC name of secondary haloalkane of C3H7X. What happens when the secondary haloalkane is heated with Na in the presence of dry ether?",
                "answer": """**Structure and IUPAC name:**
$$\\text{CH}_3\\text{-CH(X)-CH}_3$$
- IUPAC Name: **2-halopropane** (e.g., 2-chloropropane or 2-bromopropane).

**Action of Na in dry ether (Wurtz Reaction):**
$$2\\text{CH}_3\\text{CH(X)CH}_3 + 2\\text{Na} \\xrightarrow{\\text{dry ether}} (\\text{CH}_3)_2\\text{CH-CH}(\\text{CH}_3)_2 + 2\\text{NaX}$$
Yields **2,3-dimethylbutane**."""
            },
            {
                "id": "chem-ha-q16",
                "number": "16",
                "question": "A haloalkane (M) reacts with aq. NaOH to give isopropyl alcohol. What major product would you get when (M) is heated with Na in the presence of dry ether.",
                "answer": """Since haloalkane (M) gives isopropyl alcohol [$\\text{CH}_3\\text{CH(OH)CH}_3$] on hydrolysis with aq. $\\text{NaOH}$, (M) is **2-halopropane** (such as 2-chloropropane or 2-bromopropane).

When (M) is heated with Na in dry ether, it undergoes Wurtz coupling to produce **2,3-dimethylbutane**:
$$2\\text{CH}_3\\text{-CH(X)-CH}_3 + 2\\text{Na} \\xrightarrow{\\text{dry ether}} (\\text{CH}_3)_2\\text{CH-CH}(\\text{CH}_3)_2 + 2\\text{NaX}$$"""
            },
            {
                "id": "chem-ha-q17",
                "number": "17",
                "question": "Give the major products in the following equation.\nCH3-CH=CH2 + HBr -> Major product\nCH3CH2CH2Br + alc. KOH -> Major product",
                "answer": """1. Addition of $\\text{HBr}$ to propene obeys Markovnikov's rule:
$$\\text{CH}_3\\text{-CH=CH}_2 + \\text{HBr} \\rightarrow \\text{CH}_3\\text{-CH(Br)-CH}_3 \\quad (\\textbf{2-bromopropane})$$

2. Elimination of 1-bromopropane with alcoholic $\\text{KOH}$:
$$\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Br} + \\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_3\\text{-CH=CH}_2 + \\text{KBr} + \\text{H}_2\\text{O} \\quad (\\textbf{Propene})$$"""
            },
            {
                "id": "chem-ha-q18",
                "number": "18",
                "question": "Starting from iodomethane, how would you prepare Ethane and Ethene.",
                "answer": """**1. Preparation of Ethane:**
By Wurtz reaction: heat iodomethane with sodium metal in dry ether:
$$2\\text{CH}_3\\text{I} + 2\\text{Na} \\xrightarrow{\\text{dry ether}} \\text{CH}_3\\text{-CH}_3 + 2\\text{NaI} \\quad (\\text{Ethane})$$

**2. Preparation of Ethene:**
- Step 1: Convert ethane to bromoethane:
$$\\text{CH}_3\\text{-CH}_3 + \\text{Br}_2 \\xrightarrow{h\\nu} \\text{CH}_3\\text{CH}_2\\text{Br} + \\text{HBr}$$
- Step 2: Dehydrohalogenate bromoethane with alc. $\\text{KOH}$:
$$\\text{CH}_3\\text{CH}_2\\text{Br} + \\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_2\\text{=CH}_2 + \\text{KBr} + \\text{H}_2\\text{O} \\quad (\\text{Ethene})$$"""
            },
            {
                "id": "chem-ha-q19",
                "number": "19",
                "question": "Convert 1-bromopropane to 2-bromopropane.",
                "answer": """**Step 1:** Dehydrohalogenation with alcoholic $\\text{KOH}$:
$$\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Br} + \\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_3\\text{-CH=CH}_2 + \\text{KBr} + \\text{H}_2\\text{O} \\quad (\\text{Propene})$$

**Step 2:** Addition of $\\text{HBr}$ according to Markovnikov's rule:
$$\\text{CH}_3\\text{-CH=CH}_2 + \\text{HBr} \\rightarrow \\text{CH}_3\\text{-CH(Br)-CH}_3 \\quad (\\text{2-bromopropane})$$"""
            },
            {
                "id": "chem-ha-q20",
                "number": "20",
                "question": "Convert 2-chloropropane into 1-chloropropane.",
                "answer": """**Step 1:** Elimination with alcoholic $\\text{KOH}$:
$$\\text{CH}_3\\text{-CH(Cl)-CH}_3 + \\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_3\\text{-CH=CH}_2 + \\text{KCl} + \\text{H}_2\\text{O}$$

**Step 2:** Anti-Markovnikov addition of $\\text{HBr}$ in the presence of organic peroxide:
$$\\text{CH}_3\\text{-CH=CH}_2 + \\text{HBr} \\xrightarrow{\\text{Peroxide}} \\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Br}$$

**Step 3:** Hydrolysis and chlorination:
$$\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Br} + \\text{aq. KOH} \\rightarrow \\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{OH} \\xrightarrow{\\text{SOCl}_2 / \\text{Pyridine}} \\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Cl} + \\text{SO}_2 + \\text{HCl}$$"""
            },
            {
                "id": "chem-ha-q21",
                "number": "21",
                "question": "What happens when chloroethane is heated with alcoholic KOH.",
                "answer": """Chloroethane undergoes $\\beta$-elimination (dehydrohalogenation) to give **ethene**:
$$\\text{CH}_3\\text{CH}_2\\text{Cl} + \\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_2\\text{=CH}_2 + \\text{KCl} + \\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-ha-q22",
                "number": "22",
                "question": "Identify the major products A and B in the following reaction.\nCH3CH2Br + alc. KCN -> A --(H2/Ni)--> B",
                "answer": """$$\\text{CH}_3\\text{CH}_2\\text{Br} + \\text{alc. KCN} \\rightarrow \\text{CH}_3\\text{CH}_2\\text{CN} \\; (A) + \\text{KBr}$$
$$\\text{CH}_3\\text{CH}_2\\text{CN} + 2\\text{H}_2 \\xrightarrow{\\text{Ni}} \\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{NH}_2 \\; (B)$$

- **A:** **Propanenitrile** ($\text{CH}_3\text{CH}_2\text{CN}$)
- **B:** **Propan-1-amine** ($\text{CH}_3\text{CH}_2\text{CH}_2\text{NH}_2$)"""
            },
            {
                "id": "chem-ha-q23",
                "number": "23",
                "question": "Identify A and B in the following reaction:\nCH3CH2Br + AgCN (alc.) -> A --(LiAlH4)--> B",
                "answer": """$$\\text{CH}_3\\text{CH}_2\\text{Br} + \\text{alc. AgCN} \\rightarrow \\text{CH}_3\\text{CH}_2\\text{-NC} \\; (A) + \\text{AgBr}$$
$$\\text{CH}_3\\text{CH}_2\\text{-NC} \\xrightarrow{\\text{LiAlH}_4} \\text{CH}_3\\text{CH}_2\\text{-NH-CH}_3 \\; (B)$$

- **A:** **Ethyl isocyanide** ($\text{CH}_3\text{CH}_2\text{NC}$)
- **B:** **N-methylethanamine** (Secondary amine, $\text{CH}_3\text{CH}_2\text{NHCH}_3$)"""
            },
            {
                "id": "chem-ha-q24",
                "number": "24",
                "question": "Identify (X) and (Y) in the following reaction:\nCH3CH2Cl + aq. KOH -> X --(PCl5)--> Y",
                "answer": """$$\\text{CH}_3\\text{CH}_2\\text{Cl} + \\text{aq. KOH} \\xrightarrow{\\Delta} \\text{CH}_3\\text{CH}_2\\text{OH} \\; (X) + \\text{KCl}$$
$$\\text{CH}_3\\text{CH}_2\\text{OH} + \\text{PCl}_5 \\rightarrow \\text{CH}_3\\text{CH}_2\\text{Cl} \\; (Y) + \\text{POCl}_3 + \\text{HCl}$$

- **(X):** **Ethanol** ($\text{CH}_3\text{CH}_2\text{OH}$)
- **(Y):** **Chloroethane** ($\text{CH}_3\text{CH}_2\text{Cl}$)"""
            },
            {
                "id": "chem-ha-q25",
                "number": "25",
                "question": "A primary holoalkane (X), if allowed to react with KCN yields a compound (Y), which on acidic hydrolysis gave propanoic acid? Identify (X) and (Y).",
                "answer": """Since acidic hydrolysis of (Y) gives propanoic acid ($\\text{CH}_3\\text{CH}_2\\text{COOH}$):
$$\\text{Y} = \\text{CH}_3\\text{CH}_2\\text{CN} \\quad (\\textbf{Propanenitrile})$$
Since (Y) has 3 carbons and is formed by nucleophilic displacement using $\\text{KCN}$ ($+\\text{C}$ atom), the parent haloalkane (X) must contain 2 carbons:
$$\\text{X} = \\text{CH}_3\\text{CH}_2\\text{X} \\quad (\\textbf{Haloethane, e.g., Bromoethane or Chloroethane})$$

Reactions:
$$\\text{CH}_3\\text{CH}_2\\text{Br} + \\text{KCN} \\rightarrow \\text{CH}_3\\text{CH}_2\\text{CN} \\; (Y) + \\text{KBr}$$
$$\\text{CH}_3\\text{CH}_2\\text{CN} + 2\\text{H}_2\\text{O} + \\text{H}^+ \\rightarrow \\text{CH}_3\\text{CH}_2\\text{COOH} + \\text{NH}_4^+$$"""
            },
            {
                "id": "chem-ha-q26",
                "number": "26",
                "question": "Convert bromoethane to ethyne.",
                "answer": """**Step 1:** Dehydrohalogenation to ethene:
$$\\text{CH}_3\\text{CH}_2\\text{Br} + \\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_2\\text{=CH}_2 + \\text{KBr} + \\text{H}_2\\text{O}$$

**Step 2:** Halogenation to 1,2-dibromoethane:
$$\\text{CH}_2\\text{=CH}_2 + \\text{Br}_2 / \\text{CCl}_4 \\rightarrow \\text{Br-CH}_2\\text{-CH}_2\\text{-Br}$$

**Step 3:** Double dehydrohalogenation using $\\text{NaNH}_2$:
$$\\text{Br-CH}_2\\text{-CH}_2\\text{-Br} + 2\\text{NaNH}_2 \\xrightarrow{\\text{liq. NH}_3} \\text{HC}\\equiv\\text{CH} + 2\\text{NaBr} + 2\\text{NH}_3 \\quad (\\textbf{Ethyne})$$"""
            },
            {
                "id": "chem-ha-q27",
                "number": "27",
                "question": "Why does chloroform not give white precipitate with aqueous silver nitrate? Give the uses of chloroform.",
                "answer": """**Reason:**
Chloroform ($\text{CHCl}_3$) is a purely covalent molecular compound. Its $\\text{C-Cl}$ bonds do not dissociate into free chloride ions ($\\text{Cl}^-$) in aqueous medium. Because the precipitation of silver chloride requires free $\\text{Cl}^-$ ions ($\\text{Ag}^+ + \\text{Cl}^- \\rightarrow \\text{AgCl} \\downarrow$), chloroform produces no precipitate with $\\text{AgNO}_3$.

**Uses of Chloroform:**
1. Used as an industrial solvent for fats, oils, waxes, rubber, and resins.
2. Formerly used as an inhalation general anesthetic in surgery.
3. Used in the laboratory preparation of chloretone (hypnotic) and chloropicrin (insecticide/tear gas).
4. Preservation of biological anatomical specimens."""
            },
            {
                "id": "chem-ha-q28",
                "number": "28",
                "question": "Why does trichloromethane not give white ppt. with silver nitrate solution? [1]",
                "answer": """Trichloromethane ($\text{CHCl}_3$) is a non-polar covalent molecule and does not ionize in water to liberate free chloride ($\\text{Cl}^-$) ions. Therefore, no insoluble $\\text{AgCl}$ precipitate is formed."""
            },
            {
                "id": "chem-ha-q29",
                "number": "29",
                "question": "What product would you obtain when trichloromethane is treated with acetone? [1]",
                "answer": """Condensation of trichloromethane with acetone in the presence of $\\text{KOH}$ gives **Chloretone (1,1,1-trichloro-2-methylpropan-2-ol)**, used as a hypnotic drug:
$$\\text{CH}_3\\text{COCH}_3 + \\text{CHCl}_3 \\xrightarrow{\\text{KOH}} (\\text{CH}_3)_2\\text{C(OH)CCl}_3$$"""
            },
            {
                "id": "chem-ha-q30",
                "number": "30",
                "question": "An aliphatic haloalkane A is heated with aq. KOH to give B. The compound B reacts with SOCI₂ to produce C. The compound C further reacts with AgCN to yield D. On reduction of compound D with LIAIH4 produces E. The compound A with undergoes Wurtz reaction to give an alkane of molecular formula C4H10. Identify A, B, C, D and E. Also write reactions involved.",
                "answer": """Since A undergoes Wurtz reaction to give $\\text{C}_4\\text{H}_{10}$ (butane), A is a 2-carbon haloalkane:
- **A:** **Bromoethane** ($\\text{CH}_3\\text{CH}_2\\text{Br}$)
- **B:** **Ethanol** ($\\text{CH}_3\\text{CH}_2\\text{OH}$)
- **C:** **Chloroethane** ($\\text{CH}_3\\text{CH}_2\\text{Cl}$)
- **D:** **Ethyl isocyanide** ($\\text{CH}_3\\text{CH}_2\\text{-NC}$)
- **E:** **N-methylethanamine** ($\\text{CH}_3\\text{CH}_2\\text{NHCH}_3$)

Reactions:
1. $2\\text{CH}_3\\text{CH}_2\\text{Br} + 2\\text{Na} \\xrightarrow{\\text{dry ether}} \\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_3 + 2\\text{NaBr}$
2. $\\text{CH}_3\\text{CH}_2\\text{Br} + \\text{aq. KOH} \\rightarrow \\text{CH}_3\\text{CH}_2\\text{OH} \\; (B) + \\text{KBr}$
3. $\\text{CH}_3\\text{CH}_2\\text{OH} + \\text{SOCl}_2 \\rightarrow \\text{CH}_3\\text{CH}_2\\text{Cl} \\; (C) + \\text{SO}_2 + \\text{HCl}$
4. $\\text{CH}_3\\text{CH}_2\\text{Cl} + \\text{AgCN} \\rightarrow \\text{CH}_3\\text{CH}_2\\text{-NC} \\; (D) + \\text{AgCl}$
5. $\\text{CH}_3\\text{CH}_2\\text{-NC} \\xrightarrow{\\text{LiAlH}_4} \\text{CH}_3\\text{CH}_2\\text{-NH-CH}_3 \\; (E)$"""
            },
            {
                "id": "chem-ha-q31",
                "number": "31",
                "question": "Why is chloroform stored in a dark room air tied bottle containing a little ethyl alcohol?",
                "answer": """Chloroform slowly reacts with atmospheric oxygen in the presence of sunlight to form **phosgene (carbonyl chloride, $\\text{COCl}_2$)**, an extremely lethal toxic gas:
$$2\\text{CHCl}_3 + \\text{O}_2 \\xrightarrow{h\\nu} 2\\text{COCl}_2 + 2\\text{HCl}$$
- **Dark, airtight bottles filled to the brim:** Exclude light and air to prevent photo-oxidation.
- **Addition of 0.6–1% ethanol:** Ethanol acts as a negative catalyst to retard the oxidation reaction, and if any trace phosgene forms, it rapidly converts it into non-toxic **diethyl carbonate**:
$$\\text{COCl}_2 + 2\\text{C}_2\\text{H}_5\\text{OH} \\rightarrow (\\text{C}_2\\text{H}_5\\text{O})_2\\text{CO} + 2\\text{HCl}$$"""
            },
            {
                "id": "chem-ha-q32",
                "number": "32",
                "question": "Why is it discouraged to use chloroform as an anesthesia? [2]",
                "answer": """The clinical use of chloroform as an inhalation anesthetic has been abandoned because:
1. **Narrow Margin of Safety:** The therapeutic window between anesthetic dose and lethal respiratory arrest is extremely narrow.
2. **Hepatotoxicity & Nephrotoxicity:** Metabolic breakdown of chloroform causes severe liver necrosis and kidney failure.
3. **Cardiac Arrhythmias:** It sensitizes the myocardium to catecholamines, often precipitating sudden fatal ventricular fibrillation and cardiac arrest.
4. **Phosgene Toxicity:** Risk of accidental exposure to phosgene formed during storage."""
            },
            {
                "id": "chem-ha-q33",
                "number": "33",
                "question": "Write down the chemical reaction for the preparation of trichloromethane from acetone. How would you convert trichloromethane into chloretone, methane and formic acid.",
                "answer": """**Preparation of $\\text{CHCl}_3$ from Acetone:**
$$\\text{CaOCl}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{Ca(OH)}_2 + \\text{Cl}_2$$
$$\\text{CH}_3\\text{COCH}_3 + 3\\text{Cl}_2 \\rightarrow \\text{CCl}_3\\text{COCH}_3 + 3\\text{HCl} \\quad (\\text{Trichloroacetone})$$
$$2\\text{CCl}_3\\text{COCH}_3 + \\text{Ca(OH)}_2 \\rightarrow 2\\text{CHCl}_3 + (\\text{CH}_3\\text{COO})_2\\text{Ca} \\quad (\\text{Calcium acetate})$$

**Conversions:**
1. **To Chloretone:**
$$\\text{CHCl}_3 + \\text{CH}_3\\text{COCH}_3 \\xrightarrow{\\text{KOH}} (\\text{CH}_3)_2\\text{C(OH)CCl}_3$$
2. **To Methane:**
Reduction of chloroform with zinc and water:
$$\\text{CHCl}_3 + 6[\\text{H}] \\xrightarrow{\\text{Zn / }\\text{H}_2\\text{O}} \\text{CH}_4 + 3\\text{HCl}$$
3. **To Formic acid:**
Alkaline hydrolysis followed by acidification:
$$\\text{CHCl}_3 + 4\\text{KOH (aq)} \\xrightarrow{\\Delta} \\text{HCOOK} + 3\\text{KCl} + 2\\text{H}_2\\text{O}$$
$$\\text{HCOOK} + \\text{HCl} \\rightarrow \\text{HCOOH} + \\text{KCl}$$"""
            },
            {
                "id": "chem-ha-q34",
                "number": "34",
                "question": "How does trichloromethane react with Phenol, Silver powder and Conc. nitric acid?",
                "answer": """1. **With Phenol and aq. NaOH (Reimer-Tiemann Reaction):**
Produces salicylaldehyde:
$$\\text{C}_6\\text{H}_5\\text{OH} + \\text{CHCl}_3 + 3\\text{NaOH} \\xrightarrow{65^\\circ\\text{C}} o\\text{-}\\text{HOC}_6\\text{H}_4\\text{CHO} + 3\\text{NaCl} + 2\\text{H}_2\\text{O}$$

2. **With Silver Powder:**
Produces ethyne:
$$2\\text{CHCl}_3 + 6\\text{Ag} \\xrightarrow{\\Delta} \\text{CH}\\equiv\\text{CH} + 6\\text{AgCl}$$

3. **With Conc. Nitric Acid:**
Produces chloropicrin:
$$\\text{CHCl}_3 + \\text{HNO}_3 \\text{ (conc.)} \\xrightarrow{\\Delta} \\text{CCl}_3\\text{NO}_2 + \\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-ha-q35",
                "number": "35",
                "question": "A haloalkane P reacts with aq. KOH to give Q. The compound Q on oxidation with K2Cr2O7 + H+ gives R and R undergoes Clemmensen reduction to produce S. The compound P react with sodium in presence of dry ether to form 2, 3- dimethylbutane, write chemical reactions involved and identify P, Q, R and S.",
                "answer": """Since P reacts with sodium in dry ether to form 2,3-dimethylbutane, P is **2-halopropane**:
- **P:** **2-bromopropane** [$\\text{CH}_3\\text{CH(Br)CH}_3$]
- **Q:** **Propan-2-ol** [$\\text{CH}_3\\text{CH(OH)CH}_3$]
- **R:** **Propan-2-one (Acetone)** [$\\text{CH}_3\\text{COCH}_3$]
- **S:** **Propane** [$\\text{CH}_3\\text{CH}_2\\text{CH}_3$]

Reactions:
1. $2\\text{CH}_3\\text{CH(Br)CH}_3 + 2\\text{Na} \\xrightarrow{\\text{dry ether}} (\\text{CH}_3)_2\\text{CH-CH}(\\text{CH}_3)_2 + 2\\text{NaBr}$
2. $\\text{CH}_3\\text{CH(Br)CH}_3 + \\text{aq. KOH} \\rightarrow \\text{CH}_3\\text{CH(OH)CH}_3 \\; (Q) + \\text{KBr}$
3. $\\text{CH}_3\\text{CH(OH)CH}_3 + [\\text{O}] \\xrightarrow{\\text{K}_2\\text{Cr}_2\\text{O}_7 / \\text{H}^+} \\text{CH}_3\\text{COCH}_3 \\; (R) + \\text{H}_2\\text{O}$
4. $\\text{CH}_3\\text{COCH}_3 + 4[\\text{H}] \\xrightarrow{\\text{Zn-Hg / conc. HCl}} \\text{CH}_3\\text{CH}_2\\text{CH}_3 \\; (S) + \\text{H}_2\\text{O}$ (Clemmensen Reduction)"""
            },
            {
                "id": "chem-ha-q36",
                "number": "36",
                "question": "How would you obtain:\na. Ethane from Bromoethane\nb. Ethyne from trichloromethane\nc. Give reactions to convert into ethanoic acid.",
                "answer": """**a. Ethane from Bromoethane:**
Catalytic or chemical reduction:
$$\\text{CH}_3\\text{CH}_2\\text{Br} + 2[\\text{H}] \\xrightarrow{\\text{Zn / HCl}} \\text{CH}_3\\text{CH}_3 + \\text{HBr} \\quad (\\text{Ethane})$$

**b. Ethyne from Trichloromethane:**
$$2\\text{CHCl}_3 + 6\\text{Ag} \\xrightarrow{\\Delta} \\text{CH}\\equiv\\text{CH} + 6\\text{AgCl} \\quad (\\text{Ethyne})$$

**c. Bromoethane to Ethanoic acid:**
$$\\text{CH}_3\\text{CH}_2\\text{Br} \\xrightarrow{\\text{aq. KOH}} \\text{CH}_3\\text{CH}_2\\text{OH} \\xrightarrow{\\text{K}_2\\text{Cr}_2\\text{O}_7 / \\text{H}_2\\text{SO}_4} \\text{CH}_3\\text{COOH} \\quad (\\text{Ethanoic acid})$$"""
            },
            {
                "id": "chem-ha-q37",
                "number": "37",
                "question": "Write any three methods of preparation of iodoethane. What happens when iodoethane is heated with Sodium in the presence of dry ether and alc. NaOH.",
                "answer": """**Three Methods of Preparation of Iodoethane:**
1. *From Ethanol:*
$$3\\text{C}_2\\text{H}_5\\text{OH} + \\text{PI}_3 \\rightarrow 3\\text{C}_2\\text{H}_5\\text{I} + \\text{H}_3\\text{PO}_3 \\quad (\\text{or Red P} + \\text{I}_2)$$
2. *From Ethene:*
$$\\text{CH}_2\\text{=CH}_2 + \\text{HI} \\rightarrow \\text{CH}_3\\text{CH}_2\\text{I}$$
3. *From Chloroethane/Bromoethane (Finkelstein reaction):*
$$\\text{CH}_3\\text{CH}_2\\text{Br} + \\text{NaI} \\xrightarrow{\\text{dry acetone}} \\text{CH}_3\\text{CH}_2\\text{I} + \\text{NaBr} \\downarrow$$

**Reactions:**
- **With Sodium in dry ether (Wurtz reaction):**
$$2\\text{CH}_3\\text{CH}_2\\text{I} + 2\\text{Na} \\xrightarrow{\\text{dry ether}} \\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_3 + 2\\text{NaI} \\quad (n\\text{-Butane})$$
- **With alcoholic NaOH (Elimination):**
$$\\text{CH}_3\\text{CH}_2\\text{I} + \\text{alc. NaOH} \\xrightarrow{\\Delta} \\text{CH}_2\\text{=CH}_2 + \\text{NaI} + \\text{H}_2\\text{O} \\quad (\\text{Ethene})$$"""
            },
            {
                "id": "chem-ha-q38",
                "number": "38",
                "question": "Starting with trichoromethane, how would you prepare:\na. Ethyne\nb. Methane\nc. Chloropicrin\nd. Carbonyl chloride\ne. Chloretone",
                "answer": """**a. Ethyne:**
$$2\\text{CHCl}_3 + 6\\text{Ag} \\xrightarrow{\\Delta} \\text{CH}\\equiv\\text{CH} + 6\\text{AgCl}$$

**b. Methane:**
$$\\text{CHCl}_3 + 6[\\text{H}] \\xrightarrow{\\text{Zn / }\\text{H}_2\\text{O}} \\text{CH}_4 + 3\\text{HCl}$$

**c. Chloropicrin:**
$$\\text{CHCl}_3 + \\text{HNO}_3 \\text{ (conc.)} \\xrightarrow{\\Delta} \\text{CCl}_3\\text{NO}_2 + \\text{H}_2\\text{O}$$

**d. Carbonyl chloride (Phosgene):**
$$2\\text{CHCl}_3 + \\text{O}_2 \\xrightarrow{h\\nu} 2\\text{COCl}_2 + 2\\text{HCl}$$

**e. Chloretone:**
$$\\text{CHCl}_3 + \\text{CH}_3\\text{COCH}_3 \\xrightarrow{\\text{solid KOH}} (\\text{CH}_3)_2\\text{C(OH)CCl}_3$$"""
            },
            {
                "id": "chem-ha-q39",
                "number": "39",
                "question": "A secondary haloalkane A gives compound B when heated with alc.KOH. B on ozonolysis produces ethanal and methanal as major products. Identify A and B, also write chemical reaction. What product would you expect when A is heated with sodium in the presence of dry ether?",
                "answer": """Since ozonolysis of B produces ethanal ($\\text{CH}_3\\text{CHO}$) and methanal ($\\text{HCHO}$):
$$\\text{B} = \\text{CH}_3\\text{-CH=CH}_2 \\quad (\\textbf{Propene})$$

Since B is formed by $\\beta$-elimination of secondary haloalkane A with alc. $\\text{KOH}$:
$$\\text{A} = \\text{CH}_3\\text{-CH(X)-CH}_3 \\quad (\\textbf{2-halopropane, e.g., 2-bromopropane})$$

Reactions:
1. $\\text{CH}_3\\text{CH(Br)CH}_3 + \\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_3\\text{-CH=CH}_2 \\; (B) + \\text{KBr} + \\text{H}_2\\text{O}$
2. $\\text{CH}_3\\text{-CH=CH}_2 + \\text{O}_3 \\rightarrow \\text{Ozonide} \\xrightarrow{\\text{Zn / }\\text{H}_2\\text{O}} \\text{CH}_3\\text{CHO} + \\text{HCHO} + \\text{ZnO}$

**Reaction with Na in dry ether (Wurtz Reaction):**
$$2\\text{CH}_3\\text{-CH(Br)-CH}_3 + 2\\text{Na} \\xrightarrow{\\text{dry ether}} (\\text{CH}_3)_2\\text{CH-CH}(\\text{CH}_3)_2 + 2\\text{NaBr}$$
The product is **2,3-dimethylbutane**."""
            },
            {
                "id": "chem-ha-q40",
                "number": "40",
                "question": "An aliphatic haloalkane A gives compound B when heated with alc.NaOH. The compound reacts with HBr to give major product C. On heating compound C with sodium in the presence of dry ether yields 2, 3- dimethyl butane. What products will you expect when the compound is B subjected to ozonolysis?",
                "answer": """Since C yields 2,3-dimethylbutane on Wurtz reaction, C is **2-bromopropane**.
Since B adds $\\text{HBr}$ to give 2-bromopropane, B is **Propene ($\\text{CH}_3\\text{-CH=CH}_2$)**.
Alkene B can be formed from either 1-halopropane or 2-halopropane (A).

**Ozonolysis of compound B (Propene):**
$$\\text{CH}_3\\text{-CH=CH}_2 + \\text{O}_3 \\rightarrow \\text{Propene ozonide} \\xrightarrow{\\text{Zn / }\\text{H}_2\\text{O}} \\text{CH}_3\\text{CHO} + \\text{HCHO} + \\text{ZnO}$$
The products are **Ethanal (Acetaldehyde)** and **Methanal (Formaldehyde)**."""
            },
            {
                "id": "chem-ha-q41",
                "number": "41",
                "question": "An organic compound A on catalytic reduction gives B, B on chlorination gives C, C on heating with sodium metal in presence of ether gives D, D on chlorination gives 2-chlorobutane as a major product. Give names for A, B, C and D.",
                "answer": """Working backwards:
- Chlorination of D yields 2-chlorobutane as major product $\\implies$ **D** is **n-Butane** ($\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_3$).
- D is formed by Wurtz coupling of C $\\implies$ **C** is **Chloroethane** ($\\text{CH}_3\\text{CH}_2\\text{Cl}$).
- C is formed by chlorination of B $\\implies$ **B** is **Ethane** ($\\text{CH}_3\\text{CH}_3$).
- B is formed by catalytic reduction of unsaturated compound A $\\implies$ **A** is **Ethene** ($\\text{CH}_2\\text{=CH}_2$) or **Ethyne** ($\\text{CH}\\equiv\\text{CH}$).

Names:
- **A:** **Ethene**
- **B:** **Ethane**
- **C:** **Chloroethane**
- **D:** **n-Butane**"""
            },
            {
                "id": "chem-ha-q42",
                "number": "42",
                "question": "An organic compound A when heated with acetone gives hypnotic and nervous sedatives drugs and form carbonyl compound when it is exposed to air.\na. Predict the organic compound A.\nb. Write the reactions for the formation of a from ethanol.\nc. Predict the compound by treating it with percent treated nitric acid.\nd. Convert a into Acetylene.",
                "answer": """**a. Compound A:** **Chloroform (Trichloromethane, $\\text{CHCl}_3$)**

**b. Preparation from Ethanol:**
$$\\text{CH}_3\\text{CH}_2\\text{OH} + \\text{Cl}_2 \\rightarrow \\text{CH}_3\\text{CHO} + 2\\text{HCl}$$
$$\\text{CH}_3\\text{CHO} + 3\\text{Cl}_2 \\rightarrow \\text{CCl}_3\\text{CHO} + 3\\text{HCl}$$
$$2\\text{CCl}_3\\text{CHO} + \\text{Ca(OH)}_2 \\rightarrow 2\\text{CHCl}_3 + (\\text{HCOO})_2\\text{Ca}$$

**c. Reaction with concentrated nitric acid:**
$$\\text{CHCl}_3 + \\text{HNO}_3 \\text{ (conc.)} \\xrightarrow{\\Delta} \\text{CCl}_3\\text{NO}_2 + \\text{H}_2\\text{O} \\quad (\\textbf{Chloropicrin / Tear gas})$$

**d. Conversion to Acetylene:**
$$2\\text{CHCl}_3 + 6\\text{Ag} \\xrightarrow{\\Delta} \\text{CH}\\equiv\\text{CH} + 6\\text{AgCl}$$"""
            },
            {
                "id": "chem-ha-q43",
                "number": "43",
                "question": "The given table stores the compounds and their molecular formula. How can you convert P to Q, where Q is a compound in which two methyl groups are substituted at adjacent carbon atoms? How is P obtained from T, where T is secondary alcohol? Write the reactions involved in the conversion of P into R and S.\nP: C3H7Br, Q: C6H14, R: CH2O, S: C2H4O, T: C3H8O",
                "answer": """**Identification:**
- **T ($\text{C}_3\text{H}_8\text{O}$):** **Propan-2-ol** [$(\\text{CH}_3)_2\\text{CHOH}$] (secondary alcohol)
- **P ($\text{C}_3\text{H}_7\text{Br}$):** **2-bromopropane** [$(\\text{CH}_3)_2\\text{CHBr}$]
- **Q ($\text{C}_6\text{H}_{14}$):** **2,3-dimethylbutane** [$(\\text{CH}_3)_2\\text{CH-CH}(\\text{CH}_3)_2$] (adjacent methyl groups)
- **R ($\text{CH}_2\text{O}$):** **Methanal (Formaldehyde)**
- **S ($\text{C}_2\text{H}_4\text{O}$):** **Ethanal (Acetaldehyde)**

**1. Conversion of P to Q (Wurtz Reaction):**
$$2(\\text{CH}_3)_2\\text{CHBr} + 2\\text{Na} \\xrightarrow{\\text{dry ether}} (\\text{CH}_3)_2\\text{CH-CH}(\\text{CH}_3)_2 + 2\\text{NaBr}$$

**2. Preparation of P from T:**
$$3(\\text{CH}_3)_2\\text{CHOH} + \\text{PBr}_3 \\rightarrow 3(\\text{CH}_3)_2\\text{CHBr} + \\text{H}_3\\text{PO}_3$$

**3. Conversion of P into R and S:**
- Dehydrohalogenation of P gives propene:
$$(\\text{CH}_3)_2\\text{CHBr} + \\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_3\\text{-CH=CH}_2 + \\text{KBr} + \\text{H}_2\\text{O}$$
- Ozonolysis of propene yields S (ethanal) and R (methanal):
$$\\text{CH}_3\\text{-CH=CH}_2 + \\text{O}_3 \\rightarrow \\text{Ozonide} \\xrightarrow{\\text{Zn / }\\text{H}_2\\text{O}} \\text{CH}_3\\text{CHO} \\; (S) + \\text{HCHO} \\; (R) + \\text{ZnO}$$"""
            },
            {
                "id": "chem-ha-q44",
                "number": "44",
                "question": "A chemical reaction occurs as follows :\nCH3 CH2 CH2 Br + aq. KOH → B + KBr (A)\na) Identify the compound 'B' in the above reaction. [1]\nb) Which substitution reaction mechanism occurs in the above reaction and why ? [2]\nc) What is the product formed when alc. KOH solution is used instead of aq. KOH in the above reaction ? [1]\nd) How can you obtain nitropropane from compound 'A' ? [1]",
                "answer": """**a) Identification of B:**
Compound 'B' is **Propan-1-ol** ($\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{OH}$).

**b) Mechanism ($S_N2$):**
The reaction proceeds predominantly via the **$S_N2$ (Substitution Nucleophilic Bimolecular)** mechanism because:
1. Compound 'A' is a primary ($1^\\circ$) haloalkane, which has minimal steric hindrance around the $\\alpha$-carbon, allowing easy backside nucleophilic attack by $\\text{OH}^-$.
2. The primary carbocation is energetically unstable, so the concerted single-step transition state ($S_N2$) is strongly favored over carbocation formation ($S_N1$).

**c) Reaction with alcoholic KOH:**
Instead of substitution, $\\beta$-elimination occurs to form **Propene**:
$$\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Br} + \\text{alc. KOH} \\xrightarrow{\\Delta} \\text{CH}_3\\text{-CH=CH}_2 + \\text{KBr} + \\text{H}_2\\text{O}$$

**d) Preparation of 1-nitropropane from compound 'A':**
Reflux 1-bromopropane with silver nitrite ($\\text{AgNO}_2$) in ethanol:
$$\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{Br} + \\text{AgNO}_2 \\xrightarrow{\\Delta} \\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{NO}_2 + \\text{AgBr} \\downarrow \\quad (\\textbf{1-nitropropane})$$"""
            }
        ]
    }
