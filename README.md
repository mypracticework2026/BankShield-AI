# 🛡️ BankShield AI — Enterprise Fraud Detection Platform

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green)](https://fastapi.tiangolo.com/)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.0.0-orange)](https://xgboost.ai/)

A production‑ready fraud detection dashboard built for financial institutions. Features a premium dark UI (inspired by Stripe/Revolut), a real‑time transaction simulator, and a trained XGBoost model for risk scoring.

---

## ✨ Features

- 🏦 **Executive Dashboard** – KPI cards (Total Transactions, Fraud Rate, Model Accuracy)
- 📈 **Interactive Charts** – Fraud distribution, ROC curve, Confusion Matrix, Feature Importance
- 🧪 **Transaction Simulator** – Adjust sliders (Amount, Time, Merchant Risk, International, Card Present) to see risk scores change in real‑time
- 🔍 **AI Reasoning Panel** – Explains *why* a transaction is flagged (e.g., "High Amount", "Card Not Present")
- 📊 **Live Transaction Feed** – Simulated real‑time updates (fraud vs. legitimate)
- 📉 **Analytics Page** – Precision, Recall, F1, ROC‑AUC metrics
- 🌙 **Dark Theme** – Professional fintech design

---

## 🧠 How It Works

1. **User adjusts sliders** (e.g., sets Amount = $4,500, Time = 3 AM, Merchant Risk = High).
2. **Frontend sends JSON payload** to FastAPI backend (`/predict`).
3. **Backend processes inputs**:
   - Maps `Hour` → `Time` (seconds)
   - Maps `Amount` directly
   - Applies **feature engineering** to adjust PCA features (V1–V28) based on business rules (Card Present, International, Merchant Risk)
4. **XGBoost model** predicts fraud probability.
5. **Result** (probability + reasoning) is returned and displayed with a risk tier (LOW / MEDIUM / HIGH).

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | Vanilla JavaScript, Chart.js, Font Awesome |
| **Backend** | FastAPI (Python) |
| **ML Model** | XGBoost (trained on Credit Card Fraud Detection dataset) |
| **Deployment** | Uvicorn (local) / Render + GitHub Pages (cloud) |

---

## 🚀 Getting Started (Run Locally)

### Prerequisites
- Python 3.8+
- `pip` (Python package manager)

### Clone the repository
```bash
git clone https://github.com/your-username/BankShield-AI.git
cd BankShield-AI
