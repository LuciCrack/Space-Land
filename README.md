# Space Land 🚀 – Your Home in Space (NASA Space Apps Challenge 2025)

**Team:** Luciana, Mateo, Matías, Antu, Maite
**Challenge:** Your Home in Space  
**Event:** NASA Space Apps Challenge 2025, Chile

---

## 🌍 What is Space Land?

Space Land is a web application designed for the "Your Home in Space" challenge at NASA Space Apps 2025.  
It lets users **design their own off-world habitat** by combining real engineering trade-offs, NASA-inspired modules, and playful interactivity.

**Key Features:**
- Choose your mission: build for the Moon, Mars, or in Orbit.
- Select habitat construction method: inflatable, prefab, or ISRU (in-situ resource utilization).
- Place and arrange modules (labs, greenhouses, solar panels, etc.) on an interactive 2D grid editor.
- See your habitat's **Viability Index** (VI) calculated in real-time, based on food, water, O₂, energy, and space—using NASA data and real-world astronaut needs.
- Explore your base in 3D with a real-time model viewer (Three.js).
- Educational overlays: see how different choices affect sustainability and crew survival.

---

## 🌟 Why does this matter?

- **Realism:** We use NASA data on crew needs, module types, and mission constraints. All resource calculations are transparent and hackathon-documented.
- **Educational Value:** The app teaches users about the challenges of sustaining life beyond Earth, making abstract concepts (like O₂, energy, volume) tangible and playful.
- **User Experience:** Everything is interactive, visual, and easy to try—no login, no install, just build and learn.
- **Scalability:** The modular system lets you add new modules, planets, or constraints using simple data tables.
---

## 🛠️ How does it work?

### App Flow

1. **Mission Selection:** Choose your destination and construction style.
2. **Editor:** Place modules (drag & drop) on a grid. Each module has real stats (resource generation/storage, volume, etc.).
3. **Viability Index:** Enter crew size and mission days. The backend computes whether your base can support the mission. Get instant feedback!
4. **3D Viewer:** View your assembled base as a 3D model (Three.js + GLTF).
6. **Learn:** Hover icons and results for explanations, resource breakdowns, and fun facts.

### Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, vanilla JS
- **3D:** Three.js (GLTF models)
- **Data:** NASA/ESA open resources

---

## Run & Test

### Local Setup

1. **Clone the repo:**
   ```sh
   git clone https://github.com/LuciCrack/Space-Land.git
   cd Space-Land
   ```

2. **(Optional) Create a virtualenv:**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install requirements:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```sh
   flask run
   ```
   Then open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## 🧮 How is the Viability Index calculated?

- **Inputs:** Number of crew, mission duration, placed modules
- **Factors:** Food, O₂, Water, Energy, Volume
- **Each subindex:** `min(available / required, 1)`
- **Final VI:** Simple average of all subindices (so missing a resource reduces, but does not zero, the score)

---

## 🎯 What makes Space Land unique?

- **Realistic, but playful:** We blend actual engineering needs with a game-like UI
- **Transparent:** All calculations and resource trade-offs are visible and referenced
- **Extensible:** Built to be a base for more advanced mission planning, STEM education, or research

---


**Good luck to all teams and thanks for visiting our repo!**

