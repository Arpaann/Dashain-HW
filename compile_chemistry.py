import json
import os
import sys

sys.path.append(r"C:\Users\Arpan\.gemini\antigravity\scratch\studyroom")

from chem_haloalkanes import get_haloalkanes
from chem_haloarenes import get_haloarenes
from chem_metals import get_copper, get_zinc
from chem_iron_mercury_silver import get_mercury, get_iron, get_silver
from chem_ionic import get_ionic_equilibrium

out_dir = r"C:\Users\Arpan\.gemini\antigravity\scratch\studyroom\data"

chemistry_data = {
    "id": "chemistry",
    "title": "Chemistry",
    "icon": "flask-conical",
    "description": "Haloalkanes, Haloarenes, Transition Metals (Copper, Zinc, Mercury, Iron, Silver), and Ionic Equilibrium.",
    "sections": [
        get_haloalkanes(),
        get_haloarenes(),
        get_copper(),
        get_zinc(),
        get_mercury(),
        get_iron(),
        get_silver(),
        get_ionic_equilibrium()
    ]
}

target_file = os.path.join(out_dir, "chemistry.js")
with open(target_file, "w", encoding="utf-8") as f:
    f.write("window.CHEMISTRY_DATA = " + json.dumps(chemistry_data, indent=2, ensure_ascii=False) + ";\n")

total_q = sum(len(sec["questions"]) for sec in chemistry_data["sections"])
print(f"Wrote chemistry.js successfully with {total_q} questions across {len(chemistry_data['sections'])} sections!")
