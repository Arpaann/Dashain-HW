import json
import os

out_dir = r"C:\Users\Arpan\.gemini\antigravity\scratch\studyroom\data"
os.makedirs(out_dir, exist_ok=True)

english_data = {
    "id": "english",
    "title": "English",
    "icon": "book-open",
    "description": "Literary analysis, formal correspondence, creative narrative, professional resume, argumentative essay, and linguistic development.",
    "sections": [
        {
            "name": "Compulsory English",
            "questions": [
                {
                    "id": "eng-q1",
                    "number": "1",
                    "question": "Define literature. Argue the usefulness of studying various genres of literature in your personal and professional life, drawing upon texts from your Compulsory English textbook to support your arguments.",
                    "answer": """### Definition of Literature
Literature is the artistic expression of human thought, imagination, emotion, and cultural experience in written or spoken language of lasting aesthetic, intellectual, and moral value. It is not merely a mirror reflecting societal realities, but a living medium through which humanity explores the deepest questions of existence, morality, justice, and empathy.

### Usefulness in Personal Life
Studying diverse literary genres—poetry, short stories, essays, and drama—cultivates emotional intelligence, introspection, and ethical awareness.
1. **Poetry and Emotional Resilience:** In W.B. Yeats's poem *"The Lamentation of the Old Pensioner"*, the speaker contrasts the vigor of youth with the frailty of old age, raging against 'Time' rather than fellow human beings. Engaging with this lyric poetry instills personal resilience, helping us confront unavoidable human limitations and aging with dignity and acceptance.
2. **Short Stories and Compassion:** Anton Chekhov's short story *"About Love"* examines the moral dilemmas and silent heartbreak born of social restraint and unspoken affection. It teaches that love cannot be reduced to dogmatic formulas or suppressed for fear of public judgment, urging us to approach personal relationships with courage, empathy, and honesty. Similarly, Anita Desai's *"A Devoted Son"* reveals the painful paradoxes between parental expectations and generational autonomy, warning us against turning filial duty into rigid, mechanical control.

### Usefulness in Professional Life
The analytical and communicative faculties nurtured by literature are indispensable assets in modern professional careers:
1. **Critical Thinking and Human Psychology:** H.G. Wells's adventure story *"The Treasure in the Forest"* exposes how raw human greed blinds individuals to peril, leading to the demise of Evans and Hooker through their impatience and arrogance. In professional leadership and project management, recognizing the destructive nature of unchecked greed and short-sightedness prevents catastrophic managerial errors.
2. **Communication, Rhetoric, and Persuasion:** Analyzing persuasive essays in our textbook hone rhetorical precision, logical argumentation, and structural clarity—skills vital for drafting reports, delivering keynote presentations, negotiating commercial contracts, and formulating policy.
3. **Cross-Cultural Competence:** Literature exposes professionals to varied worldview perspectives, nurturing cross-cultural sensitivity and team collaboration in globalized workplaces.

Thus, literature bridges personal empathy with professional acumen, transforming students into reflective individuals and ethical professionals."""
                },
                {
                    "id": "eng-q2",
                    "number": "2",
                    "question": "Write a letter to your best friend living in Delhi describing your recent Dashain-Tihar vacation.",
                    "answer": """Tokha-08, Baniyatar  
Kathmandu, Nepal  
October 24, 2026  

Dear Rohan,

I hope this letter finds you in radiant health and cheer. It has been quite a while since we caught up, and as the festive season in the Kathmandu valley draws to a peaceful close, I could not resist writing to share how I spent my recent Dashain and Tihar vacation.

This year's Dashain was extraordinarily memorable. After months of grueling Grade 12 studies and college internal tests, the festival arrived as a much-needed breath of fresh air. Kathmandu shed its usual chaotic bustle as families gathered in traditional attire. On the auspicious day of Vijaya Dashami, our entire extended family assembled at our ancestral home. My grandfather and grandmother placed the vibrant red *tika* on our foreheads and adorned us with golden *jamara*, showering blessings for our wisdom, health, and academic success. Afterwards, we enjoyed festive delicacies like mutton curry, *sel roti*, and spiced pickles. The joy of flying colorful kites against the crisp autumn sky and soaring high on the traditional bamboo *ping* (swing) made me feel completely revitalized.

No sooner had the Dashain euphoria settled than Tihar—the festival of lights and flowers—arrived. Our neighborhood transformed into a wonderland illuminated with clay *diyas*, fairy lights, and golden marigold garlands. On *Kukur Tihar*, we honored our loyal dog Bruno, and on *Laxmi Puja*, we welcomed the goddess of wealth with intricate, powdered *rangoli* patterns at our doorstep. The pinnacle of the holiday was *Bhai Tika*. My sister adorned me with the seven-colored *saptarangi tika* and gifted me traditional dry fruits, and in return, I promised to support and protect her.

Amidst the festivities, I also managed to set aside a few quiet morning hours each day to complete my holiday assignments. This vacation struck the ideal balance between joyful celebration, familial bonding, and peaceful academic revision.

How did you celebrate Diwali in Delhi? Please convey my warmest regards to uncle and aunty. Write back as soon as you find time!

Yours affectionately,  
**Arpan**"""
                },
                {
                    "id": "eng-q3",
                    "number": "3",
                    "question": "Write a narrative essay about a few memorable moments you had during this vacation.",
                    "answer": """### Whispers of Autumn: Memorable Moments of My Dashain Vacation

Vacations often arrive like gentle rain upon parched earth, but the recent Dashain vacation arrived as a spiritual and emotional sanctuary. Transitioning from the relentless academic pace of Grade 12 science into the golden embrace of the festive season offered moments of deep joy, reflection, and quiet wonder that remain indelibly etched in my memory.

The first truly unforgettable moment occurred on the afternoon of Fulpati on the terrace of our home in Baniyatar. The autumn sky was an immaculate, crystalline blue, scrubbed clean of monsoon haze. A crisp breeze swept down from the Shivapuri hills, carrying the scent of blooming marigolds. My younger cousin and I launched a handcrafted paper kite into the air currents. As the kite ascended higher, catching the sunlight like a prism, I looked across the valley and saw hundreds of identical kites dancing above Kathmandu’s terracotta rooftops. At that moment, I felt an exhilarating sense of weightlessness. All the anxieties about upcoming board exams, physics derivations, and chemistry equations dissolved into the sky. It was a rare, pure experience of childhood freedom reclaimed.

Another moment that etched itself into my consciousness took place on the morning of Vijaya Dashami. In the quiet sanctum of our prayer room, three generations of our family stood together amidst the fragrance of burning camphor, sandalwood paste, and wet barley shoots (*jamara*). When my grandfather, with hands weathered by eighty years of life and love, placed the crimson rice grains on my forehead and murmured ancient Sanskrit verses of blessing, his eyes met mine. In his gentle smile, I witnessed an enduring continuity of culture, sacrifice, and unconditional love. That brief ritual was not merely a ceremonial gesture; it was an anchor connecting me to my ancestral roots and reminding me of the values of integrity and perseverance.

Finally, the most peaceful memory took place on a solitary evening walk towards the edge of our village near the pine forests of Tokha. As the sun slipped behind the western hills, painting the horizon in shades of amber and violet, temple bells resonated softly through the twilight. The laughter of village children swinging on the towering bamboo *ping* echoed across the terraced fields. Standing there in the cool autumn twilight, I was enveloped by a profound stillness. It reminded me that life’s greatest wealth does not lie in frantic haste, but in these quiet intervals of gratitude, presence, and harmony with nature.

These vacation memories have become an inner wellspring of strength. As I step back into the rigorous rhythm of college life, I carry forward not just completed assignments, but a heart renewed by love, heritage, and the simple beauty of living."""
                },
                {
                    "id": "eng-q4",
                    "number": "4",
                    "question": "Write a job application for the post of an English teacher lying vacant in a prestigious school in your locality. Include a CV too.",
                    "answer": """### Job Application Letter

Tokha-08, Baniyatar  
Kathmandu, Nepal  
October 25, 2026  

To,  
The Principal,  
Fluorescent Secondary School / +2 College,  
Tokha-08, Kathmandu, Nepal.  

**Subject: Application for the post of Secondary Level English Teacher**

Respected Sir/Madam,

In response to your vacancy advertisement published in *The Himalayan Times* on October 20, 2026, inviting applications for the position of Secondary Level English Teacher, I wish to offer my candidature for the same.

Having completed my Master’s Degree in English Literature from Tribhuvan University with first division, along with a formal Bachelor of Education (B.Ed.), I possess over three years of successful classroom teaching experience at reputed higher secondary institutions in the valley. My pedagogy emphasizes communicative language teaching (CLT), student-centered literary analysis, and structured creative writing. I am adept at integrating modern digital teaching tools, multimedia presentations, and interactive grammar activities to cultivate genuine linguistic confidence and critical inquiry among students.

Fluorescent Secondary School has earned a stellar reputation for fostering academic excellence and ethical citizenship. I am confident that my dedication, pedagogical skill, and passion for English language and literature will allow me to make meaningful contributions to your esteemed institution.

My detailed Curriculum Vitae and copies of relevant credentials are enclosed herewith for your kind perusal. I look forward to the opportunity of discussing my qualifications in an interview.

Thank you for your time and consideration.

Yours faithfully,  
*(Signature)*  
**Arpan Bhattarai**  
Contact: +977-98XXXXXXXX  
Email: arpan.bhattarai@email.com  

---

### CURRICULUM VITAE (CV)

**Arpan Bhattarai**  
*Address:* Tokha-08, Baniyatar, Kathmandu, Nepal  
*Contact:* +977-98XXXXXXXX | *Email:* arpan.bhattarai@email.com  
*LinkedIn:* https://www.linkedin.com/in/arpan-bhattarai-8b63ba370/  

**Career Objective:**  
A dedicated, dynamic, and student-focused English Educator with over three years of experience in secondary and higher secondary teaching, seeking to foster communicative excellence, literary appreciation, and critical thinking in students at Fluorescent Secondary School.

**Academic Qualifications:**
1. **Master of Arts (M.A.) in English Literature**  
   *Institution:* Tribhuvan University, Central Department of English, Kirtipur  
   *Year:* 2023 | *Division:* First Division (68.5%)
2. **Bachelor of Education (B.Ed.) in English**  
   *Institution:* Mahendra Ratna Campus, Tahachal, Kathmandu  
   *Year:* 2021 | *Division:* First Division (72%)
3. **Bachelor of Arts (B.A.) in English & Mass Communication**  
   *Institution:* Patan Multiple Campus, Tribhuvan University  
   *Year:* 2020 | *Division:* First Division (70.2%)
4. **Higher Secondary Education (+2 Science / Humanities)**  
   *Board:* NEB, Nepal | *Year:* 2017 | *GPA:* 3.65 / 4.0

**Professional Teaching Experience:**
- **Secondary Level English Teacher** (April 2023 – Present)  
  *Wisdom Light Secondary School, Kathmandu*  
  - Taught Compulsory English and Literature to Grades 9, 10, and 11.  
  - Designed interactive lesson plans utilizing multimedia, debates, and creative workshops.  
  - Mentored the school literary club and edited the annual school magazine.
- **Assistant English Teacher & Language Tutor** (January 2021 – March 2023)  
  *Valley View Academy, Kathmandu*  
  - Conducted remedial grammar and creative writing clinics for struggling students.  
  - Coordinated inter-school elocution, quiz, and spelling bee competitions.

**Key Skills & Competencies:**
- Pedagogical Mastery in Communicative Language Teaching (CLT).
- In-depth knowledge of NEB English curriculum and examination standards.
- Excellent classroom management, public speaking, and interpersonal communication.
- Proficient in Educational Technology: Google Classroom, MS Office, and Smart Board tools.

**Trainings & Certifications:**
- Teacher Training on Competency-Based Evaluation, CDC Nepal (2023).
- British Council English Teaching Online Workshop (2022).

**References:**
1. Prof. Dr. K. P. Sharma, Department of English, Tribhuvan University (Email: kpsharma@tu.edu.np)
2. Mr. B. R. Thapa, Academic Director, Wisdom Light Secondary School (Contact: +977-98XXXXXXXX)"""
                },
                {
                    "id": "eng-q5",
                    "number": "5",
                    "question": "Some people argue that the use of AI tools is reducing human creativity. Do you agree or disagree? Write a five-paragraph essay supporting your position with relevant arguments and examples.",
                    "answer": """### Artificial Intelligence and Human Creativity: Augmentation, Not Diminution

The meteoric ascent of generative Artificial Intelligence tools such as ChatGPT, Midjourney, and Claude has ignited an impassioned global debate regarding the preservation of human ingenuity. Skeptics frequently contend that delegating cognitive, literary, and artistic tasks to automated algorithms breeds intellectual inertia, thereby eroding our intrinsic creative capacity. However, a discerning examination of technological history reveals that creativity is never a fixed quantity destined to perish upon the arrival of new tools. I disagree with the assertion that AI tools diminish human creativity; rather, when employed conscientiously, artificial intelligence serves as a cognitive catalyst that democratizes artistic expression, eliminates mechanical drudgery, and expands the frontier of imaginative innovation.

Historically, the emergence of groundbreaking technologies has routinely provoked apocalyptic predictions about the death of human artistry. When photography was invented in the nineteenth century, conventional painters lamented that the craft of painting had reached its ultimate demise; instead, photography emancipated painters from the burden of literal representation, midwifing revolutionary movements such as Impressionism, Cubism, and Abstract Expressionism. Similarly, digital synthesizers and word processors were once dismissed as artificial shortcuts that would ruin musicianship and literature. In identical fashion, AI tools do not obliterate human creativity; they merely replace laborious technical bottlenecks with instantaneous generative drafts, enabling creators to focus on higher-level conceptualization, emotional resonance, and thematic coherence.

A primary advantage of artificial intelligence lies in its ability to serve as an inexhaustible collaborative partner that obliterates creative block. Writers, composers, and researchers often grapple with the paralysis of the blank page. AI models excel at generating diverse initial variations, alternative plot devices, poetic rhyming patterns, and unorthodox structural analogies within seconds. For example, an aspiring novelist in Kathmandu can use AI to research historical details of seventeenth-century trade routes or brainstorm twenty distinct personality flaws for a protagonist. The final literary voice, the moral nuance, and the psychological truth of the narrative remain entirely human, but the generative exploration is accelerated by orders of magnitude.

Furthermore, artificial intelligence democratizes the realm of creative execution, dismantling economic and technical barriers that previously silenced imaginative voices. Millions of individuals possess brilliant conceptual ideas, compelling narratives, and inventive architectural designs, yet lack the rigorous mechanical dexterity or financial resources needed to operate sophisticated software or master complex rendering techniques. AI image generators and audio processors translate conceptual natural language prompts into stunning visual storyboards and melodic harmonies. This empowers independent creators, educators, and grassroots artists to bring multidimensional projects to life, diversifying the global cultural landscape rather than homogenizing it.

In conclusion, creativity is fundamentally an act of consciousness, empathy, and lived existential experience—attributes that silicon microprocessors and statistical algorithms can never genuinely possess. AI can recombine existing data patterns with astonishing velocity, but it cannot mourn a lost loved one, marvel at a mountain sunrise, or yearn for social justice. Far from diminishing the human spirit, AI tools elevate human creativity by relieving creators from mechanical repetition and serving as powerful cognitive sounding boards. The responsibility rests upon our shoulders to wield these instruments with ethical discernment and critical agency, ensuring that technology remains a faithful brush in the hands of the human artist."""
                },
                {
                    "id": "eng-q6",
                    "number": "6",
                    "question": "Make notes of ‘Working with words’ unit 1-10 from Language Development section.",
                    "answer": """### Notes on 'Working with Words' (Units 1 – 10)
*Compiled from the Grade 12 Compulsory English Language Development Curriculum:*

---

#### Unit 1: Critical Thinking (Word Formation & Affixation)
- **Prefixes for Negation & Reversal:**
  - *un-* (predictable $\\rightarrow$ unpredictable, ethical $\\rightarrow$ unethical)
  - *in- / im- / il- / ir-* (competent $\\rightarrow$ incompetent, plausible $\\rightarrow$ implausible, legible $\\rightarrow$ illegible, rational $\\rightarrow$ irrational)
  - *dis-* (illusion $\\rightarrow$ disillusion, integrate $\\rightarrow$ disintegrate)
  - *mis-* (interpret $\\rightarrow$ misinterpret, conceive $\\rightarrow$ misconceive)
- **Suffixes for Categorical Shifts:**
  - Verb to Noun: *-tion / -sion* (deduce $\\rightarrow$ deduction, conclude $\\rightarrow$ conclusion)
  - Adjective to Noun: *-ity / -ness* (fallible $\\rightarrow$ fallibility, aware $\\rightarrow$ awareness)
  - Verb/Noun to Adjective: *-able / -ive* (analyze $\\rightarrow$ analyzable, cogitate $\\rightarrow$ cogitative)

---

#### Unit 2: Family & Relationships (Collocations & Idioms)
- **Essential Collocations:**
  - *Nuclear family* vs. *extended family*
  - *Flesh and blood* (close blood relative)
  - *Kith and kin* (friends and relatives)
  - *Breadwinner* (primary earning member)
  - *Filial piety / filial duty* (reverence and care shown by children toward parents)
- **Phrasal Verbs of Relationship:**
  - *Bring up* (rear/raise a child)
  - *Take after* (resemble an elder in appearance or character)
  - *Look up to* (admire and respect)
  - *Fall out with* (quarrel and cease communication)

---

#### Unit 3: Sports (Sports Jargon & Action Verbs)
- **Key Sports Vocabulary:**
  - *Decathlon / Triathlon* (multi-discipline athletic contests)
  - *Sportsmanship* (fair play, integrity, and respect for opponents)
  - *Referee / Umpire* (adjudicators in football/rugby vs. cricket/tennis)
  - *Podium finish* (securing top three ranks)
- **Idiomatic Expressions derived from Sports:**
  - *Ball is in your court* (it is your turn to take action or make a decision)
  - *Touch and go* (precarious, uncertain outcome)
  - *Saved by the bell* (rescued from a dire predicament at the very last second)
  - *Below the belt* (unfair or cruel remark)

---

#### Unit 4: Education (Academic Vocabulary & Synonyms)
- **Core Academic Lexicon:**
  - *Pedagogy* (the method and practice of teaching)
  - *Curriculum* (the aggregate of courses of study in an academic institution)
  - *Didactic* (instructive, intended to convey moral instruction)
  - *Rote learning* (memorization based on repetition without deeper understanding)
- **Synonyms & Antonyms:**
  - *Cognitive:* Intellectual, cerebral (Antonym: Intuitive, physical)
  - *Lucid:* Crystal clear, comprehensible (Antonym: Obscure, ambiguous)

---

#### Unit 5: Contemporary Society (Sociological Terms & Compound Nouns)
- **Societal Lexicon:**
  - *Marginalization* (treatment of an individual or group as peripheral or insignificant)
  - *Social cohesion* (interpersonal bonding and solidarity within a society)
  - *Stereotyping* (oversimplified and generalized belief regarding a group)
  - *Egalitarian* (believing in equal rights and opportunities for all people)
- **Compound Formations:**
  - *Welfare state, grass-roots, open-mindedness, civic-minded.*

---

#### Unit 6: Ecology and Environment (Eco-Terminology & Causes)
- **Environmental Concepts:**
  - *Biodiversity hotspot* (biogeographic region with significant reservoir of endemic species under threat)
  - *Carbon footprint* (total greenhouse gas emissions produced directly and indirectly by human activities)
  - *Anthropogenic* (originating from human activity, particularly regarding environmental pollutants)
  - *Eutrophication* (excessive richness of nutrients in water causing dense plant growth and animal death)
- **Collocations:** *Sustainable development, irreversible degradation, ecological equilibrium.*

---

#### Unit 7: Career Opportunities (Professional Terminology)
- **Workplace Lexicon:**
  - *Curriculum Vitae (CV) / Resume* (formal summary of education, work history, and skills)
  - *Aptitude* (natural ability or talent to acquire a specific skill)
  - *Remuneration* (money paid for work or a service; salary/compensation)
  - *Probationary period* (trial period during which an employee is evaluated)
- **Action Verbs for Resumes:** *Spearheaded, coordinated, formulated, optimized, facilitated, demonstrated.*

---

#### Unit 8: Human Rights (Legal and Civic Terminology)
- **Key Concepts:**
  - *Inalienable* (unable to be taken away or transferred)
  - *Universal suffrage* (the right of all adult citizens to vote in political elections)
  - *Due process* (fair treatment through the normal judicial system)
  - *Discrimination* (unjust or prejudicial treatment on grounds of race, gender, or creed)
- **Confusing Pairs:**
  - *Right* (moral/legal entitlement) vs. *Rite* (ceremonial religious practice)
  - *Statute* (enacted written law) vs. *Statue* (carved or cast sculpture)

---

#### Unit 9: Leisure and Entertainment (Sensory Words & Tone)
- **Entertainment Vocabulary:**
  - *Catharsis* (emotional release and psychological purification achieved through art)
  - *Genre* (a category of artistic, musical, or literary composition characterized by a particular style)
  - *Protagonist / Antagonist* (the central character vs. the opposing adversary)
  - *Aesthetic* (concerned with beauty or the appreciation of artistic taste)
- **Nuanced Descriptive Adjectives:** *Mesmerizing, enthralling, lackadaisical, poignant, evocative.*

---

#### Unit 10: Fantasy and Imagination (Literary Devices)
- **Figurative Language & Imagery:**
  - *Metaphor* (direct comparison asserting one thing is another: e.g., "Life is a journey")
  - *Simile* (comparison using 'like' or 'as': e.g., "Fought as fierce as a lion")
  - *Personification* (attributing human emotions or actions to inanimate objects or concepts)
  - *Hyperbole* (deliberate extravagant exaggeration for emotional emphasis)
  - *Oxymoron* (a figure of speech in which contradictory terms appear in conjunction: e.g., "Deafening silence")"""
                }
            ]
        }
    ]
}

with open(os.path.join(out_dir, "english.js"), "w", encoding="utf-8") as f:
    f.write("window.ENGLISH_DATA = " + json.dumps(english_data, indent=2, ensure_ascii=False) + ";\n")

print("Wrote english.js successfully")
