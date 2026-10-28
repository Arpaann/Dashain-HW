window.PHYSICS_DATA = {
  "id": "physics",
  "title": "Physics",
  "icon": "atom",
  "description": "Mechanics (SHM, Spring-Mass), Wave Optics & Acoustics (Laplace Correction), Modern Physics (Photoelectric, Decay), and Electromagnetism (Biot-Savart, Ampere's Law).",
  "sections": [
    {
      "name": "Theory",
      "questions": [
        {
          "id": "phys-q1",
          "number": "1",
          "question": "Describe the Newtons formula for velocity of sound in air with Laplace’s correction.",
          "answer": "**1. Newton's Formula:**\nNewton assumed that sound travels in a gas under **isothermal conditions** (temperature remains constant).\n- Isothermal Bulk modulus: $E_\theta = P$ (atmospheric pressure)\n- Velocity of sound:\n$$v = \\sqrt{\frac{E_\theta}{\rho}} = \\sqrt{\frac{P}{\rho}}$$\nAt STP ($P = 1.013 \times 10^5\\text{ N/m}^2, \\rho = 1.293\\text{ kg/m}^3$):\n$$v = \\sqrt{\\frac{1.013 \\times 10^5}{1.293}} \\approx 280\\text{ m/s}$$\nThis value is about 15% lower than the experimental value ($332\\text{ m/s}$).\n\n**2. Laplace's Correction:**\nLaplace pointed out that:\n- Compressions and rarefactions occur very rapidly.\n- Air is a bad conductor of heat.\nHence, the process is **adiabatic** (no heat exchange).\n- Adiabatic Bulk modulus: $E_s = \\gamma P$ (where $\\gamma = C_p/C_v$)\n- Corrected velocity formula:\n$$v = \\sqrt{\\frac{E_s}{\\rho}} = \\sqrt{\\frac{\\gamma P}{\\rho}}$$\nFor air, $\\gamma = 1.4$. At STP:\n$$v = \\sqrt{\\frac{1.4 \\times 1.013 \\times 10^5}{1.293}} \\approx 332\\text{ m/s}$$\nThis closely matches the experimental value, proving Laplace's correction valid."
        },
        {
          "id": "phys-q2",
          "number": "2",
          "question": "How did Einstein explain photoelectric equation?",
          "answer": "Einstein explained the photoelectric effect using Planck's quantum theory:\n1. Light consists of packets of energy called **photons**, each with energy $E = h\\nu$.\n2. When a photon strikes an electron on a metal surface, its energy is used in two ways:\n   - Part of energy is used as **work function** ($\\phi_0 = h\\nu_0$) to liberate the electron.\n   - The remaining energy is given to the emitted electron as **maximum kinetic energy** ($K_{\\max} = \\frac{1}{2}mv_{\\max}^2$).\n\nBy conservation of energy:\n$$E = \\phi_0 + K_{\\max}$$\n$$h\\nu = h\\nu_0 + \\frac{1}{2}m v_{\\max}^2$$\n$$K_{\\max} = \\frac{1}{2}m v_{\\max}^2 = h(\\nu - \\nu_0)$$\nwhere $h$ is Planck's constant, $\\nu$ is incident frequency, and $\\nu_0$ is threshold frequency.\n\n**Key conclusions:**\n- If $\\nu < \\nu_0$, no photoelectrons are emitted (threshold frequency).\n- Kinetic energy depends linearly on frequency $\\nu$, not on intensity.\n- Intensity only determines the number of emitted electrons per second."
        },
        {
          "id": "phys-q3",
          "number": "3",
          "question": "Derive decay equation",
          "answer": "**Radioactive Decay Law:**\nThe rate of disintegration of radioactive nuclei at any instant is directly proportional to the number of active nuclei ($N$) present at that instant.\n$$-\\frac{dN}{dt} \\propto N \\implies \\frac{dN}{dt} = -\\lambda N$$\nwhere $\\lambda$ is the decay constant, and the negative sign indicates decrease in $N$.\n\n$$\\frac{dN}{N} = -\\lambda dt$$\n\nIntegrating both sides:\n$$\\int \\frac{dN}{N} = -\\lambda \\int dt$$\n$$\\ln N = -\\lambda t + C \\quad \\text{--- (1)}$$\n\nAt $t = 0$, $N = N_0$ (initial number of nuclei):\n$$\\ln N_0 = C$$\n\nSubstituting $C$ into (1):\n$$\\ln N = -\\lambda t + \\ln N_0$$\n$$\\ln\\left(\\frac{N}{N_0}\\right) = -\\lambda t$$\n$$\\frac{N}{N_0} = e^{-\\lambda t}$$\n$$N = N_0 e^{-\\lambda t}$$\nThis is the radioactive decay equation."
        },
        {
          "id": "phys-q4",
          "number": "4",
          "question": "Describe the motion of electron and show that the path followed by it is parabolic.",
          "answer": "Consider an electron (mass $m$, charge $-e$) projected horizontally with velocity $v_x$ into a uniform electric field $E$ directed along the y-axis between two parallel plates.\n\n**1. Horizontal motion (no horizontal force):**\n$$a_x = 0$$\n$$x = v_x \\cdot t \\implies t = \\frac{x}{v_x}$$\n\n**2. Vertical motion (electric force acts along vertical):**\nElectric force: $F_y = eE$\nVertical acceleration: $a_y = \\frac{eE}{m}$\nUsing $y = u_y t + \\frac{1}{2}a_y t^2$ with initial $u_y = 0$:\n$$y = \\frac{1}{2} \\left(\\frac{eE}{m}\\right) t^2$$\n\nSubstituting $t = \\frac{x}{v_x}$:\n$$y = \\left(\\frac{eE}{2m v_x^2}\\right) x^2$$\n$$y = k x^2 \\quad \\text{where } k = \\frac{eE}{2m v_x^2} = \\text{constant}$$\n\nThis equation is of the form $y = kx^2$, which represents a **parabola**. Hence, the path of an electron in a uniform transverse electric field is parabolic."
        },
        {
          "id": "phys-q5",
          "number": "5",
          "question": "Define simple harmonic motion.",
          "answer": "**Simple Harmonic Motion (SHM):**\nSHM is a special type of periodic oscillatory motion in which:\n1. The acceleration of the particle is directly proportional to its displacement from the mean (equilibrium) position.\n2. The acceleration is always directed towards the mean position.\n\n**Mathematical Condition:**\n$$a \\propto -x \\implies a = -\\omega^2 x$$\nor\n$$F = -kx$$\nwhere $a$ is acceleration, $x$ is displacement, $\\omega$ is angular frequency, and $k$ is the spring/force constant."
        },
        {
          "id": "phys-q6",
          "number": "6",
          "question": "Derive the total energy in Simple harmonic motion",
          "answer": "For a particle of mass $m$ executing SHM with amplitude $A$ and angular frequency $\\omega$:\n- Displacement: $x$\n- Velocity: $v = \\omega\\sqrt{A^2 - x^2}$\n\n**1. Kinetic Energy ($E_k$):**\n$$E_k = \\frac{1}{2}mv^2 = \\frac{1}{2}m\\omega^2(A^2 - x^2)$$\n\n**2. Potential Energy ($E_p$):**\nWork done against restoring force $F = kx = m\\omega^2 x$:\n$$E_p = \\int_0^x kx \\, dx = \\frac{1}{2}kx^2 = \\frac{1}{2}m\\omega^2 x^2$$\n\n**3. Total Energy ($E$):**\n$$E = E_k + E_p = \\frac{1}{2}m\\omega^2(A^2 - x^2) + \\frac{1}{2}m\\omega^2 x^2$$\n$$E = \\frac{1}{2}m\\omega^2 A^2 = \\frac{1}{2}kA^2 = \\text{constant}$$\n\n**Conclusion:** Total energy is independent of displacement $x$ and remains constant at all points during the motion."
        },
        {
          "id": "phys-q7",
          "number": "7",
          "question": "Derive an expression for the time of oscillation for a mass m attached to a vertical spring of force  constant k.",
          "answer": "**1. Equilibrium Position:**\nWhen mass $m$ is suspended, it produces extension $e$:\n$$mg = ke \\implies \\frac{m}{k} = \\frac{e}{g}$$\n\n**2. Displaced Position:**\nWhen pulled down by an additional displacement $y$ and released:\n- Total extension $= e + y$\n- Restoring force: $F = -k(e + y) + mg = -ke - ky + mg$\nSince $mg = ke$:\n$$F = -ky$$\n$$m a = -ky \\implies a = -\\left(\\frac{k}{m}\\right)y$$\n\nComparing with standard SHM equation $a = -\\omega^2 y$:\n$$\\omega = \\sqrt{\\frac{k}{m}}$$\n\n**3. Time Period ($T$):**\n$$T = \\frac{2\\pi}{\\omega} = 2\\pi\\sqrt{\\frac{m}{k}}$$\nAlso, since $\\frac{m}{k} = \\frac{e}{g}$:\n$$T = 2\\pi\\sqrt{\\frac{e}{g}}$$"
        },
        {
          "id": "phys-q8",
          "number": "8",
          "question": "State and explain Biot-Savart law",
          "answer": "**Biot-Savart Law:**\nThe magnetic field $dB$ at a point due to a current-carrying element $I\\,dl$ is:\n1. Directly proportional to current: $dB \\propto I$\n2. Directly proportional to length element: $dB \\propto dl$\n3. Directly proportional to $\\sin\\theta$ (where $\\theta$ is the angle between $d\\vec{l}$ and position vector $\\vec{r}$): $dB \\propto \\sin\\theta$\n4. Inversely proportional to square of distance: $dB \\propto \\frac{1}{r^2}$\n\nCombining these:\n$$dB = \\frac{\\mu_0}{4\\pi} \\frac{I \\, dl \\sin\\theta}{r^2}$$\nwhere $\\frac{\\mu_0}{4\\pi} = 10^{-7}\\text{ T}\\cdot\\text{m/A}$, and $\\mu_0$ is the permeability of free space.\n\nIn vector form:\n$$d\\vec{B} = \\frac{\\mu_0}{4\\pi} \\frac{I(d\\vec{l} \\times \\hat{r})}{r^2}$$"
        },
        {
          "id": "phys-q9",
          "number": "9",
          "question": "Obtain an expression for magnetic field strength at the axis of current carrying circular coil using Biot-Savart’s law.",
          "answer": "Consider a circular coil of radius $a$ carrying current $I$. We find the magnetic field at a point $P$ on its axis at distance $x$ from the center.\n- Distance from current element $dl$ to point $P$: $r = \\sqrt{a^2 + x^2}$\n- Angle between $d\\vec{l}$ and $\\vec{r}$ is $90^\\circ$ ($\\sin 90^\\circ = 1$).\n\nBy Biot-Savart law:\n$$dB = \\frac{\\mu_0}{4\\pi} \\frac{I \\, dl}{r^2}$$\n\nResolving $dB$:\n- Components perpendicular to axis ($dB\\cos\\phi$) cancel out due to symmetry.\n- Components along the axis ($dB\\sin\\phi$) add up.\n\nTotal magnetic field along the axis:\n$$B = \\int dB \\sin\\phi = \\int \\frac{\\mu_0}{4\\pi} \\frac{I \\, dl}{r^2} \\left(\\frac{a}{r}\\right) = \\frac{\\mu_0 I a}{4\\pi r^3} \\int dl$$\nSince $\\int dl = 2\\pi a$:\n$$B = \\frac{\\mu_0 I a (2\\pi a)}{4\\pi r^3} = \\frac{\\mu_0 I a^2}{2(a^2 + x^2)^{3/2}}$$\n\nFor a coil with $N$ turns:\n$$B = \\frac{\\mu_0 N I a^2}{2(a^2 + x^2)^{3/2}}$$"
        },
        {
          "id": "phys-q10",
          "number": "10",
          "question": "State and explain Amper’s law",
          "answer": "**Ampere's Circuital Law:**\nThe line integral of magnetic field $\\vec{B}$ around any closed closed loop (called an Amperian loop) in free space is equal to $\\mu_0$ times the net current ($I_{\\text{enc}}$) enclosed by the loop.\n\n$$\\oint \\vec{B} \\cdot d\\vec{l} = \\mu_0 I_{\\text{enc}}$$\n\nwhere:\n- $\\oint$ is line integral around closed path.\n- $\\vec{B}$ is magnetic field vector.\n- $d\\vec{l}$ is length element of the path.\n- $\\mu_0$ is permeability of free space ($4\\pi \\times 10^{-7}\\text{ T}\\cdot\\text{m/A}$).\n- $I_{\\text{enc}}$ is net steady current passing through the surface enclosed by the loop."
        },
        {
          "id": "phys-q11",
          "number": "11",
          "question": "Derive an expression for the magnetic field strength inside a long current carrying solenoid using Ampere’s circuital law.",
          "answer": "Consider a long solenoid having $n$ turns per unit length carrying current $I$.\nTake a rectangular Amperian loop $abcd$ where:\n- Side $ab = L$ lies inside the solenoid parallel to axis.\n- Sides $bc$ and $da$ are perpendicular to axis (field component is zero).\n- Side $cd$ lies outside the solenoid (field $B \\approx 0$).\n\nEvaluating line integral:\n$$\\oint \\vec{B} \\cdot d\\vec{l} = \\int_a^b \\vec{B}\\cdot d\\vec{l} + \\int_b^c \\vec{B}\\cdot d\\vec{l} + \\int_c^d \\vec{B}\\cdot d\\vec{l} + \\int_d^a \\vec{B}\\cdot d\\vec{l}$$\n$$\\oint \\vec{B} \\cdot d\\vec{l} = B \\cdot L + 0 + 0 + 0 = B L$$\n\nTotal current enclosed by loop:\n$$I_{\\text{enc}} = (n L) I$$\n\nBy Ampere's circuital law:\n$$\\oint \\vec{B} \\cdot d\\vec{l} = \\mu_0 I_{\\text{enc}}$$\n$$B L = \\mu_0 (n L I)$$\n$$B = \\mu_0 n I$$"
        },
        {
          "id": "phys-q12",
          "number": "12",
          "question": "Show that Cp - Cv= R, where symbols carry their usual meaning.",
          "answer": "**Mayer's Relation:**\nConsider 1 mole of an ideal gas at temperature $T$, pressure $P$, and volume $V$.\n\n1. **At constant volume ($V$ constant):**\n   No work is done ($dW = P dV = 0$).\n   Heat supplied: $dQ = C_v dT$\n   By First Law: $dU = dQ - dW = C_v dT$\n\n2. **At constant pressure ($P$ constant):**\n   Heat supplied: $dQ = C_p dT$\n   Work done: $dW = P dV$\n   By First Law: $dQ = dU + dW$\n   $$C_p dT = dU + P dV$$\n\nSubstituting $dU = C_v dT$:\n$$C_p dT = C_v dT + P dV$$\n$$(C_p - C_v) dT = P dV \\quad \\text{--- (1)}$$\n\nFor 1 mole of ideal gas:\n$$PV = RT$$\nDifferentiating at constant pressure:\n$$P dV = R dT \\quad \\text{--- (2)}$$\n\nSubstituting (2) into (1):\n$$(C_p - C_v) dT = R dT$$\n$$C_p - C_v = R$$"
        },
        {
          "id": "phys-q13",
          "number": "13",
          "question": "Derive an expression for work done during isothermal process.",
          "answer": "In an **isothermal process**, temperature $T$ remains constant.\nFor $n$ moles of an ideal gas:\n$$PV = nRT \\implies P = \\frac{nRT}{V}$$\n\nWork done when gas expands from volume $V_1$ to $V_2$:\n$$W = \\int_{V_1}^{V_2} P \\, dV = \\int_{V_1}^{V_2} \\frac{nRT}{V} \\, dV$$\n$$W = nRT [\\ln V]_{V_1}^{V_2} = nRT \\ln\\left(\\frac{V_2}{V_1}\\right)$$\nIn terms of base 10:\n$$W = 2.303 \\, nRT \\log_{10}\\left(\\frac{V_2}{V_1}\\right)$$\nSince $P_1 V_1 = P_2 V_2 \\implies \\frac{V_2}{V_1} = \\frac{P_1}{P_2}$:\n$$W = 2.303 \\, nRT \\log_{10}\\left(\\frac{P_1}{P_2}\\right)$$"
        },
        {
          "id": "phys-q14",
          "number": "14",
          "question": "Derive an expression for work done during adiabatic process.",
          "answer": "In an **adiabatic process**, no heat enters or leaves the system ($dQ = 0$).\nEquation of state: $PV^\\gamma = K$ (constant) $\\implies P = K V^{-\\gamma}$\n\nWork done as gas expands from $V_1$ to $V_2$:\n$$W = \\int_{V_1}^{V_2} P \\, dV = K \\int_{V_1}^{V_2} V^{-\\gamma} \\, dV$$\n$$W = K \\left[ \\frac{V^{1-\\gamma}}{1-\\gamma} \\right]_{V_1}^{V_2} = \\frac{1}{1-\\gamma} (K V_2^{1-\\gamma} - K V_1^{1-\\gamma})$$\nSince $K = P_1 V_1^\\gamma = P_2 V_2^\\gamma$:\n$$W = \\frac{P_2 V_2 - P_1 V_1}{1 - \\gamma} = \\frac{P_1 V_1 - P_2 V_2}{\\gamma - 1}$$\nUsing $PV = nRT$:\n$$W = \\frac{nR(T_1 - T_2)}{\\gamma - 1}$$"
        }
      ]
    },
    {
      "name": "Numerical",
      "questions": [
        {
          "id": "phys-num1",
          "number": "1",
          "question": "A circular coil of 100 turns has a radius of 10 cm and carries a current of 5A. Determine the magnetic field at a point on the axis of the coil at a distance of 5cm from the center of the coil.",
          "answer": "**Given:**\n- Number of turns, $N = 100$\n- Radius of coil, $a = 10\\text{ cm} = 0.1\\text{ m}$\n- Current, $I = 5\\text{ A}$\n- Axial distance, $x = 5\\text{ cm} = 0.05\\text{ m}$\n\n**Formula:**\n$$B = \\frac{\\mu_0 N I a^2}{2(a^2 + x^2)^{3/2}}$$\n\n**Calculation:**\n$$a^2 + x^2 = (0.1)^2 + (0.05)^2 = 0.01 + 0.0025 = 0.0125\\text{ m}^2$$\n$$(a^2 + x^2)^{3/2} = (0.0125)^{1.5} \\approx 1.3975 \\times 10^{-3}\\text{ m}^3$$\n\n$$B = \\frac{(4\\pi \\times 10^{-7}) \\times 100 \\times 5 \\times (0.1)^2}{2 \\times 1.3975 \\times 10^{-3}}$$\n$$B = \\frac{6.283 \\times 10^{-6}}{2.795 \\times 10^{-3}} \\approx 2.25 \\times 10^{-3}\\text{ T}$$\n\n**Answer:** The magnetic field is **$2.25 \\times 10^{-3}\\text{ T}$** (or $2.25\\text{ mT}$)."
        },
        {
          "id": "phys-num2",
          "number": "2",
          "question": "At what temperature, the velocity of sound in air is increased by 60% to that at 27℃?",
          "answer": "**Given:**\n- Initial temperature, $T_1 = 27^\\circ\\text{C} = 27 + 273 = 300\\text{ K}$\n- Initial velocity $= v_1$\n- Final velocity, $v_2 = v_1 + 60\\% \\text{ of } v_1 = 1.6 \\, v_1$\n\n**Formula:**\n$$v \\propto \\sqrt{T} \\implies \\frac{v_2}{v_1} = \\sqrt{\\frac{T_2}{T_1}}$$\n\n**Calculation:**\n$$\\frac{1.6 \\, v_1}{v_1} = \\sqrt{\\frac{T_2}{300}}$$\n$$1.6 = \\sqrt{\\frac{T_2}{300}}$$\n$$1.6^2 = \\frac{T_2}{300}$$\n$$2.56 = \\frac{T_2}{300} \\implies T_2 = 2.56 \\times 300 = 768\\text{ K}$$\n\nIn Celsius:\n$$t_2 = 768 - 273 = 495^\\circ\\text{C}$$\n\n**Answer:** The required temperature is **$495^\\circ\\text{C}$** (or $768\\text{ K}$)."
        },
        {
          "id": "phys-num3",
          "number": "3",
          "question": "A bob of mass 8 kg performs SHM of amplitude 30cm. The restoring force is 60N. Calculate: - i) Time period ii) The maximum acceleration.",
          "answer": "**Given:**\n- Mass of bob, $m = 8\\text{ kg}$\n- Amplitude, $A = 30\\text{ cm} = 0.3\\text{ m}$\n- Restoring force at extreme position ($x = A$), $F = 60\\text{ N}$\n\n**Calculation:**\n**i) Time Period ($T$):**\n$$F = k A \\implies k = \\frac{F}{A} = \\frac{60}{0.3} = 200\\text{ N/m}$$\nAngular frequency:\n$$\\omega = \\sqrt{\\frac{k}{m}} = \\sqrt{\\frac{200}{8}} = \\sqrt{25} = 5\\text{ rad/s}$$\n$$T = \\frac{2\\pi}{\\omega} = \\frac{2 \\times 3.1416}{5} \\approx 1.26\\text{ s}$$\n\n**ii) Maximum Acceleration ($a_{\\max}$):**\n$$a_{\\max} = \\omega^2 A = (5)^2 \\times 0.3 = 25 \\times 0.3 = 7.5\\text{ m/s}^2$$\n\n**Answer:**\ni) Time period = **$1.26\\text{ s}$**  \nii) Maximum acceleration = **$7.5\\text{ m/s}^2$**"
        },
        {
          "id": "phys-num4",
          "number": "4",
          "question": "Determine the electric field supplied when the electric force applied between the two horizontal plates just balances an oil drop with 4 electrons attached to it having mass 1.31 x 10-14 kg.",
          "answer": "**Given:**\n- Mass of oil drop, $m = 1.31 \\times 10^{-14}\\text{ kg}$\n- Number of excess electrons, $n = 4$\n- Charge of electron, $e = 1.6 \\times 10^{-19}\\text{ C}$\n- Total charge, $q = n e = 4 \\times 1.6 \\times 10^{-19} = 6.4 \\times 10^{-19}\\text{ C}$\n- Acceleration due to gravity, $g = 9.8\\text{ m/s}^2$\n\n**Formula:**\nAt equilibrium:\n$$\\text{Electric force } F_e = \\text{Weight } W$$\n$$q E = m g$$\n$$E = \\frac{m g}{q}$$\n\n**Calculation:**\n$$E = \\frac{1.31 \\times 10^{-14} \\times 9.8}{6.4 \\times 10^{-19}}$$\n$$E = \\frac{1.2838 \\times 10^{-13}}{6.4 \\times 10^{-19}} \\approx 2.01 \\times 10^5\\text{ V/m}$$\n\n**Answer:** The electric field is **$2.01 \\times 10^5\\text{ V/m}$** (or $\\text{N/C}$) directed vertically upwards."
        }
      ]
    }
  ]
};
