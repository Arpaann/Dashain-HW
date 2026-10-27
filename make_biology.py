import json
import os

out_dir = r"C:\Users\Arpan\.gemini\antigravity\scratch\studyroom\data"
os.makedirs(out_dir, exist_ok=True)

biology_data = {
    "id": "biology",
    "title": "Biology",
    "icon": "dna",
    "description": "Part I: Botany (Genetics, Nucleic Acids, Crossing Over) and Part II: Zoology (Circulatory System, Nervous System, AIDS).",
    "sections": [
        {
            "name": "Part I: Botany",
            "questions": [
                {
                    "id": "bio-bot-q1",
                    "number": "1",
                    "question": "Define nucleotide and nucleoside.",
                    "answer": """**Nucleoside:**
A nucleoside is a chemical compound formed by the condensation of a pentose sugar (either ribose or 2'-deoxyribose) with a nitrogenous base (purine or pyrimidine) via a $\\beta\\text{-N-glycosidic}$ bond at the 1'-carbon of the sugar. It lacks a phosphate group.
- *Formula:* $\\text{Nucleoside} = \\text{Pentose Sugar} + \\text{Nitrogenous Base}$
- *Examples:* Adenosine, Deoxyadenosine, Guanosine, Cytidine, Thymidine, Uridine.

**Nucleotide:**
A nucleotide is the phosphorylated form of a nucleoside, consisting of a pentose sugar, a nitrogenous base, and one or more phosphate groups attached by an ester linkage to the 5'-carbon of the sugar. Nucleotides are the fundamental monomeric building blocks of nucleic acids (DNA and RNA).
- *Formula:* $\\text{Nucleotide} = \\text{Nucleoside} + \\text{Phosphoric Acid} = \\text{Sugar} + \\text{Base} + \\text{Phosphate}$
- *Examples:* Adenosine monophosphate (AMP), Deoxyadenosine monophosphate (dAMP), dGMP, dCMP, dTMP."""
                },
                {
                    "id": "bio-bot-q2",
                    "number": "2",
                    "question": "Define chromosomes, DNA and Chromatin fiber.",
                    "answer": """**Chromosomes:**
Chromosomes are highly condensed, rod-like structural units composed of DNA and basic histone proteins found in the nucleus of eukaryotic cells, which become distinctly visible during cell division (metaphase). They function as the physical carriers of genetic information (genes) from one generation to the next.

**DNA (Deoxyribonucleic Acid):**
DNA is a long polymeric macromolecule composed of two complementary polynucleotide chains coiled around a common central axis into a double helix. It contains the hereditary genetic blueprint responsible for development, functioning, growth, and reproduction of all known cellular organisms and many viruses.

**Chromatin fiber:**
Chromatin fiber is a relaxed, uncoiled, diffuse, nucleoprotein filament network present inside the eukaryotic nucleus during the interphase stage of the cell cycle. It consists of DNA wrapped around an octamer of histone proteins (nucleosomes), which condenses into chromosomes during cell division."""
                },
                {
                    "id": "bio-bot-q3",
                    "number": "3",
                    "question": "Discuss the structure of nucleotide. (Must include (Pentose sugar, nitrogenous base and phosphoric acid).",
                    "answer": """A nucleotide is the structural monomeric unit of nucleic acids. Every nucleotide is composed of three chemically distinct components:

```
      Phosphate Group          Pentose Sugar           Nitrogenous Base
         (PO4³⁻)            (Ribose / Deoxyribose)   (Purine / Pyrimidine)
            |                         |                       |
       [Phosphate] --- phosphoester --- [ C5' - Sugar - C1' ] --- N-glycosidic --- [Base]
                                            bond                    bond
```

**1. Pentose Sugar:**
A five-carbon monosaccharide ring.
- In RNA, the sugar is $\\text{D-ribose}$ ($\\text{C}_5\\text{H}_{10}\\text{O}_5$), which has a hydroxyl group ($-\\text{OH}$) at both the 2' and 3' carbon positions.
- In DNA, the sugar is $\\text{2'-deoxy-D-ribose}$ ($\\text{C}_5\\text{H}_{10}\\text{O}_4$), which lacks an oxygen atom at the 2' position (possessing $-\\text{H}$ instead of $-\\text{OH}$), making DNA chemically more stable than RNA.

**2. Nitrogenous Base:**
Nitrogen-containing heterocyclic aromatic ring compounds attached to the 1'-carbon ($\\text{C}_1'$) of the pentose sugar by a $\\beta\\text{-N-glycosidic bond}$. They are divided into two classes:
- **Purines:** Double-ring structures containing a six-membered pyrimidine ring fused to a five-membered imidazole ring. These are Adenine (A) and Guanine (G).
- **Pyrimidines:** Single six-membered rings. These are Cytosine (C), Thymine (T) (found only in DNA), and Uracil (U) (found only in RNA in place of Thymine).

**3. Phosphoric Acid ($\\text{H}_3\\text{PO}_4$):**
Phosphate group provides an acidic character and a net negative charge to the nucleic acid. It is esterified to the hydroxyl group attached to the 5'-carbon ($\\text{C}_5'$) of the pentose sugar via a phosphoester bond. When multiple nucleotides polymerize, adjacent nucleotides are linked by $3',5'\\text{-phosphodiester bonds}$ between the $3'\\text{-OH}$ of one sugar and the $5'\\text{-phosphate}$ of the next."""
                },
                {
                    "id": "bio-bot-q4",
                    "number": "4",
                    "question": "Discuss the Watson and crick model of DNA with well labelled diagram. Mention the function of DNA.",
                    "answer": """In 1953, James Watson and Francis Crick proposed the double-helical secondary structure model of B-DNA based on X-ray diffraction data obtained by Rosalind Franklin and Maurice Wilkins.

### Key Features of the Watson-Crick Model:
1. **Double Helix:** DNA consists of two antiparallel polynucleotide chains wound around a common central axis in a right-handed spiral. One strand runs in the $5' \\rightarrow 3'$ direction, while the complementary strand runs in the $3' \\rightarrow 5'$ direction.
2. **Backbone and Base Rungs:** The outer sugar-phosphate-sugar chain forms the structural backbone, while the hydrophobic nitrogenous bases project inward into the helix, arranged perpendicular to the main axis like the rungs of a spiral staircase.
3. **Complementary Base Pairing:** Purines always pair with pyrimidines through specific hydrogen bonds:
   - Adenine pairs exclusively with Thymine ($A = T$) via two hydrogen bonds.
   - Guanine pairs exclusively with Cytosine ($G \\equiv C$) via three hydrogen bonds.
4. **Dimensions of B-DNA:**
   - The diameter of the double helix is uniformly $2.0 \\text{ nm}$ ($20 \\text{ \\AA}$).
   - The pitch (length of one complete helical turn) is $3.4 \\text{ nm}$ ($34 \\text{ \\AA}$).
   - Each complete turn contains approximately $10$ base pairs, giving a distance between two adjacent base pairs of $0.34 \\text{ nm}$ ($3.4 \\text{ \\AA}$).
   - Each helix contains alternating major grooves and minor grooves along its outer surface.

### Labelled Diagram of DNA Double Helix:
```
     5' End                                              3' End
       |                                                    |
     [ P ] - Sugar --- A ===================== T --- Sugar - [ P ]
               |                                       |
             [ P ] - Sugar --- G ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡ C --- Sugar - [ P ]
                       |                               |
                     [ P ] - Sugar --- T ===================== A --- Sugar - [ P ]
                               |                               |
                             [ P ] - Sugar --- C ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡ G --- Sugar - [ P ]
                                       |                               |
                                     3' End                          5' End

      |<------------------------ 2.0 nm (Diameter) ------------------------>|
      |<---------- Distance between adjacent base pairs = 0.34 nm --------->|
      |<---------- One complete turn (10 bp) = 3.4 nm (Pitch) -------------->|
```

### Functions of DNA:
1. **Genetic Information Storage:** Stores all hereditary instructions required for the architecture, growth, and functioning of the organism.
2. **Replication and Inheritance:** DNA replicates semi-conservatively during the S-phase of the cell cycle, ensuring precise transmission of genetic traits to daughter cells.
3. **Protein Synthesis (Gene Expression):** Acts as a master template to transcribe messenger RNA (mRNA), which directs the sequence of amino acids during translation.
4. **Source of Genetic Variations:** Spontaneous mutations and recombination provide variations essential for adaptation and biological evolution."""
                },
                {
                    "id": "bio-bot-q5",
                    "number": "5",
                    "question": "Discuss the different types of DNA.",
                    "answer": """Based on conformation, pitch, base pairs per turn, and conditions of hydration, double-stranded DNA exhibits different structural forms:

1. **B-DNA:**
   - The standard, physiologically prevalent, right-handed double-helical form found under physiological conditions (high humidity and low ionic strength).
   - Contains $10$ base pairs per helical turn, with a diameter of $2.0 \\text{ nm}$ and a helical rise of $0.34 \\text{ nm}$ per base pair.
2. **A-DNA:**
   - A wider, more compact right-handed double helix that forms under dehydrated conditions (75% relative humidity) and high salt concentrations.
   - Contains $11$ base pairs per turn, with a diameter of $2.6 \\text{ nm}$ and a pitch of $2.8 \\text{ nm}$. The base pairs are tilted at $20^\\circ$ to the helical axis.
3. **C-DNA:**
   - A right-handed double helix formed at approximately 66% relative humidity in the presence of lithium ions ($\\text{Li}^+$).
   - Contains $9.33$ base pairs per turn with a pitch of $3.1 \\text{ nm}$ and diameter of $1.9 \\text{ nm}$.
4. **D-DNA:**
   - A rare right-handed variant observed in synthetic DNA polymers devoid of guanine, containing $8$ base pairs per turn.
5. **Z-DNA:**
   - A left-handed double helix discovered by Alexander Rich, characterized by a zigzag sugar-phosphate backbone.
   - Forms in alternating purine-pyrimidine sequences (e.g., poly(dG-dC)) at high salt concentrations.
   - Contains $12$ base pairs ($6$ dimers) per turn, a narrower diameter of $1.8 \\text{ nm}$, and a pitch of $4.5 \\text{ nm}$.

*(Based on location, DNA is also classified into Nuclear DNA found inside the nucleus, and Extranuclear/Organellar DNA found in mitochondria and chloroplasts.)*"""
                },
                {
                    "id": "bio-bot-q6",
                    "number": "6",
                    "question": "Write the Chargaff rule of DNA.",
                    "answer": """In the late 1940s, Erwin Chargaff formulated fundamental empirical generalizations regarding the quantitative composition of bases in double-stranded DNA:

1. **Equimolar Ratio of Purines to Pyrimidines:** In any double-stranded DNA molecule, the total concentration of purines equals the total concentration of pyrimidines:
$$[\\text{Purines}] = [\\text{Pyrimidines}] \\implies [A] + [G] = [T] + [C]$$
2. **Specific Base Pairing Equality:** The molar amount of Adenine is always equal to Thymine, and the molar amount of Guanine is always equal to Cytosine:
$$[A] = [T] \\implies \\frac{[A]}{[T]} = 1$$
$$[G] = [C] \\implies \\frac{[G]}{[C]} = 1$$
3. **Base Ratio ($A+T / G+C$):** The ratio $\\frac{[A] + [T]}{[G] + [C]}$ is constant for a given biological species, but varies widely between different taxonomic species.
4. **Single-stranded exception:** Chargaff's rules apply strictly to double-stranded DNA (dsDNA) and do not hold for single-stranded DNA (ssDNA) or RNA."""
                },
                {
                    "id": "bio-bot-q7",
                    "number": "7",
                    "question": "Define RNA. Discuss its structure and types with their functions.",
                    "answer": """**Definition:**
Ribonucleic Acid (RNA) is a single-stranded polymeric biological macromolecule composed of ribonucleotide units linked by $3',5'\\text{-phosphodiester bonds}$. It acts as the genetic material in certain viruses (retroviruses) and plays a central role in gene expression and protein biosynthesis in all living cells.

**Structure of RNA:**
- Unlike DNA, cellular RNA is typically single-stranded, although it can fold back onto itself to form localized hairpins and loops containing short complementary double-helical regions.
- Its pentose sugar is $\\text{D-ribose}$ containing a reactive $2'\\text{-OH}$ group.
- The nitrogenous bases consist of Adenine (A), Guanine (G), Cytosine (C), and Uracil (U) (which replaces Thymine).

### Major Types of RNA and Their Functions:

1. **Messenger RNA (mRNA):**
   - Comprises 3–5% of total cellular RNA.
   - Linear, variable-length molecule carrying genetic codons from chromosomal DNA in the nucleus to the ribosomes in the cytoplasm.
   - *Function:* Serves as the direct template for polypeptide synthesis during translation.

2. **Transfer RNA (tRNA) / Soluble RNA:**
   - Comprises 10–15% of total cellular RNA.
   - Smallest RNA molecule (73–93 nucleotides) folded into a characteristic cloverleaf secondary structure.
   - *Function:* Acts as an adaptor molecule that reads the mRNA codon sequence via its anticodon triplet and brings the matching activated amino acid to the growing polypeptide chain.

3. **Ribosomal RNA (rRNA):**
   - Comprises the most abundant fraction (80–85% of total cellular RNA).
   - Highly folded and integrated with ribosomal proteins to form the two subunits of ribosomes (e.g., 70S ribosomes in prokaryotes; 80S in eukaryotes).
   - *Function:* Provides the structural framework for ribosomes and exhibits catalytic peptidyl transferase activity (as a ribozyme) that catalyzes peptide bond formation."""
                },
                {
                    "id": "bio-bot-q8",
                    "number": "8",
                    "question": "Write a short note of t-RNA.",
                    "answer": """Transfer RNA (tRNA), also known as soluble RNA (sRNA), is an essential adaptor molecule in protein biosynthesis. It was modeled into a cloverleaf secondary structure by Robert Holley in 1965.

```
                     3' End - A - C - C - OH  (Amino Acid Binding Site)
                     5' End - G - ...
                                  |
                           [ D-Arm & Loop ] ---- [ Variable Loop ]
                                  |
                         [ Anticodon Loop ]
                              ( | | | )
                            3'- U A C -5'  (Anticodon Triplet)
```

### Key Structural Features:
1. **Amino Acid Acceptor Stem:** Consists of a 7-base-pair stem ending in an unpaired $5'\\text{-CCA-}3'$ sequence at the 3'-terminal hydroxyl group, to which a specific amino acid is covalently attached during aminoacylation.
2. **Anticodon Loop:** Contains a specific sequence of three unpaired nucleotides (anticodon) complementary to a specific codon on mRNA.
3. **D-Loop (DHU Arm):** Contains the modified base dihydrouracil, involved in recognition by the enzyme aminoacyl-tRNA synthetase.
4. **$\\text{T}\\psi\\text{C}$ Loop:** Contains pseudouridine ($\\psi$) and thymine, responsible for binding the tRNA molecule to the ribosome.
5. **Variable Loop:** A small loop of variable size situated between the anticodon loop and the $\\text{T}\\psi\\text{C}$ loop.

**Function:**
tRNA transfers specific activated amino acids from the cytoplasm to the ribosome and accurately aligns them according to the genetic code on the mRNA template."""
                },
                {
                    "id": "bio-bot-q9",
                    "number": "9",
                    "question": "Write about the similarities between DNA and RNA.",
                    "answer": """1. **Chemical Composition:** Both are linear polymers of nucleotides (polynucleotides) composed of three shared basic components: a pentose sugar, heterocyclic nitrogenous bases, and phosphoric acid.
2. **Phosphodiester Linkages:** In both DNA and RNA, adjacent monomeric nucleotides are joined together by covalent $3',5'\\text{-phosphodiester bonds}$.
3. **Common Nitrogenous Bases:** Both macromolecules share three common nitrogenous bases: Adenine (A), Guanine (G), and Cytosine (C).
4. **Carriers of Genetic Information:** Both can store and transmit genetic information (DNA in cellular organisms; RNA in RNA viruses such as HIV, Tobacco Mosaic Virus, and influenza).
5. **Synthesis Mechanism:** Both polymers are synthesized in the $5' \\rightarrow 3'$ direction using an existing nucleic acid template by polymerase enzymes (DNA polymerase and RNA polymerase)."""
                },
                {
                    "id": "bio-bot-q10",
                    "number": "10",
                    "question": "Differentiate between DNA and RNA.",
                    "answer": """| S.N. | Feature | DNA (Deoxyribonucleic Acid) | RNA (Ribonucleic Acid) |
| :--- | :--- | :--- | :--- |
| 1. | **Strand Structure** | Typically double-stranded double helix (except in certain viruses like $\\phi \\times 174$). | Typically single-stranded linear or folded chain. |
| 2. | **Pentose Sugar** | 2'-deoxy-D-ribose ($\\text{C}_5\\text{H}_{10}\\text{O}_4$), lacking oxygen at 2' carbon. | D-ribose ($\\text{C}_5\\text{H}_{10}\\text{O}_5$), possessing a hydroxyl group ($-\\text{OH}$) at 2' carbon. |
| 3. | **Pyrimidines** | Contains Cytosine (C) and Thymine (T). | Contains Cytosine (C) and Uracil (U) in place of Thymine. |
| 4. | **Chargaff's Rule** | Strictly obeys Chargaff's base pairing rules ($A=T, G \\equiv C$). | Does not obey Chargaff's rule because it is single-stranded. |
| 5. | **Stability** | Highly stable chemically and genetically due to lack of $2'\\text{-OH}$. | Chemically more labile and reactive due to free $2'\\text{-OH}$ group. |
| 6. | **Location** | Chiefly confined to the nucleus; small amounts in mitochondria and chloroplasts. | Synthesized in nucleus; mainly found distributed in cytoplasm and ribosomes. |
| 7. | **Function** | Permanent storage of hereditary genetic information. | Protein synthesis, gene expression, and regulatory roles. |
| 8. | **Action of Alkali** | Resistant to dilute alkaline hydrolysis. | Easily hydrolyzed by dilute alkali due to the reactive $2'\\text{-OH}$ group. |"""
                },
                {
                    "id": "bio-bot-q11",
                    "number": "11",
                    "question": "What do you mean by crossing over. And mention its significance.",
                    "answer": """**Definition:**
Crossing over is the reciprocal physical exchange of non-sister chromatid segments between homologous chromosomes that occurs during the pachytene stage of prophase-I of meiosis, resulting in genetic recombination. The point of contact where crossing over occurs is called a chiasma (plural: chiasmata).

### Significance of Crossing Over:
1. **Production of Genetic Variation:** By breaking existing linkage groups and producing new combinations of maternal and paternal alleles, crossing over provides new variations in progeny.
2. **Raw Material for Evolution:** Genetic variations produced by recombination are subject to natural selection, driving adaptation and organic evolution.
3. **Chromosome Mapping:** The frequency of crossing over between two gene loci is directly proportional to the physical distance between them on the chromosome. This principle is used to construct genetic linkage maps.
4. **Evidence for Linear Gene Order:** Crossing over provides direct genetic proof that genes are arranged in a linear sequence along the chromosome.
5. **Proper Chromosome Segregation:** Chiasmata formed by crossing over help maintain homologous chromosome alignment, ensuring proper segregation during anaphase-I."""
                }
            ]
        },
        {
            "name": "Part II: Zoology",
            "questions": [
                {
                    "id": "bio-zoo-q1",
                    "number": "1",
                    "question": "Describe the internal structure of human heart with diagram.",
                    "answer": """The human heart is a hollow, muscular, cone-shaped organ situated in the thoracic cavity between the lungs in the mediastinum. Internally, it is divided into four distinct chambers: two superior receiving chambers (atria) and two inferior pumping chambers (ventricles).

```
                            Superior Vena Cava
                                    │
                                    ▼
       ┌──────────────────── Interatrial Septum ────────────────────┐
       │                                                            │
  Right Atrium (Deox. blood)                                   Left Atrium (Ox. blood)
  - Receives blood from SVC,                                   - Receives blood from 4
    IVC, and Coronary Sinus                                      Pulmonary Veins
       │                                                            │
  Tricuspid Valve                                              Bicuspid (Mitral) Valve
       │                                                            │
       ▼                                                            ▼
  Right Ventricle                                              Left Ventricle
  - Pushes blood into                                          - Thickest myocardium; pushes
    Pulmonary Artery                                             blood into Systemic Aorta
  - Pulmonary Semilunar Valve                                  - Aortic Semilunar Valve
       │                                                            │
       └────────────────── Interventricular Septum ─────────────────┘
                           (Papillary Muscles & Chordae Tendineae)
```

**1. Atria (Auricles):**
- **Right Atrium:** Thin-walled chamber that receives deoxygenated blood from all parts of the body via the Superior Vena Cava, Inferior Vena Cava, and Coronary Sinus. Its inner wall features a depression called the fossa ovalis (remnant of the embryonic foramen ovale).
- **Left Atrium:** Receives oxygenated blood from the lungs via four pulmonary veins.
- The two atria are separated internally by a thin, muscular partition called the **interatrial septum**.

**2. Ventricles:**
- **Right Ventricle:** Pumping chamber that forces deoxygenated blood into the pulmonary artery through the pulmonary semilunar valve to the lungs.
- **Left Ventricle:** Has walls approximately three times thicker than the right ventricle because it must pump blood under high pressure throughout the systemic circulation via the aorta.
- The two ventricles are separated by a thick, obliquely oriented **interventricular septum**. The internal ventricular walls contain muscular ridges called *trabeculae carneae* and projection muscles called *papillary muscles*.

**3. Heart Valves:**
- **Atrioventricular (AV) Valves:**
  - *Tricuspid Valve:* Located between right atrium and right ventricle; composed of three fibrous cusps.
  - *Bicuspid (Mitral) Valve:* Located between left atrium and left ventricle; composed of two cusps.
  - Both AV valves are tethered to papillary muscles by strong collagenous cords called *chordae tendineae*, which prevent the valve flaps from inverting into the atria during ventricular contraction.
- **Semilunar Valves:**
  - *Pulmonary Semilunar Valve:* Located at the origin of the pulmonary trunk from the right ventricle.
  - *Aortic Semilunar Valve:* Located at the root of the aorta from the left ventricle. Both prevent backflow of blood into the ventricles during diastole."""
                },
                {
                    "id": "bio-zoo-q2",
                    "number": "2",
                    "question": "Describe the structure and function of cerebrum of human brain.",
                    "answer": """The cerebrum is the largest and most developed portion of the human brain, constituting about 80–85% of total brain mass. It occupies the anterior and middle cranial fossae.

### Structure of Cerebrum:
1. **Cerebral Hemispheres:** The cerebrum is longitudinally divided into two symmetrical halves—the right and left cerebral hemispheres—by a deep median vertical groove called the longitudinal cerebral fissure.
2. **Corpus Callosum:** The two hemispheres are connected internally at their base by a broad, curved tract of transverse nerve fibers called the corpus callosum.
3. **Cerebral Cortex and White Matter:**
   - The outer zone is the cerebral cortex (grey matter), measuring 2–4 mm in thickness, composed of unmyelinated neuronal cell bodies and dendrites.
   - The inner zone is the cerebral medulla (white matter), composed of myelinated nerve fibers.
4. **Gyri and Sulci:** The cerebral cortex is folded into ridges called gyri, separated by shallow grooves called sulci (or deeper fissures), which greatly expand the surface area available for neuronal processing.
5. **Lobes of Cerebrum:** Each hemisphere is divided by three prominent sulci (central sulcus, lateral sulcus, and parieto-occipital sulcus) into four lobes:
   - *Frontal Lobe:* Anterior region.
   - *Parietal Lobe:* Middle-superior region.
   - *Temporal Lobe:* Lateral-inferior region.
   - *Occipital Lobe:* Posterior region.

### Functions of Cerebrum:
1. **Sensory Processing:** Receives and interprets sensory inputs from all sense organs (vision in occipital lobe, hearing in temporal lobe, touch and temperature in parietal lobe, smell in olfactory area).
2. **Motor Control:** The pre-central motor cortex of the frontal lobe initiates and coordinates all voluntary muscular activities.
3. **Higher Cognitive Abilities:** Seat of intelligence, abstract thinking, memory, reasoning, judgment, learning, willpower, emotion, and personality.
4. **Speech and Language:** Contains Broca's motor speech area (speech production) and Wernicke's sensory area (comprehension of spoken and written language)."""
                },
                {
                    "id": "bio-zoo-q3",
                    "number": "3",
                    "question": "Describe the structure and function of cerebellum of human brain.",
                    "answer": """The cerebellum (meaning "little brain") is the second largest part of the human brain, located in the posterior cranial fossa inferior to the occipital lobes of the cerebrum and posterior to the pons and medulla oblongata.

### Structure of Cerebellum:
1. **External Organization:** The cerebellum consists of a central, narrow, worm-like band called the **vermis**, and two expanded lateral cerebellar hemispheres.
2. **Folia and Sulci:** The cerebellar surface is divided into numerous parallel transverse leaf-like folds called **folia**, separated by narrow fissures.
3. **Cortex and Medulla:**
   - The outer cortex consists of grey matter containing three layers of cells, including specialized large inhibitory neurons called **Purkinje cells**.
   - The inner medulla consists of white matter that branches in a tree-like pattern called the **arbor vitae** ("tree of life").
4. **Cerebellar Peduncles:** Three pairs of thick fiber bundles (superior, middle, and inferior cerebellar peduncles) connect the cerebellum to the midbrain, pons, and medulla oblongata respectively.

### Functions of Cerebellum:
1. **Coordination of Voluntary Movements:** Coordinates and synchronizes the timing and force of skeletal muscle contractions initiated by the cerebrum, ensuring smooth, precise motor actions.
2. **Maintenance of Posture and Balance:** Integrates sensory signals from the vestibular apparatus of the inner ear and proprioceptors in muscles and joints to maintain equilibrium and upright posture.
3. **Regulation of Muscle Tone:** Adjusts tone in opposing flexor and extensor muscle groups.
4. **Motor Learning:** Essential for learning and automating repetitive physical skills (such as typing, cycling, playing a musical instrument, and dancing)."""
                },
                {
                    "id": "bio-zoo-q4",
                    "number": "4",
                    "question": "Briefly discuss on: i) Diencephalon ii) Pons varoli and medulla oblongata",
                    "answer": """**i) Diencephalon:**
The diencephalon is the posterior part of the forebrain situated between the cerebrum and the midbrain, surrounding the slit-like third ventricle (cavity). It comprises three primary divisions:
1. **Thalamus:** Two large ovoid masses of grey matter that serve as the central relay station for all incoming sensory impulses (except olfaction) ascending to the cerebral cortex. It also processes pain, temperature, and crude touch sensations.
2. **Hypothalamus:** Located on the floor of the third ventricle below the thalamus. It is the principal control center for autonomic functions, visceral activities, and homeostatic regulation (body temperature, hunger, thirst, sleep-wake cycles, emotional responses). It controls the endocrine system by producing releasing/inhibitory hormones and neurohypophysial hormones (oxytocin and ADH).
3. **Epithalamus:** The dorsal roof of the diencephalon; includes the pineal gland, which secretes melatonin to regulate circadian rhythms.

**ii) Pons Varolii and Medulla Oblongata:**
- **Pons Varolii:**
  - A prominent bridge-like transverse bulge of white nerve fibers located superior to the medulla and anterior to the cerebellum.
  - Contains fiber tracts connecting the spinal cord with higher brain regions and linking the cerebral cortex with the opposite cerebellar hemisphere.
  - Houses the pneumotaxic and apneustic centers, which regulate the transition between inspiration and expiration to ensure a rhythmic breathing rate.
- **Medulla Oblongata:**
  - The lowest, conical portion of the brainstem that extends downwards from the lower border of the pons and continues into the spinal cord at the foramen magnum.
  - Contains vital autonomic reflex centers:
    - *Cardiac Center:* Regulates heart rate and force of myocardial contraction.
    - *Vasomotor Center:* Controls blood vessel diameter and blood pressure.
    - *Respiratory Rhythmicity Center:* Generates baseline rhythmic rate and depth of respiration.
    - *Non-vital Reflex Centers:* Coordinates swallowing, vomiting, coughing, sneezing, and salivation."""
                },
                {
                    "id": "bio-zoo-q5",
                    "number": "5",
                    "question": "What is AIDS? Mention the causative agent, mode of infection, incubation period, symptoms, diagnosis, treatment and prevention.",
                    "answer": """**Definition:**
AIDS (Acquired Immunodeficiency Syndrome) is a chronic, life-threatening viral disease characterized by progressive failure and severe suppression of the human cell-mediated immune system, leaving the body vulnerable to opportunistic infections and rare malignancies.

- **Causative Agent:**
  Human Immunodeficiency Virus (HIV), an enveloped, single-stranded spherical RNA retrovirus belonging to the family Retroviridae (genus *Lentivirus*). It contains the reverse transcriptase enzyme, enabling it to convert its viral RNA into double-stranded proviral DNA that integrates into the host cell genome. It preferentially infects helper T-lymphocytes ($\\text{CD4}^+$ cells), macrophages, and dendritic cells.

- **Modes of Infection (Transmission):**
  1. Unprotected sexual intercourse with an HIV-infected partner.
  2. Transfusion of contaminated blood or blood products.
  3. Sharing of unsterilized, infected needles, syringes, or surgical equipment (common among intravenous drug users).
  4. Vertical transmission from an infected mother to child transplacentally during pregnancy, during childbirth (parturition), or through breastfeeding.

- **Incubation Period:**
  Highly variable; typically ranges from a few months up to 5 to 10 years (or longer) before full-blown AIDS symptoms develop, although the infected person remains capable of transmitting the virus.

- **Symptoms:**
  - *Early (Acute) Stage:* Flu-like illness, fever, headache, sore throat, and generalized lymphadenopathy.
  - *Full-blown AIDS Stage:* Prolonged fever lasting more than a month, chronic diarrhea, unexplained weight loss (>10% of body weight, termed "slim disease"), persistent dry cough, nocturnal sweating.
  - *Opportunistic Infections:* Candidiasis of mouth and esophagus, *Pneumocystis jirovecii* pneumonia, tuberculosis, and malignancies such as Kaposi's sarcoma.

- **Diagnosis:**
  1. *Screening Test:* ELISA (Enzyme-Linked Immunosorbent Assay) for detecting HIV antibodies/antigens.
  2. *Confirmatory Test:* Western Blot test for detecting specific viral proteins.
  3. *Molecular Test:* RT-PCR (Reverse Transcriptase Polymerase Chain Reaction) to determine viral load and proviral DNA.

- **Treatment:**
  - There is currently no permanent cure or preventive vaccine for HIV.
  - Managed with **HAART** (Highly Active Antiretroviral Therapy) or ART, using combinations of:
    - Nucleoside/Nucleotide Reverse Transcriptase Inhibitors (NRTIs, e.g., Zidovudine, Tenofovir, Lamivudine),
    - Non-nucleoside Reverse Transcriptase Inhibitors (NNRTIs, e.g., Efavirenz),
    - Protease Inhibitors and Integrase Inhibitors.
  - ART suppresses viral replication, prolongs life, and restores $\\text{CD4}^+$ T-cell counts.

- **Prevention and Control:**
  1. Practicing safe sexual practices and using barrier methods (condoms).
  2. Ensuring that all donated blood and organ tissues are screened for HIV.
  3. Using disposable, single-use syringes and sterilized surgical needles.
  4. Preventing needle sharing among intravenous drug users.
  5. Administering prophylactic antiretroviral therapy to pregnant mothers with HIV to prevent mother-to-child transmission.
  6. Widespread public education and awareness regarding transmission modes."""
                }
            ]
        }
    ]
}

with open(os.path.join(out_dir, "biology.js"), "w", encoding="utf-8") as f:
    f.write("window.BIOLOGY_DATA = " + json.dumps(biology_data, indent=2, ensure_ascii=False) + ";\n")

print("Wrote biology.js successfully")
