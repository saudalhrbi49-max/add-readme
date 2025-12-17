# 🏥 Hospital Services Navigator

An AI-powered bilingual web application that helps patients access hospital services such as booking appointments, viewing lab results, and managing visits using natural language queries in Arabic and English.

---

## 📋 Overview

Hospital Services Navigator is a simple intelligent web application designed to assist patients in navigating common hospital services. The system understands user questions and provides step-by-step guidance for each service.

The application is built using Streamlit and Python, making it lightweight, easy to run, and suitable for educational projects.

---

## ✨ Key Features

- 🧠 Natural language understanding (Arabic & English)
- 🌍 Bilingual support (RTL & LTR)
- 💬 Chat-based interface
- 🏥 Hospital service focused
- ⚡ Fast and lightweight
- 🎓 Suitable for academic projects

---

## 📁 Project Structure

```
HOSPITAL_SERVICES_NAVIGATOR/
│
├── app.py              # Main Streamlit application
├── llm_backend.py      # Service matching logic
├── services.json       # Hospital services database
├── README.md           # Project documentation
└── .streamlit/
└── config.toml     # Streamlit configuration (optional)
```

---

## 🛠️ Technology Stack

-
- *Programming Language*: Python 3.8+
- *Web Framework*: Streamlit
- *AI Logic*: Rule-based (extendable to LLM)
- *Data Storage*: JSON
- *Font Support*: Arabic & English

---

## 📦 Installation

### 1️⃣ Install Python

Download and install Python from:
https://www.python.org/downloads/

---

### 2️⃣ Install Dependencies

```bash
pip install streamlit



## 💡 Usage Examples

### Example Queries (Arabic)

| Query | - |
|-------|----------------|
| حجز موعد في المستشفى |
| الدخول على بوابة المستشفى |
| تسجيل الدخول بحساب المريض |
| اختيار العيادة والطبيب |
| تحديد التاريخ والوقت |
| تأكيد الحجز |

### Example Queries (English)

| Query | - | 
|-------|----------------|
| Visit the hospital portal | 
| Login to your patient account | 
| Choose clinic and doctor | 
| Select date and time | 
| Confirm the appointment |
 
### Multiple Services

The AI can match multiple services in one query:

**Query**: "كيف أحجز موعد في المستشفى؟"

---


## 🏗️ Architecture

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Patient Input│────▶│  LLM Engine  │────▶│   Services   │
│ (Streamlit)  │     │ (Qwen2.5)    │     │  (JSON)     │
└──────────────┘     └──────────────┘     └──────────────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             ▼
                    ┌──────────────┐
                    │   Response   │
                    │     (UI)     │
                    └──────────────┘
```

