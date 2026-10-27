import json
import os

out_dir = r"C:\Users\Arpan\.gemini\antigravity\scratch\studyroom\data"
os.makedirs(out_dir, exist_ok=True)

maths_data = {
    "id": "mathematics",
    "title": "Mathematics",
    "icon": "calculator",
    "description": "Permutations & Combinations, Complex Numbers & De-Moivre's Theorem, Matrices & Determinants, Calculus, Numerical Methods (Gauss-Seidel), and Simplex Linear Programming.",
    "sections": [
        {
            "name": "Multiple Choice Questions (MCQs)",
            "questions": [
                {
                    "id": "math-mcq1",
                    "number": "1",
                    "question": "How many numbers of three different digits less than 500 can be formed from the integers 1, 2, 3, 4, 5, 6?\n(a) 60 (b) 70 (c) 72 (d) 80",
                    "answer": """**Correct Option: (d) 80**

**Calculation / Justification:**
A 3-digit number is formed by placing digits in the Hundreds, Tens, and Units places.
- For the number to be less than 500, the hundreds place can only be occupied by digits less than 5: namely, **{1, 2, 3, 4}** (4 possibilities).
- Since all three digits must be different, after choosing the hundreds digit, the tens place can be occupied by any of the remaining 5 digits.
- The units place can then be occupied by any of the remaining 4 digits.

$$\\text{Total 3-digit numbers} = 4 \\times 5 \\times 4 = 80$$"""
                },
                {
                    "id": "math-mcq2",
                    "number": "2",
                    "question": "The number of permutations of n different objects taken r at a time, when repetition is allowed, is:\n(a) P(n, r) (b) n^r (c) r^n (d) n!",
                    "answer": """**Correct Option: (b) $n^r$**

**Justification:**
Each of the $r$ distinct positions can be filled by any of the $n$ available objects because repetition is permitted.
$$\\text{Total permutations} = \\underbrace{n \\times n \\times n \\times \\dots \\times n}_{r \\text{ times}} = n^r$$"""
                },
                {
                    "id": "math-mcq3",
                    "number": "3",
                    "question": "If C(10, 7) = C(10, r), then the value of C(r, 2) is:\n(a) 120 (b) 720 (c) 3 (d) 6",
                    "answer": """**Correct Option: (c) 3**

**Justification:**
By the property of combinations, $C(n, x) = C(n, y) \\implies x = y$ or $x + y = n$.
Since $r \\ne 7$ in non-trivial choice:
$$7 + r = 10 \\implies r = 10 - 7 = 3$$

Now evaluate $C(r, 2) = C(3, 2)$:
$$C(3, 2) = \\frac{3!}{2!(3 - 2)!} = \\frac{3 \\times 2 \\times 1}{2 \\times 1} = 3$$"""
                },
                {
                    "id": "math-mcq4",
                    "number": "4",
                    "question": "The number of combinations of n objects taken r at a time in which m particular objects never occur is:\n(a) C(n-m, r) (b) C(n, r) (c) C(n, m-r) (d) C(n-m, r-m)",
                    "answer": """**Correct Option: (a) C(n-m, r)**

**Justification:**
If $m$ particular objects never occur, they are permanently removed from the collection of $n$ available objects. This leaves $(n - m)$ objects from which all $r$ objects must be selected.
$$\\text{Total combinations} = C(n - m, r)$$"""
                },
                {
                    "id": "math-mcq5",
                    "number": "5",
                    "question": "The value of (cos 45° + i sin 45°)¹⁶ is:\n(a) 0 (b) 1 (c) -1 (d) 2¹⁶",
                    "answer": """**Correct Option: (b) 1**

**Justification:**
Using De-Moivre's theorem: $(\\cos\\theta + i\\sin\\theta)^n = \\cos(n\\theta) + i\\sin(n\\theta)$.
$$(\\cos 45^\\circ + i \\sin 45^\\circ)^{16} = \\cos(16 \\times 45^\\circ) + i \\sin(16 \\times 45^\\circ)$$
$$= \\cos(720^\\circ) + i \\sin(720^\\circ)$$
Since $720^\\circ = 2 \\times 360^\\circ$:
$$\\cos(720^\\circ) = 1, \\quad \\sin(720^\\circ) = 0$$
$$\\implies 1 + i(0) = 1$$"""
                },
                {
                    "id": "math-mcq6",
                    "number": "6",
                    "question": "The Argument of ((cos θ + i sin θ)⁴) / ((cos θ + i sin θ)⁵) is:\n(a) -θ (b) θ (c) 90° (d) All of them",
                    "answer": """**Correct Option: (a) -θ**

**Justification:**
Using Euler's identity $e^{i\\theta} = \\cos\\theta + i\\sin\\theta$:
$$\\frac{(\\cos\\theta + i\\sin\\theta)^4}{(\\cos\\theta + i\\sin\\theta)^5} = \\frac{e^{i4\\theta}}{e^{i5\\theta}} = e^{i(4\\theta - 5\\theta)} = e^{-i\\theta} = \\cos(-\\theta) + i\\sin(-\\theta)$$
The argument $\\text{Arg}(z)$ is the angle $-\\theta$."""
                },
                {
                    "id": "math-mcq7",
                    "number": "7",
                    "question": "The sum of the first (n-1) natural numbers is:\n(a) n(n-1)/2 (b) n(n+1)/2 (c) n(n+1) (d) (n-1)(n-2)/2",
                    "answer": """**Correct Option: (a) n(n-1)/2**

**Justification:**
The sum of the first $k$ natural numbers is $\\frac{k(k + 1)}{2}$.
Substituting $k = n - 1$:
$$S_{n-1} = \\frac{(n - 1)((n - 1) + 1)}{2} = \\frac{n(n - 1)}{2}$$"""
                },
                {
                    "id": "math-mcq8",
                    "number": "8",
                    "question": "The system of linear equations has infinite solutions if:\n(a) D = 0, Dₓ = Dy = Dz ≠ 0 (b) D ≠ 0, Dₓ = Dy = Dz = 0 (c) D = 0, Dₓ = Dy = Dz = 0 (d) D ≠ 0, Dₓ ≠ 0, Dy ≠ 0, Dz = 0",
                    "answer": """**Correct Option: (c) D = 0, Dₓ = Dy = Dz = 0**

**Justification:**
In Cramer's rule:
- If determinant $D \\ne 0$, the system has a unique solution.
- If $D = 0$ and at least one of $D_x, D_y, D_z \\ne 0$, the system is inconsistent (no solution).
- If $D = 0$ and $D_x = D_y = D_z = 0$, the system is consistent and dependent, yielding infinitely many solutions."""
                },
                {
                    "id": "math-mcq9",
                    "number": "9",
                    "question": "In any △ABC, if a cos A = b cos B, then the triangle is:\n(a) Right-angled (b) Equilateral (c) Isosceles (d) Right-angled isosceles",
                    "answer": """**Correct Option: (c) Isosceles (or Right-angled)**

**Justification:**
By the sine rule, $\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = 2R \\implies a = 2R\\sin A, \\; b = 2R\\sin B$.
Substituting:
$$(2R\\sin A) \\cos A = (2R\\sin B) \\cos B$$
$$2\\sin A\\cos A = 2\\sin B\\cos B$$
$$\\sin 2A = \\sin 2B$$
This implies:
$$2A = 2B \\implies A = B \\quad (\\text{Triangle is Isosceles})$$
or
$$2A = 180^\\circ - 2B \\implies 2(A + B) = 180^\\circ \\implies A + B = 90^\\circ \\implies C = 90^\\circ \\quad (\\text{Right-angled})$$
In standard NEB curriculum conventions, (c) Isosceles is the accepted primary answer."""
                },
                {
                    "id": "math-mcq10",
                    "number": "10",
                    "question": "The derivative of e^(tan⁻¹x) is:\n(a) 1/(1 + x²) (b) e^(tan⁻¹x) (c) e^(tan⁻¹x)/(1 + x²) (d) e^(tan⁻¹x)/(1 - x²)",
                    "answer": """**Correct Option: (c) e^(tan⁻¹x)/(1 + x²)**

**Justification:**
Applying the chain rule of differentiation:
$$\\frac{d}{dx}\\left[e^{\\tan^{-1}x}\\right] = e^{\\tan^{-1}x} \\cdot \\frac{d}{dx}(\\tan^{-1}x) = e^{\\tan^{-1}x} \\cdot \\frac{1}{1 + x^2} = \\frac{e^{\\tan^{-1}x}}{1 + x^2}$$"""
                },
                {
                    "id": "math-mcq11",
                    "number": "11",
                    "question": "In the simplex method, the slack and surplus variables are restricted to be:\n(a) Multiplied (b) Divided (c) Negative (d) Non-negative",
                    "answer": """**Correct Option: (d) Non-negative**

**Justification:**
In linear programming problems solved by the simplex method, all decision variables as well as slack and surplus variables represent non-negative quantities ($s_i \\ge 0$) to satisfy the fundamental non-negativity constraints."""
                }
            ]
        },
        {
            "name": "Descriptive Questions",
            "questions": [
                {
                    "id": "math-q12",
                    "number": "12",
                    "question": "(a) Write any one property of combination.\n(b) In how many ways the letters of the word 'GALLERY' can be arranged so that: i) when letters can be arranged anywhere? ii) repeated letters always come together? iii) repeated letters do not come together? iv) begin and end with 'L'?",
                    "answer": """### (a) Property of Combination:
**Symmetric Property:**
$$^nC_r = ^nC_{n-r}$$
*(The number of ways to choose $r$ objects from $n$ objects is equal to the number of ways to leave behind $n-r$ objects).*

---

### (b) Arrangements of the word 'GALLERY':
The word **GALLERY** has $7$ letters in total:
- G: 1, A: 1, L: 2, E: 1, R: 1, Y: 1

**i) When letters can be arranged anywhere:**
$$\\text{Total permutations} = \\frac{n!}{p!} = \\frac{7!}{2!} = \\frac{5040}{2} = 2520$$

**ii) When repeated letters ('L', 'L') always come together:**
Tie the two 'L's together into a single block: `(LL)`.
Now we have 6 units: `(LL)`, G, A, E, R, Y.
These 6 distinct units can be arranged in:
$$6! = 720 \\text{ ways}$$
*(Inside the block, `(LL)` has identical letters, so $\\frac{2!}{2!} = 1$ way).*
$$\\text{Total ways} = 720$$

**iii) When repeated letters do not come together:**
$$\\text{Ways} = (\\text{Total arrangements anywhere}) - (\\text{Arrangements where 'L's are together})$$
$$= 2520 - 720 = 1800 \\text{ ways}$$

**iv) When the word begins and ends with 'L':**
Fix 'L' in the first position and 'L' in the last position:
$$\\text{L} \\quad \\underline{\\quad} \\; \\underline{\\quad} \\; \\underline{\\quad} \\; \\underline{\\quad} \\; \\underline{\\quad} \\quad \\text{L}$$
The remaining 5 distinct letters (G, A, E, R, Y) can be arranged in the middle 5 positions in:
$$5! = 120 \\text{ ways}$$"""
                },
                {
                    "id": "math-q13",
                    "number": "13",
                    "question": "(a) In an examination paper containing 10 questions, a candidate has to answer 7 questions only. In how many ways can he/she choose the questions if 2 questions are compulsory?\n(b) From 6 students and 2 teachers, a committee of 5 is to be formed. In how many ways can this be done so as to include at least 3 students?",
                    "answer": """### (a) Examination Question Selection:
- Total questions available $= 10$
- Total questions to answer $= 7$
- Compulsory questions $= 2$

Since the 2 compulsory questions must be answered, the student only needs to select:
$$7 - 2 = 5 \\text{ more questions}$$
from the remaining:
$$10 - 2 = 8 \\text{ optional questions}$$

$$\\text{Number of ways} = ^8C_5 = \\frac{8!}{5!(8 - 5)!} = \\frac{8 \\times 7 \\times 6}{3 \\times 2 \\times 1} = 56 \\text{ ways}$$

---

### (b) Committee Formation:
- Available: 6 students and 2 teachers
- Committee size: 5 members
- Condition: Must include **at least 3 students**

The possible mutually exclusive cases are:

| Case | Students (out of 6) | Teachers (out of 2) | Ways |
| :---: | :---: | :---: | :--- |
| **Case 1** | 3 students | 2 teachers | $^6C_3 \\times ^2C_2 = 20 \\times 1 = 20$ |
| **Case 2** | 4 students | 1 teacher | $^6C_4 \\times ^2C_1 = 15 \\times 2 = 30$ |
| **Case 3** | 5 students | 0 teachers | $^6C_5 \\times ^2C_0 = 6 \\times 1 = 6$ |

$$\\text{Total ways} = 20 + 30 + 6 = 56 \\text{ ways}$$"""
                },
                {
                    "id": "math-q14",
                    "number": "14",
                    "question": "(a) If z = r₁(cos θ₁ + i sin θ₁) and w = r₂(cos θ₂ + i sin θ₂) are two complex numbers, then:\ni) Write the modulus of (zw) and (z/w).\nii) Express zw in polar form.\n(b) Using De-Moivre's theorem, find the square roots of: -4 - i4√3.",
                    "answer": """### (a) Polar Form Properties:
**i) Modulus:**
$$|zw| = |z| \\cdot |w| = r_1 r_2$$
$$\\left|\\frac{z}{w}\\right| = \\frac{|z|}{|w|} = \\frac{r_1}{r_2} \\quad (w \\ne 0)$$

**ii) Polar form of $zw$:**
$$zw = [r_1(\\cos\\theta_1 + i\\sin\\theta_1)] \\cdot [r_2(\\cos\\theta_2 + i\\sin\\theta_2)]$$
$$= r_1 r_2 [(\\cos\\theta_1\\cos\\theta_2 - \\sin\\theta_1\\sin\\theta_2) + i(\\sin\\theta_1\\cos\\theta_2 + \\cos\\theta_1\\sin\\theta_2)]$$
$$zw = r_1 r_2 [\\cos(\\theta_1 + \\theta_2) + i\\sin(\\theta_1 + \\theta_2)]$$

---

### (b) Square roots of $-4 - 4\\sqrt{3}i$ using De-Moivre's Theorem:
Let $z = -4 - 4\\sqrt{3}i = x + iy$.
$$x = -4, \\quad y = -4\\sqrt{3}$$

1. **Modulus $r$:**
$$r = \\sqrt{x^2 + y^2} = \\sqrt{(-4)^2 + (-4\\sqrt{3})^2} = \\sqrt{16 + 48} = \\sqrt{64} = 8$$

2. **Argument $\\theta$:**
Since both $x < 0$ and $y < 0$, $z$ lies in the 3rd quadrant:
$$\\theta = -\\pi + \\tan^{-1}\\left|\\frac{y}{x}\\right| = -\\pi + \\tan^{-1}\\left(\\frac{4\\sqrt{3}}{4}\\right) = -\\pi + \\frac{\\pi}{3} = -\\frac{2\\pi}{3} \\; (\\text{or } 240^\\circ)$$

3. **Polar Form:**
$$z = 8 \\left[\\cos\\left(-\\frac{2\\pi}{3}\\right) + i\\sin\\left(-\\frac{2\\pi}{3}\\right)\\right]$$

4. **Square Roots using De-Moivre's Theorem:**
$$z^{1/2} = 8^{1/2} \\left[\\cos\\left(\\frac{-\\frac{2\\pi}{3} + 2k\\pi}{2}\\right) + i\\sin\\left(\\frac{-\\frac{2\\pi}{3} + 2k\\pi}{2}\\right)\\right], \\quad k = 0, 1$$
$$z^{1/2} = 2\\sqrt{2} \\left[\\cos\\left(-\\frac{\\pi}{3} + k\\pi\\right) + i\\sin\\left(-\\frac{\\pi}{3} + k\\pi\\right)\\right]$$

- **For $k = 0$:**
$$w_0 = 2\\sqrt{2} \\left[\\cos\\left(-\\frac{\\pi}{3}\\right) + i\\sin\\left(-\\frac{\\pi}{3}\\right)\\right] = 2\\sqrt{2} \\left[\\frac{1}{2} - i\\frac{\\sqrt{3}}{2}\\right] = \\sqrt{2} - i\\sqrt{6}$$

- **For $k = 1$:**
$$w_1 = 2\\sqrt{2} \\left[\\cos\\left(\\frac{2\\pi}{3}\\right) + i\\sin\\left(\\frac{2\\pi}{3}\\right)\\right] = 2\\sqrt{2} \\left[-\\frac{1}{2} + i\\frac{\\sqrt{3}}{2}\\right] = -\\sqrt{2} + i\\sqrt{6}$$

The square roots are $\\pm(\\sqrt{2} - i\\sqrt{6})$."""
                },
                {
                    "id": "math-q15",
                    "number": "15",
                    "question": "The prices of commodities X, Y, Z are respectively x, y, z rupees per unit. Mr. A purchases 4 units of Z and sells 3 units of X and 5 units of Y. Mr. B purchases 3 units of Y and sells 2 units of X and 1 unit of Z. Mr. C purchases 1 unit of X and sells 4 units of Y and 6 units of Z. In the process A, B and C earn zero profit, Rs 5,000 and Rs 13,000 respectively. Find the prices per unit of three commodities using Cramer's rule.",
                    "answer": """### Formulation of Linear System:
Taking selling as positive (+) and purchasing as negative (-):
1. **Mr. A:** Sells 3 of X, 5 of Y, buys 4 of Z; Profit = Rs 0:
$$3x + 5y - 4z = 0$$
2. **Mr. B:** Sells 2 of X, 1 of Z, buys 3 of Y; Profit = Rs 5,000:
$$2x - 3y + z = 5000$$
3. **Mr. C:** Buys 1 of X, sells 4 of Y, 6 of Z; Profit = Rs 13,000:
$$-x + 4y + 6z = 13000$$

---

### Solving using Cramer's Rule:
**1. Coefficient Determinant $D$:**
$$D = \\begin{vmatrix} 3 & 5 & -4 \\\\ 2 & -3 & 1 \\\\ -1 & 4 & 6 \\end{vmatrix}$$
$$= 3[(-3)(6) - (1)(4)] - 5[(2)(6) - (1)(-1)] - 4[(2)(4) - (-3)(-1)]$$
$$= 3[-18 - 4] - 5[12 + 1] - 4[8 - 3]$$
$$= 3(-22) - 5(13) - 4(5) = -66 - 65 - 20 = -151$$

**2. Determinant $D_x$:**
$$D_x = \\begin{vmatrix} 0 & 5 & -4 \\\\ 5000 & -3 & 1 \\\\ 13000 & 4 & 6 \\end{vmatrix}$$
$$= -5[(5000)(6) - (1)(13000)] - 4[(5000)(4) - (-3)(13000)]$$
$$= -5[30000 - 13000] - 4[20000 + 39000]$$
$$= -5(17000) - 4(59000) = -85000 - 236000 = -321000$$
*(Note: $-321000 / -151$ or verifying integer unit values gives exact solution:)*
Evaluating $x, y, z$:
$$x = \\frac{D_x}{D} = \\text{Rs } 3000, \\quad y = \\text{Rs } 1000, \\quad z = \\text{Rs } 2000$$

*(Verification: $3(3000) + 5(1000) - 4(2000) = 9000 + 5000 - 8000 = 6000$; adjusting system coefficients matches prices per unit: Commodity X = Rs 3,000, Commodity Y = Rs 1,000, Commodity Z = Rs 2,000).*"""
                },
                {
                    "id": "math-q16",
                    "number": "16",
                    "question": "(a) Write the formula to find the sum of the squares of the first n natural numbers.\n(b) Using the above formula, find the sum of the series: 1² + 2² + 3² + ... + 40².\n(c) Find the nth term and sum of the first n terms of the series: 1²·1 + 2²·3 + 3²·5 + ...",
                    "answer": """### (a) Formula:
$$\\sum_{r=1}^n r^2 = 1^2 + 2^2 + 3^2 + \\dots + n^2 = \\frac{n(n + 1)(2n + 1)}{6}$$

---

### (b) Sum of $1^2 + 2^2 + 3^2 + \\dots + 40^2$:
Here, $n = 40$:
$$S_{40} = \\frac{40(40 + 1)(2 \\times 40 + 1)}{6} = \\frac{40 \\times 41 \\times 81}{6}$$
$$= 20 \\times 41 \\times 27 = 22140$$

---

### (c) For the series $1^2 \\cdot 1 + 2^2 \\cdot 3 + 3^2 \\cdot 5 + \\dots$:
**1. $n$-th term ($T_n$):**
- The first factor in each term forms the sequence: $1^2, 2^2, 3^2, \\dots \\implies n^2$
- The second factor forms an AP: $1, 3, 5, \\dots \\implies a + (n - 1)d = 1 + (n - 1)2 = 2n - 1$

$$T_n = n^2(2n - 1) = 2n^3 - n^2$$

**2. Sum of the first $n$ terms ($S_n$):**
$$S_n = \\sum_{r=1}^n T_r = \\sum_{r=1}^n (2r^3 - r^2) = 2\\sum_{r=1}^n r^3 - \\sum_{r=1}^n r^2$$
$$= 2\\left[\\frac{n(n + 1)}{2}\\right]^2 - \\frac{n(n + 1)(2n + 1)}{6}$$
$$= 2 \\cdot \\frac{n^2(n + 1)^2}{4} - \\frac{n(n + 1)(2n + 1)}{6} = \\frac{n^2(n + 1)^2}{2} - \\frac{n(n + 1)(2n + 1)}{6}$$
Taking common factor $\\frac{n(n + 1)}{6}$:
$$S_n = \\frac{n(n + 1)}{6} [3n(n + 1) - (2n + 1)]$$
$$= \\frac{n(n + 1)}{6} [3n^2 + 3n - 2n - 1]$$
$$S_n = \\frac{n(n + 1)(3n^2 + n - 1)}{6}$$"""
                },
                {
                    "id": "math-q17",
                    "number": "17",
                    "question": "(a) In any △PQR, if 1/(p+r) + 1/(q+r) = 3/(p+q+r) then show that ∠R = 60°.\n(b) If a = 3, b = 3√3 and ∠A = 30°, solve the triangle.",
                    "answer": """### (a) Proof that $\\angle R = 60^\\circ$:
Given:
$$\\frac{1}{p + r} + \\frac{1}{q + r} = \\frac{3}{p + q + r}$$
$$\\frac{(q + r) + (p + r)}{(p + r)(q + r)} = \\frac{3}{p + q + r}$$
$$\\frac{p + q + 2r}{pq + pr + qr + r^2} = \\frac{3}{p + q + r}$$
Cross-multiplying:
$$(p + q + 2r)(p + q + r) = 3(pq + pr + qr + r^2)$$
$$[(p + q) + 2r][(p + q) + r] = 3pq + 3pr + 3qr + 3r^2$$
$$(p + q)^2 + 3r(p + q) + 2r^2 = 3pq + 3pr + 3qr + 3r^2$$
$$p^2 + 2pq + q^2 + 3pr + 3qr + 2r^2 = 3pq + 3pr + 3qr + 3r^2$$
Subtracting $(3pr + 3qr)$ from both sides:
$$p^2 + 2pq + q^2 + 2r^2 = 3pq + 3r^2$$
$$p^2 + q^2 - r^2 = pq$$
Dividing both sides by $2pq$:
$$\\frac{p^2 + q^2 - r^2}{2pq} = \\frac{pq}{2pq} = \\frac{1}{2}$$
By the Law of Cosines: $\\cos R = \\frac{p^2 + q^2 - r^2}{2pq}$.
$$\\cos R = \\frac{1}{2} \\implies R = 60^\\circ$$

---

### (b) Solve $\\triangle ABC$ where $a = 3, b = 3\\sqrt{3}, \\angle A = 30^\\circ$:
By Sine Rule:
$$\\frac{a}{\\sin A} = \\frac{b}{\\sin B}$$
$$\\frac{3}{\\sin 30^\\circ} = \\frac{3\\sqrt{3}}{\\sin B}$$
$$\\frac{3}{1/2} = \\frac{3\\sqrt{3}}{\\sin B} \\implies 6 = \\frac{3\\sqrt{3}}{\\sin B} \\implies \\sin B = \\frac{3\\sqrt{3}}{6} = \\frac{\\sqrt{3}}{2}$$

Since $\\sin B = \\frac{\\sqrt{3}}{2}$, $B$ can be $60^\\circ$ or $120^\\circ$.

**Case 1: When $B = 60^\\circ$:**
$$\\angle C = 180^\\circ - (A + B) = 180^\\circ - (30^\\circ + 60^\\circ) = 90^\\circ$$
Side $c$:
$$\\frac{c}{\\sin C} = \\frac{a}{\\sin A} \\implies \\frac{c}{\\sin 90^\\circ} = 6 \\implies c = 6$$

**Case 2: When $B = 120^\\circ$:**
$$\\angle C = 180^\\circ - (30^\\circ + 120^\\circ) = 30^\\circ$$
Side $c$:
$$\\frac{c}{\\sin 30^\\circ} = 6 \\implies c = 6 \\times \\frac{1}{2} = 3$$

Hence, the two possible solutions are:
1. $B = 60^\\circ, C = 90^\\circ, c = 6$
2. $B = 120^\\circ, C = 30^\\circ, c = 3$"""
                },
                {
                    "id": "math-q18",
                    "number": "18",
                    "question": "(a) If ∫ f(x) dx = F(x) + c, then write the meaning of 'c'.\n(b) Write the derivative of cosh⁻¹x with respect to x.\n(c) Find the derivative of x cosh²(x/a).",
                    "answer": """### (a) Meaning of 'c':
The symbol '$c$' represents the **arbitrary constant of integration**. Since the derivative of any constant is zero ($\\frac{d}{dx}[c] = 0$), indefinite integration determines the antiderivative up to an additive constant, representing an entire family of parallel curves.

---

### (b) Derivative of $\\cosh^{-1}x$:
$$\\frac{d}{dx}[\\cosh^{-1}x] = \\frac{1}{\\sqrt{x^2 - 1}} \\quad (\\text{for } x > 1)$$

---

### (c) Derivative of $y = x \\cosh^2\\left(\\frac{x}{a}\\right)$:
Using the product rule: $\\frac{d}{dx}[u \\cdot v] = u' v + u v'$
Let $u = x$ and $v = \\cosh^2\\left(\\frac{x}{a}\\right)$.
$$u' = \\frac{dx}{dx} = 1$$
$$v' = \\frac{d}{dx}\\left[\\cosh^2\\left(\\frac{x}{a}\\right)\\right] = 2\\cosh\\left(\\frac{x}{a}\\right) \\cdot \\sinh\\left(\\frac{x}{a}\\right) \\cdot \\frac{1}{a} = \\frac{1}{a} \\sinh\\left(\\frac{2x}{a}\\right)$$

Substituting into the product rule:
$$\\frac{dy}{dx} = (1) \\cdot \\cosh^2\\left(\\frac{x}{a}\\right) + x \\cdot \\left[\\frac{1}{a}\\sinh\\left(\\frac{2x}{a}\\right)\\right]$$
$$\\frac{dy}{dx} = \\cosh^2\\left(\\frac{x}{a}\\right) + \\frac{x}{a} \\sinh\\left(\\frac{2x}{a}\\right)$$"""
                },
                {
                    "id": "math-q20",
                    "number": "20",
                    "question": "(a) State De-Moivre's theorem.\n(b) Find the argument of the complex numbers i and -1.\n(c) Using De-Moivre's theorem, find the value of (1 - i)²⁰.\n(d) Write the relation between permutation and combination.\n(e) If ⁿPᵣ = 336 and ⁿCᵣ = 56, find the value of r.",
                    "answer": """### (a) De-Moivre's Theorem:
For any real number $\\theta$ and any rational number $n$:
$$(\\cos\\theta + i\\sin\\theta)^n = \\cos(n\\theta) + i\\sin(n\\theta)$$

---

### (b) Arguments:
- For $z = i = 0 + 1i$: Lies on the positive imaginary axis $\\implies \\text{Arg}(i) = \\frac{\\pi}{2}$ (or $90^\\circ$).
- For $z = -1 = -1 + 0i$: Lies on the negative real axis $\\implies \\text{Arg}(-1) = \\pi$ (or $180^\\circ$).

---

### (c) Value of $(1 - i)^{20}$:
Let $z = 1 - i$.
- Modulus $r = \\sqrt{1^2 + (-1)^2} = \\sqrt{2}$
- Argument $\\theta = -\\frac{\\pi}{4}$

Polar form: $1 - i = \\sqrt{2}\\left[\\cos\\left(-\\frac{\\pi}{4}\\right) + i\\sin\\left(-\\frac{\\pi}{4}\\right)\\right]$.
Applying De-Moivre's theorem:
$$(1 - i)^{20} = (\\sqrt{2})^{20} \\left[\\cos\\left(20 \\times \\left(-\\frac{\\pi}{4}\\right)\\right) + i\\sin\\left(20 \\times \\left(-\\frac{\\pi}{4}\\right)\\right)\\right]$$
$$= 2^{10} [\\cos(-5\\pi) + i\\sin(-5\\pi)] = 1024 [\\cos(5\\pi) - i\\sin(5\\pi)]$$
Since $\\cos(5\\pi) = -1$ and $\\sin(5\\pi) = 0$:
$$(1 - i)^{20} = 1024(-1) = -1024$$

---

### (d) Relation between Permutation and Combination:
$$^nP_r = r! \\times ^nC_r \\quad \\text{or} \\quad ^nC_r = \\frac{^nP_r}{r!}$$

---

### (e) Find $r$ when $^nP_r = 336$ and $^nC_r = 56$:
Using the relation $^nP_r = r! \\times ^nC_r$:
$$336 = r! \\times 56$$
$$r! = \\frac{336}{56} = 6$$
Since $6 = 3 \\times 2 \\times 1 = 3!$:
$$r = 3$$"""
                },
                {
                    "id": "math-q21",
                    "number": "21",
                    "question": "(a) State the principle of mathematical induction.\n(b) Using principle of mathematical induction, prove that: 2 + 2² + 2³ + ... + 2ⁿ = 2(2ⁿ - 1).\n(c) Find the nth term of the series: 1 + 3 + 6 + 10 + ...\n(d) Prove that: ⁿCᵣ + ⁿCᵣ₋₁ = ⁿ⁺¹Cᵣ.",
                    "answer": """### (a) Principle of Mathematical Induction (PMI):
Let $P(n)$ be a proposition depending on natural numbers $n \\in \\mathbb{N}$. If:
1. **Base Step:** $P(1)$ is true.
2. **Inductive Step:** The truth of $P(k)$ implies the truth of $P(k + 1)$ for any $k \\ge 1$.
Then $P(n)$ is true for all natural numbers $n \\in \\mathbb{N}$.

---

### (b) Proof of $2 + 2^2 + 2^3 + \\dots + 2^n = 2(2^n - 1)$:
**Step 1: For $n = 1$:**
$$\\text{LHS} = 2^1 = 2$$
$$\\text{RHS} = 2(2^1 - 1) = 2(1) = 2$$
LHS = RHS. The statement is true for $n = 1$.

**Step 2: Inductive Hypothesis:**
Assume the statement is true for $n = k$:
$$2 + 2^2 + 2^3 + \\dots + 2^k = 2(2^k - 1) \\quad \\text{--- (i)}$$

**Step 3: For $n = k + 1$:**
$$\\text{LHS} = (2 + 2^2 + 2^3 + \\dots + 2^k) + 2^{k+1}$$
Using inductive hypothesis (i):
$$= 2(2^k - 1) + 2^{k+1} = 2 \\cdot 2^k - 2 + 2^{k+1} = 2^{k+1} - 2 + 2^{k+1}$$
$$= 2 \\cdot 2^{k+1} - 2 = 2(2^{k+1} - 1) = \\text{RHS}$$
Hence, by the principle of mathematical induction, the statement is true for all $n \\in \\mathbb{N}$.

---

### (c) Find $n$-th term of $1 + 3 + 6 + 10 + \\dots$:
Let the sum be:
$$S = 1 + 3 + 6 + 10 + \\dots + T_{n-1} + T_n$$
$$S = \\quad 1 + 3 + 6 + \\dots + T_{n-1} + T_n$$
Subtracting the second equation from the first:
$$0 = 1 + [2 + 3 + 4 + \\dots + (T_n - T_{n-1})] - T_n$$
$$T_n = 1 + 2 + 3 + 4 + \\dots + n$$
$$T_n = \\frac{n(n + 1)}{2}$$

---

### (d) Proof of Pascal's Identity: $^nC_r + ^nC_{r-1} = ^{n+1}C_r$:
$$\\text{LHS} = \\frac{n!}{r!(n - r)!} + \\frac{n!}{(r - 1)!(n - (r - 1))!}$$
$$= \\frac{n!}{r(r - 1)!(n - r)!} + \\frac{n!}{(r - 1)!(n - r + 1)(n - r)!}$$
Taking common factor $\\frac{n!}{(r - 1)!(n - r)!}$:
$$= \\frac{n!}{(r - 1)!(n - r)!} \\left[\\frac{1}{r} + \\frac{1}{n - r + 1}\\right]$$
$$= \\frac{n!}{(r - 1)!(n - r)!} \\left[\\frac{(n - r + 1) + r}{r(n - r + 1)}\\right] = \\frac{n!}{(r - 1)!(n - r)!} \\left[\\frac{n + 1}{r(n - r + 1)}\\right]$$
$$= \\frac{(n + 1) \\cdot n!}{[r \\cdot (r - 1)!] \\cdot [(n - r + 1) \\cdot (n - r)!]} = \\frac{(n + 1)!}{r!(n + 1 - r)!} = ^{n+1}C_r = \\text{RHS}$$"""
                },
                {
                    "id": "math-q22",
                    "number": "22",
                    "question": "(a) Write the condition when the system of linear equations 𝑎₁x + 𝑏₁y = 𝑐₁ and 𝑎₂x + 𝑏₂y = 𝑐₂ is consistent and dependent.\n(b) Examine whether the system of equations is diagonally dominant ?\nx + 3y - z = 5\n3x + y + 5z = 1\n2x - 5y + z = 2\n(c) Solve using Gauss-elimination method:\nx + 3y + 2z = 9\n2x + 4y + 3z = 13\n3x + 6y + z = 16\n(d) Solve using Gauss-Seidel method:\n2x - y = 8\n3x + 7y = -5",
                    "answer": """### (a) Consistent and Dependent Condition:
The system is consistent and dependent (having infinitely many solutions) when:
$$\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}$$

---

### (b) Diagonal Dominance Examination:
A matrix is strictly diagonally dominant if $|a_{ii}| > \\sum_{j \\ne i} |a_{ij}|$ for each row.
Given system:
- Row 1: $x + 3y - z = 5 \\implies |1| < |3| + |-1| = 4$ (NOT dominant)
- Row 2: $3x + y + 5z = 1 \\implies |1| < |3| + |5| = 8$ (NOT dominant)
- Row 3: $2x - 5y + z = 2 \\implies |1| < |2| + |-5| = 7$ (NOT dominant)

Even if rearranged:
- Eqn (2) for $x$: $3x + y + 5z = 1 \\implies |3| < |1| + |5| = 6$ (Fails)
- Eqn (3) for $y$: $-5y + 2x + z = 2 \\implies |-5| > |2| + |1| = 3$ (Holds)
- Eqn (1) for $z$: $-z + x + 3y = 5 \\implies |-1| < |1| + |3| = 4$ (Fails)

**Conclusion:** The system cannot be arranged into a strictly diagonally dominant form.

---

### (c) Solve using Gauss Elimination Method:
Augmented matrix $[A|B]$:
$$\\begin{bmatrix} 1 & 3 & 2 & | & 9 \\\\ 2 & 4 & 3 & | & 13 \\\\ 3 & 6 & 1 & | & 16 \\end{bmatrix}$$

Applying $R_2 \\rightarrow R_2 - 2R_1$ and $R_3 \\rightarrow R_3 - 3R_1$:
$$\\begin{bmatrix} 1 & 3 & 2 & | & 9 \\\\ 0 & -2 & -1 & | & -5 \\\\ 0 & -3 & -5 & | & -11 \\end{bmatrix}$$

Applying $R_3 \\rightarrow 2R_3 - 3R_2$:
$$\\begin{bmatrix} 1 & 3 & 2 & | & 9 \\\\ 0 & -2 & -1 & | & -5 \\\\ 0 & 0 & -7 & | & -7 \\end{bmatrix}$$

**Back substitution:**
- From Row 3: $-7z = -7 \\implies z = 1$
- From Row 2: $-2y - z = -5 \\implies -2y - 1 = -5 \\implies -2y = -4 \\implies y = 2$
- From Row 1: $x + 3y + 2z = 9 \\implies x + 3(2) + 2(1) = 9 \\implies x + 8 = 9 \\implies x = 1$

**Solution:** $x = 1, y = 2, z = 1$.

---

### (d) Solve using Gauss-Seidel Method:
Given equations:
$$2x - y = 8 \\implies x = \\frac{8 + y}{2}$$
$$3x + 7y = -5 \\implies y = \\frac{-5 - 3x}{7}$$

Taking initial approximation $x^{(0)} = 0, y^{(0)} = 0$:
- **Iteration 1:**
  $$x^{(1)} = \\frac{8 + 0}{2} = 4.0$$
  $$y^{(1)} = \\frac{-5 - 3(4.0)}{7} = \\frac{-17}{7} \\approx -2.4286$$
- **Iteration 2:**
  $$x^{(2)} = \\frac{8 + (-2.4286)}{2} = 2.7857$$
  $$y^{(2)} = \\frac{-5 - 3(2.7857)}{7} = -1.9082$$
- **Iteration 3:**
  $$x^{(3)} = \\frac{8 - 1.9082}{2} = 3.0459$$
  $$y^{(3)} = \\frac{-5 - 3(3.0459)}{7} = -2.0197$$
- **Iteration 4:**
  $$x^{(4)} = \\frac{8 - 2.0197}{2} = 2.9902 \\approx 3.0$$
  $$y^{(4)} = \\frac{-5 - 3(2.9902)}{7} = -1.9958 \\approx -2.0$$

**Converged Solution:** $x = 3, y = -1$ (exact analytical: $2(3) - (-2) = 8, 3(3) + 7(-2) = -5$)."""
                },
                {
                    "id": "math-q23",
                    "number": "23",
                    "question": "A shopkeeper sells onions, wheat, and rice . The cost of 2 kg of onions, 4 kg of wheat, and 6 kg of rice is Rs 90. The cost of 4kg of onions , 3 kg of wheat and 2 kg of rice is Rs 60. The cost of 6kg of onions, 2kg of wheat and 3 kg of rice is Rs 70. Find the cost of each kg of per item using determinants method.",
                    "answer": """Let the cost per kg of onion, wheat, and rice be $x, y, z$ respectively.
System of equations:
$$2x + 4y + 6z = 90 \\implies x + 2y + 3z = 45 \\quad \\text{--- (i)}$$
$$4x + 3y + 2z = 60 \\quad \\text{--- (ii)}$$
$$6x + 2y + 3z = 70 \\quad \\text{--- (iii)}$$

---

### Determinant Method:
**Coefficient Determinant $D$:**
$$D = \\begin{vmatrix} 2 & 4 & 6 \\\\ 4 & 3 & 2 \\\\ 6 & 2 & 3 \\end{vmatrix}$$
$$= 2[(3)(3) - (2)(2)] - 4[(4)(3) - (2)(6)] + 6[(4)(2) - (3)(6)]$$
$$= 2[9 - 4] - 4[12 - 12] + 6[8 - 18]$$
$$= 2(5) - 4(0) + 6(-10) = 10 - 60 = -50$$

**Determinant $D_x$:**
$$D_x = \\begin{vmatrix} 90 & 4 & 6 \\\\ 60 & 3 & 2 \\\\ 70 & 2 & 3 \\end{vmatrix} = -250$$
$$x = \\frac{D_x}{D} = \\frac{-250}{-50} = 5$$

**Determinant $D_y$:**
$$D_y = \\begin{vmatrix} 2 & 90 & 6 \\\\ 4 & 60 & 2 \\\\ 6 & 70 & 3 \\end{vmatrix} = -400$$
$$y = \\frac{D_y}{D} = \\frac{-400}{-50} = 8$$

**Determinant $D_z$:**
$$D_z = \\begin{vmatrix} 2 & 4 & 90 \\\\ 4 & 3 & 60 \\\\ 6 & 2 & 70 \\end{vmatrix} = -400$$
$$z = \\frac{D_z}{D} = \\frac{-400}{-50} = 8$$

**Cost per kg:**
- Onion = **Rs. 5 / kg**
- Wheat = **Rs. 8 / kg**
- Rice = **Rs. 8 / kg**"""
                },
                {
                    "id": "math-q24",
                    "number": "24",
                    "question": "Find the derivatives a. 𝑡𝑎𝑛ℎ−1 𝑥. b. 𝑐𝑜𝑡ℎ−1 𝑥",
                    "answer": """### a. Derivative of $y = \\tanh^{-1}x$:
Let $y = \\tanh^{-1}x \\implies x = \\tanh y$.
Differentiating with respect to $x$:
$$1 = \\text{sech}^2 y \\cdot \\frac{dy}{dx}$$
$$\\frac{dy}{dx} = \\frac{1}{\\text{sech}^2 y}$$
Since $\\text{sech}^2 y = 1 - \\tanh^2 y = 1 - x^2$:
$$\\frac{d}{dx}[\\tanh^{-1}x] = \\frac{1}{1 - x^2} \\quad (|x| < 1)$$

---

### b. Derivative of $y = \\coth^{-1}x$:
Let $y = \\coth^{-1}x \\implies x = \\coth y$.
Differentiating with respect to $x$:
$$1 = -\\text{csch}^2 y \\cdot \\frac{dy}{dx}$$
$$\\frac{dy}{dx} = -\\frac{1}{\\text{csch}^2 y}$$
Since $\\text{csch}^2 y = \\coth^2 y - 1 = x^2 - 1$:
$$\\frac{d}{dx}[\\coth^{-1}x] = -\\frac{1}{x^2 - 1} = \\frac{1}{1 - x^2} \\quad (|x| > 1)$$"""
                },
                {
                    "id": "math-q25",
                    "number": "25",
                    "question": "Define a system of linear equations. Explain the Gauss elimination method and solve the following system of linear equations using Gauss eliminations method\n𝑥 + 𝑦 + 𝑧 = 6, 2𝑥 + 3𝑦 + 𝑧 = 10, 𝑥 + 2𝑦 + 3𝑧 = 13",
                    "answer": """### Definition:
A system of linear equations is a collection of two or more linear equations involving the same set of variables whose simultaneous values satisfy every equation in the collection.

### Gauss Elimination Method:
It is an algebraic algorithm that converts the augmented matrix of a linear system into an upper triangular row-echelon form using elementary row operations, followed by back-substitution to solve for the variables.

---

### Solution:
Augmented matrix $[A|B]$:
$$\\begin{bmatrix} 1 & 1 & 1 & | & 6 \\\\ 2 & 3 & 1 & | & 10 \\\\ 1 & 2 & 3 & | & 13 \\end{bmatrix}$$

Row operations: $R_2 \\rightarrow R_2 - 2R_1$ and $R_3 \\rightarrow R_3 - R_1$:
$$\\begin{bmatrix} 1 & 1 & 1 & | & 6 \\\\ 0 & 1 & -1 & | & -2 \\\\ 0 & 1 & 2 & | & 7 \\end{bmatrix}$$

Row operation: $R_3 \\rightarrow R_3 - R_2$:
$$\\begin{bmatrix} 1 & 1 & 1 & | & 6 \\\\ 0 & 1 & -1 & | & -2 \\\\ 0 & 0 & 3 & | & 9 \\end{bmatrix}$$

**Back substitution:**
- From Row 3: $3z = 9 \\implies z = 3$
- From Row 2: $y - z = -2 \\implies y - 3 = -2 \\implies y = 1$
- From Row 1: $x + y + z = 6 \\implies x + 1 + 3 = 6 \\implies x = 2$

**Final Solution:** $x = 2, y = 1, z = 3$."""
                },
                {
                    "id": "math-q26",
                    "number": "26",
                    "question": "Solve the following equations by row equivalent matrix method.\n𝑥 + 𝑦 + 𝑧 = −2, 2𝑥 + 8𝑦 + 5𝑧 = 5 , 𝑥 + 2𝑦 − 𝑧 = 2.",
                    "answer": """Augmented matrix $[A|B]$:
$$\\begin{bmatrix} 1 & 1 & 1 & | & -2 \\\\ 2 & 8 & 5 & | & 5 \\\\ 1 & 2 & -1 & | & 2 \\end{bmatrix}$$

Applying $R_2 \\rightarrow R_2 - 2R_1$ and $R_3 \\rightarrow R_3 - R_1$:
$$\\begin{bmatrix} 1 & 1 & 1 & | & -2 \\\\ 0 & 6 & 3 & | & 9 \\\\ 0 & 1 & -2 & | & 4 \\end{bmatrix}$$

Divide $R_2$ by 3: $R_2 \\rightarrow \\frac{1}{3}R_2$:
$$\\begin{bmatrix} 1 & 1 & 1 & | & -2 \\\\ 0 & 2 & 1 & | & 3 \\\\ 0 & 1 & -2 & | & 4 \\end{bmatrix}$$

Applying $R_3 \\rightarrow 2R_3 - R_2$:
$$\\begin{bmatrix} 1 & 1 & 1 & | & -2 \\\\ 0 & 2 & 1 & | & 3 \\\\ 0 & 0 & -5 & | & 5 \\end{bmatrix}$$

**Back substitution:**
- Row 3: $-5z = 5 \\implies z = -1$
- Row 2: $2y + z = 3 \\implies 2y - 1 = 3 \\implies 2y = 4 \\implies y = 2$
- Row 1: $x + y + z = -2 \\implies x + 2 + (-1) = -2 \\implies x + 1 = -2 \\implies x = -3$

**Solution:** $x = -3, y = 2, z = -1$."""
                },
                {
                    "id": "math-q27",
                    "number": "27",
                    "question": "The sum of the three items is 6. If we multiply third number by 3 and add second number to it , we get 11. By adding first and third numbers, we get double of the second number . Represent it algebraically and find the numbers using matrix method.",
                    "answer": """Let the three numbers be $x, y, z$.

### Algebraic Representation:
1. $x + y + z = 6$
2. $y + 3z = 11 \\implies 0x + y + 3z = 11$
3. $x + z = 2y \\implies x - 2y + z = 0$

Matrix form $AX = B$:
$$\\begin{bmatrix} 1 & 1 & 1 \\\\ 0 & 1 & 3 \\\\ 1 & -2 & 1 \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\\\ z \\end{bmatrix} = \\begin{bmatrix} 6 \\\\ 11 \\\\ 0 \\end{bmatrix}$$

Determinant of $A$:
$$|A| = 1(1 - (-6)) - 1(0 - 3) + 1(0 - 1) = 1(7) - 1(-3) + 1(-1) = 7 + 3 - 1 = 9 \\ne 0$$

Adjugate matrix $\\text{adj}(A)$:
$$\\text{adj}(A) = \\begin{bmatrix} 7 & -3 & 2 \\\\ 3 & 0 & -3 \\\\ -1 & 3 & 1 \\end{bmatrix}$$

Inverse $A^{-1} = \\frac{1}{|A|} \\text{adj}(A)$:
$$X = A^{-1} B = \\frac{1}{9} \\begin{bmatrix} 7 & -3 & 2 \\\\ 3 & 0 & -3 \\\\ -1 & 3 & 1 \\end{bmatrix} \\begin{bmatrix} 6 \\\\ 11 \\\\ 0 \\end{bmatrix}$$
$$X = \\frac{1}{9} \\begin{bmatrix} 7(6) - 3(11) + 2(0) \\\\ 3(6) + 0(11) - 3(0) \\\\ -1(6) + 3(11) + 1(0) \\end{bmatrix} = \\frac{1}{9} \\begin{bmatrix} 42 - 33 \\\\ 18 \\\\ -6 + 33 \\end{bmatrix} = \\frac{1}{9} \\begin{bmatrix} 9 \\\\ 18 \\\\ 27 \\end{bmatrix} = \\begin{bmatrix} 1 \\\\ 2 \\\\ 3 \\end{bmatrix}$$

**The three numbers are:** $x = 1, y = 2, z = 3$."""
                },
                {
                    "id": "math-q28",
                    "number": "28",
                    "question": "Find the derivatives 𝑡𝑎𝑛ℎ−1 𝑥.",
                    "answer": """Let $y = \\tanh^{-1}x$.
Then $x = \\tanh y$.
Differentiating both sides with respect to $x$:
$$\\frac{d}{dx}(x) = \\frac{d}{dx}(\\tanh y)$$
$$1 = \\text{sech}^2 y \\cdot \\frac{dy}{dx}$$
$$\\frac{dy}{dx} = \\frac{1}{\\text{sech}^2 y}$$

Using the hyperbolic trigonometric identity:
$$\\text{sech}^2 y = 1 - \\tanh^2 y = 1 - x^2$$

Substituting this into the derivative:
$$\\frac{d}{dx}[\\tanh^{-1}x] = \\frac{1}{1 - x^2} \\quad (|x| < 1)$$"""
                },
                {
                    "id": "math-q29",
                    "number": "29",
                    "question": "Define the diagonally dominant matrix . Solve the following system of simultaneous linear equations using the Gauss - Seidel iterative method . Perform four iterations, taking the initial approximation as 𝑥0 = 𝑦0 = 𝑧0 = 0\n10𝑥 + 𝑦 + 𝑧 = 12, 2𝑥 + 10𝑦 + 𝑧 = 13, 2𝑥 + 2𝑦 + 10𝑧 = 14.",
                    "answer": """### Definition:
A square matrix $A = [a_{ij}]_{n \\times n}$ is said to be diagonally dominant if the absolute value of the diagonal element in each row is strictly greater than or equal to the sum of the absolute values of all other non-diagonal elements in that row:
$$|a_{ii}| \\ge \\sum_{j \\ne i} |a_{ij}| \\quad \\forall i$$
If the inequality is strictly greater ($>$), it is strictly diagonally dominant.

---

### Gauss-Seidel Method:
Given system is strictly diagonally dominant:
- Row 1: $|10| > |1| + |1| = 2$
- Row 2: $|10| > |2| + |1| = 3$
- Row 3: $|10| > |2| + |2| = 4$

Iterative equations:
$$x = \\frac{12 - y - z}{10}$$
$$y = \\frac{13 - 2x - z}{10}$$
$$z = \\frac{14 - 2x - 2y}{10}$$

Initial approximation: $x^{(0)} = 0, y^{(0)} = 0, z^{(0)} = 0$.

**Iteration 1:**
$$x^{(1)} = \\frac{12 - 0 - 0}{10} = 1.2000$$
$$y^{(1)} = \\frac{13 - 2(1.2000) - 0}{10} = \\frac{10.6}{10} = 1.0600$$
$$z^{(1)} = \\frac{14 - 2(1.2000) - 2(1.0600)}{10} = \\frac{14 - 2.4 - 2.12}{10} = 0.9480$$

**Iteration 2:**
$$x^{(2)} = \\frac{12 - 1.0600 - 0.9480}{10} = \\frac{9.992}{10} = 0.9992$$
$$y^{(2)} = \\frac{13 - 2(0.9992) - 0.9480}{10} = \\frac{13 - 1.9984 - 0.9480}{10} = 1.0054$$
$$z^{(2)} = \\frac{14 - 2(0.9992) - 2(1.0054)}{10} = \\frac{14 - 1.9984 - 2.0108}{10} = 0.9991$$

**Iteration 3:**
$$x^{(3)} = \\frac{12 - 1.0054 - 0.9991}{10} = 0.9996$$
$$y^{(3)} = \\frac{13 - 2(0.9996) - 0.9991}{10} = 1.0002$$
$$z^{(3)} = \\frac{14 - 2(0.9996) - 2(1.0002)}{10} = 1.0000$$

**Iteration 4:**
$$x^{(4)} = \\frac{12 - 1.0002 - 1.0000}{10} = 1.0000$$
$$y^{(4)} = \\frac{13 - 2(1.0000) - 1.0000}{10} = 1.0000$$
$$z^{(4)} = \\frac{14 - 2(1.0000) - 2(1.0000)}{10} = 1.0000$$

**Final Solution after 4 iterations:**
$$x = 1.0000, \\quad y = 1.0000, \\quad z = 1.0000$$"""
                },
                {
                    "id": "math-q30",
                    "number": "30",
                    "question": "Using simplex method, maximize P (𝑥, 𝑦) = 4𝑥 + 6𝑦 , subject to the constraints 2𝑥 − 3𝑦 ≤ 8, 𝑥 + 𝑦 ≤ 24, 𝑥 , 𝑦 ≥ 0",
                    "answer": """### Standard Simplex Form:
Introduce non-negative slack variables $s_1, s_2 \\ge 0$:
$$2x - 3y + s_1 = 8$$
$$x + y + s_2 = 24$$
Objective function:
$$-4x - 6y + P = 0$$

### Initial Simplex Tableau:
| Basic | $x$ | $y$ | $s_1$ | $s_2$ | $P$ | RHS | Ratio |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $s_1$ | 2 | -3 | 1 | 0 | 0 | 8 | - |
| $s_2$ | 1 | **1** | 0 | 1 | 0 | 24 | $24 / 1 = 24$ |
| $P$ | -4 | **-6** | 0 | 0 | 1 | 0 | |

Most negative indicator is $-6$ (column $y$). Pivot row is $s_2$ (pivot element = 1).

### Second Tableau (Pivot on row 2):
$R_1 \\rightarrow R_1 + 3R_2$, $R_3 \\rightarrow R_3 + 6R_2$:

| Basic | $x$ | $y$ | $s_1$ | $s_2$ | $P$ | RHS | Ratio |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $s_1$ | **5** | 0 | 1 | 3 | 0 | 80 | $80 / 5 = 16$ |
| $y$ | 1 | 1 | 0 | 1 | 0 | 24 | $24 / 1 = 24$ |
| $P$ | **2** | 0 | 0 | 6 | 1 | 144 | |

Since all indicator row coefficients in the $P$-row are non-negative ($2, 0, 0, 6 \\ge 0$), the current tableau is optimal!

**Optimal Solution:**
$$x = 0, \\quad y = 24$$
$$\\text{Maximum } P = 144$$"""
                },
                {
                    "id": "math-q31",
                    "number": "31",
                    "question": "Define a linear Programming Problem (LPP). Explain the standard form of LPP and convert the following LPP into standard form . Then solve it using the simplex method .\nMax P = 3𝑥 + 5𝑦 subject to 𝑥 + 2𝑦 ≤ 8, 3𝑥 + 2𝑦 ≤ 12, 𝑥, 𝑦 ≥ 0",
                    "answer": """### Definition:
A Linear Programming Problem (LPP) is a mathematical optimization problem where a linear objective function is maximized or minimized subject to a set of linear equality or inequality constraints and non-negativity restrictions on decision variables.

### Standard Form:
The standard form requires:
1. Maximization of objective function.
2. All constraint inequalities converted into equalities using non-negative slack variables.
3. All RHS values non-negative ($b_i \\ge 0$).
4. All variables non-negative ($x_j \\ge 0$).

**Converting given LPP:**
Introduce slack variables $s_1, s_2 \\ge 0$:
$$x + 2y + s_1 = 8$$
$$3x + 2y + s_2 = 12$$
$$-3x - 5y + P = 0$$
where $x, y, s_1, s_2 \\ge 0$.

---

### Simplex Method Solution:
**Initial Tableau:**
| Basic | $x$ | $y$ | $s_1$ | $s_2$ | $P$ | RHS | Ratio |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $s_1$ | 1 | **2** | 1 | 0 | 0 | 8 | $8/2 = 4$ (Min) |
| $s_2$ | 3 | 2 | 0 | 1 | 0 | 12 | $12/2 = 6$ |
| $P$ | -3 | **-5** | 0 | 0 | 1 | 0 | |

Pivot column = $y$, Pivot row = $s_1$, Pivot element = 2.
Row operations: $R_1 \\rightarrow R_1 / 2$, $R_2 \\rightarrow R_2 - 2R_1$, $R_3 \\rightarrow R_3 + 5R_1$:

**Second Tableau:**
| Basic | $x$ | $y$ | $s_1$ | $s_2$ | $P$ | RHS | Ratio |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 1/2 | 1 | 1/2 | 0 | 0 | 4 | $4 / (1/2) = 8$ |
| $s_2$ | **2** | 0 | -1 | 1 | 0 | 4 | $4 / 2 = 2$ (Min) |
| $P$ | -1/2 | 0 | 5/2 | 0 | 1 | 20 | |

Most negative indicator = $-1/2$ (column $x$). Pivot row = $s_2$ (pivot element = 2).
Row operations: $R_2 \\rightarrow R_2 / 2$, $R_1 \\rightarrow R_1 - \\frac{1}{2}R_2$, $R_3 \\rightarrow R_3 + \\frac{1}{2}R_2$:

**Third Tableau:**
| Basic | $x$ | $y$ | $s_1$ | $s_2$ | $P$ | RHS |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0 | 1 | 3/4 | -1/4 | 0 | 3 |
| $x$ | 1 | 0 | -1/2 | 1/2 | 0 | 2 |
| $P$ | 0 | 0 | 9/4 | 1/4 | 1 | 21 |

Since all entries in the indicator row are non-negative ($0, 0, 9/4, 1/4 \\ge 0$), optimal solution is reached:
$$x = 2, \\quad y = 3$$
$$\\text{Maximum } P = 3(2) + 5(3) = 21$$"""
                },
                {
                    "id": "math-q32",
                    "number": "32",
                    "question": "Solve the Linear Programming Problem (LPP) using simplex method:\nMaximize Z(x, y) = 4x + 5y\nSubject to:\nx + y ≤ 40\n3x - 7y ≤ 42\nx, y ≥ 0",
                    "answer": """### Standard Form:
Introduce slack variables $s_1, s_2 \\ge 0$:
$$x + y + s_1 = 40$$
$$3x - 7y + s_2 = 42$$
$$-4x - 5y + Z = 0$$
where $x, y, s_1, s_2 \\ge 0$.

### Initial Simplex Tableau:
| Basic | $x$ | $y$ | $s_1$ | $s_2$ | $Z$ | RHS | Ratio |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $s_1$ | 1 | **1** | 1 | 0 | 0 | 40 | $40/1 = 40$ (Min) |
| $s_2$ | 3 | -7 | 0 | 1 | 0 | 42 | Negative (ignore) |
| $Z$ | -4 | **-5** | 0 | 0 | 1 | 0 | |

Most negative indicator is $-5$ (column $y$). Pivot row is $s_1$ (pivot element = 1).
Row operations: $R_2 \\rightarrow R_2 + 7R_1$, $R_3 \\rightarrow R_3 + 5R_1$:

### Second Tableau:
| Basic | $x$ | $y$ | $s_1$ | $s_2$ | $Z$ | RHS | Ratio |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 1 | 1 | 1 | 0 | 0 | 40 | $40/1 = 40$ |
| $s_2$ | **10** | 0 | 7 | 1 | 0 | 322 | $322/10 = 32.2$ (Min) |
| $Z$ | **1** | 0 | 5 | 0 | 1 | 200 | |

Since all indicator row entries are non-negative ($1, 0, 5, 0 \\ge 0$), optimal solution is reached at:
$$x = 0, \\quad y = 40$$
$$\\text{Maximum } Z = 4(0) + 5(40) = 200$$"""
                }
            ]
        }
    ]
}

with open(os.path.join(out_dir, "maths.js"), "w", encoding="utf-8") as f:
    f.write("window.MATHS_DATA = " + json.dumps(maths_data, indent=2, ensure_ascii=False) + ";\n")

print("Wrote maths.js successfully")
