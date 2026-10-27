# chem_metals.py
# Copper (1-25), Zinc (26-33), Mercury (34-49), Iron (50-69), Silver (70-80)

def get_copper():
    return {
        "name": "Copper",
        "questions": [
            {
                "id": "chem-cu-q1",
                "number": "1",
                "question": "A coinage metal M of electronic configuration (Ar) 3d10, 4s1 belongs to IB in the periodic table.\na. Draw the blast furnace for the smelting process during extraction of M using its chief ore.\nb. Explain the different reactions involved during the formation of matte in the furnace.",
                "answer": """**Metal M is Copper ($\text{Cu}$, $Z=29$). Chief ore: Copper Pyrites ($\text{CuFeS}_2$).**

**a. Blast Furnace for Smelting of Copper:**
```
                   Charge (Roasted ore + Coke + Silica)
                                  │
                                  ▼
                            ┌───────────┐
                            │  Throat   │  <-- Waste gases (SO2) exit
                            ├───────────┤
                            │           │
                            │   Stack   │  (Reactions occur here)
                            │  (Shaft)  │
                            │           │
                            ├───────────┤
                            │   Bosh    │  <-- Tuyeres (Blast of hot air)
                            ├───────────┤
                            │  Hearth   │
                            └──┬─────┬──┘
                  Slag Tap ----┘     └---- Matte Tap (Cu2S + FeS)
```

**b. Reactions during Matte Formation in Blast Furnace:**
The roasted ore containing $\\text{Cu}_2\\text{S}$, $\\text{FeS}$, and unreacted $\\text{FeO}$ is mixed with coke and silica ($\text{SiO}_2$) and heated:
1. *Oxidation of unreacted ferrous sulphide:*
$$2\\text{FeS} + 3\\text{O}_2 \\rightarrow 2\\text{FeO} + 2\\text{SO}_2$$
2. *Slag formation (removal of iron as fusible ferrous silicate slag):*
$$\\text{FeO} + \\text{SiO}_2 \\rightarrow \\text{FeSiO}_3 \\; (\\text{Slag, floats on top})$$
3. *Reduction of any cuprous oxide back to cuprous sulphide:*
$$\\text{Cu}_2\\text{O} + \\text{FeS} \\rightarrow \\text{Cu}_2\\text{S} + \\text{FeO}$$
The molten mixture collected at the hearth bottom consists of **copper matte** (approx. 45–50% $\\text{Cu}_2\\text{S}$ with a small amount of $\\text{FeS}$)."""
            },
            {
                "id": "chem-cu-q2",
                "number": "2",
                "question": "A metal (M) having atomic number 29 belongs to the IB in the periodic table.\na. Identify the metal (M) and write its chief ore. Chemistry\nb. In which parts of Nepal does the metal occur?\nc. Write the chemical reaction occurring in roasting step during the extraction of (M).",
                "answer": """**a. Metal and Chief Ore:**
- Metal (M): **Copper ($\text{Cu}$)**
- Chief Ore: **Copper Pyrites (Chalcopyrite, $\\text{CuFeS}_2$)**

**b. Occurrence in Nepal:**
Copper deposits in Nepal occur in **Kulekhani, Bhutkhola (Tanahun), Wapsa (Solukhumbu), Siddhi Khani (Ilam), and Buddha Khola (Bandipur)**.

**c. Roasting Reactions:**
Roasted in excess air in a reverberatory furnace:
$$2\\text{CuFeS}_2 + \\text{O}_2 \\rightarrow \\text{Cu}_2\\text{S} + 2\\text{FeS} + \\text{SO}_2 \\uparrow$$
$$2\\text{FeS} + 3\\text{O}_2 \\rightarrow 2\\text{FeO} + 2\\text{SO}_2 \\uparrow$$
$$2\\text{Cu}_2\\text{S} + 3\\text{O}_2 \\rightarrow 2\\text{Cu}_2\\text{O} + 2\\text{SO}_2 \\uparrow$$"""
            },
            {
                "id": "chem-cu-q3",
                "number": "3",
                "question": "Write down the chemistry of blue vitriol.",
                "answer": """Blue vitriol is **hydrated copper (II) sulphate, $\\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O}$**.
- **Structure:** Four water molecules are coordinated to the central $\\text{Cu}^{2+}$ ion in a square planar geometry, while the fifth water molecule is hydrogen-bonded between coordinated water and sulphate ions: $[\\text{Cu}(\\text{H}_2\\text{O})_4]\\text{SO}_4\\cdot \\text{H}_2\\text{O}$.
- **Action of Heat:**
$$\\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O} \\xrightarrow{100^\\circ\\text{C}} \\text{CuSO}_4\\cdot \\text{H}_2\\text{O} \\xrightarrow{230^\\circ\\text{C}} \\text{CuSO}_4 \\text{ (white anhydrous)} \\xrightarrow{750^\\circ\\text{C}} \\text{CuO} + \\text{SO}_2 + \\frac{1}{2}\\text{O}_2$$"""
            },
            {
                "id": "chem-cu-q4",
                "number": "4",
                "question": "Copper (II) Sulphate crystals are commonly known as blue vitriol.\na. How would you obtain for saturated CuSO4 solution?\nb. Convert blue vitriol into red oxide.\nc. Write any two applications of blue vitriol.",
                "answer": """**a. Obtaining crystals from saturated solution:**
Concentrate the saturated solution of $\\text{CuSO}_4$ by gentle heating until the crystallization point is reached, then allow it to cool slowly undisturbed. Triclinic blue crystals of $\\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O}$ separate out.

**b. Conversion into Red Oxide ($\text{Cu}_2\text{O}$):**
Boil aqueous $\\text{CuSO}_4$ with glucose or sodium hydroxide and potassium sodium tartrate (Fehling's solution):
$$2\\text{CuSO}_4 + 4\\text{NaOH} + \\text{R-CHO (glucose)} \\xrightarrow{\\Delta} \\text{Cu}_2\\text{O} \\downarrow \\text{ (red)} + \\text{R-COOH} + 2\\text{Na}_2\\text{SO}_4 + 2\\text{H}_2\\text{O}$$

**c. Two Applications:**
1. Preparation of Bordeaux mixture (fungicide: $\\text{CuSO}_4 + \\text{Ca(OH)}_2$).
2. Electrolyte in copper electroplating and electro-refining."""
            },
            {
                "id": "chem-cu-q5",
                "number": "5",
                "question": "Zinc is considered non-typical element and it belongs to the element of group II B.\na. Why are the elements of group IIB called volatile metal?\nb. Name the process of concentration of Zinc blende during the extraction of Zn.\nc. Write chemical reaction involved in roasting during extraction of zinc.\nd. What is meant by spelter zinc?\ne. How is granulated zinc prepared?",
                "answer": """**a. Volatile metals:**
Group IIB elements (Zn, Cd, Hg) have completely filled $d$-orbitals ($d^{10}$). Because no $d$-electrons participate in metallic bonding, metallic bonding is very weak, resulting in unusually low melting and boiling points (Zn boils at $907^\\circ\\text{C}$, Hg is liquid). Hence, they are called volatile metals.

**b. Concentration of Zinc blende:**
**Froth Flotation Process** using pine oil as frother and sodium ethyl xanthate as collector.

**c. Roasting Reaction:**
$$2\\text{ZnS} + 3\\text{O}_2 \\xrightarrow{850-900^\\circ\\text{C}} 2\\text{ZnO} + 2\\text{SO}_2 \\uparrow$$

**d. Spelter Zinc:**
Crude zinc obtained directly from the reduction process (approx. 97–98% pure, containing impurities of $\\text{Pb}$, $\\text{Fe}$, $\\text{Cd}$, $\\text{As}$) is called **spelter**.

**e. Preparation of Granulated Zinc:**
Prepared by melting spelter zinc in a crucible and pouring the molten metal in a thin, steady stream into cold water, causing it to solidify into fine, porous irregular granules."""
            },
            {
                "id": "chem-cu-q6",
                "number": "6",
                "question": "Penta-hydrated copper sulphate is called blue vitriol.\na. Starting from metallic, copper, how can you obtain blue vitriol?\nb. What happens when aq, solution of blue vitriol is treated with excess ammonia solution?\nc. Give chemical reaction of conversion of blue vitriol into black oxide.\nd. Why is hydrated copper sulphate called blue vitriol?",
                "answer": """**a. From metallic copper:**
Heat copper with moderately concentrated sulfuric acid in the presence of air:
$$\\text{Cu} + \\text{H}_2\\text{SO}_4 + \\frac{1}{2}\\text{O}_2 \\rightarrow \\text{CuSO}_4 + \\text{H}_2\\text{O}$$
Crystallization yields blue crystals of $\\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O}$.

**b. Reaction with excess ammonia:**
First forms a pale blue precipitate of basic copper sulphate, which dissolves in excess ammonia to give a deep blue solution of **tetramminecopper(II) sulphate**:
$$\\text{CuSO}_4 + 4\\text{NH}_4\\text{OH} \\rightarrow [\\text{Cu}(\\text{NH}_3)_4]\\text{SO}_4 \\text{ (deep blue)} + 4\\text{H}_2\\text{O}$$

**c. Conversion into Black Oxide ($\text{CuO}$):**
$$\\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O} \\xrightarrow{>750^\\circ\\text{C}} \\text{CuO (black)} + \\text{SO}_2 + \\frac{1}{2}\\text{O}_2 + 5\\text{H}_2\\text{O}$$

**d. Name origin:**
Historically, metal sulphates with glass-like crystalline luster were called 'vitriols' (from Latin *vitriolum*, meaning glassy). Because hydrated copper sulphate crystals are deep blue and transparent, it is called **blue vitriol**."""
            },
            {
                "id": "chem-cu-q7",
                "number": "7",
                "question": "Give the balanced chemical reaction for the preparation of black oxide from blue vitriol. How is black oxide converted into red oxide?",
                "answer": """**1. Preparation of Black Oxide ($\text{CuO}$) from Blue Vitriol:**
$$\\text{CuSO}_4 + 2\\text{NaOH} \\rightarrow \\text{Cu(OH)}_2 \\downarrow + \\text{Na}_2\\text{SO}_4$$
$$\\text{Cu(OH)}_2 \\xrightarrow{\\Delta} \\text{CuO (black)} + \\text{H}_2\\text{O}$$

**2. Conversion of Black Oxide ($\text{CuO}$) into Red Oxide ($\text{Cu}_2\text{O}$):**
Heat black oxide ($\text{CuO}$) with metallic copper at high temperature:
$$\\text{CuO} + \\text{Cu} \\xrightarrow{\\text{red heat}} \\text{Cu}_2\\text{O} \\; (\\textbf{Cuprous oxide / Red oxide})$$"""
            },
            {
                "id": "chem-cu-q8",
                "number": "8",
                "question": "Give the balanced chemical reaction for the preparation of copper sulphate from copper. What happens when blue vitriol is heated at 100°C?",
                "answer": """**Preparation of $\\text{CuSO}_4$:**
$$\\text{Cu} + 2\\text{H}_2\\text{SO}_4 \\text{ (conc.)} \\xrightarrow{\\Delta} \\text{CuSO}_4 + \\text{SO}_2 \\uparrow + 2\\text{H}_2\\text{O}$$

**Heating Blue Vitriol at $100^\\circ\\text{C}$:**
Loses four molecules of crystallization water to form **copper sulphate monohydrate (bluish-white)**:
$$\\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O} \\xrightarrow{100^\\circ\\text{C}} \\text{CuSO}_4\\cdot \\text{H}_2\\text{O} + 4\\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-cu-q9",
                "number": "9",
                "question": "What happens when copper sulphate solution is treated with ammonia solution?",
                "answer": """Treatment with a little ammonia produces a bluish-white precipitate of basic copper sulphate. Addition of excess ammonia dissolves this precipitate, forming an intensely deep azure blue complex solution of **tetramminecopper(II) ion**:
$$\\text{Cu}^{2+} + 4\\text{NH}_3 \\rightarrow [\\text{Cu}(\\text{NH}_3)_4]^{2+} \\; (\\text{Tetramminecopper(II) complex})$$"""
            },
            {
                "id": "chem-cu-q10",
                "number": "10",
                "question": "Write the action of heat on blue vitriol.",
                "answer": """$$\\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O} \\xrightarrow{100^\\circ\\text{C}} \\text{CuSO}_4\\cdot \\text{H}_2\\text{O} \\; (\\text{monohydrate, pale blue})$$
$$\\text{CuSO}_4\\cdot \\text{H}_2\\text{O} \\xrightarrow{230^\\circ\\text{C}} \\text{CuSO}_4 \\; (\\text{anhydrous, white powder})$$
$$\\text{CuSO}_4 \\xrightarrow{750^\\circ\\text{C}} \\text{CuO (black)} + \\text{SO}_2 \\uparrow + \\frac{1}{2}\\text{O}_2 \\uparrow$$"""
            },
            {
                "id": "chem-cu-q11",
                "number": "11",
                "question": "Write down the molecular formula of:\na. Copper pyrite\nb. Calomel\nc. Calamine\nd. Cinnabar",
                "answer": """a. **Copper pyrite:** $\\text{CuFeS}_2$  
b. **Calomel:** $\\text{Hg}_2\\text{Cl}_2$  
c. **Calamine:** $\\text{ZnCO}_3$  
d. **Cinnabar:** $\\text{HgS}$"""
            },
            {
                "id": "chem-cu-q12",
                "number": "12",
                "question": "Give reason: Mettalic copper turns black when exposed to moist air.",
                "answer": """When copper is exposed to air containing oxygen and moisture, it oxidizes on the surface to form a thin black layer of **cupric oxide ($\text{CuO}$)**:
$$2\\text{Cu} + \\text{O}_2 \\rightarrow 2\\text{CuO (black)}$$"""
            },
            {
                "id": "chem-cu-q13",
                "number": "13",
                "question": "Write an important use of red oxide and blue vitriol.",
                "answer": """- **Red oxide ($\text{Cu}_2\text{O}$):** Used as a red pigment in antifouling paints for ship hulls to prevent attachment of barnacles.
- **Blue vitriol ($\text{CuSO}_4\cdot 5\text{H}_2\text{O}$):** Used as an agricultural fungicide (Bordeaux mixture)."""
            },
            {
                "id": "chem-cu-q14",
                "number": "14",
                "question": "What is meant by copper matte?",
                "answer": """Copper matte is a molten mixture of **cuprous sulphide ($\text{Cu}_2\text{S}$, ~45–50%) and ferrous sulphide ($\text{FeS}$)** obtained from the bottom of the blast furnace during the smelting of copper pyrites."""
            },
            {
                "id": "chem-cu-q15",
                "number": "15",
                "question": "A light blue colored precipitate 'A' obtained by the addition of caustic soda in the solution of cupric sulphate is converted to a black precipitate 'B' on heating. What are 'A' and 'B'?",
                "answer": """- **Precipitate 'A':** **Cupric hydroxide [$\\text{Cu(OH)}_2$]** (light blue)
- **Precipitate 'B':** **Cupric oxide [$\\text{CuO}$]** (black)
$$\\text{CuSO}_4 + 2\\text{NaOH} \\rightarrow \\text{Cu(OH)}_2 \\downarrow \\; (A) + \\text{Na}_2\\text{SO}_4$$
$$\\text{Cu(OH)}_2 \\xrightarrow{\\Delta} \\text{CuO (black)} \\; (B) + \\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-cu-q16",
                "number": "16",
                "question": "How would you convert copper into blue vitriol? Name any one alloy of each of:\na. Copper and Zinc.\nb. Copper and tin",
                "answer": """**Conversion:**
$$\\text{Cu} + 2\\text{H}_2\\text{SO}_4 \\text{ (conc.)} \\xrightarrow{\\Delta} \\text{CuSO}_4 + \\text{SO}_2 + 2\\text{H}_2\\text{O}$$
Crystallization produces $\\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O}$.

**Alloys:**
a. Copper and Zinc: **Brass** (60–80% Cu, 20–40% Zn)  
b. Copper and Tin: **Bronze** (80–90% Cu, 10–20% Sn)"""
            },
            {
                "id": "chem-cu-q17",
                "number": "17",
                "question": "Write the action of copper upon: Moist air and con. H2SO4",
                "answer": """- **Moist Air:** Forms green basic copper carbonate (patina):
$$2\\text{Cu} + \\text{CO}_2 + \\text{O}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{CuCO}_3\\cdot\\text{Cu(OH)}_2 \\text{ (green)}$$
- **Conc. $\\text{H}_2\\text{SO}_4$:**
$$\\text{Cu} + 2\\text{H}_2\\text{SO}_4 \\text{ (conc.)} \\xrightarrow{\\Delta} \\text{CuSO}_4 + \\text{SO}_2 \\uparrow + 2\\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-cu-q18",
                "number": "18",
                "question": "Copper sulphate crystal turns white powder on heating. Why?",
                "answer": """The blue color of $\\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O}$ is due to $d-d$ transition of electrons in the $\\text{Cu}^{2+}$ ion coordinated with four water molecules. On heating to $230^\\circ\\text{C}$, it loses all water of crystallization to become **anhydrous $\\text{CuSO}_4$**, which is white because the crystal field splitting of the $d$-orbitals disappears."""
            },
            {
                "id": "chem-cu-q19",
                "number": "19",
                "question": "A brown gas is obtained when copper is treated with conc. nitric acid. Give a reason.",
                "answer": """Concentrated nitric acid acts as a powerful oxidizing agent. It oxidizes copper and itself gets reduced to **nitrogen dioxide gas ($\text{NO}_2$)**, which is reddish-brown:
$$\\text{Cu} + 4\\text{HNO}_3 \\text{ (conc.)} \\rightarrow \\text{Cu(NO}_3)_2 + 2\\text{NO}_2 \\uparrow \\text{ (brown gas)} + 2\\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-cu-q20",
                "number": "20",
                "question": "Copper becomes green when exposed to air for long time. Why?",
                "answer": """Prolonged exposure to atmospheric moisture, carbon dioxide, and oxygen leads to the formation of a protective green film called **patina**, composed of **basic copper carbonate [$\\text{CuCO}_3\\cdot\\text{Cu(OH)}_2$]**:
$$2\\text{Cu} + \\text{O}_2 + \\text{CO}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{CuCO}_3\\cdot\\text{Cu(OH)}_2$$"""
            },
            {
                "id": "chem-cu-q21",
                "number": "21",
                "question": "When happens when:\na. Ammonium hydroxide is added to a solution of copper sulphate.\nb. Copper sulphate solution is heated aqueous potassium iodide",
                "answer": """**a. Ammonium hydroxide with $\\text{CuSO}_4$:**
Forms deep blue $[\\text{Cu}(\\text{NH}_3)_4]\\text{SO}_4$:
$$\\text{CuSO}_4 + 4\\text{NH}_4\\text{OH} \\rightarrow [\\text{Cu}(\\text{NH}_3)_4]\\text{SO}_4 + 4\\text{H}_2\\text{O}$$

**b. Copper sulphate with aqueous potassium iodide:**
$\text{Cu}^{2+}$ oxidizes $\text{I}^-$ to liberate iodine, precipitating white cuprous iodide:
$$2\\text{CuSO}_4 + 4\\text{KI} \\rightarrow \\text{Cu}_2\\text{I}_2 \\downarrow \\text{ (white ppt)} + \\text{I}_2 \\text{ (brown solution)} + 2\\text{K}_2\\text{SO}_4$$"""
            },
            {
                "id": "chem-cu-q22",
                "number": "22",
                "question": "Write a compound of Cu (II) which is insoluble in water but soluble in dilute acid without effervescence.",
                "answer": """The compound is **Cupric oxide ($\text{CuO}$)**.
It is insoluble in water but dissolves smoothly in dilute acid without effervescence:
$$\\text{CuO} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{CuSO}_4 + \\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-cu-q23",
                "number": "23",
                "question": "What happens when NH3 is passed over red-hot CuO",
                "answer": """Ammonia gas is oxidized to **nitrogen gas ($\text{N}_2$)**, while cupric oxide is reduced to reddish-brown **metallic copper**:
$$3\\text{CuO} + 2\\text{NH}_3 \\xrightarrow{\\text{red heat}} 3\\text{Cu} + \\text{N}_2 \\uparrow + 3\\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-cu-q24",
                "number": "24",
                "question": "Give any one method of conversion of cupric sulphate into cuprous oxide with chemical equations.",
                "answer": """Boil cupric sulphate solution with alkaline glucose (or Fehling's solution):
$$2\\text{CuSO}_4 + 4\\text{NaOH} + \\text{C}_6\\text{H}_{12}\\text{O}_6 \\xrightarrow{\\Delta} \\text{Cu}_2\\text{O} \\downarrow \\text{ (red ppt)} + \\text{C}_6\\text{H}_{12}\\text{O}_7 + 2\\text{Na}_2\\text{SO}_4 + 2\\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-cu-q25",
                "number": "25",
                "question": "When copper wire is put into a solution of silver nitrate beautiful crystals are deposited on the surface of the copper. What are these crystals chemically? Write the reaction involved.",
                "answer": """The crystals deposited on the copper wire are **metallic Silver ($\text{Ag}$)**.
Because copper is more electropositive than silver ($E^\\circ_{\\text{Cu}^{2+}/\\text{Cu}} = +0.34\\text{ V}$ vs $E^\\circ_{\\text{Ag}^+/\\text{Ag}} = +0.80\\text{ V}$), copper displaces silver ions from solution:
$$\\text{Cu} (s) + 2\\text{AgNO}_3 (aq) \\rightarrow \\text{Cu(NO}_3)_2 (aq) + 2\\text{Ag} \\downarrow (s)$$
The solution turns blue due to the formation of hydrated cupric ions."""
            }
        ]
    }

def get_zinc():
    return {
        "name": "Zinc",
        "questions": [
            {
                "id": "chem-zn-q26",
                "number": "26",
                "question": "A metal (M) having atomic number 30 is referred to as non-typical transition metal and it belongs with the group IIB.\na. Identify the metal (M) and write its chief ore.\nb. Why is metal (M) called non-typical transition metal?\nc. Write the chemical process occurring in reduction step during the extraction of (M).",
                "answer": """**a. Identification:**
- Metal (M): **Zinc ($\text{Zn}$, $Z=30$)**
- Chief Ore: **Zinc Blende ($\text{ZnS}$)**

**b. Non-typical transition metal:**
Zinc possesses a completely filled $d$-subshell both in its ground state ($[\\text{Ar}] 3d^{10} 4s^2$) and in its only common oxidation state ($[\\text{Ar}] 3d^{10}$ in $\\text{Zn}^{2+}$). Hence, it does not show typical transition metal properties (variable oxidation states, colored ions, paramagnetism).

**c. Reduction Step:**
ZnO is reduced with crushed coke in vertical retorts at $1100–1200^\\circ\\text{C}$ (Belgian process):
$$\\text{ZnO} + \\text{C} \\xrightarrow{1100-1200^\\circ\\text{C}} \\text{Zn} \\uparrow \\text{ (vapour)} + \\text{CO} \\uparrow$$
Zinc vapours are rapidly chilled to condense into molten zinc."""
            },
            {
                "id": "chem-zn-q27",
                "number": "27",
                "question": "What happens when:\na. Zinc is dissolved in hot and conc. NaOH.\nb. White vitriol is heated up to 800oC\nc. White vitriol is treated with BaS\nd. zinc white is dissolved in excess of caustic soda.\ne. Zinc white is heated with cobalt nitrate\nf. Zinc is exposed to air.",
                "answer": """**a. Zinc with hot conc. NaOH:** Forms soluble sodium zincate and hydrogen:
$$\\text{Zn} + 2\\text{NaOH} \\rightarrow \\text{Na}_2\\text{ZnO}_2 + \\text{H}_2 \\uparrow$$

**b. White vitriol heated to $800^\\circ\\text{C}$:**
$$\\text{ZnSO}_4\\cdot 7\\text{H}_2\\text{O} \\xrightarrow{800^\\circ\\text{C}} \\text{ZnO} + \\text{SO}_2 + \\frac{1}{2}\\text{O}_2 + 7\\text{H}_2\\text{O}$$

**c. White vitriol with BaS:** Precipitates **Lithopone**:
$$\\text{ZnSO}_4 + \\text{BaS} \\rightarrow \\text{ZnS} \\downarrow + \\text{BaSO}_4 \\downarrow \\quad (\\textbf{Lithopone})$$

**d. Zinc white ($\text{ZnO}$) dissolved in excess caustic soda:**
$$\\text{ZnO} + 2\\text{NaOH} \\rightarrow \\text{Na}_2\\text{ZnO}_2 + \\text{H}_2\\text{O} \\; (\\text{Sodium zincate})$$

**e. Zinc white heated with cobalt nitrate:** Forms green pigment **Rinmann's green**:
$$2\\text{Co(NO}_3)_2 \\xrightarrow{\\Delta} 2\\text{CoO} + 4\\text{NO}_2 + \\text{O}_2$$
$$\\text{CoO} + \\text{ZnO} \\rightarrow \\text{CoZnO}_2 \\; (\\text{Cobalt zincate / Rinmann's green})$$

**f. Zinc exposed to moist air:** Forms protective dull grey basic zinc carbonate:
$$4\\text{Zn} + 3\\text{H}_2\\text{O} + \\text{CO}_2 + 2\\text{O}_2 \\rightarrow \\text{ZnCO}_3\\cdot 3\\text{Zn(OH)}_2$$"""
            },
            {
                "id": "chem-zn-q28",
                "number": "28",
                "question": "An important compound of a non-typical transition element zinc which is used as eye lotion and is also used as white vitriol.\na. Write down the method of preparation of white vitriol.\nb. Define double salt giving an example of it.\nc. How is lithopone obtained from white vitriol?\nd. Why is zinc considered as a non-typical transition element?",
                "answer": """**a. Preparation of White Vitriol ($\text{ZnSO}_4\cdot 7\text{H}_2\text{O}$):**
Dissolve granulated zinc, zinc oxide, or zinc carbonate in dilute sulfuric acid:
$$\\text{Zn} + \\text{dil. }\\text{H}_2\\text{SO}_4 \\rightarrow \\text{ZnSO}_4 + \\text{H}_2 \\uparrow$$
Concentration and crystallization below $39^\\circ\\text{C}$ yields rhombic crystals of $\\text{ZnSO}_4\\cdot 7\\text{H}_2\\text{O}$.

**b. Definition of Double Salt:**
A molecular addition compound formed by two simple stable salts crystallized in stoichiometric proportion that completely dissociates into its constituent simple ions in aqueous solution. Example: **Mohr's salt [$\\text{FeSO}_4\\cdot(\\text{NH}_4)_2\\text{SO}_4\\cdot 6\\text{H}_2\\text{O}$]** or **Potash alum [$\\text{K}_2\\text{SO}_4\\cdot\\text{Al}_2(\\text{SO}_4)_3\\cdot 24\\text{H}_2\\text{O}$]**.

**c. Lithopone from White Vitriol:**
$$\\text{ZnSO}_4 + \\text{BaS} \\rightarrow \\text{ZnS} \\cdot \\text{BaSO}_4 \\downarrow \\; (\\textbf{Lithopone})$$

**d. Non-typical transition element:**
Because it contains completely filled $d$-orbitals ($3d^{10}$) in both atomic state and $\\text{Zn}^{2+}$ ionic state, showing no incomplete $d$-orbitals."""
            },
            {
                "id": "chem-zn-q29",
                "number": "29",
                "question": "How is Rinmann’s green prepared? Write it’s an important application.",
                "answer": """**Preparation:**
A drop of dilute cobalt nitrate solution is added to a pinch of zinc white ($\text{ZnO}$) on a charcoal block and heated strongly in an oxidizing flame:
$$2\\text{Co(NO}_3)_2 \\xrightarrow{\\Delta} 2\\text{CoO} + 4\\text{NO}_2 + \\text{O}_2$$
$$\\text{CoO} + \\text{ZnO} \\rightarrow \\text{CoZnO}_2 \\quad (\\textbf{Rinmann's green / Cobalt zincate})$$

**Application:**
Used as a green pigment in paints and utilized in qualitative inorganic analysis for the **confirmatory dry test of $\\text{Zn}^{2+}$ radical**."""
            },
            {
                "id": "chem-zn-q30",
                "number": "30",
                "question": "Explain the extraction of zinc from zinc blende.",
                "answer": """1. **Crushing & Concentration:** Pulverized and concentrated by **froth flotation** using pine oil.
2. **Roasting:** Roasted at $900^\\circ\\text{C}$ in excess air to convert $\\text{ZnS}$ to $\\text{ZnO}$:
$$2\\text{ZnS} + 3\\text{O}_2 \\rightarrow 2\\text{ZnO} + 2\\text{SO}_2 \\uparrow$$
3. **Reduction:** Smelted with coke at $1200^\\circ\\text{C}$ in vertical retorts:
$$\\text{ZnO} + \\text{C} \\rightarrow \\text{Zn} \\uparrow + \\text{CO}$$
4. **Purification:** Refined by fractional distillation or electrolytic refining (pure Zn cathode, spelter anode, acidified $\\text{ZnSO}_4$ electrolyte)."""
            },
            {
                "id": "chem-zn-q31",
                "number": "31",
                "question": "A heavy metal is extracted from its oxide ore during extraction, smelting of calcinated ore is done in a blast furnace.\na. Name the metal and its ore.\nb. Draw the neat and clean diagram of blast furnace showing different zones.\nc. Write down the chemical reactions for slag formation.",
                "answer": """**a. Metal:** **Iron ($\text{Fe}$)**; Ore: **Haematite ($\text{Fe}_2\text{O}_3$)**.

**b. Blast Furnace Zones:**
- *Top (400–700°C):* Zone of Reduction ($\\text{Fe}_2\\text{O}_3 \\rightarrow \\text{Fe}_3\\text{O}_4 \\rightarrow \\text{FeO} \\rightarrow \\text{Fe}$)
- *Middle (800–1000°C):* Zone of Slag Formation ($\\text{CaCO}_3 \\rightarrow \\text{CaO} + \\text{CO}_2; \\; \\text{CaO} + \\text{SiO}_2 \\rightarrow \\text{CaSiO}_3$)
- *Lower (1200–1500°C):* Zone of Fusion
- *Bottom (1500–2000°C):* Zone of Combustion ($C + O_2 \\rightarrow CO_2; \\; CO_2 + C \\rightarrow 2CO$)

**c. Slag Formation Reactions:**
$$\\text{CaCO}_3 \\xrightarrow{\\Delta} \\text{CaO} + \\text{CO}_2$$
$$\\text{CaO} + \\text{SiO}_2 \\rightarrow \\text{CaSiO}_3 \\; (\\text{Calcium silicate slag})$$"""
            },
            {
                "id": "chem-zn-q32",
                "number": "32",
                "question": "And ammonia solution is added to the sulphate of coinage metal A, the blue precipitates(B) is formed which dissolves in excess of reagent to form deep blue solution (C). Answer the following:\na. identify A, B &C which sequence of chemical reaction.\nb. Predict the electronic configuration of metal A.\nc. Select the suitable method of the purification of metal A.",
                "answer": """**a. Identification & Reactions:**
- Metal A: **Copper ($\text{Cu}$)**
- Precipitate B: **Cupric hydroxide [$\\text{Cu(OH)}_2$]** (or basic copper sulphate)
- Solution C: **Tetramminecopper(II) sulphate [$[\\text{Cu}(\\text{NH}_3)_4]\\text{SO}_4$]**

$$\\text{CuSO}_4 + 2\\text{NH}_4\\text{OH} \\rightarrow \\text{Cu(OH)}_2 \\downarrow \\; (B) + (\\text{NH}_4)_2\\text{SO}_4$$
$$\\text{Cu(OH)}_2 + (\\text{NH}_4)_2\\text{SO}_4 + 2\\text{NH}_4\\text{OH} \\rightarrow [\\text{Cu}(\\text{NH}_3)_4]\\text{SO}_4 \\; (C) + 4\\text{H}_2\\text{O}$$

**b. Electronic Configuration of Copper ($Z=29$):**
$$\\text{Cu}: [\\text{Ar}] \\, 3d^{10} 4s^1$$

**c. Purification Method:**
**Electrolytic refining** using blister copper as anode, thin pure copper sheets as cathode, and acidified $\\text{CuSO}_4$ solution as electrolyte."""
            },
            {
                "id": "chem-zn-q33",
                "number": "33",
                "question": "X is an ore of metal M. X on calcination gives black precipitate (W) of metal oxide which belongs to group II of the basic radical in qualitative analysis. X on roasting gives metal M and a gas as a major byproduct. When the gas passes through the acidified potassium dichromate turns green.\na. Identify the metal ore X.\nb. Write down the reaction involved during calcination of ore X.\nc. Write down the reaction of the gas with potassium dichromate.\nd. Convert metal M into its vitriol.",
                "answer": """**a. Metal Ore X:**
- Ore X: **Copper Pyrites ($\\text{CuFeS}_2$)** or **Chalcocite ($\\text{Cu}_2\\text{S}$)**
- Metal M: **Copper ($\text{Cu}$)**
- Gas: **Sulphur dioxide ($\text{SO}_2$)**
- Black oxide W: **Cupric oxide ($\text{CuO}$)**

**b. Calcination reaction:**
$$\\text{CuCO}_3\\cdot\\text{Cu(OH)}_2 \\xrightarrow{\\Delta} 2\\text{CuO (black)} \\; (W) + \\text{CO}_2 + \\text{H}_2\\text{O}$$

**c. Reaction of $\\text{SO}_2$ with acidified $\\text{K}_2\\text{Cr}_2\\text{O}_7$:**
$$\\text{K}_2\\text{Cr}_2\\text{O}_7 + \\text{H}_2\\text{SO}_4 + 3\\text{SO}_2 \\rightarrow \\text{K}_2\\text{SO}_4 + \\text{Cr}_2(\\text{SO}_4)_3 \\text{ (green)} + \\text{H}_2\\text{O}$$

**d. Conversion of Metal M into Blue Vitriol:**
$$\\text{Cu} + 2\\text{H}_2\\text{SO}_4 \\xrightarrow{\\Delta} \\text{CuSO}_4 + \\text{SO}_2 + 2\\text{H}_2\\text{O} \\xrightarrow{5\\text{H}_2\\text{O}} \\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O}$$"""
            }
        ]
    }
