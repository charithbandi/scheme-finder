# 🏛️ Scheme Finder: Automated Welfare & Scholarship Eligibility Engine

> **Minor Project-I** | Department of Computer Science & Engineering | School of Computing  
> **Vel Tech Rangarajan Dr. Sagunthala R&D Institute of Science and Technology**  
> **Batch No:** 1358  
> **Authors:** Charith Bandi (24UECS0059), Kalepalli Mokshagna Tej (24UECS0136), Betha Hemanth (24UECS0438)  
> **Supervisor:** Dr. S. Suchithra, Ph.D., Professor (TTS No: 3900)

---

## 🌟 Overview

**Scheme Finder** is a centralized, transparent web platform designed to eliminate the friction in discovering and claiming government welfare schemes and student scholarships.

Instead of navigating fragmented departmental websites and manually reading dense policy PDFs, citizens and students enter their socioeconomic, academic, and demographic attributes once. The system evaluates them through a deterministic, transparent rule engine.

---

## ✨ Key Features (Matching Project Report)

1. **User Profile Input Form (Figure 4.8):**
   - Captures Annual Family Income, Caste/Social Category, Academic Marks (%), Gender, State of Domicile, and Course Level.
   - Handles targeted reservation quotas (First Graduate, Single Girl Child, Person with Disability).
   - Includes **1-Click Test Profile Presets** for rapid evaluation demonstrations.

2. **Rule-Based Eligibility Engine (Chapter 4.3 & Listing 4.1):**
   - Formulated on a strict Boolean threshold satisfaction model ($E(r_i, U) \in \{0, 1\}$).
   - Deterministic and auditable—avoids opaque AI hallucinations for statutory eligibility rules.

3. **"Why You Qualify" Explanations (Figure 4.9):**
   - For every eligible scheme, explicit verification badges show exactly which criteria passed (e.g. *`✓ Annual income ₹2.50L ≤ limit of ₹8.00L`*, *`✓ Marks 85% ≥ required 60%`*).

4. **Interactive Document Checklist Modal (Figure 4.10):**
   - Scheme-specific document checklist (Income Certificate, Marksheet, Caste Certificate, Aadhaar, Bonafide).
   - Interactive preparation checkboxes with dynamic progress tracker.
   - **Print / Save as PDF** support for physical submission at e-Sevai / CSC centers.
   - Direct button routing to official government portals (e.g., National Scholarship Portal, AICTE, PM-JAY).

5. **Scheme Directory & Live Search:**
   - Real-time instant filtering across Central & State schemes by keyword and category (Education, Women Empowerment, Healthcare, Agriculture, Social Welfare).

6. **Modern, Responsive Glassmorphic UI:**
   - Dark and Light mode toggle with local storage persistence.
   - Built with Vanilla CSS, Google Fonts (Outfit & Inter), and fluid micro-animations.

---

## 🚀 How to Run the Website

### Option 1: 🌐 Run in Cloud (1-Click in Browser via GitHub Codespaces)
Click the badge below to run Scheme Finder directly in your browser without installing anything locally:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/charithbandi/scheme-finder)

> GitHub Codespaces automatically builds the Python environment, runs the Flask server, and pops open the live website in a new tab!

---

### Option 2: 💻 Run Locally on Windows (One-Click Launcher)
Double-click `run.bat` in the repository folder:
```cmd
run.bat
```

### Option 3: Terminal / Command Line
```bash
pip install -r requirements.txt
python app.py
```
Then open your browser and navigate to:
👉 **`http://127.0.0.1:5000`**

---

## 📂 Project Architecture

```
scheme_finder/
├── app.py                 # Flask server with REST API routes & static serving
├── engine.py              # Rule-Based EligibilityEngine (Listing 4.1 in report)
├── schemes_data.py        # Database of Central & State schemes, rules, and documents
├── run.bat                # Windows one-click startup script
├── requirements.txt       # Python dependencies (flask, flask-cors)
├── README.md              # Project documentation
├── static/
│   ├── css/
│   │   ├── index.css      # Design tokens, variables, typography, dark/light theme
│   │   └── components.css # Form, cards, checklist dialog, why-qualify badges
│   └── js/
│       └── app.js         # Reactive client logic, local evaluation fallback, modal
└── templates/
    └── index.html         # Master semantic HTML5 template
```

---

## 📋 Standard Aligned
- **Data Privacy & Security:** ISO/IEC 27001 standard compliant data handling
- **SDG Goals:** SDG 1 (*No Poverty*), SDG 4 (*Quality Education*), SDG 10 (*Reduced Inequalities*), SDG 16 (*Peace, Justice & Strong Institutions*)
