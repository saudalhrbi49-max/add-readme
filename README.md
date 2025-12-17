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

{
  "title_ar": "تغيير موعد",
  "title_en": "Reschedule Appointment",
  "keywords_ar": ["تغيير", "تعديل", "موعد"],
  "keywords_en": ["reschedule", "change appointment"],
  "steps_ar": [
    "الدخول إلى حساب المريض",
    "الانتقال إلى قائمة المواعيد",
    "اختيار الموعد المراد تغييره",
    "تحديد موعد جديد",
    "تأكيد التعديل"
  ],
  "steps_en": [
    "Login to patient account",
    "Go to appointments list",
    "Select the appointment",
    "Choose a new date and time",
    "Confirm rescheduling"
  ]
},
{
  "title_ar": "عرض السجل الطبي",
  "title_en": "View Medical Record",
  "keywords_ar": ["سجل", "طبي", "ملف"],
  "keywords_en": ["medical record", "history", "file"],
  "steps_ar": [
    "تسجيل الدخول إلى حساب المريض",
    "الدخول على السجل الطبي",
    "عرض التاريخ المرضي والتقارير"
  ],
  "steps_en": [
    "Login to patient account",
    "Access medical records",
    "View medical history and reports"
  ]
},
{
  "title_ar": "مواعيد الزيارة",
  "title_en": "Visiting Hours",
  "keywords_ar": ["زيارة", "مواعيد الزيارة"],
  "keywords_en": ["visiting hours", "visit time"],
  "steps_ar": [
    "الدخول على موقع المستشفى",
    "اختيار صفحة معلومات الزوار",
    "عرض أوقات الزيارة حسب القسم"
  ],
  "steps_en": [
    "Visit hospital website",
    "Open visitor information page",
    "Check visiting hours by department"
  ]
},
{
  "title_ar": "التواصل مع المستشفى",
  "title_en": "Contact Hospital",
  "keywords_ar": ["تواصل", "اتصال", "رقم المستشفى"],
  "keywords_en": ["contact", "call hospital"],
  "steps_ar": [
    "الدخول على صفحة التواصل",
    "اختيار القسم المطلوب",
    "الاتصال أو إرسال رسالة"
  ],
  "steps_en": [
    "Open contact page",
    "Choose the required department",
    "Call or send a message"
  ]
},
{
  "title_ar": "الاستعلام عن التأمين",
  "title_en": "Insurance Information",
  "keywords_ar": ["تأمين", "شركة التأمين"],
  "keywords_en": ["insurance", "coverage"],
  "steps_ar": [
    "الدخول إلى حساب المريض",
    "اختيار معلومات التأمين",
    "عرض شركة التأمين والتغطية"
  ],
  "steps_en": [
    "Login to patient account",
    "Open insurance information",
    "View insurance provider and coverage"
  ]
}

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

