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

---

## 📦 Installation & Setup

### Prerequisites

1. **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
2. **Ollama** - [Download Ollama](https://ollama.ai)

### Step-by-Step Installation

#### 1. Install Ollama

- **Windows**: Download installer from [ollama.ai](https://ollama.ai)
- **Mac/Linux**: Follow instructions on [ollama.ai](https://ollama.ai)

#### 2. Pull the AI Model

Open terminal/command prompt and run:

```bash
ollama pull qwen2.5:14b
```

**Note**: This downloads ~8GB. Make sure you have enough disk space and a stable internet connection.

#### 3. Install Python Dependencies

Navigate to the project folder and run:

```bash
pip install streamlit Pillow
```
Or:

```bash
py -m pip install streamlit Pillow
```

This installs:
- `streamlit` - Web framework (for building the UI)
- `Pillow` - Image handling (for logo and icon support)

#### 4. Verify Installation

Test that Ollama is working:

```bash
ollama run qwen2.5:14b "Hello"
```

You should see a response from the model.

---

## 🚀 Running the Application

### Start the Application

```bash
python -m streamlit run app.py
```
Or:

```bash
py -m streamlit run app.py
```
Or:

```bash
streamlit run app.py
```


### First Time Setup

1. **Select Language**: Use the dropdown in the top-left to choose Arabic (العربية) or English
2. **Ask a Question**: Type your question about a government service
3. **Get Results**: The AI will match your query to a service and show detailed instructions

---

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

## 📊 Supported Services

The application currently supports **33 government services** across 5 platforms:

### Absher Services
- **Traffic**: Renew/Issue driving license, View digital license, Report lost license
- **Civil Affairs**: Renew national ID, Register newborn, Issue birth certificate, Update personal info
- **Passports**: Issue/Renew passport, Report lost passport, Track delivery, Add dependent

### Saudi Business Center
- **Business**: Register commercial registration, Annual confirmation, Trade name reservation, Transfer trade name

### Qiyas (Educational Testing)
- **Testing**: Paper test registration, Digital test rescheduling, View test results

### NWC (National Water Company)
- **Water**: Check bill, Pay bill, Request new meter, Transfer ownership, Report leak, Reconnection

### Saudi Electricity
- **Electricity**: Check bill, Pay bill, Request new meter, Transfer ownership, Report outage, Reconnection

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

