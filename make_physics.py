import json
import os

out_dir = r"C:\Users\Arpan\.gemini\antigravity\scratch\studyroom\data"
os.makedirs(out_dir, exist_ok=True)

physics_data = {
    "id": "physics",
    "title": "Physics",
    "icon": "zap",
    "description": "Wave optics, thermodynamics, electromagnetism, modern physics, and numerical problems.",
    "sections": [
        {
            "name": "Theory",
            "questions": [
                {
                    "id": "phy-q1",
                    "number": "1",
                    "question": "Describe the Newtons formula for velocity of sound in air with Laplace’s correction.",
                    "answer": """Sound travels through a gaseous medium in the form of longitudinal waves consisting of alternate compressions and rarefactions.

### Newton's Formula
Sir Isaac Newton assumed that when sound propagates through air or any gas, the temperature of the medium remains constant. He argued that the heat produced during compression is immediately dissipated to the surroundings, and the cooling produced during rarefaction is immediately compensated by heat from the surroundings because the process is very slow. Hence, sound propagation is an isothermal process.

For an isothermal process, the pressure-volume relation of an ideal gas is given by Boyle's law:
$$PV = \\text{constant}$$

Differentiating both sides with respect to volume $V$:
$$P\\frac{dV}{dV} + V\\frac{dP}{dV} = 0 \\implies P + V\\frac{dP}{dV} = 0$$
$$P = -V\\frac{dP}{dV} = \\frac{dP}{-\\frac{dV}{V}} = B_{\\text{iso}}$$
where $B_{\\text{iso}}$ is the isothermal bulk modulus of elasticity of the gas, which equals the pressure $P$.

The general equation for the velocity of a longitudinal wave in a fluid medium is:
$$v = \\sqrt{\\frac{B}{\\rho}}$$
where $\\rho$ is the density of the gas. Substituting $B = P$:
$$v = \\sqrt{\\frac{P}{\\rho}}$$

At normal temperature and pressure (NTP):
- Atmospheric pressure, $P = 1.013 \\times 10^5 \\text{ N/m}^2$
- Density of air, $\\rho = 1.293 \\text{ kg/m}^3$

$$v = \\sqrt{\\frac{1.013 \\times 10^5}{1.293}} \\approx 280 \\text{ m/s}$$

The experimental value of the velocity of sound in air at NTP is approximately $332 \\text{ m/s}$. The theoretical value calculated by Newton's formula is about $15.6\\%$ lower than the experimental value, showing that Newton's assumption was defective.

### Laplace's Correction
In 1816, the French mathematician and physicist Pierre-Simon Laplace pointed out two key facts:
1. Air is a very poor conductor of heat.
2. The compressions and rarefactions take place so rapidly that there is no time for heat to flow out during compression or flow in during rarefaction.

Therefore, the propagation of sound waves in air is an adiabatic process, not an isothermal process.

For an adiabatic process, the gas equation is:
$$P V^\\gamma = \\text{constant}$$
where $\\gamma = \\frac{C_p}{C_v}$ is the ratio of specific heat capacities of the gas.

Differentiating both sides:
$$\\gamma P V^{\\gamma-1} dV + V^\\gamma dP = 0$$
Dividing throughout by $V^{\\gamma-1}$:
$$\\gamma P dV + V dP = 0 \\implies \\gamma P = -V \\frac{dP}{dV} = \\frac{dP}{-\\frac{dV}{V}} = B_{\\text{adi}}$$
where $B_{\\text{adi}}$ is the adiabatic bulk modulus of elasticity. Thus, $B_{\\text{adi}} = \\gamma P$.

Substituting $B_{\\text{adi}}$ into the wave velocity formula gives Laplace's formula:
$$v = \\sqrt{\\frac{\\gamma P}{\\rho}}$$

For air (which is primarily composed of diatomic gases $\\text{N}_2$ and $\\text{O}_2$), $\\gamma \\approx 1.4$.
At NTP:
$$v = \\sqrt{\\frac{1.4 \\times 1.013 \\times 10^5}{1.293}} = \\sqrt{109675.17} \\approx 331.2 \\text{ m/s}$$

This calculated value matches the experimentally measured velocity of sound in air ($332 \\text{ m/s}$) with remarkable accuracy, confirming the validity of Laplace's correction."""
                },
                {
                    "id": "phy-q2",
                    "number": "2",
                    "question": "How did Einstein explain photoelectric equation?",
                    "answer": """In 1905, Albert Einstein explained the phenomenon of the photoelectric effect by extending Max Planck's quantum theory of radiation.

According to Einstein:
1. Light does not propagate as a continuous wave, but as localized packets or quanta of energy called photons.
2. The energy of each photon is proportional to the frequency $\\nu$ of the radiation:
$$E = h\\nu$$
where $h$ is Planck's constant ($6.626 \\times 10^{-34} \\text{ J}\\cdot\\text{s}$).
3. When a photon of frequency $\\nu$ strikes a metal surface, it collides with a single bound conduction electron and transfers its entire energy $h\\nu$ instantaneously to that electron.
4. This absorbed energy is utilized in two parts:
   - A minimum part of the energy is used to liberate the electron from the attractive forces of the metal lattice. This minimum energy is called the work function of the metal, denoted by $\\phi_0$ (where $\\phi_0 = h\\nu_0$, and $\\nu_0$ is the threshold frequency).
   - The remaining part of the photon energy is converted into the maximum kinetic energy ($K_{\\max}$) of the emitted photoelectron.

By the law of conservation of energy:
$$E = \\phi_0 + K_{\\max}$$
$$h\\nu = h\\nu_0 + \\frac{1}{2}m v_{\\max}^2$$
$$\\frac{1}{2}m v_{\\max}^2 = h(\\nu - \\nu_0)$$
where $m$ is the mass of the electron and $v_{\\max}$ is the maximum velocity of the emitted photoelectron. This relation is known as Einstein's photoelectric equation.

### Explanation of the Laws of Photoelectric Emission:
1. **Existence of Threshold Frequency:** If the incident frequency $\\nu < \\nu_0$, the photon energy $h\\nu$ is less than the work function $\\phi_0$. The maximum kinetic energy would be negative, which is physically impossible. Hence, no photoelectrons can be emitted below $\\nu_0$, regardless of the intensity of the light.
2. **Effect of Frequency on Kinetic Energy:** Since $K_{\\max} = h\\nu - \\phi_0$, the maximum kinetic energy of the emitted photoelectrons increases linearly with the frequency of incident radiation and is independent of its intensity.
3. **Effect of Intensity on Photoelectric Current:** The intensity of radiation is proportional to the number of photons striking unit area per second. Since one photon interacts with one electron, a higher intensity results in a larger number of photoelectrons emitted per second, directly increasing the photoelectric current.
4. **Instantaneous Emission:** The collision between a photon and an electron is elastic and instantaneous (time lag $< 10^{-9} \\text{ s}$), explaining why electron emission begins immediately upon illumination."""
                },
                {
                    "id": "phy-q3",
                    "number": "3",
                    "question": "Derive decay equation",
                    "answer": """Radioactive decay is a spontaneous nuclear process in which an unstable nucleus disintegrates into a more stable nucleus by emitting ionizing radiation.

### Rutherford-Soddy Law of Radioactive Decay
The rate of disintegration of radioactive nuclei at any instant of time is directly proportional to the total number of undecayed radioactive nuclei present in the sample at that instant.

Let $N_0$ be the initial number of radioactive nuclei present at time $t = 0$.
Let $N$ be the number of undecayed radioactive nuclei remaining at any subsequent time $t$.
Let $dN$ be the number of nuclei that decay in a very small time interval $dt$.

According to the law of radioactive decay:
$$-\\frac{dN}{dt} \\propto N$$
$$-\\frac{dN}{dt} = \\lambda N$$
where the negative sign indicates that the number of undecayed nuclei decreases as time increases, and $\\lambda$ is a characteristic positive constant for the given radioactive substance, known as the decay constant or disintegration constant.

Rearranging the variables:
$$\\frac{dN}{N} = -\\lambda \\, dt$$

Integrating both sides:
$$\\int \\frac{dN}{N} = -\\lambda \\int dt$$
$$\\ln N = -\\lambda t + C \\quad \\text{--- (i)}$$
where $C$ is the integration constant.

To determine $C$, apply the initial boundary condition:
At $t = 0$, $N = N_0$.
$$\\ln N_0 = -\\lambda(0) + C \\implies C = \\ln N_0$$

Substituting the value of $C$ into equation (i):
$$\\ln N = -\\lambda t + \\ln N_0$$
$$\\ln N - \\ln N_0 = -\\lambda t$$
$$\\ln\\left(\\frac{N}{N_0}\\right) = -\\lambda t$$
Taking the exponential on both sides:
$$\\frac{N}{N_0} = e^{-\\lambda t}$$
$$N = N_0 e^{-\\lambda t}$$

This is the radioactive decay equation. It shows that the number of radioactive parent nuclei decreases exponentially with time."""
                },
                {
                    "id": "phy-q4",
                    "number": "4",
                    "question": "Describe the motion of electron and show that the path followed by it is parabolic.",
                    "answer": """Consider an electron of mass $m$ and charge $-e$ entering perpendicularly into a uniform electric field $\\vec{E}$ set up between two parallel plates with an initial horizontal velocity $v_x$ along the positive x-axis.

Let the uniform electric field $\\vec{E}$ be directed vertically downwards along the negative y-axis between the plates of length $L$. Because the charge of the electron is negative, it experiences an upward electrostatic force along the positive y-axis.

```
       (+) Upper Plate -----------------------
                         ↑ F_e = eE
               e-  --->  • . . . . . . . (Parabolic Trajectory)
       (-) Lower Plate -----------------------
                         |<--------- L --------->|
```

**1. Motion along the horizontal direction (X-axis):**
Since there is no electric field or force acting horizontally:
$$F_x = 0 \\implies a_x = 0$$
The horizontal velocity remains constant throughout the motion:
$$v_x = \\text{constant}$$
The horizontal distance $x$ traversed in time $t$ is:
$$x = v_x t \\implies t = \\frac{x}{v_x} \\quad \\text{--- (i)}$$

**2. Motion along the vertical direction (Y-axis):**
The electric force acting on the electron directed vertically upwards is:
$$F_y = eE$$
By Newton's second law, the vertical acceleration $a_y$ is:
$$a_y = \\frac{F_y}{m} = \\frac{eE}{m}$$

Since the electron enters purely horizontally, its initial vertical velocity is:
$$u_y = 0$$

Using the equation of motion for vertical displacement $y$:
$$y = u_y t + \\frac{1}{2} a_y t^2$$
$$y = 0 + \\frac{1}{2} \\left(\\frac{eE}{m}\\right) t^2$$

Substituting the value of $t$ from equation (i):
$$y = \\frac{1}{2} \\left(\\frac{eE}{m}\\right) \\left(\\frac{x}{v_x}\\right)^2$$
$$y = \\left(\\frac{eE}{2m v_x^2}\\right) x^2$$

For a given setup, $e, E, m,$ and $v_x$ are constant. Setting $k = \\frac{eE}{2m v_x^2}$:
$$y = k x^2$$

This equation represents the standard equation of a parabola ($y \\propto x^2$). Hence, the path followed by an electron moving in a uniform transverse electric field is parabolic."""
                },
                {
                    "id": "phy-q5",
                    "number": "5",
                    "question": "Define simple harmonic motion.",
                    "answer": """Simple Harmonic Motion (SHM) is defined as a special type of periodic oscillatory motion of a particle about a fixed mean (equilibrium) position in which:
1. The acceleration of the particle is directly proportional to its displacement from the mean position.
2. The acceleration is always directed towards the mean equilibrium position (opposite to the displacement).

Mathematically, it is expressed as:
$$a \\propto -x$$
$$a = -\\omega^2 x$$
or in differential form:
$$\\frac{d^2 x}{dt^2} + \\omega^2 x = 0$$
where $x$ is the linear displacement, $a$ is the acceleration, and $\\omega$ is the angular frequency of oscillation."""
                },
                {
                    "id": "phy-q6",
                    "number": "6",
                    "question": "Derive the total energy in Simple harmonic motion",
                    "answer": """Consider a particle of mass $m$ executing simple harmonic motion about a mean position $O$ with amplitude $A$ and angular frequency $\\omega$.

The displacement of the particle at any time $t$ is given by:
$$x = A \\sin(\\omega t)$$

The instantaneous velocity $v$ of the particle is:
$$v = \\frac{dx}{dt} = \\frac{d}{dt}[A \\sin(\\omega t)] = A\\omega \\cos(\\omega t) = \\omega \\sqrt{A^2 - x^2}$$

**1. Kinetic Energy ($K$):**
The instantaneous kinetic energy of the vibrating particle at displacement $x$ is:
$$K = \\frac{1}{2}m v^2 = \\frac{1}{2}m \\omega^2 (A^2 - x^2)$$

**2. Potential Energy ($U$):**
When the particle is displaced by a distance $x$ from the mean position, the restoring force acting on it is:
$$F = -kx = -m\\omega^2 x$$
where $k = m\\omega^2$ is the force constant.

The work done $dW$ against this restoring force in giving the particle an additional infinitesimal displacement $dx$ is:
$$dW = -F \\, dx = -(-kx) \\, dx = kx \\, dx = m\\omega^2 x \\, dx$$

The total potential energy $U$ stored in displacing the particle from the mean position ($x = 0$) to displacement $x$ is:
$$U = \\int_0^x m\\omega^2 x \\, dx = m\\omega^2 \\left[\\frac{x^2}{2}\\right]_0^x = \\frac{1}{2}m\\omega^2 x^2$$

**3. Total Mechanical Energy ($E$):**
The total energy $E$ of the particle executing SHM is the sum of its kinetic and potential energies:
$$E = K + U$$
$$E = \\frac{1}{2}m\\omega^2 (A^2 - x^2) + \\frac{1}{2}m\\omega^2 x^2$$
$$E = \\frac{1}{2}m\\omega^2 A^2 - \\frac{1}{2}m\\omega^2 x^2 + \\frac{1}{2}m\\omega^2 x^2$$
$$E = \\frac{1}{2}m\\omega^2 A^2 = \\frac{1}{2} k A^2$$

Since $m, \\omega,$ and $A$ are constants for a given SHM, the total mechanical energy is constant at all positions and at all times, verifying the law of conservation of mechanical energy in SHM."""
                },
                {
                    "id": "phy-q7",
                    "number": "7",
                    "question": "Derive an expression for the time of oscillation for a mass m attached to a vertical spring of force constant k.",
                    "answer": """Consider a light, massless helical spring of force constant $k$ suspended vertically from a rigid support.

```
       ////// Rigid Support //////
             |
             §   Natural length L
             |
             §
             |
            [m]  Equilibrium position (stretched by e): mg = ke
             |
             ↓ y (Displaced further downward)
            [m]  Restoring force F = -ky acts upward
```

**Step 1: Equilibrium Position**
When a body of mass $m$ is gently attached to the lower free end of the spring, it stretches by an equilibrium extension $e$.
At this equilibrium position, the downward gravitational force (weight) is balanced by the upward elastic restoring force:
$$mg = ke \\quad \\text{--- (i)}$$

**Step 2: Displaced Position**
Now, let the mass be pulled vertically downwards by an additional small displacement $y$ and released.
The total elongation of the spring from its unstretched position becomes $(e + y)$.
The upward elastic restoring force exerted by the spring is:
$$F' = -k(e + y)$$

The net restoring force $F$ acting on mass $m$ is:
$$F = mg - k(e + y) = mg - ke - ky$$
Using equation (i), $mg - ke = 0$:
$$F = -ky$$

According to Newton's second law of motion:
$$F = ma = m \\frac{d^2 y}{dt^2}$$
Equating the forces:
$$ma = -ky \\implies a = -\\left(\\frac{k}{m}\\right) y \\quad \\text{--- (ii)}$$

Since $k$ and $m$ are constants, $a \\propto -y$. This shows that the acceleration is directly proportional to the displacement and directed opposite to it; hence, the mass executes Simple Harmonic Motion.

Comparing equation (ii) with the standard SHM acceleration equation $a = -\\omega^2 y$:
$$\\omega^2 = \\frac{k}{m} \\implies \\omega = \\sqrt{\\frac{k}{m}}$$

**Step 3: Time Period of Oscillation ($T$)**
The time period $T$ of the vertical oscillation is:
$$T = \\frac{2\\pi}{\\omega} = 2\\pi \\sqrt{\\frac{m}{k}}$$

Also, from equation (i), $\\frac{m}{k} = \\frac{e}{g}$, so the time period can also be written as:
$$T = 2\\pi \\sqrt{\\frac{e}{g}}$$"""
                },
                {
                    "id": "phy-q8",
                    "number": "8",
                    "question": "State and explain Biot-Savart law",
                    "answer": """### Statement
Biot-Savart Law states that the magnitude of the magnetic field $d\\vec{B}$ produced at a point $P$ by an infinitesimal current element $I \\, d\\vec{l}$ of a current-carrying conductor:
1. Is directly proportional to the electric current $I$ passing through the conductor ($dB \\propto I$).
2. Is directly proportional to the length of the current element $dl$ ($dB \\propto dl$).
3. Is directly proportional to the sine of the angle $\\theta$ between the current element $d\\vec{l}$ and the position vector $\\vec{r}$ of point $P$ ($dB \\propto \\sin\\theta$).
4. Is inversely proportional to the square of the distance $r$ between the current element and point $P$ ($dB \\propto \\frac{1}{r^2}$).

```
            I ↑   /
              |  / dl
              | /_ θ
              |/----------> r ----------> P (dB)
              |
```

Combining these four factors:
$$dB \\propto \\frac{I \\, dl \\sin\\theta}{r^2}$$
$$dB = \\left(\\frac{\\mu_0}{4\\pi}\\right) \\frac{I \\, dl \\sin\\theta}{r^2}$$
where $\\frac{\\mu_0}{4\\pi}$ is the proportionality constant in SI units ($10^{-7} \\text{ T}\\cdot\\text{m/A}$), and $\\mu_0$ is the permeability of free space ($4\\pi \\times 10^{-7} \\text{ T}\\cdot\\text{m/A}$).

### Vector Form
In vector notation, since $d\\vec{l} \\times \\hat{r} = dl (1) \\sin\\theta \\, \\hat{n}$:
$$d\\vec{B} = \\frac{\\mu_0}{4\\pi} \\frac{I (d\\vec{l} \\times \\hat{r})}{r^2} = \\frac{\\mu_0}{4\\pi} \\frac{I (d\\vec{l} \\times \\vec{r})}{r^3}$$

### Direction
The direction of $d\\vec{B}$ is perpendicular to the plane containing both $d\\vec{l}$ and $\\vec{r}$, and is given by the Right-Hand Thumb Rule or the right-handed screw rule."""
                },
                {
                    "id": "phy-q9",
                    "number": "9",
                    "question": "Obtain an expression for magnetic field strength at the axis of current carrying circular coil using Biot-Savart’s law.",
                    "answer": """Consider a circular coil of radius $a$ carrying a steady current $I$. Let the axis of the coil lie along the x-axis, with its center at origin $O$. We wish to determine the magnetic field $\\vec{B}$ at an axial point $P$ at a distance $x$ from $O$.

```
               dl (top)
              /|
             / | \\
          a /  |  \\ r = √(a² + x²)
           /   |   \\
          O----+----P-----> X
               x     \\
                      \\ dB_x = dB sin α
                       \\
               dl (bottom)
```

Consider an infinitesimal current element $d\\vec{l}$ at the top of the coil. The displacement vector from this element to point $P$ is $\\vec{r}$, where:
$$r = \\sqrt{a^2 + x^2}$$

Because the element $d\\vec{l}$ lies in the plane perpendicular to the axial line, the angle between $d\\vec{l}$ and $\\vec{r}$ is $90^\\circ$ everywhere along the circumference.

By Biot-Savart's Law, the magnitude of the magnetic field $d\\vec{B}$ at $P$ due to this element is:
$$dB = \\frac{\\mu_0}{4\\pi} \\frac{I \\, dl \\sin 90^\\circ}{r^2} = \\frac{\\mu_0}{4\\pi} \\frac{I \\, dl}{a^2 + x^2}$$

The vector $d\\vec{B}$ is perpendicular to $\\vec{r}$ and can be resolved into two mutually perpendicular components:
1. Axial component: $dB_x = dB \\sin\\alpha$ along the axis of the coil.
2. Perpendicular component: $dB_y = dB \\cos\\alpha$ perpendicular to the axis.

For every current element $d\\vec{l}$ at one side, there exists a diametrically opposite element of equal length producing an equal and opposite vertical component $dB \\cos\\alpha$. Hence, all perpendicular components cancel out on integration ($\\sum dB_y = 0$).

The net magnetic field at point $P$ is obtained by integrating the axial components:
$$B = \\oint dB \\sin\\alpha$$

From the geometry of the right triangle:
$$\\sin\\alpha = \\frac{a}{r} = \\frac{a}{\\sqrt{a^2 + x^2}}$$

Substituting $dB$ and $\\sin\\alpha$:
$$B = \\oint \\left(\\frac{\\mu_0}{4\\pi} \\frac{I \\, dl}{a^2 + x^2}\\right) \\left(\\frac{a}{\\sqrt{a^2 + x^2}}\\right) = \\frac{\\mu_0 I a}{4\\pi (a^2 + x^2)^{3/2}} \\oint dl$$

Since the integral $\\oint dl$ around the circular loop equals the circumference $2\\pi a$:
$$B = \\frac{\\mu_0 I a}{4\\pi (a^2 + x^2)^{3/2}} (2\\pi a) = \\frac{\\mu_0 I a^2}{2(a^2 + x^2)^{3/2}}$$

For a circular coil having $N$ tightly wound turns, the total magnetic field is:
$$B = \\frac{\\mu_0 N I a^2}{2(a^2 + x^2)^{3/2}}$$

*(Special case: At the center of the coil, $x = 0$, which gives $B = \\frac{\\mu_0 N I}{2a}$.)*"""
                },
                {
                    "id": "phy-q10",
                    "number": "10",
                    "question": "State and explain Amper’s law",
                    "answer": """### Statement
Ampere's Circuital Law states that the line integral of the magnetic field $\\vec{B}$ around any closed closed loop (known as an Amperian loop) in free space is equal to $\\mu_0$ times the total net electric current $I_{\\text{enclosed}}$ threaded or enclosed by the loop.

Mathematically:
$$\\oint \\vec{B} \\cdot d\\vec{l} = \\mu_0 I_{\\text{enclosed}}$$
where:
- $\\oint$ represents integration around the complete closed path,
- $d\\vec{l}$ is the infinitesimal vector displacement along the path,
- $\\mu_0$ is the permeability of vacuum ($4\\pi \\times 10^{-7} \\text{ T}\\cdot\\text{m/A}$),
- $I_{\\text{enclosed}}$ is the algebraic sum of all currents passing through the surface bounded by the closed path.

### Explanation
Ampere's circuital law provides an alternative method to Biot-Savart law to calculate magnetic fields for symmetrical current distributions.
1. A closed hypothetical loop of arbitrary shape is chosen around the current-carrying conductors.
2. Sign convention of current: Curl the fingers of the right hand along the chosen direction of integration along the loop; the extended thumb indicates the positive direction of current. Currents flowing in this direction are taken as positive, while opposite currents are negative:
$$I_{\\text{enclosed}} = \\sum I_{\\text{in}} - \\sum I_{\\text{out}}$$
3. If no net current is enclosed by the Amperian loop ($I_{\\text{enclosed}} = 0$), then $\\oint \\vec{B} \\cdot d\\vec{l} = 0$."""
                },
                {
                    "id": "phy-q11",
                    "number": "11",
                    "question": "Derive an expression for the magnetic field strength inside a long current carrying solenoid using Ampere’s circuital law.",
                    "answer": """A solenoid consists of an insulated long conducting wire closely wound in the form of a tight helix. 

Let:
- $L$ be the length of the solenoid,
- $N$ be the total number of turns,
- $n = \\frac{N}{L}$ be the number of turns per unit length,
- $I$ be the steady current passing through the solenoid.

Inside a long solenoid, the magnetic field lines are uniform, parallel to the solenoid axis, and closely spaced. Outside the solenoid, the magnetic field is extremely weak and can be assumed to be practically zero ($B \\approx 0$).

```
        ....................................... (Top turns: current out ⊙)
        
              a ------------ b
              |              |
           B  |   (Inside)   |   Amperian rectangular loop abcd
              |              |
              d ------------ c
        ....................................... (Bottom turns: current in ⊗)
```

Consider a rectangular Amperian loop $abcd$ of length $h$:
- Side $ab = h$ lies completely inside the solenoid parallel to the axis.
- Sides $bc$ and $da$ are perpendicular to the axis.
- Side $cd$ lies completely outside the solenoid.

Evaluating the closed line integral of $\\vec{B}$ along loop $abcd$:
$$\\oint_{abcd} \\vec{B} \\cdot d\\vec{l} = \\int_a^b \\vec{B} \\cdot d\\vec{l} + \\int_b^c \\vec{B} \\cdot d\\vec{l} + \\int_c^d \\vec{B} \\cdot d\\vec{l} + \\int_d^a \\vec{B} \\cdot d\\vec{l}$$

1. Along side $ab$: $\\vec{B}$ and $d\\vec{l}$ are parallel ($\\theta = 0^\\circ$):
$$\\int_a^b \\vec{B} \\cdot d\\vec{l} = \\int_a^b B \\, dl \\cos 0^\\circ = B \\int_a^b dl = B h$$
2. Along sides $bc$ and $da$: $\\vec{B}$ is perpendicular to $d\\vec{l}$ inside the solenoid ($\\theta = 90^\\circ$), and $B = 0$ outside:
$$\\int_b^c \\vec{B} \\cdot d\\vec{l} = 0 \\quad \\text{and} \\quad \\int_d^a \\vec{B} \\cdot d\\vec{l} = 0$$
3. Along side $cd$: The magnetic field outside is zero ($B = 0$):
$$\\int_c^d \\vec{B} \\cdot d\\vec{l} = 0$$

Adding all segments:
$$\\oint_{abcd} \\vec{B} \\cdot d\\vec{l} = Bh + 0 + 0 + 0 = Bh \\quad \\text{--- (i)}$$

Now, determine the total current enclosed by the loop:
Number of turns within length $h = n \\cdot h$
Total current enclosed, $I_{\\text{enclosed}} = (n h) I \\quad \\text{--- (ii)}$

Applying Ampere's circuital law:
$$\\oint_{abcd} \\vec{B} \\cdot d\\vec{l} = \\mu_0 I_{\\text{enclosed}}$$
$$Bh = \\mu_0 (n h I)$$
$$B = \\mu_0 n I$$

This gives the magnetic field strength inside a long current-carrying solenoid."""
                },
                {
                    "id": "phy-q12",
                    "number": "12",
                    "question": "Show that Cp - Cv= R, where symbols carry their usual meaning.",
                    "answer": """Consider one mole of an ideal gas enclosed in a cylinder fitted with a frictionless, movable piston.

Let:
- $P$, $V$, and $T$ be the initial pressure, volume, and absolute temperature of the gas.
- $C_v$ be the molar heat capacity at constant volume.
- $C_p$ be the molar heat capacity at constant pressure.

By the first law of thermodynamics:
$$dQ = dU + dW = dU + P \\, dV$$

### Case 1: Heat supplied at constant volume
If the gas is heated at constant volume ($dV = 0$) such that its temperature rises by $dT$:
$$dW = P \\, dV = 0$$
$$dQ_v = C_v \\, dT$$
Substituting into the first law:
$$C_v \\, dT = dU + 0 \\implies dU = C_v \\, dT \\quad \\text{--- (i)}$$
Because internal energy $U$ of an ideal gas depends solely on temperature, the change in internal energy is always $dU = C_v \\, dT$ for any process where the temperature changes by $dT$.

### Case 2: Heat supplied at constant pressure
If the same one mole of gas is heated at constant pressure such that its temperature increases by the same amount $dT$:
The heat supplied is:
$$dQ_p = C_p \\, dT$$
The gas expands and does external work:
$$dW = P \\, dV$$

Substituting these into the first law:
$$C_p \\, dT = dU + P \\, dV$$
Using equation (i) ($dU = C_v \\, dT$):
$$C_p \\, dT = C_v \\, dT + P \\, dV \\quad \\text{--- (ii)}$$

For one mole of an ideal gas, the equation of state is:
$$PV = RT$$
Differentiating both sides at constant pressure:
$$P \\, dV = R \\, dT \\quad \\text{--- (iii)}$$

Substituting equation (iii) into equation (ii):
$$C_p \\, dT = C_v \\, dT + R \\, dT$$
$$(C_p - C_v) \\, dT = R \\, dT$$
Dividing both sides by $dT$:
$$C_p - C_v = R$$

This relation is known as Mayer's relation, where $R$ is the universal gas constant."""
                },
                {
                    "id": "phy-q13",
                    "number": "13",
                    "question": "Derive an expression for work done during isothermal process.",
                    "answer": """An isothermal process is a thermodynamic process in which the temperature of the system remains strictly constant ($T = \\text{constant}$).

Consider $n$ moles of an ideal gas enclosed in a cylinder with perfectly conducting walls, fitted with a frictionless and movable piston, maintained at a constant absolute temperature $T$.

Let the gas expand isothermally from an initial state $(P_1, V_1, T)$ to a final state $(P_2, V_2, T)$.

For an ideal gas:
$$PV = nRT \\implies P = \\frac{nRT}{V}$$

When the gas expands by an infinitesimal volume $dV$, the external work done by the gas is:
$$dW = P \\, dV = \\frac{nRT}{V} dV$$

The total work done $W$ during isothermal expansion from volume $V_1$ to $V_2$ is:
$$W = \\int_{V_1}^{V_2} dW = \\int_{V_1}^{V_2} \\frac{nRT}{V} \\, dV$$

Since $n, R,$ and $T$ are constants:
$$W = nRT \\int_{V_1}^{V_2} \\frac{dV}{V} = nRT [\\ln V]_{V_1}^{V_2}$$
$$W = nRT (\\ln V_2 - \\ln V_1) = nRT \\ln\\left(\\frac{V_2}{V_1}\\right)$$

Converting natural logarithm to base 10:
$$W = 2.303 \\, nRT \\log_{10}\\left(\\frac{V_2}{V_1}\\right)$$

According to Boyle's law, at constant temperature:
$$P_1 V_1 = P_2 V_2 \\implies \\frac{V_2}{V_1} = \\frac{P_1}{P_2}$$

Therefore, the work done in terms of initial and final pressures is:
$$W = 2.303 \\, nRT \\log_{10}\\left(\\frac{P_1}{P_2}\\right)"""
                },
                {
                    "id": "phy-q14",
                    "number": "14",
                    "question": "Derive an expression for work done during adiabatic process.",
                    "answer": """An adiabatic process is a thermodynamic process in which no exchange of heat takes place between the system and its surroundings ($dQ = 0$).

Consider $n$ moles of an ideal gas enclosed in a cylinder having non-conducting walls and fitted with an insulating, frictionless piston.
Let the gas expand adiabatically from an initial state $(P_1, V_1, T_1)$ to a final state $(P_2, V_2, T_2)$.

For a reversible adiabatic process:
$$P V^\\gamma = K \\text{ (constant)}$$
$$P = \\frac{K}{V^\\gamma} = K V^{-\\gamma}$$
where $\\gamma = \\frac{C_p}{C_v}$ is the adiabatic index.

The work done in a small volume change $dV$ is:
$$dW = P \\, dV = K V^{-\\gamma} \\, dV$$

The total work done $W$ as the volume expands from $V_1$ to $V_2$ is:
$$W = \\int_{V_1}^{V_2} K V^{-\\gamma} \\, dV = K \\left[\\frac{V^{-\\gamma + 1}}{-\\gamma + 1}\\right]_{V_1}^{V_2} = \\frac{K}{1 - \\gamma} [V_2^{1-\\gamma} - V_1^{1-\\gamma}]$$
$$W = \\frac{1}{1 - \\gamma} [K V_2^{1-\\gamma} - K V_1^{1-\\gamma}]$$

Since the points lie on the same adiabatic path:
$$K = P_2 V_2^\\gamma = P_1 V_1^\\gamma$$
Substituting $K = P_2 V_2^\\gamma$ in the first term and $K = P_1 V_1^\\gamma$ in the second term:
$$W = \\frac{1}{1 - \\gamma} [(P_2 V_2^\\gamma) V_2^{1-\\gamma} - (P_1 V_1^\\gamma) V_1^{1-\\gamma}]$$
$$W = \\frac{1}{1 - \\gamma} [P_2 V_2 - P_1 V_1] = \\frac{P_1 V_1 - P_2 V_2}{\\gamma - 1}$$

Using the ideal gas equation:
$$P_1 V_1 = nRT_1 \\quad \\text{and} \\quad P_2 V_2 = nRT_2$$
$$W = \\frac{nR(T_1 - T_2)}{\\gamma - 1}$$

This is the required expression for work done during an adiabatic process."""
                }
            ]
        },
        {
            "name": "Numerical",
            "questions": [
                {
                    "id": "phy-num1",
                    "number": "1",
                    "question": "A circular coil of 100 turns has a radius of 10 cm and carries a current of 5A. Determine the magnetic field at a point on the axis of the coil at a distance of 5cm from the center of the coil.",
                    "answer": """**Given:**
- Number of turns, $N = 100$
- Radius of the circular coil, $a = 10 \\text{ cm} = 0.1 \\text{ m}$
- Current, $I = 5 \\text{ A}$
- Axial distance from center, $x = 5 \\text{ cm} = 0.05 \\text{ m}$
- Permeability of free space, $\\mu_0 = 4\\pi \\times 10^{-7} \\text{ T}\\cdot\\text{m/A}$

**Required:**
- Magnetic field at the axial point, $B = ?$

**Formula:**
$$B = \\frac{\\mu_0 N I a^2}{2(a^2 + x^2)^{3/2}}$$

**Calculation:**
$$a^2 + x^2 = (0.1)^2 + (0.05)^2 = 0.01 + 0.0025 = 0.0125 \\text{ m}^2$$
$$(a^2 + x^2)^{3/2} = (0.0125)^{3/2} = 0.0125 \\times \\sqrt{0.0125} = 0.0125 \\times 0.111803 \\approx 1.3975 \\times 10^{-3} \\text{ m}^3$$

Numerator:
$$\\mu_0 N I a^2 = (4\\pi \\times 10^{-7}) \\times 100 \\times 5 \\times (0.1)^2$$
$$= 4\\pi \\times 10^{-7} \\times 500 \\times 0.01 = 2\\pi \\times 10^{-5} \\approx 6.2832 \\times 10^{-5} \\text{ T}\\cdot\\text{m}^3$$

Denominator:
$$2(a^2 + x^2)^{3/2} = 2 \\times 1.3975 \\times 10^{-3} = 2.795 \\times 10^{-3} \\text{ m}^3$$

$$B = \\frac{6.2832 \\times 10^{-5}}{2.795 \\times 10^{-3}} \\approx 2.25 \\times 10^{-2} \\text{ T}$$

The magnetic field at the point on the axis is $2.25 \\times 10^{-2} \\text{ T}$."""
                },
                {
                    "id": "phy-num2",
                    "number": "2",
                    "question": "At what temperature, the velocity of sound in air is increased by 60% to that at 27℃?",
                    "answer": """**Given:**
- Initial temperature, $t_1 = 27^\\circ\\text{C}$
- Absolute initial temperature, $T_1 = 27 + 273 = 300 \\text{ K}$
- Let initial velocity of sound be $v_1$.
- Final velocity of sound, $v_2 = v_1 + 60\\% \\text{ of } v_1 = v_1 + 0.60 v_1 = 1.60 v_1$

**Required:**
- Final temperature, $T_2 = ?$ (and in $^\\circ\\text{C}$, $t_2$)

**Formula:**
The velocity of sound in a gas is directly proportional to the square root of its absolute temperature:
$$v \\propto \\sqrt{T} \\implies \\frac{v_2}{v_1} = \\sqrt{\\frac{T_2}{T_1}}$$

**Calculation:**
$$\\frac{1.60 v_1}{v_1} = \\sqrt{\\frac{T_2}{300}}$$
$$1.60 = \\sqrt{\\frac{T_2}{300}}$$

Squaring both sides:
$$(1.60)^2 = \\frac{T_2}{300}$$
$$2.56 = \\frac{T_2}{300}$$
$$T_2 = 2.56 \\times 300 = 768 \\text{ K}$$

Converting into Celsius:
$$t_2 = 768 - 273 = 495^\\circ\\text{C}$$

At $495^\\circ\\text{C}$ (or $768 \\text{ K}$), the velocity of sound in air is increased by $60\\%$ compared to that at $27^\\circ\\text{C}$."""
                },
                {
                    "id": "phy-num3",
                    "number": "3",
                    "question": "A bob of mass 8 kg performs SHM of amplitude 30cm. The restoring force is 60N. Calculate: - i) Time period ii) The maximum acceleration.",
                    "answer": """**Given:**
- Mass of the bob, $m = 8 \\text{ kg}$
- Amplitude, $A = 30 \\text{ cm} = 0.30 \\text{ m}$
- Maximum restoring force (at extreme position $x = A$), $F_{\\max} = 60 \\text{ N}$

**Required:**
- i) Time period, $T = ?$
- ii) Maximum acceleration, $a_{\\max} = ?$

**Formula and Calculation:**
**i) Time Period:**
At the extreme position ($x = A$), the restoring force is related to the force constant $k$ by:
$$F_{\\max} = k A \\implies k = \\frac{F_{\\max}}{A} = \\frac{60 \\text{ N}}{0.30 \\text{ m}} = 200 \\text{ N/m}$$

The time period of SHM is:
$$T = 2\\pi \\sqrt{\\frac{m}{k}} = 2\\pi \\sqrt{\\frac{8}{200}} = 2\\pi \\sqrt{\\frac{1}{25}} = 2\\pi \\left(\\frac{1}{5}\\right) = \\frac{2 \\times 3.1416}{5} \\approx 1.26 \\text{ s}$$

**ii) Maximum Acceleration:**
The maximum acceleration occurs at the extreme position:
$$a_{\\max} = \\frac{F_{\\max}}{m} = \\frac{60 \\text{ N}}{8 \\text{ kg}} = 7.5 \\text{ m/s}^2$$
*(Alternatively: $a_{\\max} = \\omega^2 A = \\left(\\frac{k}{m}\\right) A = \\frac{200}{8} \\times 0.30 = 25 \\times 0.30 = 7.5 \\text{ m/s}^2$.)*

i) Time period $= 1.26 \\text{ s}$, ii) Maximum acceleration $= 7.5 \\text{ m/s}^2$."""
                },
                {
                    "id": "phy-num4",
                    "number": "4",
                    "question": "Determine the electric field supplied when the electric force applied between the two horizontal plates just balances an oil drop with 4 electrons attached to it having mass 1.31 x 10-14 kg.",
                    "answer": """**Given:**
- Mass of the oil drop, $m = 1.31 \\times 10^{-14} \\text{ kg}$
- Number of excess electrons, $n = 4$
- Elementary charge of an electron, $e = 1.6 \\times 10^{-19} \\text{ C}$
- Net charge on the oil drop, $q = n e = 4 \\times 1.6 \\times 10^{-19} \\text{ C} = 6.4 \\times 10^{-19} \\text{ C}$
- Acceleration due to gravity, $g = 9.8 \\text{ m/s}^2$

**Required:**
- Electric field supplied, $E = ?$

**Formula:**
For the oil drop to remain stationary (balanced), the upward electrostatic force must exactly balance the downward gravitational force (weight):
$$F_e = F_g$$
$$q E = m g \\implies E = \\frac{m g}{q}$$

**Calculation:**
$$E = \\frac{(1.31 \\times 10^{-14} \\text{ kg}) \\times (9.8 \\text{ m/s}^2)}{6.4 \\times 10^{-19} \\text{ C}}$$
$$E = \\frac{1.2838 \\times 10^{-13}}{6.4 \\times 10^{-19}} \\approx 2.01 \\times 10^5 \\text{ V/m} \\text{ (or N/C)}$$

The required electric field is $2.01 \\times 10^5 \\text{ V/m}$ (directed vertically downwards so that the upward force on the negative charge balances gravity)."""
                }
            ]
        }
    ]
}

with open(os.path.join(out_dir, "physics.js"), "w", encoding="utf-8") as f:
    f.write("window.PHYSICS_DATA = " + json.dumps(physics_data, indent=2, ensure_ascii=False) + ";\n")

print("Wrote physics.js successfully")
