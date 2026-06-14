# 🔧 Engineering Material Selector

> AI-powered tool that recommends the best engineering material category based on your technical requirements — built by a Mechanical Engineering student combining domain knowledge with Machine Learning.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://engineering-material-selector.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![Accuracy](https://img.shields.io/badge/Accuracy-95%25-brightgreen)

---

## 🌐 Live Demo

👉 **[Try the App Here](https://engineering-material-selector.streamlit.app/)**

---

## 📌 About The Project

Selecting the right engineering material is a critical decision in mechanical design. Wrong material selection leads to product failure, safety risks, and financial loss.

This AI-powered tool solves that problem — enter your engineering requirements and instantly get the best material category recommendation powered by Machine Learning.

**Who is this for?**
- Mechanical Engineers during design phase
- Engineering students learning material selection
- Manufacturers optimizing material choices

---

## ✨ Features

- 🎯 Predicts 5 major engineering material categories
- ⚡ Real-time prediction with instant results
- 🖥️ Clean and simple web interface
- 📊 Trained on 100 carefully curated engineering materials
- 🔧 Built by a Mech Engineer — domain knowledge included!

---

## 🗂️ Material Categories

| Category | Example Materials | Typical Use |
|---|---|---|
| **Structural** | Mild Steel, Carbon Steel, Cast Iron | Buildings, Bridges, Frames |
| **Aerospace** | Titanium, Carbon Fiber, Aluminum Alloy | Aircraft, Rockets, Satellites |
| **Medical** | Medical Titanium, Cobalt Chrome, PEEK | Implants, Surgical Tools |
| **Electrical** | Copper, Brass, Silver | Wiring, Conductors, Circuits |
| **High_Temp** | Inconel, Tungsten, Hastelloy | Jet Engines, Turbines, Furnaces |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Core programming language |
| **Pandas** | Data loading and preprocessing |
| **Scikit-learn** | Random Forest ML model |
| **Streamlit** | Web application interface |
| **Pickle** | Model saving and loading |
| **Label Encoding** | Converting text features to numbers |

---

## 📊 Model Performance

| Metric | Value |
|---|---|
| Algorithm | Random Forest Classifier |
| Dataset Size | 100 materials |
| Categories | 5 balanced classes |
| Training Accuracy | 100% |
| **Test Accuracy** | **95%** |
| Train/Test Split | 80% / 20% |

### 🔍 Key ML Challenge Solved
Initial model gave **0% accuracy** due to overfitting — 19 unique target categories with only 20 rows caused the model to memorize instead of learn. Fixed by restructuring to **5 balanced categories across 100 materials**, improving accuracy from 0% to 95%.

---

## 📁 Project Structure

```
engineering-material-selector/
│
├── app.py                  ← Streamlit web application
├── train_model.py          ← ML model training script
├── materials.csv           ← Dataset (100 engineering materials)
├── material_model.pkl      ← Trained Random Forest model
├── target_encoder.pkl      ← Encoder for output categories
├── label_encoder.pkl       ← Encoder for input features
├── requirements.txt        ← Required Python libraries
└── README.md               ← Project documentation
```

---

## ⚙️ How to Run Locally

### Step 1 — Clone Repository
```
git clone https://github.com/madhan-s02/engineering-material-selector.git
cd engineering-material-selector
```

### Step 2 — Install Dependencies
```
pip install -r requirements.txt
```

### Step 3 — Run App
```
streamlit run app.py
```

### Step 4 — Open Browser
```
http://localhost:8501
```

---

## 🎯 How to Use

1. Enter **Maximum Temperature** your material must withstand (°C)
2. Enter **Tensile Strength** requirement (MPa)
3. Select **Cost** preference (Low / Medium / High)
4. Select **Weight** requirement (Light / Medium / Heavy)
5. Select **Corrosion Resistance** needed (Low / Medium / High)
6. Click **"Find Best Material Category"**
7. Get instant AI recommendation! 🎉

---

## 🧠 What I Learned

- End-to-end ML project development
- Data preprocessing with Label Encoding
- Random Forest classification
- Diagnosing and fixing overfitting
- Model persistence with Pickle
- Web app deployment with Streamlit Cloud

---

## 🙋 Author

**Madhan S**
- 🎓 2nd Year Mechanical Engineering — Anna University, CEG Campus
- 💼 GitHub: [@madhan-s02](https://github.com/madhan-s02)
- 🤖 Combining Mechanical Engineering with AI/ML

---

## 📄 Certifications

- 🏆 IBM — Python for Data Science, AI & Development
- 🏆 Google — Crash Course on Python

---

> ⭐ If you found this project useful, please give it a star on GitHub!
