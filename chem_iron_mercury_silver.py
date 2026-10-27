# chem_iron_mercury_silver.py
# Mercury (34-49), Iron (50-69), Silver (70-80)

def get_mercury():
    return {
        "name": "Mercury",
        "questions": [
            {
                "id": "chem-hg-q34",
                "number": "34",
                "question": "Write two methods of preparation of corrosive sublimate. Give its action with:\na. Excess of KI\nb. NH3.\nc. SnCl2 solution\nd. NH4OH solution",
                "answer": """**Preparation of Corrosive Sublimate ($\text{HgCl}_2$):**
1. *By heating mercuric sulphate with sodium chloride:*
$$\\text{HgSO}_4 + 2\\text{NaCl} \\xrightarrow{\\Delta, \\text{MnO}_2} \\text{HgCl}_2 \\uparrow \\text{ (sublimes)} + \\text{Na}_2\\text{SO}_4$$
2. *By passing chlorine gas over heated mercury:*
$$\\text{Hg} + \\text{Cl}_2 \\xrightarrow{\\Delta} \\text{HgCl}_2$$

**Reactions:**
a. **Excess KI:** First forms red precipitate of $\\text{HgI}_2$, which dissolves in excess $\\text{KI}$ to form **Nessler's reagent**:
$$\\text{HgCl}_2 + 2\\text{KI} \\rightarrow \\text{HgI}_2 \\downarrow \\text{ (scarlet red)} + 2\\text{KCl}$$
$$\\text{HgI}_2 + 2\\text{KI} \\rightarrow \\text{K}_2[\\text{HgI}_4] \\; (\\text{Potassium tetraiodomercurate(II)})$$

b. **Ammonia gas ($\text{NH}_3$):** Forms white precipitate of ammonobasic mercuric chloride:
$$\\text{HgCl}_2 + 2\\text{NH}_3 \\rightarrow \\text{Hg}(\\text{NH}_2)\\text{Cl} \\downarrow \\text{ (infusible white ppt)} + \\text{NH}_4\\text{Cl}$$

c. **$\\text{SnCl}_2$ solution:** First reduces $\\text{HgCl}_2$ to white silky calomel ($\text{Hg}_2\text{Cl}_2$), then to grey metallic mercury:
$$2\\text{HgCl}_2 + \\text{SnCl}_2 \\rightarrow \\text{Hg}_2\\text{Cl}_2 \\downarrow \\text{ (white)} + \\text{SnCl}_4$$
$$\\text{Hg}_2\\text{Cl}_2 + \\text{SnCl}_2 \\rightarrow 2\\text{Hg} \\downarrow \\text{ (grey)} + \\text{SnCl}_4$$

d. **$\\text{NH}_4\\text{OH}$ solution:**
$$\\text{HgCl}_2 + 2\\text{NH}_4\\text{OH} \\rightarrow \\text{Hg}(\\text{NH}_2)\\text{Cl} \\downarrow \\text{ (white ppt)} + \\text{NH}_4\\text{Cl} + 2\\text{H}_2\\text{O}$$"""
            },
            {
                "id": "chem-hg-q35",
                "number": "35",
                "question": "Mention any two important uses of corrosive sublimate.",
                "answer": """1. Used in very dilute solution (1:1000) as a powerful **surgical antiseptic and disinfectant**.
2. Used for the preservation of anatomical specimens and wood against fungal decay."""
            },
            {
                "id": "chem-hg-q36",
                "number": "36",
                "question": "Give the chemistry of corrosive sublimate.",
                "answer": """Corrosive sublimate is **mercuric chloride ($\text{HgCl}_2$)**. It is a white, crystalline, covalent solid with a linear molecule ($\text{Cl-Hg-Cl}$). It is moderately soluble in cold water but highly soluble in hot water, alcohol, and ether. It is highly poisonous (corrosive to mucous membranes) and sublimes upon heating without melting at $302^\\circ\\text{C}$."""
            },
            {
                "id": "chem-hg-q37",
                "number": "37",
                "question": "Give the balanced chemical equation\na. Corrosive sublimate reacts with excess Kl solution\nb. HgCl2 is allowed to react with SnCl2",
                "answer": """**a. Reaction with excess KI:**
$$\\text{HgCl}_2 + 4\\text{KI} \\rightarrow \\text{K}_2[\\text{HgI}_4] + 2\\text{KCl}$$

**b. Reaction with $\\text{SnCl}_2$:**
$$2\\text{HgCl}_2 + \\text{SnCl}_2 \\rightarrow \\text{Hg}_2\\text{Cl}_2 \\downarrow \\text{ (white)} + \\text{SnCl}_4$$
$$\\text{Hg}_2\\text{Cl}_2 + \\text{SnCl}_2 \\rightarrow 2\\text{Hg} \\downarrow \\text{ (grey)} + \\text{SnCl}_4$$"""
            },
            {
                "id": "chem-hg-q38",
                "number": "38",
                "question": "A metal (M) is extracted from its suphide ore whose atomic number is 80. It also occurs as the amalgams of certain metals and is popularly known as quick silver.\na. Name the metal 'M' and write down the molecular formula of its common ore. Why is this metal called quick silver?\nb. State the process by which the ore is concentrated during its extraction.\nc. Write down the chemical reaction involved during reduction in its extraction.\nd. Mention a major use of the metal.",
                "answer": """**a. Name and Quick Silver:**
- Metal 'M': **Mercury ($\text{Hg}$, $Z=80$)**
- Common Ore: **Cinnabar ($\text{HgS}$)**
- *Why called quick silver:* Because it is a mobile, silvery-white liquid at room temperature with high surface tension, resembling liquid silver that flows quickly.

**b. Concentration Process:**
**Froth flotation process** using pine oil and xanthates.

**c. Reduction Reaction:**
Cinnabar is roasted in air at $500–600^\\circ\\text{C}$. $\\text{HgO}$ formed decomposes spontaneously into mercury vapour:
$$\\text{HgS} + \\text{O}_2 \\xrightarrow{\\Delta} \\text{Hg} \\uparrow + \\text{SO}_2 \\uparrow$$
*(Or $2\\text{HgS} + 3\\text{O}_2 \\rightarrow 2\\text{HgO} + 2\\text{SO}_2$, followed by $2\\text{HgO} \\rightarrow 2\\text{Hg} \\uparrow + \\text{O}_2$).*

**d. Major Use:**
Used in clinical thermometers, barometers, and fluorescent mercury vapour lamps."""
            },
            {
                "id": "chem-hg-q39",
                "number": "39",
                "question": "How is Nessler's reagent prepared from corrosive sublimate? Give a Laboratory use of Nessler's reagent.",
                "answer": """**Preparation:**
Corrosive sublimate solution is treated with potassium iodide until the scarlet-red precipitate of $\\text{HgI}_2$ just dissolves, and the resulting solution is made strongly alkaline with $\\text{KOH}$:
$$\\text{HgCl}_2 + 2\\text{KI} \\rightarrow \\text{HgI}_2 \\downarrow + 2\\text{KCl}$$
$$\\text{HgI}_2 + 2\\text{KI} \\rightarrow \\text{K}_2[\\text{HgI}_4]$$
$$\\text{Nessler's Reagent} = \\text{Alkaline solution of } \\text{K}_2[\\text{HgI}_4] + \\text{KOH}$$

**Laboratory Use:**
Used as an extremely sensitive analytical test for detecting **ammonia and ammonium ions ($\\text{NH}_4^+$)**, giving a characteristic reddish-brown precipitate of iodide of Millon's base."""
            },
            {
                "id": "chem-hg-q40",
                "number": "40",
                "question": "What happens when ammonia gas is passed through the aqueous solution of\na. Corrosive sublimate\nb. Calomel",
                "answer": """**a. Corrosive sublimate with ammonia:**
Gives a white precipitate of ammonobasic mercuric chloride (infusible white precipitate):
$$\\text{HgCl}_2 + 2\\text{NH}_3 \\rightarrow \\text{Hg}(\\text{NH}_2)\\text{Cl} \\downarrow \\text{ (white)} + \\text{NH}_4\\text{Cl}$$

**b. Calomel with ammonia:**
Turns black due to disproportionation yielding a mixture of finely divided grey metallic mercury and white ammonobasic mercuric chloride:
$$\\text{Hg}_2\\text{Cl}_2 + 2\\text{NH}_3 \\rightarrow [\\text{Hg}(\\text{NH}_2)\\text{Cl} + \\text{Hg}] \\downarrow \\text{ (black mixture)} + \\text{NH}_4\\text{Cl}$$"""
            },
            {
                "id": "chem-hg-q41",
                "number": "41",
                "question": "Write down a balanced chemical equation for the preparation of calomel. What happens when calomel is treated with ammonia solution?",
                "answer": """**Preparation of Calomel ($\text{Hg}_2\text{Cl}_2$):**
Triturate corrosive sublimate with metallic mercury and sublime:
$$\\text{HgCl}_2 + \\text{Hg} \\xrightarrow{\\Delta} \\text{Hg}_2\\text{Cl}_2$$

**Treatment with Ammonia Solution:**
Turns intensely black:
$$\\text{Hg}_2\\text{Cl}_2 + 2\\text{NH}_3 \\rightarrow \\text{Hg}(\\text{NH}_2)\\text{Cl} + \\text{Hg} \\downarrow \\text{ (black)} + \\text{NH}_4\\text{Cl}$$"""
            },
            {
                "id": "chem-hg-q42",
                "number": "42",
                "question": "How would you convert calomel into corrosive sublimate and vice versa, giving suitable chemical equations? Write an important use of calomel.",
                "answer": """**1. Calomel to Corrosive Sublimate:**
Heat calomel with chlorine water or aqua regia:
$$\\text{Hg}_2\\text{Cl}_2 + \\text{Cl}_2 \\rightarrow 2\\text{HgCl}_2$$

**2. Corrosive Sublimate to Calomel:**
Heat with metallic mercury or reduce with $\\text{SnCl}_2$:
$$\\text{HgCl}_2 + \\text{Hg} \\rightarrow \\text{Hg}_2\\text{Cl}_2$$

**Important Use of Calomel:**
Used in constructing the **standard calomel electrode (SCE)** as a reference electrode in electrochemical pH measurements."""
            },
            {
                "id": "chem-hg-q43",
                "number": "43",
                "question": "What is meant by mercury poisoning?",
                "answer": """Mercury poisoning (hydrargaria / Minamata disease) is severe toxic damage caused by inhalation of mercury vapours or ingestion of soluble mercuric salts and methylmercury. Mercury binds strongly to sulfhydryl ($-SH$) groups of enzymes and cellular proteins, causing central nervous system damage, tremors, sensory impairment, kidney damage, and cognitive degeneration."""
            },
            {
                "id": "chem-hg-q44",
                "number": "44",
                "question": "Give the molecular formula of: Nessler's reagent.",
                "answer": """$$\\text{K}_2[\\text{HgI}_4] \\quad (\\text{Potassium tetraiodomercurate(II)})$$"""
            },
            {
                "id": "chem-hg-q45",
                "number": "45",
                "question": "Write the action of Mercury with aqua regia.",
                "answer": """Aqua regia (3 parts conc. $\\text{HCl}$ + 1 part conc. $\\text{HNO}_3$) generates nascent chlorine, which oxidizes mercury into **corrosive sublimate ($\text{HgCl}_2$)**:
$$3\\text{HCl} + \\text{HNO}_3 \\rightarrow \\text{NOCl} + 2[\\text{Cl}] + 2\\text{H}_2\\text{O}$$
$$\\text{Hg} + 2[\\text{Cl}] \\rightarrow \\text{HgCl}_2$$"""
            },
            {
                "id": "chem-hg-q46",
                "number": "46",
                "question": "Write down the chemistry of corrosive sublimate.",
                "answer": """Corrosive sublimate is **mercuric chloride, $\\text{HgCl}_2$**. It is a white, needle-shaped crystalline covalent solid. It sublimes at $302^\\circ\\text{C}$ and hydrolyzes slightly in water. It is an extremely potent poison, acting as an enzyme inhibitor. It reacts with reducing agents ($\text{SnCl}_2$) to give white calomel and grey mercury."""
            },
            {
                "id": "chem-hg-q47",
                "number": "47",
                "question": "What peculiar behaviour does mercury have?",
                "answer": """1. It is the **only metal that is a liquid** at room temperature ($25^\\circ\\text{C}$, melting point $-38.83^\\circ\\text{C}$).
2. Exhibits high surface tension, forming spherical droplets that do not wet glass.
3. Readily dissolves other metals (except iron, platinum, tungsten) to form **amalgams**.
4. Shows relativistic contraction of $6s$ valence electrons, making them poorly available for metallic bonding."""
            },
            {
                "id": "chem-hg-q48",
                "number": "48",
                "question": "Write short notes on chemistry of calomel.",
                "answer": """Calomel is **mercurous chloride, $\\text{Hg}_2\\text{Cl}_2$**. It contains the dimeric ion $[\\text{Hg-Hg}]^{2+}$. It is an insoluble, heavy white powder. It is non-poisonous due to its insolubility in water. It decomposes upon exposure to sunlight into $\\text{HgCl}_2$ and grey $\\text{Hg}$. Used as a purgative in medicine and in calomel reference electrodes."""
            },
            {
                "id": "chem-hg-q49",
                "number": "49",
                "question": "What is meant by tailing of mercury?",
                "answer": """When pure mercury comes into contact with **ozone gas ($\text{O}_3$)**, it gets oxidized to mercurous oxide ($\text{Hg}_2\text{O}$), which dissolves in the remaining mercury:
$$2\\text{Hg} + \\text{O}_3 \\rightarrow \\text{Hg}_2\\text{O} + \\text{O}_2$$
Due to this, mercury loses its high surface tension, meniscus, and fluidity, and starts sticking to glass walls in the form of an elongated tail. This phenomenon is called **tailing of mercury**. It is restored by shaking with dilute acid or hydrogen peroxide."""
            }
        ]
    }

def get_iron():
    return {
        "name": "Iron",
        "questions": [
            {
                "id": "chem-fe-q50",
                "number": "50",
                "question": "A heavy metal is extracted from its oxide ore. During extraction, smelting of the calcinated ore is done in a blast furnace.\na. Name the metal and the ore.\nb. Draw the clean and labeled diagram of the blast furnace showing different zones.\nc. Write down the balanced chemical equations of slag formation reactions.",
                "answer": """**a. Name:** Metal: **Iron ($\text{Fe}$)**; Ore: **Haematite ($\text{Fe}_2\text{O}_3$)**

**b. Diagram of Blast Furnace:**
```
                     Charge (Ore + Coke + Limestone)
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Double Cup & Cone │
                         ├─────────────────────┤
     400°C - 700°C       │  Zone of Reduction  │  Fe2O3 -> Fe3O4 -> FeO -> Fe
                         ├─────────────────────┤
     800°C - 1000°C      │  Zone of Slag Form. │  CaCO3 -> CaO + CO2; CaO + SiO2 -> CaSiO3
                         ├─────────────────────┤
     1200°C - 1300°C     │   Zone of Fusion    │  Iron melts, absorbs carbon
                         ├─────────────────────┤
     1500°C - 2000°C     │ Zone of Combustion  │  C + O2 -> CO2; CO2 + C -> 2CO
                         ├─────────────────────┤  <-- Hot Air Blast (Tuyeres)
                         │       Hearth        │
                         └───┬─────────────┬───┘
                    Slag Tap ┘             └ Molten Iron Tap (Pig Iron)
```

**c. Slag Formation Reactions:**
Limestone acts as basic flux:
$$\\text{CaCO}_3 \\xrightarrow{\\Delta} \\text{CaO} + \\text{CO}_2$$
$$\\text{CaO} + \\text{SiO}_2 \\rightarrow \\text{CaSiO}_3 \\; (\\text{Fusible slag})$$"""
            },
            {
                "id": "chem-fe-q51",
                "number": "51",
                "question": "Describe rusting theory of Iron. Name the process of preventing iron from rusting.",
                "answer": """**Electrochemical Theory of Rusting:**
Rusting occurs through the formation of miniature electrochemical galvanic cells on the metal surface in the presence of dissolved oxygen and moisture.
- **Anodic Area (Oxidation):**
$$\\text{Fe} (s) \\rightarrow \\text{Fe}^{2+} (aq) + 2e^- \\quad (E^\\circ = -0.44\\text{ V})$$
- **Cathodic Area (Reduction):**
$$\\text{O}_2 + 4\\text{H}^+ + 4e^- \\rightarrow 2\\text{H}_2\\text{O} \\quad (E^\\circ = +1.23\\text{ V})$$
- **Overall Cell Reaction:**
$$2\\text{Fe} + \\text{O}_2 + 4\\text{H}^+ \\rightarrow 2\\text{Fe}^{2+} + 2\\text{H}_2\\text{O}$$
The $\\text{Fe}^{2+}$ ions are further oxidized by atmospheric oxygen to form hydrated ferric oxide:
$$4\\text{Fe}^{2+} + \\text{O}_2 + 4\\text{H}_2\\text{O} + 2x\\text{H}_2\\text{O} \\rightarrow 2\\text{Fe}_2\\text{O}_3\\cdot x\\text{H}_2\\text{O} \\; (\\textbf{Rust}) + 8\\text{H}^+$$

**Methods of Prevention:**
1. **Galvanization:** Coating iron with a thin layer of zinc.
2. **Cathodic Protection (Sacrificial Anode):** Attaching blocks of more electropositive metals like magnesium."""
            },
            {
                "id": "chem-fe-q52",
                "number": "52",
                "question": "Describe the Open-Hearth process for the manufacture of steel.",
                "answer": """The Open-Hearth (Siemens-Martin) process uses a regenerative reverberatory furnace lined with basic materials ($\\text{CaO, MgO}$) or acidic materials ($\\text{SiO}_2$).
1. **Charge:** Molten pig iron, scrap steel, and haematite ($\text{Fe}_2\text{O}_3$).
2. **Fuel:** Producer gas preheated in regenerative checker brickwork chambers to reach $1600–1700^\\circ\\text{C}$.
3. **Reactions:** Haematite oxidizes impurities:
$$3\\text{C} + \\text{Fe}_2\\text{O}_3 \\rightarrow 2\\text{Fe} + 3\\text{CO} \\uparrow$$
$$\\text{Si} + \\text{Fe}_2\\text{O}_3 \\rightarrow 2\\text{Fe} + 3\\text{SiO}_2$$
4. **Recarburization:** Calculated amount of **Spiegeleisen** (alloy of Fe, Mn, and C) is added to deoxidize the melt and achieve the desired percentage of carbon (0.1–1.5%)."""
            },
            {
                "id": "chem-fe-q53",
                "number": "53",
                "question": "Steel manufactured by Open Hearth process.\na. What is open Hearth process?\nb. Write down the chemical reactions occurring in Open-Hearth furnace.\nc. Why is Spiegeleisen added in the Open-Hearth furnace?\nd. Write down the composition of stainless steel.",
                "answer": """**a. Open Hearth Process:**
A modern commercial metallurgical process for manufacturing high-quality steel by oxidizing impurities from pig iron and scrap steel using iron ore ($\text{Fe}_2\text{O}_3$) in a shallow open-hearth reverberatory furnace using regenerative heating.

**b. Chemical Reactions:**
$$2\\text{Fe}_2\\text{O}_3 + 3\\text{Si} \\rightarrow 4\\text{Fe} + 3\\text{SiO}_2$$
$$\\text{Fe}_2\\text{O}_3 + 3\\text{Mn} \\rightarrow 2\\text{Fe} + 3\\text{MnO}$$
$$\\text{Fe}_2\\text{O}_3 + 3\\text{C} \\rightarrow 2\\text{Fe} + 3\\text{CO} \\uparrow$$
$$\\text{CaO} + \\text{SiO}_2 \\rightarrow \\text{CaSiO}_3 \\; (\\text{Slag})$$

**c. Role of Spiegeleisen:**
Spiegeleisen is an alloy of iron, manganese, and carbon.
1. Manganese acts as a **deoxidizer**, scavenging dissolved oxygen and removing dissolved sulphur as $\\text{MnS}$ into the slag.
2. Supplies the **exact stoichiometric amount of carbon** required to convert wrought-like melt into the desired grade of steel.

**d. Composition of Stainless Steel:**
- Iron ($\text{Fe}$): 70–74%
- Chromium ($\text{Cr}$): 18%
- Nickel ($\text{Ni}$): 8%
- Carbon ($\text{C}$): 0.1–0.2%"""
            },
            {
                "id": "chem-fe-q54",
                "number": "54",
                "question": "Write down the composition and an important use of cast iron.",
                "answer": """- **Composition:** 92–95% Iron, 2.5–4.5% Carbon, and small amounts of Si, Mn, P, and S.
- **Use:** Used for casting heavy machine bases, drain pipes, lamp posts, engine blocks, and railway sleepers due to its high hardness and fluidity when melted."""
            },
            {
                "id": "chem-fe-q55",
                "number": "55",
                "question": "Give an important use of each of the Stainless steel.",
                "answer": """Used for manufacturing surgical instruments, kitchen cutlery, household cooking utensils, and chemical reactor vessels due to its high resistance to rust and acidic corrosion."""
            },
            {
                "id": "chem-fe-q56",
                "number": "56",
                "question": "Write the compositions of\na. Stainless steel\nb. Spiegeleisen",
                "answer": """a. **Stainless Steel:** Fe (70–74%), Cr (18%), Ni (8%), C (0.1–0.2%).  
b. **Spiegeleisen:** Fe (60–80%), Mn (15–30%), C (4–5%)."""
            },
            {
                "id": "chem-fe-q57",
                "number": "57",
                "question": "Write the formula and one use of each green vitriol and Mohr's salt",
                "answer": """- **Green Vitriol:**
  - *Formula:* $\\text{FeSO}_4\\cdot 7\\text{H}_2\\text{O}$
  - *Use:* Used in making black writing inks and in medicine to treat iron-deficiency anaemia.
- **Mohr's Salt:**
  - *Formula:* $\\text{FeSO}_4\\cdot(\\text{NH}_4)_2\\text{SO}_4\\cdot 6\\text{H}_2\\text{O}$
  - *Use:* Used as a primary analytical standard in redox titrations (permanganometry)."""
            },
            {
                "id": "chem-fe-q58",
                "number": "58",
                "question": "Give the composition and uses of wrought iron.",
                "answer": """- **Composition:** Purest commercial form of iron containing 99.8–99.9% Iron, with only 0.1–0.25% Carbon and traces of slag.
- **Uses:** Highly malleable and ductile; used for making chains, anchors, bolts, nails, agricultural tools, and electromagnets."""
            },
            {
                "id": "chem-fe-q59",
                "number": "59",
                "question": "What is the composition of stainless steel? Give an important use of such steel.",
                "answer": """- **Composition:** Fe (approx. 72–74%), Cr (18%), Ni (8%), C (0.1–0.2%).
- **Use:** Used in surgical instruments and dairy/chemical processing tanks."""
            },
            {
                "id": "chem-fe-q60",
                "number": "60",
                "question": "Name any two important ores of iron. Which parts of Nepal are these ores mainly found?",
                "answer": """- **Two Important Ores:**
  1. **Haematite** ($\\text{Fe}_2\\text{O}_3$)
  2. **Magnetite** ($\\text{Fe}_3\\text{O}_4$)
- **Occurrence in Nepal:**
  Large iron deposits are located in **Phulchoki (Lalitpur), Toshe (Ramechhap), Labdi Khola (Tanahun), and Dhuwakot (Parbat)**."""
            },
            {
                "id": "chem-fe-q61",
                "number": "61",
                "question": "Write down chemical reactions that occur in zone of reduction of blast furnace during extraction of iron.",
                "answer": """In the Zone of Reduction ($400–700^\\circ\\text{C}$):
$$3\\text{Fe}_2\\text{O}_3 + \\text{CO} \\xrightarrow{400^\\circ\\text{C}} 2\\text{Fe}_3\\text{O}_4 + \\text{CO}_2 \\uparrow$$
$$\\text{Fe}_3\\text{O}_4 + \\text{CO} \\xrightarrow{500-600^\\circ\\text{C}} 3\\text{FeO} + \\text{CO}_2 \\uparrow$$
$$\\text{FeO} + \\text{CO} \\xrightarrow{700^\\circ\\text{C}} \\text{Fe (spongy iron)} + \\text{CO}_2 \\uparrow$$"""
            },
            {
                "id": "chem-fe-q62",
                "number": "62",
                "question": "What is meant by Thomas Slag? Write its one use.",
                "answer": """Thomas slag is **calcium silicophosphate [$\\text{Ca}_3(\\text{PO}_4)_2\\cdot\\text{CaSiO}_3$]**, produced during steel manufacturing in the basic Bessemer process when basic lining ($\text{CaO/MgO}$) reacts with phosphorus and silica impurities:
$$6\\text{CaO} + \\text{P}_4\\text{O}_{10} \\rightarrow 2\\text{Ca}_3(\\text{PO}_4)_2$$
- **Use:** Finely powdered and used as a valuable **phosphate fertilizer** in agriculture."""
            },
            {
                "id": "chem-fe-q63",
                "number": "63",
                "question": "Differentiate between cast iron and wrought iron.",
                "answer": """| S.N. | Feature | Cast Iron (Pig Iron) | Wrought Iron |
| :--- | :--- | :--- | :--- |
| 1. | **Carbon Content** | High (2.5% to 4.5% C) | Lowest (0.1% to 0.25% C) |
| 2. | **Purity** | Most impure commercial iron | Purest commercial form of iron (~99.9% Fe) |
| 3. | **Hardness & Brittleness**| Extremely hard and brittle | Soft, malleable, and highly ductile |
| 4. | **Malleability** | Cannot be forged or welded | Easily forged, bent, and welded |
| 5. | **Melting Point** | Lower (~1200°C) | Higher (~1500°C) |"""
            },
            {
                "id": "chem-fe-q64",
                "number": "64",
                "question": "Why is the open-hearth process more advantageous than the Bessemer process of manufacture of steel?",
                "answer": """1. **Better Quality Control:** The process is slower (taking 8–10 hours), allowing periodic chemical sampling and testing to adjust the exact carbon and alloy composition.
2. **Direct Use of Scrap:** Consumes large quantities of inexpensive steel scrap.
3. **Higher Yield & Low Loss:** Temperature can be accurately regulated; metal loss by volatilization is minimal.
4. **No Air Blast Contamination:** Does not entrap atmospheric nitrogen gas, producing steel with superior tensile strength."""
            },
            {
                "id": "chem-fe-q65",
                "number": "65",
                "question": "Define Rusting of iron. Write two methods by which rusting of iron can be prevented.",
                "answer": """**Definition:**
Rusting is the slow, spontaneous, electrochemical corrosion of iron in the presence of atmospheric oxygen and moisture to form a brown, flaky, porous deposit of **hydrated ferric oxide ($\text{Fe}_2\text{O}_3\cdot x\text{H}_2\text{O}$)**.

**Prevention Methods:**
1. **Galvanization:** Coating the iron surface with molten zinc.
2. **Barrier Coating:** Applying anti-rust paint, grease, or oil."""
            },
            {
                "id": "chem-fe-q66",
                "number": "66",
                "question": "What happens when: Few drops of potassium ferrocyanide is added to aqueous solution of FeCl3.",
                "answer": """A deep blue precipitate or colloidal suspension of **Prussian blue [ferric ferrocyanide, $\\text{Fe}_4[\\text{Fe(CN)}_6]_3$]** is formed:
$$4\\text{FeCl}_3 + 3\\text{K}_4[\\text{Fe(CN)}_6] \\rightarrow \\text{Fe}_4[\\text{Fe(CN)}_6]_3 \\downarrow \\text{ (Prussian blue)} + 12\\text{KCl}$$"""
            },
            {
                "id": "chem-fe-q67",
                "number": "67",
                "question": "What is stainless steel?",
                "answer": """Stainless steel is an alloy steel composed of iron containing **18% Chromium, 8% Nickel, and 0.1–0.2% Carbon**. Chromium forms an invisible, self-healing passive surface oxide film of $\\text{Cr}_2\\text{O}_3$ that protects the iron from rusting."""
            },
            {
                "id": "chem-fe-q68",
                "number": "68",
                "question": "What is the function of limestone in the smelting of iron? b. Write the principle involved in manufacture of steel by Open Hearth process.",
                "answer": """**a. Function of Limestone:**
Limestone ($\text{CaCO}_3$) acts as a **basic flux**. At high furnace temperature, it decomposes to calcium oxide ($\text{CaO}$), which combines with infusible acidic gangue ($\text{SiO}_2$) to form a low-density, fusible molten slag:
$$\\text{CaCO}_3 \\rightarrow \\text{CaO} + \\text{CO}_2$$
$$\\text{CaO} + \\text{SiO}_2 \\rightarrow \\text{CaSiO}_3 \\; (\\text{Slag})$$

**b. Principle of Open-Hearth Process:**
Excess carbon, silicon, manganese, and phosphorus present in pig iron and scrap steel are oxidized to volatile oxides or fusible slag by the addition of calculated quantities of solid iron ore ($\text{Fe}_2\text{O}_3$), followed by deoxidation and recarburization with Spiegeleisen."""
            },
            {
                "id": "chem-fe-q69",
                "number": "69",
                "question": "What is rusting ? Describe the electrochemical theory of rusting of iron. List any two methods for the prevention of rusting. [5]",
                "answer": """**Rusting:**
Rusting is the slow electrochemical oxidation of iron in the presence of air and moisture to produce reddish-brown hydrated ferric oxide ($\text{Fe}_2\text{O}_3\cdot x\text{H}_2\text{O}$).

### Electrochemical Theory of Rusting:
1. **Anodic Reaction:** Impure iron acts as the anode, releasing electrons:
$$\\text{Fe} \\rightarrow \\text{Fe}^{2+} + 2e^- \\quad (E^\\circ = -0.44\\text{ V})$$
2. **Cathodic Reaction:** Dissolved oxygen in water droplets containing dissolved $\\text{CO}_2$ ($\text{H}^+$ ions) acts as the cathode:
$$\\text{O}_2 + 4\\text{H}^+ + 4e^- \\rightarrow 2\\text{H}_2\\text{O} \\quad (E^\\circ = +1.23\\text{ V})$$
3. **Overall Cell Reaction:**
$$2\\text{Fe} + \\text{O}_2 + 4\\text{H}^+ \\rightarrow 2\\text{Fe}^{2+} + 2\\text{H}_2\\text{O}$$
4. **Rust Formation:** Ferrous ions diffuse and are oxidized by atmospheric oxygen:
$$4\\text{Fe}^{2+} + \\text{O}_2 + 4\\text{H}_2\\text{O} + 2x\\text{H}_2\\text{O} \\rightarrow 2\\text{Fe}_2\\text{O}_3\\cdot x\\text{H}_2\\text{O} \\; (\\textbf{Rust}) + 8\\text{H}^+$$

**Prevention Methods:**
1. **Galvanization:** Coating with zinc.
2. **Cathodic Protection:** Sacrificial anode of magnesium or zinc."""
            }
        ]
    }

def get_silver():
    return {
        "name": "Silver",
        "questions": [
            {
                "id": "chem-ag-q70",
                "number": "70",
                "question": "Give an important use of silver nitrate.",
                "answer": """Silver nitrate is used as an **electoral indelible ink** to mark voters' fingers during democratic elections, as a reagent for detecting halide ions, and in silvering mirrors."""
            },
            {
                "id": "chem-ag-q71",
                "number": "71",
                "question": "What is meant by frosting silver?",
                "answer": """Frosting of silver is the chemical treatment of an alloy of silver and copper with dilute sulfuric acid to dissolve the surface copper, leaving behind a microscopic, porous layer of pure silver that gives the surface a soft, matte white, frosted appearance."""
            },
            {
                "id": "chem-ag-q72",
                "number": "72",
                "question": "Why is silver nitrate solution used for staining fingers of voters during elections?",
                "answer": """When silver nitrate contacts the skin, it reacts with epidermal proteins and skin secretions to form an insoluble silver-protein complex, which photo-reduces rapidly in daylight into colloidal metallic silver:
$$2\\text{Ag}^+ + \\text{organic tissue} \\xrightarrow{h\\nu} 2\\text{Ag (colloidal black)} \\downarrow$$
This stain cannot be washed off with water or soap and only disappears as the dead epidermal cells naturally shed."""
            },
            {
                "id": "chem-ag-q73",
                "number": "73",
                "question": "Why is silver nitrate solution protected from sunlight?",
                "answer": """Silver nitrate undergoes photochemical decomposition when exposed to sunlight, reducing into finely divided black metallic silver and brown nitrogen dioxide gas:
$$2\\text{AgNO}_3 \\xrightarrow{h\\nu} 2\\text{Ag} \\downarrow \\text{ (black)} + 2\\text{NO}_2 \\uparrow + \\text{O}_2 \\uparrow$$
To prevent degradation, it is stored in amber or dark brown bottles."""
            },
            {
                "id": "chem-ag-q74",
                "number": "74",
                "question": "What is meant by 'Spongy Silver'?",
                "answer": """Spongy silver is a porous, finely divided, high-surface-area form of metallic silver obtained by the thermal decomposition of silver carbonate or silver oxalate:
$$2\\text{Ag}_2\\text{CO}_3 \\xrightarrow{\\Delta} 4\\text{Ag (spongy)} + 2\\text{CO}_2 \\uparrow + \\text{O}_2 \\uparrow$$"""
            },
            {
                "id": "chem-ag-q75",
                "number": "75",
                "question": "Give reason: Silver nitrate produces permanent black stain on the skin?",
                "answer": """Upon touching the skin, $\\text{AgNO}_3$ oxidizes organic protein tissues and is reduced to metallic silver in a colloidal black state, staining the skin black until outer skin layers shed."""
            },
            {
                "id": "chem-ag-q76",
                "number": "76",
                "question": "What is the action of heat on silver nitrate.",
                "answer": """$$\\text{AgNO}_3 \\xrightarrow{212^\\circ\\text{C}} \\text{Melts without decomposition}$$
$$\\text{AgNO}_3 \\xrightarrow{450^\\circ\\text{C}} \\text{AgNO}_2 + \\frac{1}{2}\\text{O}_2$$
$$\\text{AgNO}_2 \\xrightarrow{\\text{red heat}} 2\\text{Ag (metallic)} + 2\\text{NO}_2 \\uparrow + \\text{O}_2 \\uparrow$$"""
            },
            {
                "id": "chem-ag-q77",
                "number": "77",
                "question": "What do you mean by noble metals? Give any two examples.",
                "answer": """Noble metals are metallic chemical elements that have very high standard reduction potentials, low chemical reactivity, and exceptional resistance to corrosion and oxidation even at elevated temperatures. Examples: **Gold ($\text{Au}$)** and **Platinum ($\text{Pt}$)**."""
            },
            {
                "id": "chem-ag-q78",
                "number": "78",
                "question": "Give two uses of silver nitrate.",
                "answer": """1. In analytical chemistry as a laboratory reagent for testing and estimating halides ($\text{Cl}^-$, $\text{Br}^-$, $\text{I}^-$).
2. In medicine as a mild antiseptic, caustic agent, and astringent (Lunar caustic)."""
            },
            {
                "id": "chem-ag-q79",
                "number": "79",
                "question": "How is the presence of halide ions tested with silver nitrate solution?",
                "answer": """To an aqueous solution of the halide acidified with dilute $\\text{HNO}_3$, add $\\text{AgNO}_3$ solution:
- **Chloride ($\\text{Cl}^-$):** Gives a **curdy white ppt** of $\\text{AgCl}$, soluble in dilute $\\text{NH}_4\\text{OH}$.
$$\\text{Ag}^+ + \\text{Cl}^- \\rightarrow \\text{AgCl} \\downarrow \\text{ (white)}$$
- **Bromide ($\\text{Br}^-$):** Gives a **pale yellow ppt** of $\\text{AgBr}$, sparingly soluble in concentrated $\\text{NH}_4\\text{OH}$.
$$\\text{Ag}^+ + \\text{Br}^- \\rightarrow \\text{AgBr} \\downarrow \\text{ (pale yellow)}$$
- **Iodide ($\\text{I}^-$):** Gives a **canary yellow ppt** of $\\text{AgI}$, completely insoluble in $\\text{NH}_4\\text{OH}$.
$$\\text{Ag}^+ + \\text{I}^- \\rightarrow \\text{AgI} \\downarrow \\text{ (yellow)}$$"""
            },
            {
                "id": "chem-ag-q80",
                "number": "80",
                "question": "Why are silver ores leached with metal cyanides for the extraction of silver?",
                "answer": """In the **MacArthur-Forrest Cyanide Process**, powdered silver ore is leached with dilute (0.4–0.7%) sodium cyanide ($\\text{NaCN}$) in the presence of continuous air blowing:
$$4\\text{Ag} + 8\\text{NaCN} + 2\\text{H}_2\\text{O} + \\text{O}_2 \\rightarrow 4\\text{Na}[\\text{Ag(CN)}_2] + 4\\text{NaOH}$$
$$\\text{Ag}_2\\text{S} + 4\\text{NaCN} \\rightleftharpoons 2\\text{Na}[\\text{Ag(CN)}_2] + \\text{Na}_2\\text{S}$$
Cyanide forms an extremely stable, water-soluble complex **sodium dicyanoargentate(I) [$\\text{Na}[\\text{Ag(CN)}_2]$]**, allowing silver to be cleanly separated from insoluble gangue impurities. Silver is then displaced by zinc dust."""
            }
        ]
    }
