# 🛡️ CyberLaw AI Assistant – MVP

An AI-powered platform to guide users through cybercrime reporting, Indian cyber laws, FIR generation, and digital safety.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green.svg)
![Gemini API](https://img.shields.io/badge/Google%20Gemini-AI%20Model-red.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## 🚀 Features

🔹 **AI Cyber Law Guidance**  
> Explains IPC + IT Act sections for reported cybercrimes in clean, structured legal format.

🔹 **Smart FIR Generator (PDF)**  
> Auto-fills a legally styled First Information Report based on AI response and user inputs.

🔹 **Precaution Awareness Page**  
> Shows security tips and real-life cybercrime scenarios based on user’s case.

🔹 **Uses Free Google Gemini API**  
> No billing required. Fully open-source and accessible.

---

## 📸 Screenshots

| Report Interface | FIR PDF |
|------------------|---------|
| ![report](docs/report.png) | ![fir](docs/fir.png) |

---

## 🧱 Tech Stack

- 🧠 **AI:** Google Gemini 1.5 Pro
- 🌐 **Backend:** Flask (Python)
- 🎨 **Frontend:** HTML, CSS (Dark UI)
- 📄 **PDF Generator:** `pdfkit` + `wkhtmltopdf`
- ☁️ **Future Ready:** Can connect to Firebase, Dark Web APIs, or Police Dashboards

---

## 🛠️ Local Setup

git clone https://github.com/your-username/cyberlaw-mvp.git
cd cyberlaw-mvp
pip install -r requirements.txt
