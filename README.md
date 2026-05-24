RealityCheck AI 🚀
AI Output Verification & Reliability Platform

RealityCheck AI is an advanced AI reliability and trust verification platform designed to evaluate datasets, AI model outputs, and prediction trustworthiness using statistical validation, anomaly detection, hallucination auditing, confidence analysis, and evidence verification.

The platform helps users understand whether an AI system is producing reliable outputs or requires human verification.

🌐 Live Deployment
Frontend (Vercel)

RealityCheck AI Live App

Backend API (Render)

RealityCheck AI Backend API

📌 Project Overview

RealityCheck AI performs three major types of verification:

1️⃣ Dataset Audit

Evaluates:

Missing values
Duplicate records
Anomalies
Bias detection
Data drift
Relationship discovery
Trust score
Dataset quality grade
Data health status
2️⃣ Model Output Verification

Audits prediction outputs using:

Accuracy evaluation
Wrong prediction analysis
Overconfident error detection
Confidence auditing
Model trust scoring

Required columns:

actual
predicted
confidence
3️⃣ Combined AI Trust Verification

Combines:

Dataset quality
AI model output reliability
Statistical claim verification
Contradiction detection
Hallucination auditing
Evidence validation

Final verdicts include:

TRUSTED
PARTIALLY TRUSTED
UNRELIABLE
🧠 Core Idea

Most AI systems only generate predictions.

RealityCheck AI evaluates:

Can this AI output actually be trusted?

The system acts as an AI auditor that validates:

whether the data is reliable
whether the AI predictions are correct
whether the AI reasoning is statistically valid
whether the AI is overconfident or hallucinating
✨ Features
✅ Dataset Quality Audit
✅ Model Output Verification
✅ Combined AI Trust Evaluation
✅ Hallucination Detection
✅ Confidence Auditing
✅ Statistical Claim Verification
✅ Contradiction Detection
✅ Evidence Validation
✅ Bias Detection
✅ Data Drift Analysis
✅ Auto Relationship Discovery
✅ Interactive Dashboard
✅ Real-Time Trust Scoring
✅ Professional 3D UI/UX
🛠️ Tech Stack
Frontend
React.js
Axios
Chart.js
CSS3
Backend
FastAPI
Python
Pandas
NumPy
Scikit-learn
Deployment
Vercel (Frontend)
Render (Backend)
GitHub
🧩 System Architecture
User Upload
     ↓
RealityCheck AI Engine
     ↓
Dataset Audit
Model Output Audit
AI Reasoning Audit
     ↓
Trust Evaluation Engine
     ↓
Final AI Trust Verdict
📂 Supported File Formats
Dataset Audit

Supported:

.csv
.xlsx
Model Output Verification

Required columns:

actual
predicted
confidence
📊 Example Outputs

The platform generates:

Trust Scores
Risk Levels
Confidence Levels
AI Reliability Reports
Statistical Evidence Reports
Contradiction Warnings
Hallucination Alerts
🚀 Local Installation
1️⃣ Clone Repository
git clone https://github.com/saravagnamahasiva/RealityCheckAI.git
🔧 Backend Setup
Navigate to backend
cd backend
Create virtual environment
python -m venv venv
Activate virtual environment
Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate
Install dependencies
pip install -r requirements.txt
Run FastAPI backend
uvicorn main:app --reload

Backend runs on:

http://localhost:8000
🎨 Frontend Setup
Navigate to frontend
cd frontend
Install packages
npm install
Start React app
npm start

Frontend runs on:

http://localhost:3000
☁️ Deployment Process
Backend Deployment (Render)
Build Command
pip install -r requirements.txt
Start Command
uvicorn main:app --host 0.0.0.0 --port $PORT
Frontend Deployment (Vercel)
Build Command
npm run build
Output Directory
build
📁 Project Structure
RealityCheckAI/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── utils/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── sample_data/
│
└── README.md
📈 Future Improvements
PDF Audit Report Export
Authentication System
Explainable AI Integration
LLM-Based Reasoning Audit
Advanced Statistical Validation
Real-Time Monitoring Dashboard
Multi-Model Benchmarking
👨‍💻 Developed By
Mahasiva Saravagna Sai Lakshmi

Built as an AI Reliability Engineering & Trust Verification Platform for evaluating the correctness, consistency, and trustworthiness of AI systems.

⭐ If you like this project

Please consider:

Starring the repository
Sharing feedback
Contributing improvements
📜 License

This project is intended for educational, research, and AI reliability experimentation purposes.
